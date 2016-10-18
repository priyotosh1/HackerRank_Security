outputstr=""
for num in (input().strip()):
    outputstr+=str((int(num)+1)%10)
print(outputstr)