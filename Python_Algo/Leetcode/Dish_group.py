dishes=[["Salad","Tomato","Cucumber","Salad","Sauce"], 
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]

def groupingDishes(dishes):
    dictionary = {}
    for dish in dishes:
        for index, ingredient in enumerate(dish):
            if index != 0:
                if ingredient in dictionary:
                    dictionary[ingredient].append(dish[0])
                else:
                    dictionary[ingredient] = [dish[0]]
    result = []
    for key in dictionary:
        if len(dictionary[key]) > 1:            
            result.append([key] + sorted(dictionary[key]))
    return sorted(result)
    
print(groupingDishes(dishes))