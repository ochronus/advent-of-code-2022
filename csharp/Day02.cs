using aoc2022.Utils;

namespace aoc2022;

public class Day02
{
    private string[] _input;

    public Day02()
    {
        var strInput = FileUtils.DayInputToString("02");
        _input = strInput.Split("\n");
    }

    public int Part1() =>
        _input
        .Select(_ => (_[0] - '@', _[2] - 'W'))
            .Select(_ => _ switch
            {
                var (p1, p2) when p1 == p2 => 3 + p2,
                (1, 2) => 8,
                (2, 3) => 9,
                (3, 1) => 7,
                var (_, p2) => p2
            })
            .Sum();


    public int Part2() =>
        _input
        .Select(_ => (_[0] - '@', _[2] - 'W'))
            .Select(_ =>
            {
                var (p1, p2) = _;
                return p2 == 1 ? (--p1 < 1 ? 3 : p1) : p2 == 3 ? 6 + (++p1 > 3 ? 1 : p1) : 3 + p1;
            })
            .Sum();

}