using System.Text.Json.Serialization;

namespace frontend_blazor.Models
{
  public record MatchResultBy(
    [property: JsonPropertyName("runs")] int? Runs,
    [property: JsonPropertyName("wickets")] int? Wickets
  );

  public record MatchResult(
      [property: JsonPropertyName("by")] MatchResultBy By,
      [property: JsonPropertyName("winner")] string Winner,
      [property: JsonPropertyName("method")] string? Method
  );
}
