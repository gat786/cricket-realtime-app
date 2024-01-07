<script lang="ts">
  import type { Player } from "$lib/models";
  export let player_data: Player;
</script>
<div>
  <img src={player_data.image_path} alt="">
  {player_data.fullname}
</div>
