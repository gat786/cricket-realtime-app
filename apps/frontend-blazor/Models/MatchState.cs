namespace frontend_blazor.Models {
  public class BatsmanStat {
    public string? FullName, FName, LName;
    public int RunsScored, BallsFaced, Fours, Sixes = 0;

    public bool hasBeenDismissed = false;

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
    public int? InningNumber;
    public List<BatsmanStat> BatsmanStats;
    public List<BowlerStat> BowlerStats;

    public int LegalDeliveriesBowled, DeliveriesBowled, Score, Extras, WicketsFallen;
    public BatsmanStat? OnstrikeBatsman, OffstrikeBatsman;
    public BowlerStat? CurrentBowler;

    public Innings(string battingTeam, string bowlingTeam, int InningNumber) {
      this.BattingTeam = battingTeam;
      this.BowlingTeam = bowlingTeam;
      this.InningNumber = InningNumber;

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
      if (ballDataRoot is null) {
        return;
      }

      this.Score                    += ballDataRoot.Data.Runs.Total;
      this.DeliveriesBowled         += 1;
      this.LegalDeliveriesBowled    += 1;
      this.Extras                   += ballDataRoot.Data.Runs.Extras;

      //  when a inning is starting
      if (this.OnstrikeBatsman is null && this.OffstrikeBatsman is null) {
        BatsmanStat batsmanStat = new BatsmanStat(ballDataRoot.Data.Batter);
        this.OnstrikeBatsman = batsmanStat;
        this.BatsmanStats.Add(batsmanStat);

        BatsmanStat offStrikeBatsmanStat = new BatsmanStat(ballDataRoot.Data.NonStriker);
        this.OffstrikeBatsman = offStrikeBatsmanStat;
        this.BatsmanStats.Add(offStrikeBatsmanStat);
      }

      // update score
      foreach(var player in this.BatsmanStats) {
        if (player.FullName == ballDataRoot.Data.Batter) {
          player.BallsFaced += 1;
          player.RunsScored += ballDataRoot.Data.Runs.Batter;
          if (ballDataRoot.Data.Runs.Batter == 4) {
            player.Fours += 1;
          } else if (ballDataRoot.Data.Runs.Batter == 6) {
            player.Sixes += 1;
          }
        }
      }

      // if a wicket has been taken
      if (ballDataRoot?.Data.Wickets is not null) {
        this.BatsmanStats.Find(player => player.FullName == ballDataRoot.Data?.Wickets[0]?.PlayerOut).hasBeenDismissed = true;
        this.BowlerStats.Find(bowler => bowler.FullName == ballDataRoot.Data.Bowler).WicketsTaken += 1;
        this.WicketsFallen += 1;
      }

      // if a new batsman is on strike and we dont have him in batsmanstats
      if (this.BatsmanStats.Find(player => player.FullName == ballDataRoot.Data.Batter) is null) {
        BatsmanStat batsmanStat = new BatsmanStat(ballDataRoot.Data.Batter);
        this.OnstrikeBatsman = batsmanStat;
        this.BatsmanStats.Add(batsmanStat);
      }


      if(this.BowlerStats.Find(bowler => bowler.FullName == ballDataRoot.Data.Bowler) is null) {
        BowlerStat bowlerStat = new BowlerStat();
        bowlerStat.FullName = ballDataRoot.Data.Bowler;
        bowlerStat.DeliveriesBowled = 1;
        if(ballDataRoot?.Data?.Runs?.Extras == 0) {
          bowlerStat.LegalDeliveriesBowled += 1;
        }
        bowlerStat.RunsGiven = ballDataRoot.Data.Runs.Total;
        this.BowlerStats.Add(bowlerStat);
      }else {
        var bowlerToUpdate = this.BowlerStats.Find(bowler => bowler.FullName == ballDataRoot.Data.Bowler);
        bowlerToUpdate.DeliveriesBowled += 1;
        bowlerToUpdate.RunsGiven += ballDataRoot.Data.Runs.Total;
        if(ballDataRoot?.Data?.Runs?.Extras == 0) {
          bowlerToUpdate.LegalDeliveriesBowled += 1;
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
        this.FirstInnings   = new Innings(tossWinningTeam, tossLosingTeam, 0);
        this.SecondInnings  = new Innings(tossLosingTeam, tossWinningTeam, 1);
      } else {
        this.FirstInnings   = new Innings(tossLosingTeam, tossWinningTeam, 0);
        this.SecondInnings  = new Innings(tossWinningTeam, tossLosingTeam, 1);
      }
    }
  }
}
