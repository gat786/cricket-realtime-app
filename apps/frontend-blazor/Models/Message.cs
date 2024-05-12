using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
  public record Message (
    [property: JsonPropertyName("message")] string MessageText
  );
}
