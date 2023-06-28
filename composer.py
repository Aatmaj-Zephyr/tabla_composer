Matrix=[[0.4,0.5,0.8,0.2,0,0.5],
[0.4,0,0.7,0.6,0,0],
[0.8,0,0.2,0,0,0.5],
[0.4,0,0,0,0.8,0.3],
[0,0,0,0,0,0],
[1,1,1,0,0,0]]
Bols=["dha","ge","ti ta","tin na","ke na","s"]

Unicode=["&#2343;&#2366;","&#2340;&#2367;","&#2335;","&#2327;&#2375;","&#2340;&#2367;&#2306;","&#2344;&#2366;","&#2325;&#2375;","&#2343;&#2367;&#2306;","&#2365;"]
index=["Dha","Ti","Ta","Ga","Tun","Na","Ke","Dhin","s"] # not used just for reference for playing sound and unicode

code_dha=['0','3','1 2','4 5','6 5','8'] #codes used everywhere eg dha is 0, ge is 3 etc
code_ta=['5','6', '1 2','7 5','3 5','8']#codes used everywhere eg na is 4, ke is 6 etc

importance=[0.3,0.5,0.7,0.5,0.5,0.1] #importance of every bol
for j in range(0,len(Matrix)):
    for i in range(0,len(importance)):
         Matrix[j][i]=Matrix[j][i]*importance[i] #multiply importance on the matrix
         

import random     
matra_req=[1,1,2,2,2,1] #matras required per bol
allowed_end=[0,0,0,1,1,0] #bols allowed at the end
numbers=[0,1,2,3,4,5] #array of the number of bols
Max_matra = 32 #number of matras
allowed_start = [1,1,1,0,0,1]

def compose(Matrix,code_dha,code_ta,matra_req,Max_matra,numbers,allowed_end): 
    current=0 # current state in automaton
    matra=0
    answer=[]
    for i in range(0,20000):
            if(sum( Matrix[current])<=0):
                #end reached without covering proper matras
                answer=[]  #restart
                current=0
                matra=0
                continue
            current=random.choices(numbers, Matrix[current], k=1)[0]
            
                
            answer.append(current)
            matra=matra+matra_req[current]
            
            
            if(matra==Max_matra):
                    if(allowed_end[current]==1):
                     break
                    else:
                        #end reached, but ends at a matra that is not allowed.
                        answer=[]
                        current=0
                        matra=0
                        continue
             
            if(matra>Max_matra):
                  #matra exceed
                        answer=[]
                        current=0
                        matra=0
                        continue
       
    #print(answer)
    answer_dha=""
    answer_ta=""
    # convert to code
    for i in answer:
        answer_dha+=code_dha[i]+" "
        answer_ta+=code_ta[i]+" "
    return answer_dha+"|"+","+answer_ta+"|" +";"

def compose_pure(Matrix,matra_req,Max_matra,numbers,allowed_end,allowed_start): 
    current=0 # current state in automaton
    matra=0
    answer=[]
    for i in range(0,20000):
           
                 
            if(sum( Matrix[current])<=0):
                #end reached without covering proper matras
                answer=[]  #restart
                current=0
                matra=0
                continue
            if(len(answer)==0): # for first iteration wont work if single one is greater than matras
                 current=random.choices(numbers,allowed_start,k=1)[0] # for starting
            else:
             current=random.choices(numbers, Matrix[current], k=1)[0]
            
                
            answer.append(current)
            matra=matra+matra_req[current]
            
            
            if(matra==Max_matra):
                    if(allowed_end[current]==1):
                     break
                    else:
                        #end reached, but ends at a matra that is not allowed.
                        answer=[]
                        current=0
                        matra=0
                        continue
             
            if(matra>Max_matra):
                  #matra exceed
                        answer=[]
                        current=0
                        matra=0
                        continue
       
    return answer

