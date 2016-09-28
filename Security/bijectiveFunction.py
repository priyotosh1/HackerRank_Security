def bijective():
    flag=1
    for i in range(0,input1):
        for j in range(0,i):
            if((j+1) in input2):
                continue
            else:
                return "NO"
            
    return "YES"      
    
input1 = int(input())
input2 = [int(x) for x in (input().split())]