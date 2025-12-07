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




num_counter=[]
counter=0
for i in ranges:
    for j in range (i[0],i[1]+1):
        s=len(str(j))
        for c in range(1,int(s**0.5 )+1):
            if s%c==0:
                num_counter.append(c)
                if c!=s//c:
                    num_counter.append(s//c)
        for c in num_counter:
            c=int(c)
            if c!=s:
                if str(j)[:c]*(s//c)==str(j):
                    counter+=j 
                    break       
        num_counter=[]        

print(counter)