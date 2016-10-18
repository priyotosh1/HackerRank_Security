def func():
    str1 = input()
    if(len(str1)<1 or len(str1)>10):
        return
    try:
        num = int(str1)
    except:
        return
    input2=int(input())
    list1 = []
    num2 = num
    while(num2 > 0):
        list1.append(num2%10)
        num2=num2//10
        
    list1.reverse()
    ouputStr = ""
    for i in list1:
            ouputStr+=str((i+input2)%10)
    
    print (ouputStr)
    
func()
