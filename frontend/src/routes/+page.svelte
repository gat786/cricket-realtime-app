<script>

	import { PUBLIC_SCORE_SERVICE_ENDPOINT } from "$env/static/public";

	const get_matches = () => {

		fetch('/api/matches')
			.then(res => res.json())
			.then(matches => {
				console.log(matches);
			});
	}

</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	This is my home section
</section>

<style>
</style>
