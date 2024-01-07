<script lang="ts">
  import type { player_search_callback } from "$lib/constants";
  import type { PlayerInfo } from "$lib/models";

  export let player_info: PlayerInfo;
  export let on_click: player_search_callback;
</script>

<button
  on:click={() => {
    on_click(player_info.name, player_info.country_name);
  }}
>
  {player_info.name}
</button>
