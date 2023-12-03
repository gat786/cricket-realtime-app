<script lang="ts">
	import constants from "$lib/constants";
	import type { LiveScore, Match } from "$lib/models";
	import { onMount } from "svelte";

	export let match_list: Match[] = [];
	export let selected_match: Match | undefined = undefined;
	export let selected_match_index: number | undefined = undefined;
	export let div_styles = {
		"selected_style": "border-white bg-blue-500 hover:bg-blue-600 active:bg-blue-700 text-white",
		"unselected_style":  "border-gray-200 hover:bg-slate-200 active:bg-slate-300 text-black"
	};

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

	const get_matches = () => {
		const score_endpoint = constants.endpoints.score;

		fetch(`${score_endpoint}/list`)
			.then((res) => res.json())
			.then((matches) => {
				console.log(matches);
				if ("match_list" in matches){
					match_list = matches["match_list"];
				}
			})
			.catch((err) => {
				console.log("Error while fetching matches, check if server is running");
				console.log(err);
			});
	};

	const start_streaming_match_data = (match_file_id: string) => {
		const websockets_endpoint = constants.endpoints.score_streaming + "/live/";

		close_socket();

		socket = new WebSocket(websockets_endpoint);

		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			if("over" in data){
				console.log("Over data received");
				console.log(data);
				current_score = {
					live_score: 0,
					overs_bowled: data["over"],
					balls_bowled_in_current: data["delivery"],
					onstrike_batsman: data["data"]["batter"],
					offstrike_batsman: data["data"]["non_striker"],
					current_bowler: data["data"]["bowler"],
					wickets_fallen: 0,
					batsmen_already_out: [],
				};
			}
			else{
				console.log(data);
			}
		};

		socket.onopen = () => {
			console.log("Socket connection opened");
			const initiation_message = JSON.stringify({
				"match_id": match_file_id
			});
			socket?.send(initiation_message);
		};
	}

	function close_socket(){
		if (socket !== undefined){
			console.log("Closing socket connection");
			socket.close();
			socket.onclose = () => {
				console.log("Socket connection closed, it is now ready to open a new connection");
			};
		}else{
			console.log("No socket connections already open");
		}
	}

	onMount(() => {
		get_matches();
		if (socket !== undefined){
			close_socket();
		}
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<nav class="font-bold bg-gray-200 h-16 flex items-center px-8">
	<span class="text-xl"> Cricket Realtime Application </span>
</nav>

<div class="flex">
	<div class="w-1/4 bg-slate-100 h-full">
		<!-- this will display the list of matches -->
		<ul>
			{#each match_list as match, index}
				<li>
					<button
						class={
							`p-4 border-b cursor-pointer w-full text-start ` +
							`${selected_match_index === index ? div_styles.selected_style : div_styles.unselected_style}`
						}
						on:click={()=> {
							selected_match = match;
							selected_match_index = index;
							start_streaming_match_data(match.match_file_id);
						}}>
						{match.match_title}
				</button>
				</li>
			{/each}
		</ul>
	</div>
	<div class="w-3/4 h-full ">
		<!-- this will display match detail -->
		{#if selected_match !== undefined}
			<div class="flex bg-slate-700 justify-between items-center p-4 text-white">
				<div class="text-2xl font-bold">{selected_match.match_title}</div>
				<div class="text-2xl font-thin">{selected_match.match_date}</div>
				<div class="text-2xl font-thin">Match Game Type: {selected_match.match_game_type}</div>	
			</div>

			<div>
				Current Score: {current_score.live_score}
				Current Over: {current_score.overs_bowled}.{current_score.balls_bowled_in_current}
				Current On Strike Batsman: {current_score.onstrike_batsman}
				Current Off Strike Batsman: {current_score.offstrike_batsman}
				Current Bowler: {current_score.current_bowler}
			</div>
		{:else}
			<div class="flex justify-center items-center h-full">
				<div class="text-2xl font-bold">Select a match to view details</div>
			</div>
		{/if}
	</div>
</div>

<style>
</style>
