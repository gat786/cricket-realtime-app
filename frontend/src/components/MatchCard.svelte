<script lang="ts">
  import { onMount } from "svelte";
  import { writable, type Writable } from "svelte/store";

  import type { Match, TeamData } from "$lib/models";
  import exports from "$lib/constants";
  import TeamFlag from "./TeamFlag.svelte";
  export let match : Match;

  const team_service_endpoint = exports.endpoints.team;
  const teams = match.match_teams;
  let teams_data: Writable<TeamData[]> = writable([]);

  const get_country_data = async (country_name: string) => {
    let search_string = country_name.trim().toLowerCase();
    const team_info = await fetch(`${team_service_endpoint}/${search_string}`);
    const team_info_json = await team_info.json();
    return team_info_json;
  };

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
