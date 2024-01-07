import constants from "./constants";

export const get_country_data = async (country_name: string) => {
  const team_service_endpoint = constants.endpoints.team;
  let search_string = country_name.trim().toLowerCase();
  const team_info = await fetch(`${team_service_endpoint}/${search_string}`);
  const team_info_json = await team_info.json();
  return team_info_json;
};
