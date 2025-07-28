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
style.configure('My.TLabel', font=('TH Sarabun New', 20)) # สไตล์สำหรับ Label คำอธิบาย

# Label คำอธิบาย
input_label = ttk.Label(GUI, text="ป้อนคำถามของคุณที่นี่:", style='My.TLabel')
input_label.pack(pady=5)

# ช่องสำหรับรับ input แบบหลายบรรทัด
input_text_area = Text(GUI, height=5, width=60, font=('TH Sarabun New', 18))
input_text_area.pack(pady=10)


def AIreply():
    print('ai กำลังตอบ')
    # ดึงข้อความจาก Text widget
    # 1.0 คือจากบรรทัดที่ 1 อักขระที่ 0 (เริ่มต้น)
    # END-1c คือถึงตัวอักษรสุดท้าย ลบด้วย 1 ตัวอักษร (เพื่อไม่เอาอักขระขึ้นบรรทัดใหม่ที่ Text สร้างขึ้นมา)
    user_query = input_text_area.get("1.0", END + "-1c")
    print(f"คำถามที่ได้รับ: {user_query}")

    result = textqa.generate(user_query)
    text = result['content']
    wrapped_text = textwrap.fill(text, width=70)
    
    v_result.set(wrapped_text)

B1 = ttk.Button(GUI,text='ถาม AI', style='My.TButton',command=AIreply) 
B1.pack(pady=10,ipadx=30, ipady=20)

v_result = StringVar()
v_result.set('-----output-----')
L1 = ttk.Label(GUI,textvariable=v_result,font=(None,40))
L1.pack()

GUI.mainloop()