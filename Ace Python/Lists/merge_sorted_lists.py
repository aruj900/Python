def merge_list(lst1,lst2):
    ind_arr1 = 0
    ind_arr2 = 0
    ind_result = 0
    result = []
    
    result = [0]*(len(lst1)+len(lst2))
    while (ind_arr1 < len(lst1)) and (ind_arr2 < len(lst2)):
        if lst1[ind_arr1] < lst2[ind_arr2]:
            result[ind_result] = lst1[ind_arr1]
            ind_arr1 += 1
            ind_result += 1
        else:
            result[ind_result] = lst2[ind_arr2]
            ind_arr2 +=1
            ind_result += 1
    
    while ind_arr1 < len(lst1):
        result[ind_result] = lst1[ind_arr1]
        ind_arr1 += 1
        ind_result += 1
    while ind_arr2 < len(lst2):
        result[ind_result] = lst2[ind_arr2]
        ind_result += 1
        ind_arr2 += 1
    return result
