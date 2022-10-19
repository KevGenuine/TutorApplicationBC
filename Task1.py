def Task1(intList: list[int]):
    multiplier = 1
    Sum = 0

    # takes the last int in the list, gets multiplied with a multiplier, then added to Sum
    for i in reversed(intList):
        Sum += i * multiplier
        multiplier *= 10

    # for i in range(len(intList)):
    #     Sum += intList[-i-1] * multiplier
    #     multiplier *= 10

    return Sum