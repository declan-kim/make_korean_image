import os
import numpy as np
from tqdm import tqdm
co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
co = co.split(" ")
kor_start = "AC00"
kor_end = "D7A3"
fonts = os.listdir("C:/declan_src/img_declan_src/font_uni")
Hangul_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]

Hangul_Syllables = np.array(Hangul_Syllables)

kor_s = np.where(kor_start == Hangul_Syllables)[0][0]
kor_e = np.where(kor_end == Hangul_Syllables)[0][0]

Hangul_Syllables = Hangul_Syllables[kor_s : kor_e + 1]
kor_unicodeChars = chr(int(Hangul_Syllables[0], 16))
count = 0
passer = 0
passer_w = 16
path = r"F:\declan_src\test_data_gen"
for uni in tqdm(Hangul_Syllables):
    cho = (((int(uni,16) - int("AC00",16))/28)/21) + 4352
    jung = (((int(uni,16) - int("AC00",16))/28)%21) +19
    jong = ((int(uni,16) - int("AC00",16))%28) + 4520
    if int(jung) <28:
        #일반 중성, ㅏㅐㅑㅒㅓㅔㅕㅖㅗ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+'_'+str(int(jung))
        else :
            name = str(int(cho)-4352)+'_'+str(int(jung))+'_'+str(int(jong)-4520+32)
        
    elif int(jung) < 30:
        #조합중성, ㅘㅙ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(27)+"_"+str(int(jung)-9)
        else :
            name = str(int(cho)-4352)+"_"+str(27)+"_"+str(int(jung)-9)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) == 30:
        #조합중성, ㅚ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(27)+"_"+str(32)
        else :
            name = str(int(cho)-4352)+"_"+str(27)+"_"+str(32)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) < 33:
        #일반중성, ㅛㅜ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(int(jung)-3)
        else :
            name = str(int(cho)-4352)+"_"+str(int(jung)-3)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) < 35:
        #조합중성, ㅝㅞ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(29)+"_"+str(int(jung)-10)
        else :
            name = str(int(cho)-4352)+"_"+str(29)+"_"+str(int(jung)-10)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) == 35:
        #조합중성, ㅟ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(29)+"_"+str(32)
        else :
            name = str(int(cho)-4352)+"_"+str(29)+"_"+str(32)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) < 38:
        #일반중성, ㅠㅡ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(int(jung)-6)
        else :
            name = str(int(cho)-4352)+"_"+str(int(jung)-6)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) == 38:
        #조합중성, ㅢ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(31)+"_"+str(32)
        else:
            name = str(int(cho)-4352)+"_"+str(31)+"_"+str(32)+'_'+str(int(jong)-4520+32)
        
    elif int(jung) == 39:
        #일반중성, ㅣ
        if int(int(jong)-4520+32) == 32:
            name = str(int(cho)-4352)+"_"+str(32)
        else :
            name = str(int(cho)-4352)+"_"+str(32)+'_'+str(int(jong)-4520+32)
        
    name = "-img-" + name
    for ttf in fonts:
        if (passer != passer_w):
            passer = passer +1
            continue
        else :
            passer_w = passer + 16
        f = open(path+"\\"+name+".txt")
        lines = f.read()
        for line in lines.splitlines():
            value = line.split(' ')
            if int(value[0]) < 19:
                os.system(r'copy '+path+"\\"+name+'.jpg'+" "+path+"\\"+'cho')
                f1 = open(path+r'\cho'+"\\"+name+'.txt','a',-1,'utf-8')
                f1.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' '+value[4]+'\n')
                f1.close()
                continue
            elif int(value[0]) <33:
                os.system(r'copy '+path+"\\"+name+'.jpg'+" "+path+"\\"+'jung')
                f1 = open(path+r'\jung'+"\\"+name+'.txt','a',-1,'utf-8')
                value[0] = str(int(value[0])-19)
                f1.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' '+value[4]+'\n')
                #f1.write(line+'\n')
                f1.close()
                continue
            else :
                os.system(r'copy '+path+"\\"+name+'.jpg'+" "+path+"\\"+'jong')
                f1 = open(path+r'\jong'+"\\"+name+'.txt','a',-1,'utf-8')
                value[0] = str(int(value[0])-33)
                f1.write(value[0]+' '+value[1]+' '+value[2]+' '+value[3]+' '+value[4]+'\n')
                f1.close()
                continue
        count = count + 1 