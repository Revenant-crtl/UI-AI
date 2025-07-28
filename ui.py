from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import textwrap

from aift import setting
from aift.multimodal import textqa
setting.set_api_key('Jaq4cvMvKvA2g1nli09iN95etj7cXMPr')


GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหารวันนี้ by ภีม') # ชื่อโปรแกรม
GUI.geometry('700x600') # ปรับขนาดหน้าจอ
GUI.state('zoomed')
style = ttk.Style() # สร้างสไตล์
style.configure('My.TButton', font=('TH Sarabun New', 24)) # ขนาดฟอนต์

def AIreply():
   print('ai กำลังตอบ')
   result = textqa.generate('กินอะไรดีเที่ยงนี้? ขอแบบพิศดาร')
   text = result['content']
   wrapped_text = textwrap.fill(text, width=50)
   
   v_result.set(wrapped_text)

B1 = ttk.Button(GUI,text='วีนนี้กินอะไรดี', style='My.TButton',command=AIreply) 
B1.pack(pady=30,ipadx=30, ipady=20)

v_result = StringVar()
v_result.set('-----output-----')
L1 = ttk.Label(GUI,textvariable=v_result,font=(None,40))
L1.pack()

GUI.mainloop()
