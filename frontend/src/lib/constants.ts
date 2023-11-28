import { PUBLIC_SCORE_SERVICE_ENDPOINT } from "$env/static/public";
import { PUBLIC_PLAYER_SERVICE_ENDPOINT } from "$env/static/public";
import { PUBLIC_SCORE_SOCKET_ENDPOINT } from "$env/static/public";

const endpoints = {
  score: PUBLIC_SCORE_SERVICE_ENDPOINT,
  score_streaming: PUBLIC_SCORE_SOCKET_ENDPOINT,
  player: PUBLIC_PLAYER_SERVICE_ENDPOINT,
};

export default {
  endpoints
};
