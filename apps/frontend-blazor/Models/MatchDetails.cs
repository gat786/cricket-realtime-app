using System.Text.Json.Serialization;

namespace frontend_blazor.Models
{
  public class By
  {
    [JsonPropertyName("wickets")]
    public int Wickets { get; set; }
  }

  public class MatchDataDetailed
  {
    [JsonPropertyName("balls_per_over")]
    public int BallsPerOver { get; set; }

    [JsonPropertyName("city")]
    public string City { get; set; }

    [JsonPropertyName("dates")] 
    public List<string> Dates { get; set; }

    [JsonPropertyName("event")]
    public EventModel Event { get; set; }
    [JsonPropertyName("gender")]
    public string Gender { get; set; }

    [JsonPropertyName("match_type")]
    public string MatchType { get; set; }
    [JsonPropertyName("match_type_number")]
    public int MatchTypeNumber { get; set; }

    [JsonPropertyName("officials")]
    public OfficialsModel Officials { get; set; }
    [JsonPropertyName("outcome")]
    public OutcomeModel Outcome { get; set; }
    [JsonPropertyName("overs")]
    public int Overs { get; set; }

    [JsonPropertyName("player_of_match")]
    public List<string> PlayerOfMatch { get; set; }
    [JsonPropertyName("players")]
    public Dictionary<string,List<string>> Players { get; set; }
    [JsonPropertyName("registry")]
    public RegistryModel Registry { get; set; }
    [JsonPropertyName("season")]
    public string Season { get; set; }
    [JsonPropertyName("team_type")]
    public string TeamType { get; set; }
    [JsonPropertyName("teams")]
    public List<string> Teams { get; set; }
    [JsonPropertyName("toss")]
    public Toss Toss { get; set; }
    [JsonPropertyName("venue")]
    public string VenueName { get; set; }
  }

  public class EventModel
  {
    [JsonPropertyName("name")]
    public string Name { get; set; }
    [JsonPropertyName("stage")]
    public string Stage { get; set; }
  }

  public class OfficialsModel
  {
    [JsonPropertyName("match_referees")]
    public List<string> MatchReferees { get; set; }
    [JsonPropertyName("reserve_umpires")]
    public List<string> ReserveUmpires { get; set; }
    [JsonPropertyName("tv_umpires")]
    public List<string> tv_umpires { get; set; }
    [JsonPropertyName("umpires")]
    public List<string> Umpires { get; set; }
  }

  public class OutcomeModel
  {
    [JsonPropertyName("winner")]
    public string Winner { get; set; }
    [JsonPropertyName("by")]
    public By ByCause { get; set; }
  }
  public class RegistryModel
  {
    [JsonPropertyName("people")]
    public Dictionary<String, String> People { get; set; }
  }

  public class MatchDetailsRoot
  {
    [JsonPropertyName("message")]
    public string Message { get; set; }

    [JsonPropertyName("match_id")]
    public string MatchId { get; set; }

    [JsonPropertyName("data")]
    public MatchDataDetailed Data { get; set; }
  }

  public class Toss
  {
    [JsonPropertyName("decision")]
    public string Decision { get; set; }
    [JsonPropertyName("winner")]
    public string Winner { get; set; }
  }

}