def Peshkar(Matrix,code_dha,code_ta,matra_req,Max_matra,numbers,allowed_end): 
    allowed_start=[1,0,0,0,0,0]
    answer = compose_pure(Matrix,matra_req,Max_matra,numbers,allowed_end,allowed_start)
    answer_dha=""
    answer_ta=""
    
   # tihai_matra=random.choice(range(0,(Max_matra+1)//3)) # eg 4*3+5=17  for complete tihai
    tihai_matra=random.choice([0,4,4,4,5,5,6,7]) # wont work for all taals
    tihai_start=Max_matra-tihai_matra*3 +1 if tihai_matra>0 else Max_matra
  #  print(tihai_start)
  #  print(tihai_matra)
   

    matras_to_be_added_to_ta = tihai_start
    # convert to code
    temp=0
    for i in answer:
        temp+=matra_req[i] # matras covered
        answer_dha+=code_dha[i]+" "
        if(temp<=tihai_start):
              answer_ta+=code_ta[i]+" "
              matras_to_be_added_to_ta-=matra_req[i]
   # print(matras_to_be_added_to_ta)
    #print("----")
    if(matras_to_be_added_to_ta != 0): # for half matra problem, put entire new ta string
         answer_ta = ""
         new_ta= compose_pure(Matrix,matra_req,tihai_start,numbers,allowed_end,allowed_start)
         for i in new_ta:
           answer_ta+=code_ta[i]+" "
   
    #print(temp) must be 32
  
    tihai = compose_pure(Matrix,matra_req,tihai_matra,numbers,[1,0,0,0,0,0],[0,0.2,0,0,0,0.8]) # begins with pause, ends with dha
    tihai=tihai+tihai+tihai[:-1] #remove last element dha
    for i in tihai:
        answer_ta+=code_dha[i]+" "
    return answer_dha+"|"+","+answer_ta+"|" +";"


def convert_unicode(string):
    danda="&#2404;" # seperator sign |

    converted=""
    for i in string:
        if(i==","):
            converted+=" <br> "
        elif(i==";"):
            converted+=" <br> "
        elif(i=="|"):
            converted+=danda
        elif (i==" "):
            converted+=" "
        else:
            try:
              converted+=Unicode[int(i)]
            except:
                 print("!error",i)
    return converted
            

    
import librosa
import numpy as np
import librosa.display
import soundfile as sf

def play(input):
    ''' 
   not needed as new method emerges

     teen_taal=[0,7,7,0,0,7,7,0,0,4,4,5,5,7,7,0]
    teen_taal =  [x for item in teen_taal for x in (item, '8')]


    teen_taal = ''.join(str(x) for x in teen_taal)
    input = teen_taal + teen_taal +input + teen_taal 
    '''
   
    speed = 0.1875

    Dha, sr = librosa.load("Bols/Dha.wav",duration=speed)


    Ti, sr = librosa.load("Bols/Ta.wav",duration=speed)


    Ta, sr = librosa.load("Bols/Ti.wav",duration=speed)

    Ga, sr = librosa.load("Bols/Ga.wav",duration=speed)

    Tun, sr = librosa.load("Bols/Tun.wav",duration=speed)

    Na, sr = librosa.load("Bols/Na.wav",duration=speed)

    Ke, sr = librosa.load("Bols/Ke.wav",duration=speed)

    Dhin, sr = librosa.load("Bols/Dhin.wav",duration=speed)

    s , sr = librosa.load("Bols/s.wav",duration=speed)

    index=["Dha","Ti","Ta","Ga","Tun","Na","Ke","Dhin","s"] # for reference
    var_index=[Dha,Ti,Ta,Ga,Tun,Na,Ke,Dhin,s] # index of variables

    output=[] #output array of variables
    input = [ x for x in input if x.isdigit() ] #remove all other symbols
    for i in range(len(input)):
        if(i==0 and input[i] == '8'):
            pass
            #if starts with pause not tested yet
        elif(i<len(input)-1):
            if(input[i+1]=='8'):
                pause,sr = librosa.load("Bols/"+index[int(input[i])]+".wav",duration=2*speed)
                output.append(pause)
            else:  
                if(input[i]!='8'):
                    output.append(var_index[int(input[i])])
        elif(input[i]!='8'): # last beat
            output.append(var_index[int(input[i])])

   


    teentaal, sr = librosa.load("teen_taal.wav")
    output=[teentaal,teentaal]+output+[teentaal]
    
    z = np.concatenate(output) # concentate variables to make array
    
    
    sf.write('Output.wav', z, sr) #make sound file
 
    

playble_output=""

f = open("Kaida.md","w")
for i in range(0,100):
    f.write(" <hr> <br> ")
    raw_composed=Peshkar(Matrix,code_dha,code_ta,matra_req,Max_matra,numbers,allowed_end)
    playble_output+=raw_composed
    f.write(convert_unicode(raw_composed))
    
teentaal=[]
#play('012345678') #test case
play(playble_output)