def solution(triangle):
    answer = 0
    length = len(triangle)
    for i in range(1,len(triangle)):                
        for j in range(len(triangle[i])):
            test = []
            
            if j-1 >= 0:
                test.append(triangle[i-1][j-1] + triangle[i][j])
                
            if j < len(triangle[i-1]):
                test.append(triangle[i-1][j]+triangle[i][j])
                
            triangle[i][j] = max(test)
                
                
            
    answer = max(triangle[length-1])
            
            
    return answer