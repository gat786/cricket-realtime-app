<script lang="ts">
  import type { Innings } from "$lib/models";
  export let innings_data: Innings;
</script>

<div>
  <div>
    Score: {innings_data.score} for {innings_data.wickets_down}
  </div>
  <div>
    Overs: {Math.floor(
      innings_data.legal_deliveries / 6,
    )}.{innings_data.legal_deliveries % 6}
  </div>
  <div>
    Extras: {innings_data.extras}
  </div>
  <div>
    🏏 - {innings_data.batsmen.on_onstrike.name} - {innings_data.batsmen.on_onstrike.score} 

  </div>
  <div>
    🏃‍♂️ - {innings_data.batsmen.on_offstrike.name} - {innings_data.batsmen.on_offstrike.score}
  </div>
  <div>
    🎾 - {innings_data.current_bowler}
  </div>
</div>
