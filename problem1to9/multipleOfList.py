def isMultipleOfList(number,listOfNumbers):
    for factor in listOfNumbers:
        if number % factor == 0:
            return True
    return False
