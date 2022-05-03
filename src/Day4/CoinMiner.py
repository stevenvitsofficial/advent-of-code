import hashlib
from src.exceptions import *


def Mine(secretkey):

    if(type(secretkey) != str):
        raise InputValueNotStringError("Input should be a string")

    suffix = 0
    hashstart = '11111'

    while(hashstart != '00000'):
        suffix = suffix + 1
        fullkey = secretkey + str(suffix)
        hash = hashlib.md5(fullkey.encode('utf-8')).hexdigest()
        hashstart = hash[0:5]

    return suffix