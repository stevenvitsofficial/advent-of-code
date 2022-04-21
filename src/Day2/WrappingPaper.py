def OrderPaper(width, height, length):

    dim = [width, height, length]

    if(not all([(isinstance(item, float)  or isinstance(item, int)) for item in dim])):
        raise Exception('The input does not consist of numbers only')
    elif(any(item <= 0 for item in dim)):
        raise Exception('The input has negative or 0 numbers')

    dim.sort()

    paperorder = 2*(dim[0]*dim[1]+dim[1]*dim[2]+dim[0]*dim[2])+dim[0]*dim[1]

    return paperorder

