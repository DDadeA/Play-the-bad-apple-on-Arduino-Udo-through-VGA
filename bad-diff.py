# sourcse
# https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
# https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil
# https://cjsal95.tistory.com/35

# 영감을 받은 곳: https://www.youtube.com/watch?v=YeJHNLg92Qs
# 제작자: 정연호 (DDadeA)

from PIL import Image
import math

print('몇 프레임까지 이미지를 변환할까요? ')
fm = int(input()) + 1
bias = 40
#scale = 1

f = open("gen.txt", 'w')
f2 = open("gen2.txt", 'w')

#f.write('#include <VGAX.h>\n\n')

#frames=2
#while frames < fm:
#    f.write('extern uint8_t img_'+str(frames)+'_data[];\n')
#    frames = frames + 1

#f2.write('#include <avr/pgmspace.h>\n\n')
frames=2
differs = []
f2.write("const PROGMEM unsigned char *const data_list[] = {")

while frames < fm:
    differ = 0
    #dir_path = filedialog.askopenfilename(parent=root,initialdir="/",title='이미지를 선택해주세요(*.jpg, *.png)')
    #dir_path = 'Z:\\PROJECT\\0_arduino\\vga\\rickroll-120-60-8fps\\a\\a ('+str(frames)+').png'
    dir_path = 'Z:\\PROJECT\\0_arduino\\vga\\40-20-6fps-diff\\ba 3\\a ('+str(frames)+').png'
    #dir_path = 'Z:\\PROJECT\\0_arduino\\vga\\40-20-6fps-diff\\a ('+str(frames)+').png'
    print("\ndir_path : ", dir_path)
    imagesrc = dir_path
    
    x = 0
    y = 0
    
    
    im = Image.open(imagesrc) # Can be many different formats.
    pix = im.load()    # Can be many different formats.
    #osize = im.size 
    size = im.size 
    
    
    #im = im.resize((math.floor(osize[0]*scale),math.floor(osize[1]*scale)),Image.ANTIALIAS) #이미지 크기 변경 내림
    #im = im.resize((math.round(osize[0]*scale),math.round(osize[1]*scale)),Image.ANTIALIAS) #반올림
    #im = im.resize((math.ceil(osize[0]*scale),math.ceil(osize[1]*scale)),Image.ANTIALIAS) #올림
    #size = im.size #수정 후 크기 다시 불러오기
    #pix = im.load()
    

    print("%d, %d" % (size[0],size[1]))
    #f2.write("const unsigned char img_"+str(frames)+"_data["+str(size[0])+"]["+str(size[1])+"] PROGMEM={\n   ")

    f.write("const PROGMEM unsigned char data_"+str(frames)+"[] ={ ")
    f2.write("data_"+str(frames)+", ")
    k = 0
    while y < size[1]:
        #f2.write('{')
        
        while x < size[0]:
            #tp = [str(int((int(pix[x,y][0])+int(pix[x,y][1])+int(pix[x,y][2]))/3)),str(int((int(pix[x+1,y][0])+int(pix[x+1,y][1])+int(pix[x+1,y][2]))/3)),str(int((int(pix[x+2,y][0])+int(pix[x+2,y][1])+int(pix[x+2,y][2]))/3)),str(int((int(pix[x+3,y][0])+int(pix[x+3,y][1])+int(pix[x+3,y][2]))/3))]
            #pt = str(pix[x,y][0]).replace('255','1')
            #print(pt)
            if pix[x,y][0]==255:
                differ = differ + 1
                if not (x+y*40-k) >= 255:
                    f.write(str(x+y*40-k)+", ")
                    k = x+y*40
                else:
                    n = x+y*40-k
                    while n > 255:
                        f.write('255'+", ")
                        differ = differ + 1
                        n = n - 255
                    f.write(str(n)+", ")
                    k = x+y*40
                #f.write(str(y*40+x)+",")
            x = x + 1
        #f2.write("},\n   ")
        #f2.write("\n   ")
        x = 0
        y = y + 1
    f.write('};\n')
    differs.append(differ)
    frames=frames+1
    
#f.write('VGAX vga;\n\nvoid setup() {\n  vga.begin();\n  vga.copy((byte*)img_2_data);\n}\nvoid loop() {\n  static unsigned cnt;\n  if (!(cnt % 10))\n    vga.noTone();\n  if (!(cnt++%20))\n  vga.tone(cnt*10+11);\n  if (cnt>='+str(bias*fm)+')\n    cnt=0;')
#f.write('\n  if (cnt<'+str(bias)+')\n  vga.copy((byte*)img_2_data);')

"""k = 3
while k < fm:
    f.write('\n  else if (cnt<'+str(bias*k)+')\n    vga.copy((byte*)img_'+str(k)+'_data);')
    k = k + 1
f.write('\n}') """

f2.write("};\n")
f2.write("const PROGMEM uint16_t data_length[] = {"+str(differs)[:-1][1:]+"};")

f.close
f2.close
