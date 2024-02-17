// Root myDeserializedClass = JsonConvert.DeserializeObject<Root>(myJsonResponse);
    public class By
    {
        public int wickets { get; set; }
    }

    public class Data
    {
        public int balls_per_over { get; set; }
        public string city { get; set; }
        public List<string> dates { get; set; }
        public Event @event { get; set; }
        public string gender { get; set; }
        public string match_type { get; set; }
        public int match_type_number { get; set; }
        public Officials officials { get; set; }
        public Outcome outcome { get; set; }
        public int overs { get; set; }
        public List<string> player_of_match { get; set; }
        public Players players { get; set; }
        public Registry registry { get; set; }
        public string season { get; set; }
        public string team_type { get; set; }
        public List<string> teams { get; set; }
        public Toss toss { get; set; }
        public string venue { get; set; }
    }

    public class Event
    {
        public string name { get; set; }
        public string stage { get; set; }
    }

    public class Officials
    {
        public List<string> match_referees { get; set; }
        public List<string> reserve_umpires { get; set; }
        public List<string> tv_umpires { get; set; }
        public List<string> umpires { get; set; }
    }

    public class Outcome
    {
        public string winner { get; set; }
        public By by { get; set; }
    }
    public class Players
    {
        public List<string> Australia { get; set; }
        public List<string> England { get; set; }
    }

    public class Registry
    {
        public Dictionary<String,String> people { get; set; }
    }

    public class MatchDetailsRoot
    {
        public string message { get; set; }
        public string match_id { get; set; }
        public Data data { get; set; }
    }

    public class Toss
    {
        public string decision { get; set; }
        public string winner { get; set; }
    }
