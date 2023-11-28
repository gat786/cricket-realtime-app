<script>
  import constants from "$lib/constants";
	import { onMount } from "svelte";

	const get_matches = () => {
		const score_endpoint = constants.endpoints.score;
		fetch(`${score_endpoint}/list`)
			.then(res => res.json())
			.then(matches => {
				console.log(matches);
			});
	}

	onMount(() => {
		get_matches();
	});

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<nav class="font-bold bg-gray-200 h-16 flex items-center px-8">
	<span class="text-xl">
		Cricket Realtime Application
	</span>
</nav>

<div class="flex">
	<div class="w-1/4 bg-slate-100 h-full">
		<!-- this will display the list of matches -->
		<ul>
			<li>Eng vs Aus</li>
			<li>Ind vs Pak</li>
			<li>Aus vs Ind</li>
			<li>SA vs NZ</li>
		</ul>
	</div>
	<div class="w-3/4 bg-slate-700 h-full text-white">
		<!-- this will display match detail -->
		hello
	</div>
</div>

<style>
</style>
