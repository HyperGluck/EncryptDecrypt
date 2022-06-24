#EXE 1 

def albam(message,Albam1,Albam2):  
    result_message='';
    count=1;
    for i in message:
         for j in range(len(Albam1)):
             if(i.lower()==Albam1[j]):
                 result_message +=Albam2[j];
                 count+=1;
             if(i.lower()==Albam2[j]):
                 result_message +=Albam1[j];
                 count+=1;
             if(count%5==0):
                 result_message +=" ";
                 count+=1;
    return result_message;

def ToEncrypted_MonoAlpha(message,abc,MonoAlpha):  
    result_message='';
    for i in message:
        for j in range(len(abc)):
            if(i.lower()==abc[j]):
                result_message +=MonoAlpha[j];
                
    return result_message;

def ToDecrypt_MonoAlpha(message,abc,MonoAlpha):   
    result_message='';
    for i in message:
         for j in range(len(MonoAlpha)):
             if(i.lower()==MonoAlpha[j]):
                 result_message +=abc[j];     
    return result_message;


def ToEncrypted_Shihluf(message,abc,Nums):    
    result_message='';
    numCast=[];
    S=5

    for i in message:
        for j in range(len(Nums)):
            if(i.lower()==abc[j]):
                numCast.append(Nums[j]);

    for P in numCast:
            if( (P+S)>25 ):
                result_message +=abc[(P+S)%26]
            else:
                result_message +=abc[P+S]

    return result_message;

def ToDecrypt_Shihluf(message,abc,Nums): 
    result_message='';
    numCast=[];
    S=5

    for i in message:
        for j in range(len(Nums)):
            if(i.lower()==abc[j]):
                numCast.append(Nums[j]);

    for P in numCast:
       X=P-S;
       if( (X)<0 ):
           result_message +=abc[26+X]
       else:
           result_message +=abc[P-S]

    return result_message;




filename = 'Sentences.txt'
NumOfLine=1;
SentencesArray=[];
Tempstr="";
EncDecoList=["MonoAlpha","ALBAM","Modolary"];
Nums=[0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
MonoAlpha=['j','f','u','g','t','c','h','v','n','m','d','q','a','i','r','w','l','o','e','s','y','p','z','k','b','x'];
Albam1=['a','b','c','d','e','f','g','h','i','j','k','l','m'];
Albam2=['n','o','p','q','r','s','t','u','v','w','x','y','z'];

with open (filename,'r') as inFile:
    for line in inFile:
        for char in line:
            if( (ord(char)>64 and ord(char) <91) or (ord(char)> 96 and ord(char)< 123) or char==" "):
                Tempstr=Tempstr+char;
        SentencesArray.append(Tempstr)
        Tempstr="";

print("The Sentences from Sentences.txt: \n")

for sente in SentencesArray:
    print(NumOfLine,":",sente);
    NumOfLine+=1

print()
inputSentence= int(input("Choose 1 OF The Sentences: "))
print()


print("3 Diffrent Encryptions: \n")
for i in range(3):
    print(i+1,":",EncDecoList[i]);

print()
inputEncryption= int(input("Choose 1 OF The Encryptions: "))
print()

print("3 Diffrent Decodings (JUST MAKE SURE THIS IS THE SAME NUMBER OF THE ENCRYPTION):  \n")
for i in range(3):
    print(i+1,":",EncDecoList[i]);

print()
inputDecryption= int(input("Choose 1 OF The Decodings: "))
print()


while(inputDecryption!=inputEncryption):
    print("Wrong Number Of Decoding Option Please Choose The Same Option Number Like The Option Number Of The Encryption  \n")
    for i in range(3):
         print(i+1,":",EncDecoList[i]);

    inputDecryption= int(input("Choose 1 OF The Decodings: "))
    print()

if(inputDecryption==1):
    print("The Choosen Message By The User IS:",SentencesArray[inputSentence-1])

    EncryptedMess=ToEncrypted_MonoAlpha(SentencesArray[inputSentence-1],abc,MonoAlpha);
    print("this is encrypted message from MONO:",EncryptedMess);
    DecryptedMess=ToDecrypt_MonoAlpha(EncryptedMess,abc,MonoAlpha);
    print ("this is decrypted message from MONO:",DecryptedMess)

if(inputDecryption==2):
    print("The Choosen Message By The User IS:",SentencesArray[inputSentence-1])

    EncryptedMess=albam(SentencesArray[inputSentence-1],Albam1,Albam2);
    print("this is encrypted message from ALBAM:",EncryptedMess);
    DecryptedMess=albam(EncryptedMess,Albam1,Albam2);
    print("this is decrypted message from ALBAM:",DecryptedMess);

if(inputDecryption==3):
    print("The Choosen Message By The User IS:",SentencesArray[inputSentence-1])

    EncryptedMess=ToEncrypted_Shihluf(SentencesArray[inputSentence-1],abc,Nums);
    print("this is encrypted message from MODOLARY:",EncryptedMess);
    DecryptedMess=ToDecrypt_Shihluf(EncryptedMess,abc,Nums)
    print("this is decrypted message from MODOLARY:",DecryptedMess);


print()

#MATRIX EXE2


def editMatrix(mat):
    copyMat=[];

    for i in range(len(mat)):
        row=[]
        for j in range(len(mat)):
            row.append(mat[i][j])
        copyMat.append(row);

    for i in range(len(mat)):
          for j in range(len(mat)): 
              if(copyMat[i][j]==0):
                    for k in range(len(mat)):
                           mat[k][j]=0;
                           mat[i][k]=0;


N= int(input("Please input N Dimensions: "))
mat=[];
for i in range(N):
    row=[]
    for j in range(N):
         num=int(input());
         row.append(num)
    mat.append(row)

editMatrix(mat);

for array in mat:
    print(array)





    




