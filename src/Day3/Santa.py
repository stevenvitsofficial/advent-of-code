from src.Day3.House import House
from src.exceptions import *


def VisitHouses(directions):

    position = [0, 0]
    houses = []

    house = House(position[0], position[1])
    house.Visit()

    houses.append(house)

    for direction in directions:
        if (direction == '^'):
            position[1] = position[1] + 1
        elif (direction == '>'):
            position[0] = position[0] + 1
        elif (direction == 'v'):
            position[1] = position[1] - 1
        elif (direction == '<'):
            position[0] = position[0] - 1
        else:
            #raise Exception('The input contained an invalid command character')
            raise InvalidInputCharacterError('The input contained an invalid command character')

        housevisited = False
        for house in houses:
            if(house.GetCoordinates() == position):
                house.Visit()
                housevisited = True
                break

        if(housevisited == False):
            house = House(position[0], position[1])
            house.Visit()

            houses.append(house)

    return len(houses)
