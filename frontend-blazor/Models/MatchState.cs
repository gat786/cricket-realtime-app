namespace frontend_blazor.Models {
  class BatsmanStat {

  }

  class BowlerStat {

  }
  class Innings {
    string battingTeam, bowlingTeam;
    List<BatsmanStat> batsmanStats;
    List<BowlerStat> bowlerStats;

    int legalDeliveriesBowled, deliveriesBowled, score, extras, wicketsFallen;
    string onstrikeBatsman, offstrikeBatsman;
    string currentBowler;

    public Innings() {}
  }
  class MatchState {
    Innings firstInnings = new Innings();
    Innings secondInnings = new Innings();
  }
}
