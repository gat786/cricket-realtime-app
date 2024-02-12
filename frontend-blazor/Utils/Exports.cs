namespace frontend_blazor.Utils;

public class Exports {
  private IConfiguration Configuration;
  public string? PlayersUrl, TeamsUrl, ScoreUrl;
  public Exports(){
    if (Configuration!= null){
      PlayersUrl  = Configuration["Urls:Players"];
      TeamsUrl    = Configuration["Urls:Teams"];
      ScoreUrl    = Configuration["Urls:Score"];
    }
  }
}
