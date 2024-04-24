import qrcode
import tkinter as tk

#input website
link = input("Enter your link: ")
filename = input("Enter your filename: ")

# qr code settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=1,
)
qr.add_data(link)
qr.make(fit=True)

# generate qr code
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"Codes/{filename}.png")

#create window
win = tk.Tk()
win.geometry("650x650")
win.title("Your QR Code")
win.resizable(False, False)

# set icon to your qr code
icon = tk.PhotoImage(file=f"Codes/{filename}.png")
win.iconphoto(False, icon)


print(f"Your QR code has been saved as {filename}.png in the 'Codes' folder\nYou can also view it in the tkinter window.")

#display image
photo = tk.PhotoImage(file=f"Codes/{filename}.png")
image = tk.Label(win, image=photo)
image.pack()

win.mainloop()
