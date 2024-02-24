using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
  // Root myDeserializedClass = JsonSerializer.Deserialize<Root>(myJsonResponse);
    public record Player(
        [property: JsonPropertyName("firstname")] string Firstname,
        [property: JsonPropertyName("lastname")] string Lastname,
        [property: JsonPropertyName("fullname")] string Fullname,
        [property: JsonPropertyName("id")] int Id = 1,
        [property: JsonPropertyName("image_path")] string ImagePath = "",
        [property: JsonPropertyName("dateofbirth")] string Dateofbirth = "",
        [property: JsonPropertyName("gender")] string Gender = "",
        [property: JsonPropertyName("battingstyle")] string Battingstyle = "",
        [property: JsonPropertyName("bowlingstyle")] string Bowlingstyle = "",
        [property: JsonPropertyName("position")] string Position = "",
        [property: JsonPropertyName("updated_at")] DateTime UpdatedAt = new DateTime(),
        [property: JsonPropertyName("continent_id")] int ContinentId = 0,
        [property: JsonPropertyName("continent_name")] string ContinentName = "",
        [property: JsonPropertyName("country_id")] int CountryId = 0,
        [property: JsonPropertyName("country_name")] string CountryName = "",
        [property: JsonPropertyName("country_image_path")] string CountryImagePath = ""
    );

    public record PlayersSearchResponse(
        [property: JsonPropertyName("players")] IReadOnlyList<Player> Players
    );


}
