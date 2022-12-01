package days

class Day1 : Day(1) {

    private var elves: List<Elf> = emptyList()

    private data class Elf(val calories: List<Int>)

    override fun partOne(): Any {
        elves = inputString.split("\n\n").map { group -> Elf(group.split("\n").filter { it.length > 0 }.map { it.toInt() }) }
        return elves.maxOf { it.calories.sum() }
    }

    override fun partTwo(): Any {
        return elves.map { it.calories.sum() }.sortedDescending().take(3).sum()
    }
}
