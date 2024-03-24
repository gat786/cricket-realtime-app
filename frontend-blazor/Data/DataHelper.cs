using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.Extensions.Configuration;
using frontend_blazor.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Components;

namespace frontend_blazor.Data {

  public class DataHelper {

    [Inject]
    private IConfiguration Configuration {get; set;}
    HttpClient client = new HttpClient();
    string TeamsUrl;
    string PlayersUrl;
    string ScoreUrl;

    public DataHelper(){
      // Console.WriteLine("Data helper constructor: ", Configuration);
      
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

    public async Task<Player> GetPlayerAsync() {
      PlayersUrl = Configuration["Urls:Players"];

      return 0;
    }
  }
}
