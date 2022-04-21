def OrderPaper(width, height, length):

    dim = [width, height, length]
    dim.sort()

    paperorder = 2*(dim[0]*dim[1]+dim[1]*dim[2]+dim[0]*dim[2])+dim[0]*dim[1]

    return paperorder
