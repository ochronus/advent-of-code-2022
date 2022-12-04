
using aoc2022.Utils;

namespace aoc2022;

public class Day04
{
    private IEnumerable<int[][]> _input;
    public Day04()
    {
        _input = FileUtils.DayInputToString("04")
            .Split("\n")
            .Select(_ => _.Split(",")
            .Select(_ => _.Split("-")
            .Select(_ => Convert.ToInt32(_)).ToArray()).ToArray());
    }

    public int Part1() =>
        _input
            .Count(pair => (pair[0][0] <= pair[1][0] && pair[0][1] >= pair[1][1])
                        || (pair[0][0] >= pair[1][0] && pair[0][1] <= pair[1][1]));



    public int Part2() =>
        _input
        .Count(pair => pair.First().Intersect(pair.Last()).Any());
}
