def search_quadruplets(arr,target):
    all_pairs = {}
    quadruplets = []
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)):
            current_sum = arr[i] + arr[j]
            differnce = target - current_sum
            if differnce in all_pairs:
                for pair in all_pairs[differnce]:
                    quadruplets.append(pair + [arr[i],arr[j]])
        for k in range(0,i):
            current_sum = arr[i] + arr[k]
            if current_sum not in all_pairs:
                all_pairs[current_sum] = [[arr[k],arr[i]]]
            else:
                all_pairs[current_sum].append([arr[k],arr[i]])
    return quadruplets


                