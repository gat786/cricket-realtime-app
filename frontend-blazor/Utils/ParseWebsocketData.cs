using System.Text.Json;
using System.Web;
using frontend_blazor.Models;

namespace frontend_blazor.Utils {

  public enum WebsocketResponseType {
    Information,
    MatchDetails,
    BallData,
    ErrorMessage,
    Outcome
  }
  public static class ParseWebsocketData {
    public static WebsocketResponseType? GetMessageType(string data) {
      dynamic? dataDynamic = JsonSerializer.Deserialize<dynamic>(data);
      if (dataDynamic is null) {
        return null;
      }
      JsonElement type = dataDynamic.GetProperty("type");
      string? messageType = type.GetString();

      if (messageType != null) {
        switch(messageType) {
          case "ball_data":
            Console.WriteLine("We are processing Ball Data");
            return WebsocketResponseType.BallData;
          case "match_details":
            Console.WriteLine("We have received Match Details");
            return WebsocketResponseType.MatchDetails;
          case "information":
            Console.WriteLine("We are processing information");
            return WebsocketResponseType.Information;
          case "error-message":
            return WebsocketResponseType.ErrorMessage;
          case "outcome":
            return WebsocketResponseType.Outcome;
          default:
            Console.WriteLine("Unable to identify message type");
            return null; 
        }
      }
      return null;
    }

  }
}
