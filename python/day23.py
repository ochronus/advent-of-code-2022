from collections import defaultdict

InputStrings = []
with open("../input/day23.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputStrings.append(Line)

InitialPositionSet = set()
for y, f in enumerate(InputStrings):
    for x, c in enumerate(f):
        if c == "#":
            InitialPositionSet.add((x, y))

DirectionCheckList = ["N", "S", "W", "E"]
DirectionFan = {
    "N": (-1, -1, 0, -1, 1, -1),
    "S": (-1, 1, 0, 1, 1, 1),
    "E": (1, 1, 1, 0, 1, -1),
    "W": (-1, -1, -1, 0, -1, 1),
}


def Scoring():
    MinX, MinY, MaxX, MaxY = 2, 2, 2, 2
    for u in StartingElfPositions:
        X, Y = u
        if X < MinX:
            MinX = X
        if X > MaxX:
            MaxX = X
        if Y < MinY:
            MinY = Y
        if Y > MaxY:
            MaxY = Y
    Answer = (MaxX - MinX + 1) * (MaxY - MinY + 1) - len(StartingElfPositions)
    return Answer


StartingElfPositions = InitialPositionSet.copy()
for t in range(10000):
    ElfMoved = False
    ElfMoveDict = defaultdict()
    ElfProposalsSet = set()
    StandoffSet = set()
    for u in StartingElfPositions:
        X, Y = u
        ProposeMove = None
        NeedMove = False
        for FX in [-1, 0, 1]:
            for FY in [-1, 0, 1]:
                if FX == 0 and FY == 0:
                    continue
                HX, HY = X + FX, Y + FY
                if (HX, HY) in StartingElfPositions:
                    NeedMove = True
                    break
        if NeedMove:
            for d in DirectionCheckList:
                DX1, DY1, DX2, DY2, DX3, DY3 = DirectionFan[d]
                NX1, NY1, NX2, NY2, NX3, NY3 = (
                    X + DX1,
                    Y + DY1,
                    X + DX2,
                    Y + DY2,
                    X + DX3,
                    Y + DY3,
                )
                if (
                    (NX1, NY1) not in StartingElfPositions
                    and (NX2, NY2) not in StartingElfPositions
                    and (NX3, NY3) not in StartingElfPositions
                ):
                    ProposeMove = (NX2, NY2)
                    break
        if ProposeMove in StandoffSet:
            ProposeMove = None
        if ProposeMove in ElfProposalsSet:
            StandoffSet.add(ProposeMove)
            ProposeMove = None
        if ProposeMove != None:
            ElfProposalsSet.add(ProposeMove)
        ElfMoveDict[u] = ProposeMove

    ElfEndPositions = set()
    for u in StartingElfPositions:
        if ElfMoveDict[u] in StandoffSet:
            ElfMoveDict[u] = None
            ElfEndPositions.add(u)
        elif ElfMoveDict[u] == None:
            ElfEndPositions.add(u)
        else:
            ElfEndPositions.add(ElfMoveDict[u])
            ElfMoved = True
    StartingElfPositions = ElfEndPositions.copy()
    MoveDirection = DirectionCheckList.pop(0)
    DirectionCheckList.append(MoveDirection)
    if t == 9:
        Part1Answer = Scoring()
    if not (ElfMoved):
        Part2Answer = t + 1
        break

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")
