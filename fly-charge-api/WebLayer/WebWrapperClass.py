
# candidate matrix initialisation

candidateMatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Dictionary containing longitudes and latitudes of residential areas
gpsResidentialAreas={1: [42.3,83.1],
                     2: [42.3,83],
                     3: [42.2,83],
                     4: [42.2,83.1],
                     5: [42.3,82.9],
                     6: [42.2,83.9],
                     7: [42.1,83.1],
                     8: [42.2,82.8],
                     9: [42.3,82.7],
                     10: [42,82.6]}

# dictionary containing longitudes and latitudes of existing rechargeing stations
gpsExistingChargingStations = {1: [42.2, 83],
                               2: [42.3, 83],
                               3: [42.3, 83.1],
                               4: [42.3, 83],
                               5: [42.2, 82.9],
                               6: [42.3, 82.8],
                               7: [42.2, 82.8],
                               8: [42.1,83.1],
                               9: [42, 82.7],
                               10: [42.1, 82.6]}



# dictionary containing longitudes and latitudes of high activity areas
haAreas = {1: [42.3, 83],
           2: [42.3, 82.9],
           3: [42.3,82.8],
           4: [42.31, 82.9],
           }

# dictionary containing longitudes and latitudes of medium activity areas
maAreas = {1:[42.3,83.1],
           2:[42.3,83],
           3:[42.2,83],
           4:[42.2,83.1],
           5:[42.3,82.9],
           6:[42.23,83],
           7:[42.3,82.8],
           8:[42,82.6],
           9:[42.1,82.8],
           10:[42.1,83]}

# dictionary containing longitudes and latitudes of low activity areas
laAreas = {1: [42.3, 82.9],
           2: [42.2, 83],
           3: [42.1, 82.9],
           4: [42, 83],
           5: [42.1, 83],
           6: [42.3, 82.7],
           7: [42.2, 82.7],
           8: [42.2, 82.6],
           9: [42.2, 82.9],
           10: [42, 82.7],
           11: [42, 82.5],
           12: [42, 82.6],
           13: [42.1, 82.6],
           14: [42.1, 82.5],
           15: [42.1, 82.7],
           16: [42.1, 83]}




# array containing longitudes of highways
lonHighway = [82.9, 82.6 ]

# array containing latitudes of highways
latHighway = [42.3, 42.2 , 42.1 ]



###################################################################

#### Converting GPS data to index


def convertGPStoIndex(lat,lon):

    latindex = int(((42.3 - lat)*111)/5)
    lonindex = int(((83.1-lon)*85)/5)

    if latindex > 5:
        latindex = 5

    if latindex < 0:
        latindex = 0

    if lonindex > 9:
        lonindex = 9

    if lonindex < 0:
        lonindex = 0

    arrindex = [latindex, lonindex]
    return arrindex


#### Converting index data to GPS


def convertIndextoGPS(latindex, lonindex):

    lat = 42.3 - ((((2*latindex + 1)/2)*5) / 111)
    lon = 83.1 - ((((2*lonindex + 1)/2)*5) / 85)

    arrindex = [lat, lon]

    return arrindex


# matrix showing areas with the number of already existing charging stations
# noOfChargingStationsInArea[][] = i  i.e. area represented by this element has 'i' charging stations already

#initialising 6*10 array

def findCandidatesForChargingStations():

    noOfChargingStationsInArea = [[0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    for key in gpsExistingChargingStations:

        arr = gpsExistingChargingStations[key]
        arrin = convertGPStoIndex(arr[0], arr[1])
        noOfChargingStationsInArea[arrin[0]][arrin[1]] = noOfChargingStationsInArea[arrin[0]][arrin[1]]  + 1


    # matrix showing areas with level of activity
    # activityInArea[][] = i  i.e. area represented by this element has activity level 'i'

    activityInArea = [["low", "low", "low", "low", "low", "low", "low", "low", "low", "low"],
                      ["low", "low", "low", "low", "low", "low", "low", "low", "low", "low"],
                      ["low", "low", "low", "low", "low", "low", "low", "low", "low", "low"],
                      ["low", "low", "low", "low", "low", "low", "low", "low", "low", "low"],
                      ["low", "low", "low", "low", "low", "low", "low", "low", "low", "low"],
                      ["low", "low", "low", "low", "low", "low", "low", "low", "low", "low"]]


    for key in haAreas:

        arr = haAreas[key]
        arrin = convertGPStoIndex(arr[0], arr[1])
        activityInArea[arrin[0]][arrin[1]]  = "high"


    for key in maAreas:

        arr = maAreas[key]
        arrin = convertGPStoIndex(arr[0], arr[1])
        activityInArea[arrin[0]][arrin[1]]  = "medium"

    # matrix showing areas with highway
    # highwayInArea[][] = i  i.e. area represented by this element has highway if i=1

    highwayInArea =   [[0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for key in lonHighway:

        arr = key
        arrin = int(((83.1-arr)*85)/5)

        if arrin > 9:
            arrin = 9

        if arrin < 0:
            arrin = 0

        for k in range(6):
            highwayInArea[k][arrin] = 1

    for key in latHighway:

        arr = key
        arrin = int(((42.3 - arr)*111)/5)

        if arrin > 5:
            arrin = 5

        if arrin < 0:
            arrin = 0

        for k in range(10):
            highwayInArea[arrin][k] = 1


    # matrix showing residential areas
    # residenceInArea[][] = i  i.e. area represented by this element has residences if i=1

    residenceInArea = [[0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    for key in gpsResidentialAreas:

        arr = gpsResidentialAreas[key]
        arrin = convertGPStoIndex(arr[0], arr[1])
        residenceInArea[arrin[0]][arrin[1]]  = 1



    #####################################################
    #### Creating final possibility matrix
    ######################################################




    for i in range(6):
        for j in range(10):

            if residenceInArea[i][j] == 1:

                candidateMatrix[i][j] = 0

            elif highwayInArea[i][j] == 1:

                candidateMatrix[i][j] = 0

            elif noOfChargingStationsInArea[i][j] > 2:

                candidateMatrix[i][j] = 0;

            elif noOfChargingStationsInArea[i][j] > 1 and  activityInArea[i][j] == "medium":

                candidateMatrix[i][j] = 0;

            elif noOfChargingStationsInArea[i][j] > 0 and  activityInArea[i][j] == "low":

                candidateMatrix[i][j] = 0;

            else:
                candidateMatrix[i][j] = 1;


def getPrimaryCandidates(noOfChargingStations):
    count = 0
    findCandidatesForChargingStations()
    for i in range(6):
        for j in range(10):

            if (candidateMatrix[i][j]):
                count = count + 1
                print(i, j)


def getChargingStationsNeeded(noOfChargingStations):
    getPrimaryCandidates(noOfChargingStations)





#getChargingStationsNeeded()