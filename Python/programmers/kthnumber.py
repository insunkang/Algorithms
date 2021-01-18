import copy
def solution(array, commands):
    result = []
    for i in range(len(commands)):
        a = copy.deepcopy(array)
        test = array[commands[i][0]-1:commands[i][1]]
        test.sort()
        result.append(test[commands[i][2]-1])

    return(result)