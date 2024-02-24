using System.Text.Json;
using System.Web;

namespace frontend_blazor.Utils {

  public enum WebsocketResponseType {
    Information,
    BallData,
    ErrorMessage,
    Outcome
  }
  public static class ParseWebsocketData {
    public static WebsocketResponseType? GetMessageType(string data) {
      dynamic? dataDynamic = JsonSerializer.Deserialize<dynamic>(data);
      JsonElement type = dataDynamic.GetProperty("type");
      string? messageType = type.GetString();

      if (messageType != null) {
        switch(messageType) {
          case "ball_data":
            Console.WriteLine("We are processing Ball Data");
            return WebsocketResponseType.BallData;
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
