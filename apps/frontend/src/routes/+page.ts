// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

import { PUBLIC_PLAYER_SERVICE_ENDPOINT } from '$env/static/public';

const playerServiceEndpoint = PUBLIC_PLAYER_SERVICE_ENDPOINT;
