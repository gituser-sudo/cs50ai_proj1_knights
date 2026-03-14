from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

IamKnight = Symbol("I am a Knight")
IamKnave = Symbol("I am a Knave")

#   Model                                                   Knowledge
# AKnight  AKnave  BKnight  BKnave  CKnight  CKnave  Query
#   True     False   X        X        X       X               AKnight
#   False    True    X        X        X       X               No solution
#   True      True                                             AKanve
#   False     True                                             No solution

# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(

    # IamKnight,
    # IamKnave,
    # Implication(And(AKnave, IamKnave), False),
    # Implication(And(AKnave, IamKnight), AKnave),
    # Implication(And(AKnight, IamKnave), False),
    # Implication(And(AKnight, IamKnight), AKnight),
    # Or(
    #     And(AKnave, Or(Not(IamKnave), Not(IamKnight))),
    #     And(AKnight, And(IamKnight, IamKnave))
    # )

    Implication(AKnave, IamKnight),
    Implication(AKnave, Not(IamKnave)),
    Implication(AKnight, IamKnight),
    Implication(AKnight, Not(IamKnave)),
    Or(
        Or(Not(IamKnight), Not(IamKnave)),
        And(IamKnight, IamKnave)
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
   AKnave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    AKnave, BKnight
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    AKnight, BKnave, CKnight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
