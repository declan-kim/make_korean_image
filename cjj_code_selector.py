import numpy as np
co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
co = co.split(" ")
kor_start = "AC00"
kor_end = "D7A3"
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
f = open("C:/declan_src/img_declan_src/cjj_seperate/test.txt","w",-1,"utf-8")
for uni in(Hangul_Syllables):
    name = str()
    unicodeChars = chr(int(uni, 16))
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
        
    f.write(name+"_"+chr(int(cho))+"_"+chr(int(jung)-19+4449)+" _"+chr(int(jong)-1)+"  _"+str(count)+"\n")
    print(name+"_"+chr(int(cho))+"_"+chr(int(jung)-19+4449)+" _"+chr(int(jong))+"  _"+str(count))
f.close()