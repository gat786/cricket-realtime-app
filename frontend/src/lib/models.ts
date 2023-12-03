export type Match = {
  match_title: string;
  match_player_gender: string;
  match_date: string;
  match_file_id: string;
  match_game_type: string;
  match_level: string;
}

export type LiveScore = {
  live_score: number;
  wickets_fallen: number;
  overs_bowled: number;
  balls_bowled_in_current: number;
  current_bowler: string;
  onstrike_batsman: string;
  offstrike_batsman: string;
  batsmen_already_out: string[];
}
