<script lang="ts">
	import type { PageData } from "./$types";
	import { onMount } from "svelte";
	import Navbar from "../../../components/Navbar.svelte";

	import constants from "$lib/constants";
	import { get_updated_innings } from "$lib/utils";
	import type { MatchInnings } from "$lib/utils";
	import type {
		LiveScore,
		Innings,
		MatchResponseApi,
		BallDataWithMeta,
	} from "$lib/models";

	import { defaultInnings } from "$lib/models";
    import InningsBox from "../../../components/InningsBox.svelte";
    import { stringify } from "postcss";

	export let data: PageData;
	export let socket: WebSocket | undefined = undefined;
	
	let match_innings: MatchInnings = {
		first: {
			...(JSON.parse(JSON.stringify(defaultInnings))),
		},
		second: {
			...(JSON.parse(JSON.stringify(defaultInnings))),
		},
	};

	let match_data: MatchResponseApi | undefined = undefined;
	let match_id = "";

	const innings_order: string[] = [];

	onMount(() => {
		match_data = data.data;
		const toss_data = match_data.data.toss;
		const toss_winner = toss_data.winner;
		const winner_decision = toss_data.decision;
		if (winner_decision == "bat"){
			innings_order.push(toss_winner);
			let second_batting = match_data.data.teams.filter((team) => team != toss_winner)[0];
			innings_order.push(second_batting);
		}
		else {
			let first_batting = match_data.data.teams.filter((team) => team != toss_winner)[0];
			innings_order.push(first_batting);
			innings_order.push(toss_winner);
		}

		match_id = data.slug;
		start_streaming_match_data(match_id);
	});

	const start_streaming_match_data = (match_file_id: string) => {
		const websockets_endpoint = constants.endpoints.score_streaming + "/live/";

		close_socket();

		socket = new WebSocket(websockets_endpoint);

		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			if ("over" in data) {
				console.log("Over data received");
				console.log(data);

				add_to_innings(data);
			} else {
				console.log(data);
			}
		};

		socket.onopen = () => {
			console.log("Socket connection opened");
			const initiation_message = JSON.stringify({
				match_id: match_file_id,
			});
			socket?.send(initiation_message);
		};
	};

	function close_socket() {
		if (socket !== undefined) {
			console.log("Closing socket connection");
			socket.close();
			socket.onclose = () => {
				console.log(
					"Socket connection closed, it is now ready to open a new connection",
				);
			};
		} else {
			console.log("No socket connections already open");
		}
	}

	const add_to_innings = (ball_data: BallDataWithMeta) => {
		if (ball_data.innings == 0) {
			let updated_inning_score = get_updated_innings(
				match_innings.first,
				ball_data.data,
			);

			match_innings = {
				...match_innings,
				first: updated_inning_score,
			};
		} else if (ball_data.innings == 1) {
			let updated_inning_score = get_updated_innings(
				match_innings.second,
				ball_data.data,
			);

			match_innings = {
				...match_innings,
				first: updated_inning_score,
			};
		}
	};
</script>

<head>
	<title>
		{#if match_data != undefined}
			{match_data.data.teams.join(" vs ")} - {match_data.data.match_type}
		{/if}
	</title>
</head>

<Navbar />

<div>
	<div class = "flex flex-col py-4">
		<div class="">
			{#if match_data != undefined}
				<div class="flex flex-col gap-4 justify-between p-4">
					<div class="flex gap-8 items-center">
						<div class="text-xl font-bold">{match_data.data.teams.join(" vs ")}</div>
						<div class="text-l font-thin"> Date - {match_data.data.dates[0]}</div>
						<div class="text-l font-light">
							Match Game Type: {match_data.data.match_type}
						</div>
					</div>
				</div>
				<div class="flex m-4">
					<div class="flex flex-col border p-4">
						<div class="text-xl font-bold">{innings_order[0]}'s Innings</div>
						<InningsBox innings_data={match_innings.first} />
					</div>
					<div class="flex flex-col border p-4">
						<div class="text-xl font-bold">{innings_order[1]}'s Innings</div>
						{#if JSON.stringify(match_innings.second) == JSON.stringify(defaultInnings)}
							<div class="text-l font-bold py-4">Yet to bat</div>
						{:else}
							<InningsBox innings_data={match_innings.second} />
						{/if}
					</div>
				</div>
			{/if}
		</div>
	</div>
	<div>
		<div>
			Batting Stats
			<div>
				{#each match_innings.first.batsmans as batsman}
					<div>
						{batsman.name} - {batsman.score}
					</div>
				{/each}
			</div>
		</div>
		<div>
			Batting Stats
			<div>
				{#each match_innings.first.balling as bowler}
					<div>
						{bowler.name} - {bowler.deliveries} - {bowler.runs_given}
					</div>
				{/each}
			</div>
		</div>
	</div>	
</div>
