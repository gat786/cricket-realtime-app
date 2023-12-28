<script lang="ts">
  import type { Innings } from "$lib/models";
  export let innings_data: Innings;
</script>

<div class="flex flex-col gap-2 py-4 font-thin">
  <div>
    Score: <span class="font-medium">{innings_data.score} for {innings_data.wickets_down}</span>
  </div>
  <div>
    Overs: {Math.floor(
      innings_data.legal_deliveries / 6,
    )}.{innings_data.legal_deliveries % 6}
  </div>
  <div>
    Extras: {innings_data.extras}
  </div>
  <div class="text-blue-800 flex flex-col gap-4 font-medium">
    <div>
      🏏 - {innings_data.batsmen.on_onstrike.name} - {innings_data.batsmen.on_onstrike.score} 
    </div>
    <div>
      🏃‍♂️ - {innings_data.batsmen.on_offstrike.name} - {innings_data.batsmen.on_offstrike.score}
    </div>
  </div>
  <div class="text-green-800 font-medium">
    🎾 - {innings_data.current_bowler}
  </div>
</div>
