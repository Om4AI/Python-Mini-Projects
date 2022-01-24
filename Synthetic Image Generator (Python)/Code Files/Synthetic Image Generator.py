# Libraries
import random
import math
import dataframe_image as dfi
from PIL import Image, ImageFont, ImageDraw, ImageOps
import shutil
import os
import sys

os.mkdir("Synthetic Images")
# User Argument -------------->

img_count = int(sys.argv[2]);

# Synthetic Image Generation started
for v in range(img_count):
    
#     Inputs
    ogimg = "background.png"
    tarimg = "back_cpy.png"
    shutil.copyfile(ogimg, tarimg)
    
    # Sample data from Client
    data = [
        "1千航そべフ頑供ばちむ報能ワレ氏害ド秋刑ヘハ新5態独クセナ男伸必ケセキヱ賞題ちび石沢温争効まちせ。文あクづ見府ぞす港出ぎ退部セヲキミ出心で側決書スエ導容傑ノ。",
        "入ー拡渦ス百譜ちをはの府労ぴおろざ断53転イ人属レイテア近9殴くみ都展いぜっも終役ット別丈直んと規著モテ営類投ぼや運著タヒカ領日連あ府際なンっの過男述探保れさても。",
        "由技イロ丸歩と店86価23正れくらあ禁導こは断択ミクウフ世済41高レみ情権ぐ民枚照やく。園ぎょゆづ同原ム打武ンらり財決でどっ明量改マ枠力ヒ的域み情賞ルヒラ態広ヘ与記。",
        "供文ら個並く契党ケルヲ客自ト覚聞ナヌ写収業イキ声虜アカヒキ歩思付べッ調隠ン登94無はにす頭回カソサ当護加ヘオロ止載ラヒ皇速もあわ。経毎よ索9去治ま株例ヤヲメス経。",
        "進スヨワチ内届護ロフ獣太4落株ルサヒ暖掲つゆずぴ求球特よま困乗ウオラ観族おーレぐ國平よ直親37気ょすがち担6子ひ察康候ぞ。詳ろぼもど外霊ヲセ損数ネニナシ由横。"
    ]
    
    chars = 0
    for el in data:
        chars+=len(el)
#     print("Total Characters: ", chars,"\n")

    rows = random.randint(3,7)
#     print("Number of rows: ", rows,"\n");
    
    y = 200
    oglen = len(data)
    
#     Actual Loop logic
    while(len(data)!=0):
        sent = random.choice(data)
        
        strings = []
        temp= ""
        for c in sent:
            temp+=c
            if(len(temp)==rows):
                strings.append(temp)
                temp=""
        if(len(temp)>0 and len(temp)<rows): strings.append(temp.ljust(rows))
        
        l1 = []
        p=0
        while(p<rows):
            m = ""
            for i in strings: m=m+i[p]+"  "
            l1.append(m)
            p+=1
        l1 = [x[::-1] for x in l1][::-1]
        l1.reverse()
        
        cols = len(l1[0])
        if(len(data)==oglen): x = 3500-(cols*30)+math.ceil(0.20*(cols*30))
        data.remove(sent)
    
        img = Image.open("back_cpy.png")
        draw = ImageDraw.Draw(img) 
        fontscale = 0.5
        font=ImageFont.truetype("Fonts/ArialUnicodeMS.ttf",44)
        color = (0,0,0)
        thickness = 1

        for i in l1:
            draw.text((x,y), i,fill="black", font=font)
            img.save("back_cpy.png")
            y+=50
        
        if(x-(cols*30)+math.ceil(0.20*(cols*30))) >= 300: 
            x=x-(cols*30)+math.ceil(0.20*(cols*30))
            y-=(len(l1)*50)
        else:
            x = 3500-(cols*30)+math.ceil(0.20*(cols*30))
            y += 100

        # Image name & saving
        img_name = str(v+1)+".png"
        full_name = "Synthetic Images/"+img_name
        if(len(data)==0): img.save(full_name)
    os.remove("back_cpy.png")
    print("Image: ",v+1, " created successfully!")