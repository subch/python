import tkinter as tk
from tkinter import filedialog

# HL7 field descriptions (you can expand this dictionary as needed)
HL7_FIELD_DESCRIPTIONS = {
    "OBR.1": "Set ID - OBR",
    "OBR.2": "Placer Order Number",
    "OBR.3": "Filler Order Number",
    "OBR.4": "Universal Service Identifier",
    "OBR.5": "Priority - OBR",
    "OBR.6": "Requested Date/Time",
    "OBR.7": "Observation Date/Time",
    "OBR.8": "Observation End Date/Time",
    "OBR.9": "Collection Volume",
    "OBR.10": "Collector Identifier",
    "OBR.11": "Specimen Action Code",
    "OBR.12": "Danger Code"
}

def get_field_description(segment_name, field_number):
    field_key = f"{segment_name}.{field_number}"
    return HL7_FIELD_DESCRIPTIONS.get(field_key, f"Field {field_number}")

def open_file_dialog():
    filename = filedialog.askopenfilename(filetypes=[("HL7 Files", "*.hl7")])
    if filename:
        with open(filename, "r") as hl7_file:
            hl7_message = hl7_file.read()
            segments = hl7_message.split("\n")

            window = tk.Toplevel(root)
            window.title("HL7 Segment Viewer")

            text_widget = tk.Text(window, wrap=tk.WORD)
            text_widget.pack(fill=tk.BOTH, expand=True)

            for segment in segments:
                fields = segment.split("|")
                if fields:
                    segment_name = fields[0]
                    text_widget.insert(tk.END, f"Segment: {segment_name}\n")
                    for i, field in enumerate(fields[1:], start=1):
                        if field.strip():  # Omit blank fields
                            field_description = get_field_description(segment_name, i)
                            text_widget.insert(tk.END, f"  {field_description}: {field}\n")

root = tk.Tk()
root.title("HL7 File Parser")

button = tk.Button(root, text="Open HL7 File", command=open_file_dialog)
button.pack(pady=10)

root.mainloop()
