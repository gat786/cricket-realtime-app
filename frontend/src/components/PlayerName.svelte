<script lang="ts">
    import type { player_search_callback } from "$lib/constants";

  export let player_name: string;
  export let country_name: string;
  export let on_click: player_search_callback;
</script>

<button
  on:click={() => {
    on_click(player_name, country_name);
  }}
>
  {player_name}
</button>
