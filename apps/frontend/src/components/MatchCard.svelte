<script lang="ts">
  import { onMount } from "svelte";
  import { writable, type Writable } from "svelte/store";

  import type { Match, TeamData } from "$lib/models";
  import { get_country_data } from "$lib/api";
  import exports from "$lib/constants";
  import TeamFlag from "./TeamFlag.svelte";
  export let match : Match;
  const teams = match.match_teams;
  let teams_data: Writable<TeamData[]> = writable([]);

  onMount(() => {
    teams.forEach(async (team) => {
      let data: TeamData = await get_country_data(team);
      teams_data.update((teams_data) => [...teams_data, data]);
    });
    
  });
</script>

<div class="">
  <a
    class={`cursor-pointer text-start flex flex-col items-start gap-8 border p-4`}
    href="/score/{match.match_file_id}"
  >
    <div class="flex gap-4">
      {#each $teams_data as team}
        <div class="w-40 flex items-center gap-4">
          <TeamFlag image_url={team.image_path} />
          <div>{team.name}</div>
        </div>
      {/each}
    </div>
    {match.match_teams.join(" vs ")} - {match.match_date}
  </a>
</div>
