def MoveElevator(brackets):

    floor = 0

    for el in brackets:
        if(el == '('):
            floor = floor + 1
        elif(el == ')'):
            floor = floor - 1
        else:
            raise Exception('The input contained an invalid command character')

    return floor

