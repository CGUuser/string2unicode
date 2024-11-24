import tkinter as tk

from tkinter import messagebox

# oled u8g2 chinese string to unicode
# https://blog.jmaker.com.tw/chinese_oled/

def validate_input(text):
    # Check if the input text meets the format (each character separated by a comma)
    for char in text.replace(",", ""):
        if not ('\u4e00' <= char <= '\u9fff'):
            return False
    return True


def convert_to_unicode():
    # Convert the text to Unicode format
    text = input_entry.get()
    
    # Validate the input format
    if not validate_input(text):
        messagebox.showerror("Error", "Please enter valid Traditional Chinese characters separated by commas.")
        return

    # Split the text and convert to Unicode
    unicode_list = [f"\\u{ord(char):04x}" for char in text.replace(",", "")]
    unicode_result = ",".join(unicode_list)
    unicode_output.set(unicode_result)

    # Convert to u8g2 format
    u8g2_list = [f"${ord(char):04x}" for char in text.replace(",", "")]
    u8g2_result = ",".join(u8g2_list)
    u8g2_output.set(u8g2_result)


# Create the Tkinter window
root = tk.Tk()
root.title("Traditional Chinese Conversion Tool")

# Input area
tk.Label(root, text="Enter Text (Separated by Commas)").grid(row=0, column=0, sticky="w")
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1)

# Conversion button
convert_button = tk.Button(root, text="Convert", command=convert_to_unicode)
convert_button.grid(row=0, column=2)

# Unicode output
tk.Label(root, text="Unicode Conversion Result").grid(row=1, column=0, sticky="w")
unicode_output = tk.StringVar()
unicode_label = tk.Entry(root, textvariable=unicode_output, state="readonly", width=50)
unicode_label.grid(row=1, column=1)

# u8g2 output
tk.Label(root, text="U8G2 Conversion Result").grid(row=2, column=0, sticky="w")
u8g2_output = tk.StringVar()
u8g2_label = tk.Entry(root, textvariable=u8g2_output, state="readonly", width=50)
u8g2_label.grid(row=2, column=1)

# Start the main loop
root.mainloop()
