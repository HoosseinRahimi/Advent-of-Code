def fileRead(filePath):
    content=[]
    with open(filePath, 'r') as file:
        for  line in file:
            if line:
                line=line.split(",")
                content.append(line)
            else:
                continue    
    return content            

content=fileRead("""pathToFile""")[0]
ranges=[list(map(int,item.split('-')))for item in content]




counter=0
for i in ranges:
    for j in range (i[0],i[1]+1):
        if len(str(j))%2==0 and str(j)[:len(str(j))//2]==str(j)[len(str(j))//2:]:
            counter+=j

print(counter)