from tkinter import *

root = Tk()
root.title("SUNGHWAN GUI")
root.geometry("640x480")

label = Label(root,text="안녕하세요")
label.pack()

photo = PhotoImage(file ="gui_basic/img1.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label.config(text="또 만나요") 

    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop()
