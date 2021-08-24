#어디선가 퍼온 데이터와 제가 이것저것 구상하여 넣은 아직까지는 쓰레기인 코드입니다.
import sys, os                      
import numpy as np                                          #이미지를 C++에서는 Mat로 저장하나 python에서는 numpy에 저장하게됨.
import time
from PIL import Image, ImageDraw, ImageFont
from numpy.core.numeric import False_                       #Python Imaging Library, 한글 ttf에서 한글 이미지를 만들기 위함.
from tqdm import tqdm                                       #for문 앞에 붙여줄 경우 진행정도를 알 수 있음.
from multiprocessing import Process, Queue, Pool            #생성할 이미지의 크기, 폰트, 경우를 달리하여 동시에 여러장 생성하기 위한 프로세스 라이브러리
import multiprocessing as mp                                
import array                                                
import random                                               #이미지의 위치를 랜덤으로 정하기 위하여 import
import cv2 as cv2                                           #이미지처리를 위한 OpenCV
#from keras.preprocessing.image import load_img             #케라스의 이미지 증대를 위한 라이브러리
from numpy import expand_dims                               #케라스의 이미지 증대를 사용하기 위한 추가 라이브러리
#from keras.preprocessing.image import img_to_array          
#from keras.preprocessing.image import ImageDataGenerator    
from matplotlib import pyplot as plt                        #python 데이터 시각화
from PIL import Image                                       

class ftpng:
    plt.figure(figsize=(15, 15))
    classNum = 0
    def ttftoimg(self, fonts, font_path, Syllables, unicodeChars, size, overLoad, classNum, className, text_count):
        self.classNum = classNum
        print(self.classNum)
        print("check out3")
        c_count = 0
        prefix1 =5
        prefix2 = 10
        name = str()
        for uni in tqdm(Syllables):
            unicodeChars = chr(int(uni, 16))
            #print(str(type(uni))+""+uni)
            cho = (((int(uni,16) - int("AC00",16))/28)/21) + 4352
            jung = (((int(uni,16) - int("AC00",16))/28)%21) +19
            #jung = (((int(uni,16) - int("AC00",16))/28)%21) +4449
            jong = ((int(uni,16) - int("AC00",16))%28) + 4520
            #name = chr(int(cho))+ '_' + chr(int(jung))+ '_' + chr(int(jong))
            if int(jung) <28:
                #일반 중성, ㅏㅐㅑㅒㅓㅔㅕㅖㅗ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+'_'+str(int(jung))
                else :
                    name = str(int(cho)-4352)+'_'+str(int(jung))+'_'+str(int(jong)-4520+32)
            elif int(jung) < 30:
                #조합중성, ㅘㅙ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(27)+"_"+str(int(jung)-9)
                else :
                    name = str(int(cho)-4352)+"_"+str(27)+"_"+str(int(jung)-9)+'_'+str(int(jong)-4520+32)
            elif int(jung) == 30:
                #조합중성, ㅚ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(27)+"_"+str(32)
                else :
                    name = str(int(cho)-4352)+"_"+str(27)+"_"+str(32)+'_'+str(int(jong)-4520+32)
            elif int(jung) < 33:
                #일반중성, ㅛㅜ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(int(jung)-3)
                else :
                    name = str(int(cho)-4352)+"_"+str(int(jung)-3)+'_'+str(int(jong)-4520+32)
            elif int(jung) < 35:
                #조합중성, ㅝㅞ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(29)+"_"+str(int(jung)-10)
                else :
                    name = str(int(cho)-4352)+"_"+str(29)+"_"+str(int(jung)-10)+'_'+str(int(jong)-4520+32)
            elif int(jung) == 35:
                #조합중성, ㅟ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(29)+"_"+str(32)
                else :
                    name = str(int(cho)-4352)+"_"+str(29)+"_"+str(32)+'_'+str(int(jong)-4520+32)
            elif int(jung) < 38:
                #일반중성, ㅠㅡ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(int(jung)-6)
                else :
                    name = str(int(cho)-4352)+"_"+str(int(jung)-6)+'_'+str(int(jong)-4520+32)
            elif int(jung) == 38:
                #조합중성, ㅢ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(31)+"_"+str(32)
                else:
                    name = str(int(cho)-4352)+"_"+str(31)+"_"+str(32)+'_'+str(int(jong)-4520+32)
            elif int(jung) == 39:
                #일반중성, ㅣ
                if int(int(jong)-4520+32) == 32:
                    #종성이 없을경우
                    name = str(int(cho)-4352)+"_"+str(32)
                else :
                    name = str(int(cho)-4352)+"_"+str(32)+'_'+str(int(jong)-4520+32)
            path = "F:/declan_src/four_font_data/"
            #+ str(ttf).split('.')[0]   
            prefix1_a = False
            prefix2_a = False
            holder = False
            passer = 1
            for ttf in fonts:
                path = "F:/declan_src/ten_font_gen/"
                if passer <11:
                    if (passer == prefix1) and not holder:
                        prefix1_a = True
                        passer = passer + 1
                        path = path + "valid/"
                    elif passer == prefix2 and not holder:
                        prefix2_a = True
                        passer = passer + 1
                        path = path + "valid/"
                    else :
                        passer = passer + 1
                        path = path + "train/"
                if prefix2_a and prefix1_a and True :
                    if prefix1 >1:
                        prefix1 = prefix1 -1
                        prefix2 = prefix2 -1
                    else :
                        prefix1 = 5
                        prefix2 = 10
                    prefix1_a = False
                    prefix2_a = False
                    holder =True
                os.makedirs(path, exist_ok = True)

                font = ImageFont.truetype(font = font_path + "/" + ttf, size = size)
                            
                x, y = font.getsize(unicodeChars)
                
                #val = padding.get(None)
                #factor = padding.getFactor(size)

                theImage = Image.new('RGB', (x+50, y+50), color='white')
                theDrawPad = ImageDraw.Draw(theImage)
                theDrawPad.text((25, 25), unicodeChars, font=font, fill='black' )
                msg = path
                msg = '{}'.format(msg)
                real_name = "img_" + name +"_"+str(ttf).split(".")[0]
                theImage.save(msg+real_name+'.jpg')

            c_count = c_count +1
            text_count = text_count + 1
            self.classNum = self.classNum + 1 
        return text_count


