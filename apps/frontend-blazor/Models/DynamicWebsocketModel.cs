using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
  public class DynamicWebsocketModel<T> {

    [JsonPropertyName("type")]
    public string? Type { get; set; }

    [JsonPropertyName("data")]
    public T? Data { get; set; }
  }

  public class DetailedMatchInfoWSMessage : DynamicWebsocketModel<MatchDataDetailed> {}
  public class BallDataWSMessage : DynamicWebsocketModel<BallDataRoot> {}
  public class TextWSMessage : DynamicWebsocketModel<Message> {}

  public class ResultWsMessage : DynamicWebsocketModel<MatchResult> {}
}
