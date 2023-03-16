from pyexpat import model
import tkinter as tk
import time
from PIL import ImageTk, Image
from tkinter import ttk

def current_time():
    return"Progessing ：" + str(int(progressbar["value"])) + "%"
def start():
    B=100/AA.get()
    for i in range(AA.get()): 
        change_positions(i) 
        if progressbar["value"] < progressbar["maximum"]:    # 小於最大值持續增量
            progressbar["value"] += B               # 進度增量 1
            label["text"]=current_time()    # 顯示目前值
            window.update()             # 更新視窗內容
        time.sleep(1)          # 休眠 0.1 秒 
    else:
        label["text"]="Congratulation !"
        
def stop():
    progressbar.stop()                              # 進度條歸零
    label["text"]=current_time()     # 顯示目前值

def change_positions(i):
        CC=i%3
        if CC == 1:
            canvas.coords(img, 225, 75)
           
        
            
            
        elif CC==2:
            canvas.coords(img, 375, 375)
            
            
        elif CC==0:
            canvas.coords(img,75,375)
             

    



# 建立主視窗 Framecolumn
window = tk.Tk()


AA=tk.IntVar()

# 設定視窗標題
window.title('CryRainbow_cry XD!!')

# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 50)
window.geometry("500x600+250+50")

# Define a Canvas widget
canvas = tk.Canvas (window, width=2000, height=2000, background='pink')
canvas.place(x=0,y=0)



img2=ImageTk.PhotoImage(Image.open("286050402_566798714797424_2106140193776282003_n.jpg").resize((150,150)))
canvas.create_image(225,75,image=img2)

img4=ImageTk.PhotoImage(Image.open("286539111_1380233085808451_8098911223593448440_n.jpg").resize((150,150)))
canvas.create_image(75,380,image=img4)



img6=ImageTk.PhotoImage(Image.open("286931952_396803379172765_7487291410112522820_n.jpg").resize((150,150)))
canvas.create_image(380,380,image=img6)

#move image with canvas
img3=ImageTk.PhotoImage(Image.open("286035448_1230121744454538_4255567908550044345_n.jpg").resize((50,50)))
img=canvas.create_image(75,375, image=img3)#晶圓
# canvas.create_image(300,75, image=img3)#船葉


# img3=canvas.create_image(10, 10,image=ImageTk.PhotoImage(Image.open("284407271_919438562345466_2873006905758187240_n.jpg").resize((50,50))))
# canvas.move(img3, 20, 0)




tk.Label(window, text="Down count please entry here !(s)").place(x=0,y=475)
tk.Entry(window, textvariable=AA).place(x=200,y=475)


#create progressbar
tk.Label(window, text="Progressbar：").place(x=25,y=500)
progressbar=ttk.Progressbar(window,length=250,mode="determinate")
progressbar.place(x=100,y=500)
ttk.Button(window, text="Start", command=start).place(x=175,y=525)     # 進度開始
ttk.Button(window, text="Reset", command=stop).place(x=175,y=550)     # 進度停止 (歸零)
label=ttk.Label(window)
label.place(x=175,y=575)

# 執行主程式
window.mainloop()