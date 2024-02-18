using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
  // Root myDeserializedClass = JsonSerializer.Deserialize<Root>(myJsonResponse);
    public record Data(
        [property: JsonPropertyName("batter")] string Batter,
        [property: JsonPropertyName("bowler")] string Bowler,
        [property: JsonPropertyName("non_striker")] string NonStriker,
        [property: JsonPropertyName("runs")] Runs Runs,
        [property: JsonPropertyName("wickets")] Wickets? Wickets,
        [property: JsonPropertyName("extras")] Dictionary<string, int>? Extras
    );

    public record Wickets(
      [property: JsonPropertyName("kind")] string Kind,
      [property: JsonPropertyName("player_out")] string PlayerOut
    );

    public record BallDataRoot(
        [property: JsonPropertyName("over")] int Over,
        [property: JsonPropertyName("delivery")] int Delivery,
        [property: JsonPropertyName("innings")] int Innings,
        [property: JsonPropertyName("data")] Data Data
    );

    public record Runs(
        [property: JsonPropertyName("batter")] int Batter,
        [property: JsonPropertyName("extras")] int Extras,
        [property: JsonPropertyName("total")] int Total
    );


}
