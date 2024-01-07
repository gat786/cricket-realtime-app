<script lang="ts">
  import type { Innings } from "$lib/models";
  import PlayerName from "./PlayerName.svelte";
  export let innings_data: Innings;
</script>

<table class="table table-auto w-1/2 gap-2 py-4 font-thin p-2">
  <tr class="p-2 text-xl">
    <td class="col-span-2">
      Score: <span class="font-medium"
        >{innings_data.score} for {innings_data.wickets_down}
      </span></td
    >
  </tr>
  <tr class="p-2">
    <td> Overs: </td>
    <td>
      {Math.floor(
        innings_data.legal_deliveries / 6,
      )}.{innings_data.legal_deliveries % 6}
    </td>
  </tr>
  <tr class="p-2">
    <td> Extras: </td>
    <td>
      {innings_data.extras}
    </td>
  </tr>
  <tr class="text-blue-800 font-medium p-2">
    <td>
      <PlayerName
        player_name={`🏏 : ${innings_data.batsmen.on_onstrike.name}`}
        on_click={(name) => {}}
      />
    </td>
    <td> {innings_data.batsmen.on_onstrike.score} </td>
  </tr>
  <tr class="text-blue-800 font-medium p-2">
    <td>
      <PlayerName
        player_name={`🏃‍♂️ : ${innings_data.batsmen.on_offstrike.name}`}
        on_click={(name) => {}}
      />
    </td>
    <td>{innings_data.batsmen.on_offstrike.score} </td>
  </tr>
  <tr class="text-green-800 font-medium p-2">
    <td>
      <PlayerName
        player_name={`🎾 : ${innings_data.current_bowler}`}
        on_click={(name) => {}}
      />
      
    </td>
  </tr>
</table>
