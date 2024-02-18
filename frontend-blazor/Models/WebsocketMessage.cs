using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
  public record WebsocketMessage (
    [property: JsonPropertyName("message")] string Message
  );
}
