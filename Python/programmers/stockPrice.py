from collections import deque

def solution(prices):
    answer = []
    q = deque()
    
    for i in range(len(prices)):
        q.append(prices[i])
    
    a = 1
    
    
    while q:
        stock = 0
        k = q.popleft()
        
        if a == len(prices):
            answer.append(0)
            return answer
        
        for j in range(a,len(prices)):
            if k > prices[j]:
                stock+=1
                break
            else:
                stock+=1
        answer.append(stock)
        a+=1
    
    
    return answer