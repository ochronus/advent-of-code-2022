using aoc2022.Utils;

namespace aoc2022;

public class Day03
{
    private string[] _input;

    public Day03()
    {
        var strInput = FileUtils.DayInputToString("03");
        _input = strInput.Split("\n");
    }

    public int Part1() =>
        _input
            .Select(GetCommonItem)
            .Select(GetItemPriority)
            .Sum();


    public int Part2() =>
        _input
            .Chunk(3)
            .Select(GetBadgeItem)
            .Select(GetItemPriority)
            .Sum();

    private static char GetBadgeItem(string[] items)
    {
        foreach (var item in items[0])
            if (items[1].Contains(item) && items[2].Contains(item))
                return item;
        throw new("No badge found");
    }

    private static char GetCommonItem(string sack)
    {
        var mid = sack.Length / 2;
        var chr = sack.ToCharArray();
        var commonItem = chr.Take(mid).ToArray().Intersect(chr.Skip(mid).ToArray());
        return commonItem.First();
    }

    private static int GetItemPriority(char item)
        => item is >= 'a' ? item - 'a' + 1 : item - 'A' + 27;
}