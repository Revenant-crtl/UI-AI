from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import pyttsx3
from aift import setting
from aift.multimodal import textqa

# Set API Key
setting.set_api_key('Jaq4cvMvKvA2g1nli09iN95etj7cXMPr')

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# GUI setup
GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหารวันนี้ by ภีม')
GUI.geometry('700x600')
GUI.state('zoomed')

# Style configuration
style = ttk.Style()
style.configure('My.TButton', font=('TH Sarabun New', 24))
style.configure('My.TEntry', font=('TH Sarabun New', 20))
style.configure('My.TLabel', font=('TH Sarabun New', 20))

# User input field
v_input_text = StringVar()
input_label = ttk.Label(GUI, text="ป้อนคำถามของคุณที่นี่:", style='My.TLabel')
input_label.pack(pady=5)

input_entry = ttk.Entry(GUI, textvariable=v_input_text, width=50, style='My.TEntry')
input_entry.pack(pady=10, ipadx=10, ipady=5)

# Function to call AI and speak the response
def AIreply():
    user_query = v_input_text.get()
    if user_query.strip() == "":
        return
    
    result = textqa.generate(user_query)
    text = result['content']
    
    # Speak the response
    engine.say(text)
    engine.runAndWait()

# Ask AI Button
B1 = ttk.Button(GUI, text='ถาม AI', style='My.TButton', command=AIreply)
B1.pack(pady=10, ipadx=30, ipady=20)

# Run the GUI
GUI.mainloop()
