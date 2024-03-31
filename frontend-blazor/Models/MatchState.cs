namespace frontend_blazor.Models {
  public class BatsmanStat {
    public string? FullName, FName, LName;
    public int RunsScored, BallsFaced, Fours, Sixes = 0;

    public BatsmanStat(string player_name) {
      this.FullName = player_name;
      this.FName = player_name.Split(" ")[0];
      this.LName = player_name.Replace(this.FName, "").Trim();
    }
  }

  public class BowlerStat {
    public string? FullName, FName, LName;
    public int DeliveriesBowled, RunsGiven, WicketsTaken, LegalDeliveriesBowled;
  }

  public class Innings {
    public string? BattingTeam, BowlingTeam;
    public List<BatsmanStat> BatsmanStats;
    public List<BowlerStat> BowlerStats;

    public int LegalDeliveriesBowled, DeliveriesBowled, Score, Extras, WicketsFallen;
    public BatsmanStat? OnstrikeBatsman, OffstrikeBatsman;
    public BowlerStat? CurrentBowler;

    public Innings(string battingTeam, string bowlingTeam) {
      this.BattingTeam = battingTeam;
      this.BowlingTeam = bowlingTeam;

      this.BatsmanStats = new List<BatsmanStat>();
      this.BowlerStats = new List<BowlerStat>();

      this.LegalDeliveriesBowled = 0;
      this.DeliveriesBowled = 0;
      this.Score = 0;
      this.Extras = 0;
      this.WicketsFallen = 0;

      this.OnstrikeBatsman = null;
      this.OffstrikeBatsman = null;

      this.CurrentBowler = null;
    }

    public void UpdateInningsScore(BallDataRoot ballDataRoot) {
      this.Score                    += ballDataRoot.Data.Runs.Total;
      this.DeliveriesBowled         += 1;
      this.LegalDeliveriesBowled    += 1;
      this.Extras                   += ballDataRoot.Data.Runs.Extras;

      //  when a inning is starting
      if (this.OnstrikeBatsman is null && this.OffstrikeBatsman is null) {
        BatsmanStat batsmanStat = new BatsmanStat(ballDataRoot.Data.Batter);
        BatsmanStat offStrikeBatsmanStat = new BatsmanStat(ballDataRoot.Data.NonStriker);
        this.OnstrikeBatsman = batsmanStat;
        this.OffstrikeBatsman = offStrikeBatsmanStat;

        this.BatsmanStats.Add(batsmanStat);
        this.BatsmanStats.Add(offStrikeBatsmanStat);
      }

      // update score
      foreach(var player in this.BatsmanStats) {
        if (player.FullName == ballDataRoot.Data.Batter) {
          player.BallsFaced += 1;
          player.RunsScored += ballDataRoot.Data.Runs.Batter;
        }
      }

    }
  }

  public class MatchState {
    public Innings FirstInnings, SecondInnings;
    public List<string> Teams;
    public Dictionary<string, List<string>> TeamPlayers;

    public Toss TossDetails;

    public MatchState(MatchDataDetailed matchData) {
      this.TossDetails = matchData.Toss;
      this.Teams = matchData.Teams;
      this.TeamPlayers = matchData.Players;

      string tossWinningTeam = this.TossDetails.Winner;
      string tossLosingTeam  = this.Teams[0] == tossWinningTeam ? this.Teams[1] : this.Teams[0];
      string tossDecision    = this.TossDetails.Decision;

      if (tossDecision == "bat") {
        this.FirstInnings   = new Innings(tossWinningTeam, tossLosingTeam);
        this.SecondInnings  = new Innings(tossLosingTeam, tossWinningTeam);
      } else {
        this.FirstInnings   = new Innings(tossLosingTeam, tossWinningTeam);
        this.SecondInnings  = new Innings(tossWinningTeam, tossLosingTeam);
      }
    }
  }
}
