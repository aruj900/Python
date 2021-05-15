def validStartingCity(distances,fuel,mpg):
    numberOfCities = len(distances)

    for idx in range(len(distances)):
        milesRemaining = 0
        for currentCity in range(idx,idx+numberOfCities):
            if milesRemaining < 0:
                continue 
            currentCity = currentCity % numberOfCities

            fuelFromCurrentCity = fuel[currentCity]
            distanceToNextCity = distances[currentCity]
            milesRemaining = fuelFromCurrentCity* mpg - distanceToNextCity
        if milesRemaining >= 0:
            return idx
    return -1