if __name__ == '__main__' :
    font_path = "C:/declan_src/img_declan_src/font_uni"
    fonts = os.listdir("C:/declan_src/img_declan_src/font_uni")
    print(fonts)
    co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
    iter = 0
    kor_start = "AC00"
    kor_q1 = "B6E9"
    
    kor_q2 = "B6EA"
    kor_q3 = "C1D2"

    kor_q4 = "C1D3"
    kor_end = "D7A3"                        #실패

    Hangul_Syllables_1 = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]

    Hangul_Syllables_1 = np.array(Hangul_Syllables_1)

    kor_s_1 = np.where(kor_start == Hangul_Syllables_1)[0][0]
    kor_e_1 = np.where(kor_q1 == Hangul_Syllables_1)[0][0]

    Hangul_Syllables_1 = Hangul_Syllables_1[kor_s_1 : kor_e_1 + 1]
    kor_unicodeChars_1 = chr(int(Hangul_Syllables_1[0], 16))

    Hangul_Syllables_2 = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]
    Hangul_Syllables_2 = np.array(Hangul_Syllables_2)

    kor_s_2 = np.where(kor_q2 == Hangul_Syllables_2)[0][0]
    kor_e_2 = np.where(kor_q3 == Hangul_Syllables_2)[0][0]

    Hangul_Syllables_2 = Hangul_Syllables_2[kor_s_2 : kor_e_2 + 1]
    kor_unicodeChars_2 = chr(int(Hangul_Syllables_2[0], 16))

    Hangul_Syllables_3 = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]
    Hangul_Syllables_3 = np.array(Hangul_Syllables_3)

    kor_s_3 = np.where(kor_q4 == Hangul_Syllables_3)[0][0]
    kor_e_3 = np.where(kor_end == Hangul_Syllables_3)[0][0]

    Hangul_Syllables_3 = Hangul_Syllables_3[kor_s_3 : kor_e_3 + 1]
    kor_unicodeChars_3 = chr(int(Hangul_Syllables_3[0], 16))

    English_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]


    spe_start = "0030"
    spe_end = "0040"                        #특수문자
    eng_start = "0041"
    eng_end = "007A"

    kor_c_start = "1100"
    kor_c_end = "1112"
    kor_middle_start = "1161"
    kor_middle_end = "1175"
    kor_end_start = "11A8"
    kor_end_end = "11C3"


    co = co.split(" ")

    Hangul_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]
    print("check out1")
    Hangul_Syllables = np.array(Hangul_Syllables)

    kor_s = np.where(kor_start == Hangul_Syllables)[0][0]
    kor_e = np.where(kor_end == Hangul_Syllables)[0][0]

    Hangul_Syllables = Hangul_Syllables[kor_s : kor_e + 1]
    kor_unicodeChars = chr(int(Hangul_Syllables[0], 16))

    English_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]

    English_Syllables = np.array(English_Syllables)

    eng_s = np.where(eng_start == English_Syllables)[0][0]
    eng_e = np.where(eng_end == English_Syllables)[0][0]

    English_Syllables = English_Syllables[eng_s : eng_e + 1]
    eng_unicodeChars = chr(int(English_Syllables[0], 16))

    start_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]

    start_Syllables = np.array(start_Syllables)

    start_s = np.where(kor_c_start == start_Syllables)[0][0]
    start_e = np.where(kor_c_end == start_Syllables)[0][0]

    start_Syllables = start_Syllables[start_s : start_e + 1]
    start_unicodeChars = chr(int(start_Syllables[0], 16))
    
    middle_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]

    middle_Syllables = np.array(middle_Syllables)

    middle_s = np.where(kor_middle_start == middle_Syllables)[0][0]
    middle_e = np.where(kor_middle_end == middle_Syllables)[0][0]

    middle_Syllables = middle_Syllables[middle_s : middle_e + 1]
    middle_unicodeChars = chr(int(middle_Syllables[0], 16))
    
    end_Syllables = [a+b+c+d 
                        for a in co 
                        for b in co 
                        for c in co 
                        for d in co]

    end_Syllables = np.array(end_Syllables)

    end_s = np.where(kor_end_start == end_Syllables)[0][0]
    end_e = np.where(kor_end_end == end_Syllables)[0][0]

    end_Syllables = end_Syllables[end_s : end_e + 1]
    end_unicodeChars = chr(int(end_Syllables[0], 16))

    m_ftpng = ftpng()

    #temp = m_ftpng.ttftoimg(fonts, font_path, start_Syllables, start_unicodeChars, 110, 1, 0,"Hangul",0)
    #temp = m_ftpng.ttftoimg(fonts, font_path, middle_Syllables, middle_unicodeChars, 110, 1, temp,"Hangul",temp)
    #temp = m_ftpng.ttftoimg(fonts, font_path, end_Syllables, end_unicodeChars, 110, 1, temp,"Hangul",temp)

    th1 = Process(target = m_ftpng.ttftoimg, args=(fonts, font_path, Hangul_Syllables, kor_unicodeChars, 120, 1, 0,"Hangul", 0))
    
    th1.start()

    th1.join()
