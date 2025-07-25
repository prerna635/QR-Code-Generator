import qrcode
from tkinter import *
from tkinter import messagebox

def generate_qr():
    data = entry.get()
    if data.strip() == "":
        messagebox.showwarning("Input Error", "Please enter some text or a URL.")
        return

    qr = qrcode.make(data)
    qr.save("my_qr.png")
    messagebox.showinfo("Success", "QR Code saved as my_qr.png")

# GUI Setup
root = Tk()
root.title("QR Code Generator")
root.geometry("400x200")
root.config(bg="lightblue")

Label(root, text="Enter text or URL:", font=("Arial", 14), bg="lightblue").pack(pady=10)

entry = Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

root.mainloop()
