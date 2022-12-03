package days

class Day2 : Day(2) {
    enum class Shape(
        val sign: Char,
        val signPart1: Char,
        val score: Int
    ) {
        ROCK('A', 'X', 1),
        PAPER('B', 'Y', 2),
        SCISSORS('C', 'Z', 3)
    }

    enum class Result(
        val sign: Char,
        val score: Int
    ) {
        LOSE('X', 0),
        DRAW('Y', 3),
        WIN('Z', 6)
    }

    fun decideResult(line: String): Int {
        val shapes = line
            .split(' ')
            .map { c ->
                Shape.values().first { c[0] == it.sign || c[0] == it.signPart1 }
            }

        val resultScore = when (Math.floorMod(shapes.first().score - shapes.last().score, 3)) {
            2 -> 6
            0 -> 3
            1 -> 0
            else -> -1
        }

        return resultScore
    }

    override fun partOne(): Any {
        return inputList.sumOf {
            decideResult(it) + Shape.values().first { shape -> shape.signPart1 == it.last() }.score
        }
    }

    fun decideShape(line: String): Shape {
        val shapeOther = Shape.values().first { it.sign == line.first() }
        val result = Result.values().first { it.sign == line.last() }

        var score = shapeOther.score + (result.score / 3 - 1)

        score = when (score) {
            0 -> 3
            4 -> 1
            else -> score
        }

        return Shape.values().first { it.score == score }
    }

    override fun partTwo(): Any {
        return inputList.sumOf { line ->
            Result.values().first { it.sign == line.last() }.score + decideShape(line).score
        }
    }
}
