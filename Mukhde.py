Matrix=[[0.4,0.5,0.7,0.5,0,0.5,0.5],
[0.3,0,0.7,0.4,0,0,0],
[0.8,0,0.4,0,0,0,0.4],
[0.6,0,1,0,0.8,0.4,0],
[0,0,1,0,0,0,0],
[1,1,1,0.3,0,0,0.5],
[1,1,0,0,0,0,0.5]]
Bols=["dha","ge","ti ta","tin na","ke na","s","ta ka ta tira kita"]

Unicode=["&#2343;&#2366;","&#2340;&#2367;","&#2335;","&#2327;&#2375;","&#2340;&#2367;&#2306;","&#2344;&#2366;","&#2325;&#2375;","&#2343;&#2367;&#2306;","&#2365;"]
index=["Dha","Ti","Ta","Ga","Tun","Na","Ke","Dhin","s"] # not used just for reference for playing sound and unicode
code_dha=['0','3','1 2','4 5','6 5','8','1 5 1 2'] #codes used everywhere eg dha is 0, ge is 3 etc
teen_taal_bols = [] # corresponds to code_ta


importance=[0.3,0.5,0.7,0.5,0.5,0.05,0.6] #importance of every bol
for j in range(0,len(Matrix)):
    for i in range(0,len(importance)):
         Matrix[j][i]=Matrix[j][i]*importance[i] #multiply importance on the matrix
         

import random     
matra_req=[1,1,2,2,2,1,5] #matras required per bol
allowed_end=[1,0,0,0,0,0,0] #bols allowed at the end
numbers=[0,1,2,3,4,5,6] #array of the number of bols
Max_matra = 64 #number of matras
allowed_start = [0,1,1,0,0,1,1]

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

def Mukhde(Matrix,code_dha,matra_req,Max_matra,numbers,allowed_end): 
    allowed_start=[1,0,0,0,0,0,0]
    answer = compose_pure(Matrix,matra_req,Max_matra,numbers,allowed_end,allowed_start)

    answer_ta=""
    
   # tihai_matra=random.choice(range(0,(Max_matra+1)//3)) # eg 4*3+5=17  for complete tihai
    tihai_matra=random.choice([5,5,6,7,8,8,9,10,11,12,12,12,13,14,15,15,15,16]) # wont work for all taals
    tihai_start=Max_matra-tihai_matra*3 +1 if tihai_matra>0 else Max_matra
  #  print(tihai_start)
  #  print(tihai_matra)
    teen_taal_bols = [0,7,7,0,0,7,7,0,0,4,4,5,5,7,7,0]
    


    answer_ta = ""
    teen_taal_bols_cut = teen_taal_bols[:tihai_start%16]
    for i in teen_taal_bols_cut:
        answer_ta+=str(i)+" "
   
    #print(temp) must be 32
  
    tihai = compose_pure(Matrix,matra_req,tihai_matra,numbers,allowed_start,[0,0,0,0,0,0.8,0]) # begins with pause, ends with dha
    tihai=tihai+tihai+tihai[:-1] #remove last element dha
    for i in tihai:
        answer_ta+=code_dha[i]+" "
    return answer_ta+"|" +";"


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
   
    speed = 0.15

    Dha, sr = librosa.load("Bols/Dha.wav",duration=speed)


    Ti, sr = librosa.load("Bols/Ta.wav",duration=speed)
    Ta, sr = librosa.load("Bols/Ti.wav",duration=speed)

    Tira=np.concatenate((librosa.load("Bols/Ti.wav",duration=0.5*speed)[0],librosa.load("Bols/Ta.wav",duration=0.5*speed)[0]))
    KiTa=np.concatenate((librosa.load("Bols/Ke.wav",duration=0.5*speed)[0],librosa.load("Bols/Ta.wav",duration=0.5*speed)[0]))

    Ga, sr = librosa.load("Bols/Ga.wav",duration=speed)

    Tun, sr = librosa.load("Bols/Tun.wav",duration=speed)

    Na, sr = librosa.load("Bols/Na.wav",duration=speed)

    Ke, sr = librosa.load("Bols/Ke.wav",duration=speed)

    Dhin, sr = librosa.load("Bols/Dhin.wav",duration=speed)

    s , sr = librosa.load("Bols/s.wav",duration=speed)

    index=["Dha","Tira","KiTa","Ga","Tun","Na","Ke","Dhin","s"] # for reference
    var_index=[Dha,Tira,KiTa,Ga,Tun,Na,Ke,Dhin,s] # index of variables
    teen_taal= [Dha,Dhin,Dhin,Dha,Dha,Dhin,Dhin,Dha,Dha,Tun,Tun,Na,Na,Dhin,Dhin,Dha]
    output=[] #output array of variables
    input = [ x for x in input if x.isdigit() or x=="|" ] #remove all other symbols
    for i in range(len(input)):
        if(input[i]=='|'):
            
            output.append(np.concatenate(teen_taal))
            
        elif(i==0 and input[i] == '8'):
            pass
            #if starts with pause not tested yet
        elif(i<len(input)-1):
            if(input[i+1]=='8'):
                if input[i]=='1' or input[i] == '2': # for tira kita pause ending
                    if(input[i]=='1'):
                        pause=np.concatenate((librosa.load("Bols/Ti.wav",duration=1*speed)[0],librosa.load("Bols/Ta.wav",duration=1*speed)[0]))
                        output.append(pause)
                    else:
                        pause=np.concatenate((librosa.load("Bols/Ke.wav",duration=0.5*speed)[0],librosa.load("Bols/Ta.wav",duration=0.5*speed)[0]))
                        output.append(pause)
                else:
                    pause,sr = librosa.load("Bols/"+index[int(input[i])]+".wav",duration=2*speed)
                    output.append(pause)
            else:  
                if(input[i]!='8'):
                    output.append(var_index[int(input[i])])
        elif(input[i]!='8'): # last beat
            output.append(var_index[int(input[i])])

   

    teentaal = np.concatenate(teen_taal)
    output=[teentaal,teentaal]+output+[teentaal]
    
    z = np.concatenate(output) # concentate variables to make array
    
    
    sf.write('Mukhde.wav', z, sr) #make sound file
 
    

playble_output=""

f = open("Mukhde.md","w")
for i in range(0,100):
    f.write(" <hr> <br> ")
    raw_composed=Mukhde(Matrix,code_dha,matra_req,Max_matra,numbers,allowed_end)
    playble_output+=raw_composed
    f.write(convert_unicode(raw_composed))
    

#play('012345678') #test case
play(playble_output)
