using System.Text.Json.Serialization;

public class Match
{
  [JsonPropertyName("match_date")]
  public string? Date { get; set; }

  [JsonPropertyName("match_player_gender")]
  public string? PlayerGender { get; set; }

  [JsonPropertyName("match_level")]
  public string? MatchLevel { get; set; }

  [JsonPropertyName("match_game_type")]
  public string? GameType { get; set; }

  [JsonPropertyName("match_title")]
  public string? Title { get; set; }

  [JsonPropertyName("match_file_id")]
  public string? FileId { get; set; }
  
  [JsonPropertyName("match_teams")]
  public List<string>? Teams { get; set; }

  public override string ToString() {
    return $"(Date: {Date}, Level: {MatchLevel}, Type: {GameType}, Title: {Title}, FileId: {FileId})";
  }
}

public class MatchListResponse
{
  [JsonPropertyName("match_list")]
  public List<Match>? Matches { get; set; }

  public override string ToString() {
    if (Matches == null ) {
      return "";
    }
    else if (Matches.Count < 1)  {
      return "[]";
    }else {
      string data = "";
      foreach(var MatchData in Matches){
        data = data + MatchData.ToString();
      }
      return data;
    }

  }
}
