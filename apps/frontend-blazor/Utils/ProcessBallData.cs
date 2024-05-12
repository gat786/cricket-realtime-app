using frontend_blazor.Models;

namespace frontend_blazor.Utils {
  public class ProcessBallData{
    public MatchState GetUpdatedMatchState(MatchState initialMatchState, BallDataRoot ballData) {
      MatchState updatedMatchState = initialMatchState;
      if (ballData.Innings == 0 ){
        // update first innings
        
      }
      else if (ballData.Innings == 1) {
        // update second innings
      }
      return updatedMatchState;
    }
  }
}
