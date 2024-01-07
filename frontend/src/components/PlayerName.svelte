<script lang="ts">
  export let player_name: string;
  export let on_click: (player_name: string) => void;
</script>

<button
  on:click={() => {
    on_click(player_name);
  }}
>
  {player_name}
</button>
