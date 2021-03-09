def classPhoto(redShirts,blueShirts):
    redShirts.sort(reverse = True)
    blueShirts.sort(reverse = True)

    firstRow = 'RED' if redShirts[0] < blueShirts[0] else 'BLUE'

    for idx in range(len(redShirts)):
        redShirt = redShirts[idx]
        blueShirt = blueShirts[idx]

        if firstRow == 'RED':
            if redShirt >= blueShirt:
                return False
        else:
            if blueShirt >= redShirt:
                return False
    return True