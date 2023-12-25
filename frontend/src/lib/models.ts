export type Match = {
  match_title: string;
  match_player_gender: string;
  match_date: string;
  match_file_id: string;
  match_game_type: string;
  match_level: string;
  match_teams: string[];
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

export type MatchResponse = {
  slug: string;
  data: MatchResponseApi;
}

export interface MatchResponseApi {
  match_id: string;
  data:     Data;
}

export interface Data {
  balls_per_over:    number;
  city:              string;
  dates:             Date[];
  event:             Event;
  gender:            string;
  match_type:        string;
  match_type_number: number;
  officials:         Officials;
  outcome:           Outcome;
  overs:             number;
  players:           Players;
  registry:          Registry;
  season:            string;
  team_type:         string;
  teams:             string[];
  toss:              Toss;
  venue:             string;
}

export interface Event {
  name:         string;
  match_number: number;
  group:        string;
}

export interface Officials {
  match_referees: string[];
  tv_umpires:     string[];
  umpires:        string[];
}

export interface Outcome {
  result: string;
}

export interface Players {
  Pakistan: string[];
  Zimbabwe: string[];
}

export interface Registry {
  people: Map<string, string>;
}

export interface Toss {
  decision: string;
  winner:   string;
}

export type Innings = {
  score: number;
  wickets_down: number;
  legal_deliveries: number;
  illegal_deliveries: number;
  extras: number;
  batsmen: {
    on_onstrike: BatsmanScore;
    on_offstrike: BatsmanScore;
  }
  current_bowler: string;
  batsmans: BatsmanInnings;
  balling: BallingInnings;
}

export const defaultInnings : Innings = {
  batsmans: [],
  balling: [],
  score: 0,
  wickets_down: 0,
  legal_deliveries: 0,
  illegal_deliveries: 0,
  extras: 0,
  batsmen: {
    on_offstrike: {
      name: "Loading",
      score: 0,
    },
    on_onstrike: {
      name: "Loading",
      score: 0,
    },
  },
  current_bowler: "",
}

export type BatsmanInnings = BatsmanScore[];

export type BatsmanScore = {
  name: string;
  score: number;
}

export type BallingInnings = BallingStats[];

export type BallingStats = {
  name: string;
  deliveries: number;
  runs_given: number;
}

export interface BallDataWithMeta {
  over: number;
  delivery: number;
  innings: number;
  data: BallData;
}

export interface BallData {
  batter:      string;
  bowler:      string;
  non_striker: string;
  extras:      Extras | null;
  runs:        Runs;
  wickets:     Wicket[] | null;
}

export interface Extras {
  legbyes: number | null;
  wides:   number | null;
  noballs: number | null;
}

export interface Runs {
  batter: number;
  extras: number;
  total:  number;
}

export interface Wicket {
  player_out: string;
  fielders:   Fielder[] | null;
  kind:       string;
}

export interface Fielder {
  name: string;
}

export interface TeamData {
  id: number
  name: string
  code: string
  image_path: string
  country_id: number
  national_team: boolean
  updated_at: string
}
