import type { Innings, BallData, BallDataWithMeta, PlayerInfo, } from "$lib/models"

export const get_updated_innings = (innings: Innings, ball_data: BallData) => {

  const batsman = innings.batsmans.find(b => b.name == ball_data.batter);
  let batsman_country = get_country_name_from_players_list(innings.players_list, ball_data.batter);
  if (batsman) {
    batsman.score += ball_data.runs.batter;
  }
  else {
    innings.batsmans.push({
      name: ball_data.batter,
      country_name: batsman_country,
      score: ball_data.runs.batter
    })
  }

  const baller = innings.balling.find(b => b.name == ball_data.bowler)
  let baller_country = get_country_name_from_players_list(innings.players_list, ball_data.bowler);
  if (baller) {
    baller.deliveries += 1;
    baller.runs_given += ball_data.runs.total;
  }
  else {
    innings.balling.push({
      name: ball_data.bowler,
      deliveries: 1,
      country_name: baller_country,
      runs_given: ball_data.runs.total
    })
  }

  innings.score += ball_data.runs.total;
  if (ball_data.runs.extras) {
    innings.extras += ball_data.runs.extras;
  }

  if (ball_data.extras) {
    if ("wides" in ball_data.extras) {
      innings.illegal_deliveries += 1;
    }
    else if ("noballs" in ball_data.extras) {
      innings.illegal_deliveries += 1;
    }
  }
  else {
    innings.legal_deliveries += 1;
  }

  if (ball_data.wickets && ball_data.wickets.length > 0) {
    innings.wickets_down += 1;
  }
  const on_onstrike_name = ball_data.batter;
  const on_offstrike_name = ball_data.non_striker;

  
  let onstrike_batsman_country = get_country_name_from_players_list(innings.players_list, ball_data.batter);
  let offstrike_batsman_country = get_country_name_from_players_list(innings.players_list, ball_data.non_striker);
    

  innings.batsmen.on_onstrike = innings.batsmans.find(
    (batsman) => on_onstrike_name == batsman.name,
  ) ?? {
    name: on_onstrike_name,
    country_name: onstrike_batsman_country,
    score: 0,
  };
  
  innings.batsmen.on_offstrike = innings.batsmans.find(
    (batsman) => on_offstrike_name == batsman.name,
  ) ?? {
    name: on_offstrike_name,
    country_name: offstrike_batsman_country,
    score: 0,
  };

  innings.current_bowler = {
    name: ball_data.bowler,
    country_name: baller_country,
  };

  return innings;
}

export const get_country_name_from_players_list = (players_list: PlayerInfo[], name: string) => {
  const player = players_list.find(p => p.name == name);
  return player?.country_name ?? "";
}
