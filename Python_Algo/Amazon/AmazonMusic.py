def pairs(songs):
    target = 60
    output =  []
    n = len(songs)
    dic = {}
    for song in songs:
        if target - song in dic:
            output.append([target - song, song])
        else:
            dic[song] = True
    return len(output)

print(pairs([10,50,90,30]))
        