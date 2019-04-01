from math import sqrt
"""
    Basic Statistic Module
"""

def avarageList(AnyList):
    """
    This method allows us to find the average of a list
    :param AnyList: Any numeric list
    :return:
    """
    anyListLen = len(AnyList)
    sumList    = 0

    for i in range(anyListLen):
        sumList = sumList + AnyList[i]

    return (sumList / anyListLen)

def standardDeviation(AnyList):
    """
    This method allows us to find the standard deviation of a list
    :param AnyList: Any numeric list
    :return:
    """
    anyListLen             = len(AnyList)          #Size of List     N
    responseAvarageList    = avarageList(AnyList)  #Avareage of List X'
    sumList                = 0

    for i in range(anyListLen):
        sumList = sumList + pow((AnyList[i] - responseAvarageList),2)

    sqrtList = ((sumList)/(anyListLen - 1))
    return sqrt(sqrtList)
