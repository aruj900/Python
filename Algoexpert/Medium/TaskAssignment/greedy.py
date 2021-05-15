def taskAssignments(k,tasks):
    pairTasks = []
    sortedTasks = sorted(tasks)
    taskDuration = getTaskDuration(tasks)
    for idx in range(k):
        task1Duartion = sortedTasks[idx]
        indicies1 = taskDuration[task1Duartion]
        task1Index = indicies1.pop()

        task2Duration = sortedTasks[len(tasks) - 1 - idx]
        indicies2 = taskDuration[task2Duration]
        task2Index = indicies2.pop()
        pairTasks.append([task1Index,task2Index])
    return pairTasks 

def getTaskDuration(tasks):
    dic = {}
    for idx, duration in enumerate(tasks):
        if duration in dic:
            dic[duration].append(idx)
        else:
            dic[duration] = [idx]
    return dic
