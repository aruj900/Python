def validStartingCity(distances,fuel,mpg):
    numberOfCities = len(distances)
    milesRemaining = 0

    startingCity = 0
    milesRemainingAtCity = 0

    for cityIdx in range(1,numberOfCities):
        distanceFromPrevCity = distances[cityIdx -1]
        fuelFromPrevCity = fuel[cityIdx-1]
        milesRemaining += fuelFromPrevCity*mpg - distanceFromPrevCity
        if milesRemaining < milesRemainingAtCity:
            milesRemainingAtCity = milesRemaining
            startingCity = cityIdx
    return startingCity