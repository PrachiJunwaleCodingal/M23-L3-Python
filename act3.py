#temp convertor
import tkinter as tk

def FahToCel():
    fahr = temp_ip.get()
    cel = (5/9) * (float(fahr) - 32)
    lbl_result["text"] = f"{round(cel, 2)} \N{DEGREE celsius}"
 

window = tk.Tk()
window.title("TempConverter")
window.geometry("200x200")

frm_entry = tk.Frame(master=window)
temp_ip = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE fahrenheit}")

temp_ip.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="=",command=FahToCel)
lbl_result = tk.Label(master=window, text="\N{DEGREE celsius}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()