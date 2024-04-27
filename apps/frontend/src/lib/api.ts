import constants from "./constants";
import type { PlayerInfo } from "./models";

export const get_country_data = async (country_name: string) => {
  const team_service_endpoint = constants.endpoints.team;
  let search_string = country_name.trim().toLowerCase();
  const team_info = await fetch(`${team_service_endpoint}/${search_string}`);
  const team_info_json = await team_info.json();
  return team_info_json;
};

export const search_for_player = async (player_info: PlayerInfo) => {
  const player_service_endpoint = constants.endpoints.player;
  let search_string = {
    name: player_info.name.trim().toLowerCase(),
    country_name: player_info.country_name.trim().toLowerCase(),
  };
  const response = await fetch(
    `${player_service_endpoint}/search`,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(search_string)
  });
  const player_info_json = await response.json();
  console.log(player_info_json);
  return player_info_json;
}

export default {
  search_for_player
}
