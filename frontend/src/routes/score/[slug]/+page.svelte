<script lang="ts">
	import type { PageData } from "./$types";
	import { onMount } from "svelte";

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

	export let data: PageData;
	export let socket: WebSocket | undefined = undefined;
	export let current_score: LiveScore = {
		live_score: 0,
		wickets_fallen: 0,
		overs_bowled: 0,
		balls_bowled_in_current: 0,
		batsmen_already_out: [],
		onstrike_batsman: "",
		offstrike_batsman: "",
		current_bowler: "",
	};

	
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

	onMount(() => {
		match_data = data.data;
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
				let total_score =
					current_score.live_score + data["data"]["runs"]["total"];

				if ("wickets" in data["data"]) {
					let wickets_data = data["data"]["wickets"][0];
					current_score = {
						...current_score,
						wickets_fallen: current_score.wickets_fallen + 1,
						batsmen_already_out: [
							...current_score.batsmen_already_out,
							wickets_data?.player_out,
						],
					};
				}
				current_score = {
					live_score: total_score,
					overs_bowled: data["over"],
					balls_bowled_in_current: data["delivery"],
					onstrike_batsman: data["data"]["batter"],
					offstrike_batsman: data["data"]["non_striker"],
					current_bowler: data["data"]["bowler"],
					wickets_fallen: 0,
					batsmen_already_out: [],
				};

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

{#if match_data != undefined}
	<div class="flex bg-slate-700 justify-between items-center p-4 text-white">
		<div class="text-2xl font-bold">{match_data.data.teams.join(" vs ")}</div>
		<div class="text-2xl font-thin">{match_data.data.match_type}</div>
		<div class="text-2xl font-thin">
			Match Game Type: {match_data.data.city}
		</div>
	</div>
	<div>First Innings</div>
	<InningsBox innings_data={match_innings.first} />
	<div>Second Innings</div>
	<InningsBox innings_data={match_innings.second} />	
{/if}
