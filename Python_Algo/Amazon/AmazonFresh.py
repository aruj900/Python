def isCustomerWinner(codeList,shoppingCart):
    if not codeList: return 1
    if not shoppingCart: return 0
    i,j = 0,0
    while i < len(codeList) and j + len(codeList[i]) <= len(shoppingCart):
        match = True
        for k in range(len(codeList[i])):
            if codeList[i][k] != 'anything' and codeList[i][k] != shoppingCart[j+k]:
                match = False
                break
        if match:
            j += len(codeList[i])
            i += 1
        else:
            j += 1
    return i == len(codeList)

print(isCustomerWinner([['apple','apple'],['banana','anything','banana']],['orange','apple','apple','banana','orange','banana']))