import random
import math

def distanceBtConsec(arrA, arrB):

    distance = math.sqrt((arrA[0]-arrB[0])*(arrA[0]-arrB[0])  + (arrA[1]-arrB[1])*(arrA[1]-arrB[1]))
    return distance

def optimizationFunction(solutionArray, noOfChargingStations):
    value = 0

    for i in range (noOfChargingStations-1):

        value += distanceBtConsec(solutionArray[i], solutionArray[i+1])
        return value


def getOptimizedPositionsGA(candidateArray, noOfChargingStations):

    finalOptimizationScore = 0
    primaryArray = []
    newArray = []
    #print(candidateArray, noOfChargingStations)

    if noOfChargingStations == 1:
        newArray.append(candidateArray[0])
        return newArray

    for i in range(10):
        numberrand = random.sample(range(0, 2*noOfChargingStations ), noOfChargingStations)
        solutionSet = []

        for j in numberrand:

            solutionSet.append(candidateArray[j])

        optimizationScore = optimizationFunction(solutionSet,noOfChargingStations)

        if optimizationScore > finalOptimizationScore:

            finalOptimizationScore = optimizationScore
            primaryArray.clear()
            for p in range(noOfChargingStations):
                primaryArray.append(solutionSet[p])

    print(primaryArray)
    return primaryArray


#arrayA = [[0, 0], [1, 2]]
#getOptimizedPositionsGA(arrayA, 1)