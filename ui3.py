from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import textwrap

from aift import setting
from aift.multimodal import textqa
setting.set_api_key('Jaq4cvMvKvA2g1nli09iN95etj7cXMPr')

GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหารวันนี้ by ภีม') # Program title
GUI.geometry('700x600') # Window size
GUI.state('zoomed') # Maximize window
style = ttk.Style() # Create a style
style.configure('My.TButton', font=('TH Sarabun New', 24)) # Button font size
style.configure('My.TEntry', font=('TH Sarabun New', 20)) # Entry style
style.configure('My.TLabel', font=('TH Sarabun New', 20)) # Label style for description

# Variable to store input text
v_input_text = StringVar()

# Input entry field
input_entry = ttk.Entry(GUI, textvariable=v_input_text, width=50, style='My.TEntry')
input_entry.pack(pady=10, ipadx=10, ipady=5)

# Input label
input_label = ttk.Label(GUI, text="ป้อนคำถามของคุณที่นี่:", style='My.TLabel')
input_label.pack(pady=5)

def AIreply():
    print('AI is responding')
    # Get text from Entry
    user_query = v_input_text.get()
    print(f"Question received: {user_query}")

    # Use the user's input as the query
    result = textqa.generate(user_query)
    text = result['content']
    wrapped_text = textwrap.fill(text, width=70) # Adjust width for longer text
    
    # Update the label text
    v_result.set(wrapped_text)
    
    # Update scroll region after content changes
    # This ensures the canvas scrollbars adjust to the new content size
    canvas.update_idletasks() # Ensure all pending geometry updates are processed
    canvas.config(scrollregion=canvas.bbox("all"))

B1 = ttk.Button(GUI, text='ถาม AI', style='My.TButton', command=AIreply) 
B1.pack(pady=10, ipadx=30, ipady=20)



## Setting Up the Scrollable Area

# Create a Canvas widget
canvas = Canvas(GUI, borderwidth=0, background="#f3a1de")
canvas.pack(side="left", fill="both", expand=True)

# Create a Scrollbar and link it to the Canvas
vsb = ttk.Scrollbar(GUI, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)

# Create a Frame inside the Canvas to hold the actual content
# All your scrollable widgets will go inside this frame
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Configure the canvas scrolling
# This ensures the scroll region updates when the frame's size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Output label (now inside the scrollable_frame)
v_result = StringVar()
v_result.set('-----output-----')
L1 = ttk.Label(scrollable_frame, textvariable=v_result, font=(None, 20), wraplength=550) # Added wraplength
L1.pack(pady=10, padx=10, fill="both", expand=True)

GUI.mainloop()