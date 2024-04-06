using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
  public record PlayerSearchModel {
    [JsonPropertyName("name")]
    public string Name {get; set;}
    [JsonPropertyName("country_name")]
    public string CountryName {get;set;}
  }
}
