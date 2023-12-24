import constants from '$lib/constants';
import type { MatchResponse } from '$lib/models.js';

export const ssr = false;

export const load = async({ params }) => {
  const slug = params.slug
  console.log(`We need to display score for slug: ${slug}`);

  const score_endpoint = `${constants.endpoints.score}/${slug}`; 
  const response = await fetch(score_endpoint);
  const json = await response.json();

  let response_to_return: MatchResponse = {
    slug: params.slug,
    data: json,
  }
  return response_to_return
}
