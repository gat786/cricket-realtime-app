using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.Extensions.Configuration;
using frontend_blazor.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Components;

namespace frontend_blazor.Data {

  public class DataHelper {
    private IConfiguration Configuration;
    HttpClient client = new HttpClient();
    string TeamsUrl;
    string PlayersUrl;
    string ScoreUrl;

    public DataHelper(IConfiguration configuration){
      // Console.WriteLine("Data helper constructor: ", Configuration);
      Configuration = configuration;
      
    }

    public async Task<Team?> GetTeamData (string TeamName) {
      TeamsUrl    = Configuration["Urls:Teams"];
      PlayersUrl  = Configuration["Urls:Players"];
      ScoreUrl    = Configuration["Urls:ScoreUrl"];
      string TeamDataUrl = $"{TeamsUrl}/{TeamName}";
      string TeamDataString = await client.GetStringAsync(TeamDataUrl);
      Team? TeamData = JsonSerializer.Deserialize<Team>(TeamDataString);
      if (TeamData != null){
        return TeamData;
      }
      return null;
      
    }

    public async Task<MatchListResponse?> GetMatchesList () {
      TeamsUrl    = Configuration["Urls:Teams"];
      PlayersUrl  = Configuration["Urls:Players"];
      ScoreUrl    = Configuration["Urls:ScoreUrl"];
      string matchListUrl = $"{ScoreUrl}/list";
      Console.WriteLine(matchListUrl);
      var response = await client.GetStringAsync(matchListUrl);
      MatchListResponse? matchListResponse = JsonSerializer.Deserialize<MatchListResponse>(response);

      if (matchListResponse != null){
       return matchListResponse; 
      }
      return null;
    }

    public async Task<PlayersSearchResponse?> GetPlayerAsync(string name, string countryName) {
      PlayersUrl = Configuration["Urls:Players"];

      string playersInfoUrl = $"{PlayersUrl}/search";
      var playerSearchModel = new PlayerSearchModel{ Name = name, CountryName = countryName};
      var result = await client.PostAsJsonAsync(playersInfoUrl, playerSearchModel);
      if(result.IsSuccessStatusCode){
        var response = await result.Content.ReadAsStringAsync();
        var playerInfo = JsonSerializer.Deserialize<PlayersSearchResponse>(response);
        return playerInfo;
      }
      return null;
    }
  }
}
