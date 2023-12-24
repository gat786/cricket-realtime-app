<script lang="ts">
	import constants from "$lib/constants";
	import type { LiveScore, Match } from "$lib/models";
	import { onMount } from "svelte";
    import Navbar from "../components/Navbar.svelte";

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
	<div class="h-full w-full">
		<!-- this will display the list of matches -->
		{#each match_list as match, index}
			<div class="w-72">
				<a
					class={`border-b cursor-pointer w-72 text-start `}
					href="/score/{match.match_file_id}"
				>
					{match.match_title}
				</a>
			</div>
		{/each}
	</div>
</div>

<style>
</style>
