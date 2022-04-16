import sys

def check(v,graph) : # 정점개수 / 간선개수 / 리스트 
    # print(p)
    result = [0] * (v+1)
    
    def dfs (n,result) :
        for i in graph[n] :
            if result[i] == 0 :
                if result[n] == 1 : result[i] = 2
                else : result[i] = 1                       
            else :
                if result[i] == result[n] :
                    return False
                    
    result[1] = 1
    # a = True
    for i in range(1,v+1) :
        a = dfs(i,result)
        print(result)
        if a == False : return False
    return True
        
    
 
k = int(sys.stdin.readline())

for _ in range(k) :
    v,e = map(int,sys.stdin.readline().split())
    graph = [[]for _ in range(v+1)] 
    # print(b)
    for _ in range(e) :
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

   

    if check(v,graph) :
        print('YES')
    else :
        print('NO')

