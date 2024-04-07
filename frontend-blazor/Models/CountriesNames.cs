using System.Text.Json.Serialization;

namespace frontend_blazor.Models {
    public record CountriesNames(

        [property: JsonPropertyName("countries")] IReadOnlyList<string> Countries
    );
}
