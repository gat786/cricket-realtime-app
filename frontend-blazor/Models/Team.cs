using System.Text.Json.Serialization;
using frontend_blazor.Components.Pages;

public class Team
{
  [JsonPropertyName("id")]
  public long Id { get; set; }

  [JsonPropertyName("name")]
  public string Name { get; set; }

  [JsonPropertyName("code")]
  public string Code { get; set; }

  [JsonPropertyName("image_path")]
  public Uri ImagePath { get; set; }

  [JsonPropertyName("country_id")]
  public long CountryId { get; set; }

  [JsonPropertyName("national_team")]
  public bool NationalTeam { get; set; }

  [JsonPropertyName("updated_at")]
  public DateTimeOffset UpdatedAt { get; set; }
}
