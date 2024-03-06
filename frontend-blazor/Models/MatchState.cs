namespace frontend_blazor.Models {
  class BatsmanStat {
    string FullName, FName, LName;
    int RunsScored, BallsFaced, Fours, Sixes;
  }

  class BowlerStat {
    string FullName, FName, LName;
    int DeliveriesBowled, RunsGiven, WicketsTaken, LegalDeliveriesBowled;
  }

  class Innings {
    string BattingTeam, BowlingTeam;
    List<BatsmanStat> BatsmanStats;
    List<BowlerStat> BowlerStats;

    int LegalDeliveriesBowled, DeliveriesBowled, Score, Extras, WicketsFallen;
    BatsmanStat? OnstrikeBatsman, OffstrikeBatsman;
    BowlerStat? CurrentBowler;

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
  }

  class MatchState {
    Innings FirstInnings, SecondInnings;
    List<string> Teams;
    Dictionary<string, List<string>> TeamPlayers;

    Toss TossDetails;

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
