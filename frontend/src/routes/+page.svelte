<script lang="ts">
	import constants from "$lib/constants";
	import type { LiveScore, Match } from "$lib/models";
	import { onMount } from "svelte";
    import Navbar from "../components/Navbar.svelte";
    import MatchCard from "../components/MatchCard.svelte";

	export let match_list: Match[] = [];

	const get_matches = () => {
		const score_endpoint = constants.endpoints.score;

		fetch(`${score_endpoint}/list`)
			.then((res) => res.json())
			.then((matches) => {
				console.log(matches);
				if ("match_list" in matches) {
					match_list = matches["match_list"];
				}
			})
			.catch((err) => {
				console.log("Error while fetching matches, check if server is running");
				console.log(err);
			});
	};

	onMount(() => {
		get_matches();
	});
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<Navbar />

<div class="flex">
	<div class="h-full grid grid-cols-4 items-start gap-4 p-8">
		<!-- this will display the list of matches -->
		{#each match_list as match, index}
			<MatchCard {match}/>
		{/each}
	</div>
</div>

<style>
</style>
