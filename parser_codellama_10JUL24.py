import tkinter as tk
from tkinter import messagebox
import re
class HL7Viewer(tk.Tk):
 def __init__(self, hl7_message):
    super().__init__()
    self.title("HL7 Viewer")
    self.geometry("600x400")
    self.hl7_message = hl7_message
    self.segments = re.split('n', self.hl7_message)
    self.create_widgets()
 def create_widgets(self):
 y_offset = 10
 for segment in self.segments:
 if segment:
 frame = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
 frame.pack(fill=tk.X, padx=5, pady=5)
 label = tk.Label(frame, text=segment[:30], font=("Helvetica", 12))
 label.grid(row=0, column=0, sticky="w")
    for i, data in enumerate(re.split('|', segment)):
        if data:
            frame_inside = tk.Frame(frame)
 frame_inside.pack(fill=tk.X, padx=5, pady=(y_offset, 0))
 label_data = tk.Label(frame_inside, text=f"{i+1}.{data}", font=("Helvetica", 10), cursor="hand2")
 label_data.grid(row=0, column=i)
 tooltip = ToolTip(label_data, f"Segment: {segment}nData: {data}")
 y_offset += 15
 def on_enter(event):
 if hasattr(event.widget, "tooltip"):
 event.widget.tooltip.show()
 else:
 event.widget.tooltip = ToolTip(event.widget, f"Segment: {segment}nData: {data}")
 def on_leave(event):
 if hasattr(event.widget, "tooltip"):
 event.widget.tooltip.hide()
 class ToolTip:
 def __init__(self, widget, text):
 self.widget = widget
 self.text = text
 self.widget.bind("<Enter>", self.show)
 self.widget.bind("<Leave>", self.hide)
 def show(self, event=None):
 x = y = 0
 x, y, cx, cy = self.widget.bbox("right")
 x += self.widget.winfo_rootx() + 25
 y += self.widget.winfo_rooty() + 35
 # creates a tk_popup menu
 self.tw = tk.Toplevel(self.widget)
 self.tw.wm_overrideredirect(True)
 self.tw.withdraw()
 self.tw.geometry("+%d+%d" % (x, y))
 self.tw.lift()
 self.tw.focus_set()
 tk.Label(self.tw, text=self.text, justify="left", bg="#ffffff", relief="solid", borderwidth=1, font=("Helvetica", "10")).pack()
 def hide(self, event=None):
 self.tw.destroy()
if __name__ == "__main__":
 hl7_message = """MSH|^A|B|C|D|E|F
 PID|||123456||Doe^John||19800101|M
 PV1||I||Room 201||SURGERY"""
 app = HL7Viewer(hl7_message)
 app.mainloop()