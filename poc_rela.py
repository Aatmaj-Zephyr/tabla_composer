Matrix=[[0.4,0.5,0.7,0.5,0,0.5],
[0.4,0,0.7,0.6,0,0],
[0.8,0,0,0,0,0],
[0.6,0,0,0,0.8,0.4],
[0,0,0,0,0,0],
[1,1,1,0.3,0,0]]
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
    
    #Ti=np.concatenate((librosa.load("Bols/Ti.wav",duration=0.5*speed)[0],librosa.load("Bols/Ta.wav",duration=0.5*speed)[0]))
    #Ta=np.concatenate((librosa.load("Bols/Ke.wav",duration=0.5*speed)[0],librosa.load("Bols/Ta.wav",duration=0.5*speed)[0]))

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

    output=[] #output array of variables
   
    input = [ x for x in input if x.isdigit() or x=="|" ] #remove all other symbols
    Dhaline= [Dha,Tira,KiTa,Dha,Dhin,Na,Dha,Dha,Dhin,Na,Dha,Ti,Dha,Dha,Tun,Na,Dha,Ti,s,Dha,Tira,KiTa,Dha,Dha,Tira,KiTa,Dha,Ti,Dha,Dha,Tun,Na]
    Naline= [Na,Tira,KiTa,Na,Tun,Na,Na,Na,Tun,Na,Na,Ti,Na,Na,Tun,Na,Dha,Ti,s,Dha,Tira,KiTa,Dha,Dha,Tira,KiTa,Dha,Ti,Dha,Dha,Tun,Na]
    output.append(np.concatenate(Dhaline))
    output.append(np.concatenate(Naline))
    output.append(np.concatenate(Dhaline))
    output.append(np.concatenate(Naline))
    flip =0
    for i in range(len(input)):
        if(input[i]=='|'):
            if(flip==0):
             output.append(np.concatenate(Dhaline))
             flip=1
            else:
              output.append(np.concatenate(Naline))
              flip=0
            
        elif(i==0 and input[i] == '8'):
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

   

    #teen_taal= [Dha,Dhin,Dhin,Dha,Dha,Dhin,Dhin,Dha,Dha,Tun,Tun,Na,Na,Dhin,Dhin,Dha]
    # teen_taal=np.concatenate(teen_taal)
    teen_taal,sr=librosa.load("teen_taal.wav")
    endDha,sr=librosa.load("Bols/Dha.wav",duration=2*speed)
   # end= [Dha,Tira,KiTa,Dha,Dhin,Na,Dha,Dha,Dhin,Na,Dha,Ti,Dha,Dha,Tun,Na]
    #tihai=[Dha,Ti,s,Dha,Tira,KiTa,Dha,Dha,Tira,KiTa,Dha,Ti,Dha,Dha,Tun,Na,endDha]
    #end=end+tihai+tihai+tihai
    #end=end+end+end
    #
    end=[Dha,Dha,Tira,KiTa,Dha,Tira,KiTa,Dha,Ti,endDha]
    end=end+end+end
    end=np.concatenate(end)  # output=[end]
    output=[teen_taal,teen_taal]+output+[end]
  
    z = np.concatenate(output) # concentate variables to make array
    
    
    sf.write('Rela.wav', z, sr) #make sound file
 


    


playble_output=""

f = open("Rela.md","w")
for i in range(0,7):
    f.write(" <hr> <br> ")
    raw_composed=compose(Matrix,code_dha,code_ta,matra_req,Max_matra,numbers,allowed_end)
    playble_output+=raw_composed
    f.write(convert_unicode(raw_composed))

    
teentaal=[]
#play('012345678') #test case
play(playble_output)
