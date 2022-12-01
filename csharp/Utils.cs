namespace aoc2022.Utils
{ 
    static class FileUtils
    {
        public static string DayInputToString(string day)
        {
            return File.ReadAllText($"../input/day{day}.txt");
        }
    }
}