import BasicStatistic

"""
    DataTransformation Module
"""

def normalization(AnyList):
    """
    Min-max normalization method is applied to convert data between 0 and 1 numerical values
    :param AnyList: Any numeric list
    :return:
    """

    anyListLen = len(AnyList)
    normalizationList = []
    maxValue = max(AnyList)
    minValue = min(AnyList)

    for i in range(anyListLen):
        normalizationList.append(((AnyList[i] - minValue) / (maxValue - minValue)))
    return normalizationList

def zScore(AnyList):
    """
    This method is based on converting data into new values, taking into account the mean and standard errors.
    :param AnyList: Any numeric list
    :return:
    """
    anyListLen        = len(AnyList)
    avarageList       = BasicStatistic.avarageList(AnyList) #Listenin Ortalaması X'
    standardDeviation = BasicStatistic.standardDeviation(AnyList) #Standart Sapma
    zScoreList        = []

    for i in range(anyListLen):
        zScoreList.append((AnyList[i] - avarageList)/standardDeviation)
    return zScoreList
