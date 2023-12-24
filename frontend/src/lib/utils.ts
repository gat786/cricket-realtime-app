import type { Innings, BallData, BallDataWithMeta } from "$lib/models"

export interface MatchInnings {
  first: Innings;
  second: Innings;
}

export const get_updated_innings = (innings : Innings, ball_data : BallData) => {
  const batsman = innings.batsmans.find(b => b.name == ball_data.batter)
  if (batsman) {
    batsman.score += ball_data.runs.batter;
  }
  else {
    innings.batsmans.push({
      name: ball_data.batter,
      score: ball_data.runs.batter
    })
  }

  const baller = innings.balling.find(b => b.name == ball_data.bowler)
  if (baller) {
    baller.deliveries += 1;
    baller.runs_given += ball_data.runs.total;
  }
  else {
    innings.balling.push({
      name: ball_data.bowler,
      deliveries: 1,
      runs_given: ball_data.runs.total
    })
  }

  innings.score += ball_data.runs.total;
  if (ball_data.runs.extras){
    innings.extras += ball_data.runs.extras;
  }

  if (ball_data.extras) {
    if ( "wides" in ball_data.extras ) {
      innings.illegal_deliveries += 1;
    }
    else if ( "noballs" in ball_data.extras ) {
      innings.illegal_deliveries += 1;
    }
  }
  else {
    innings.legal_deliveries += 1;
  }

  if (ball_data.wickets && ball_data.wickets.length > 0) {
    innings.wickets_down += 1;
  }

  innings.batsmen.on_onstrike = ball_data.batter;
  innings.batsmen.on_offstrike = ball_data.non_striker;
  innings.current_bowler = ball_data.bowler;

  return innings;
}
