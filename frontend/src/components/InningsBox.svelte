<script lang="ts">
  import type { BatsmanScore, Innings } from "$lib/models";
  export let innings_data: Innings;

  import { onMount } from 'svelte'

  let score_onstrike: BatsmanScore | undefined = undefined;
  let score_offstrike: BatsmanScore | undefined = undefined;

  onMount(() => {
    score_onstrike = innings_data.batsmans.find(
      (batsman) => batsman.name == innings_data.batsmen.on_onstrike,
    );

    score_offstrike = innings_data.batsmans.find(
      (batsman) => batsman.name == innings_data.batsmen.on_offstrike,
    );
  });
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
    🏏 - {innings_data.batsmen.on_onstrike} - {score_onstrike?.score}
  </div>
  <div>
    🏃‍♂️ - {innings_data.batsmen.on_offstrike} - {score_offstrike?.score}
  </div>
  <div>
    🎾 - {innings_data.current_bowler}
  </div>
</div>
