import aoc_cas.aoc2022.day13 as aoc

testData = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip()


def testPartA():
    assert aoc.part_a(testData) == 13


def testPartB():
    assert aoc.part_b(testData) == 140


if __name__ == "__main__":
    testPartA()
    testPartB()
