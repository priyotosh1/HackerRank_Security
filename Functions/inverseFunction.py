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
        dict1[i] = list2[i-1]
    
    dict2 = dict((int(v),int(k)) for k,v in dict1.items())
    
    
    for i in range(1,int(input1)+1):
        print (dict2[i])
func()