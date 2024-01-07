import { PUBLIC_SCORE_SERVICE_ENDPOINT } from "$env/static/public";
import { PUBLIC_PLAYER_SERVICE_ENDPOINT } from "$env/static/public";
import { PUBLIC_SCORE_SOCKET_ENDPOINT } from "$env/static/public";
import { PUBLIC_TEAM_SERVICE_ENDPOINT } from "$env/static/public";

const endpoints = {
  score: PUBLIC_SCORE_SERVICE_ENDPOINT,
  score_streaming: PUBLIC_SCORE_SOCKET_ENDPOINT,
  player: PUBLIC_PLAYER_SERVICE_ENDPOINT,
  team: PUBLIC_TEAM_SERVICE_ENDPOINT,
};

export default {
  endpoints
};

export type player_search_callback = (player_name: string, country_name: string) => void;
