import re



def  fileRead(file_name):
    result=[]
    with open (file_name) as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            result.append(sepNumAndStr(line))
    
    return result


def sepNumAndStr (line:str)->tuple[str,str]:
    Tokens=re.findall(r'[^0-9]+|\d+',line)
    Numbers:str=''
    strings:str=''
    for element in Tokens:
        if element.isdigit():
            Numbers+=element
        else:
            strings+=element
    
    return Numbers,strings


def finalAnswer(result):
    lock:int=50
    counter:int=0
    for i in result :
            i_cal=int(i[0])
        
            
            if i[1]=='R':   
                    lock=lock+i_cal
            
            elif i[1]=='L':
                    lock=lock-i_cal
            
            lock=lock%100
        
            if lock==0:
                counter+=1                         

    return counter




result=fileRead(r'\\path to file')
answer=finalAnswer(result)
print(answer)