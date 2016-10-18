def func():
    
    inp1 = input()
    if (len(inp1)) >1:
        try:
            input1 = int(inp1)
        except:
            return
    else:
        try:
            input1 = int(inp1)
        except:
            return    
    input2 = input()
     
    list2 = input2.split() 
    if int(input1) != len(list2):
        return 
    
    if(int(max(list2)) > int(input1)):
        return
    
    list3 = [None]*(int(input1)+1)
    dict1 = {}
    for element in list2:
        if(int(element)<1 or int(element)>20):
            return
        
    for i in range(1,(int(input1)+1)):
        dict1[i] = int(list2[i-1])
  
    
    dict2 = {}
    flag = 1
    for k,v in dict1.items():
        if(k != dict1[dict1[k]]):
            flag=0;
            break
    if (flag==1):
        print ("YES")
    else:
        print ("NO")

func() 