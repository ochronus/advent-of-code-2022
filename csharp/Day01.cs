using aoc2022.Utils;

namespace aoc2022;

public class Day01
{
    private List<int> _input;

    public Day01()
    {
        var strInput = FileUtils.DayInputToString("01");
        _input = strInput
            .Split("\n")
            .Aggregate(new List<int> { 0 }, (results, s) =>
            {
                if (s == "")
                {
                    results.Add(0);
                }
                else
                {
                    results[^1] += int.Parse(s);
                }

                return results;
            });
    }

    public int Part1() =>
        _input
            .Max();


    public int Part2() =>
        _input
            .OrderByDescending(i => i)
            .Take(3)
            .Sum();

}