from tkinter import *
import speedtest


def test():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lab_down_speed.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x700")
sp.config(bg="dodgerblue")

lab = Label(sp, text=" Internet Speed Test ", font=("calibri",20, "bold"), bg="dodgerblue", fg="white")
lab.place(x=60, y=40 ,height=50,width=380)


lab = Label(sp, text=" Download Speed ", font=("calibri",20, "bold"))
lab.place(x=60, y=140,height=50,width=380)


lab_down_speed = Label(sp, text=" 00.00 ", font=("calibri",20, "bold"))
lab_down_speed.place(x=60, y=190,height=50,width=380)


lab = Label(sp, text=" Upload Speed ", font=("calibri",20, "bold"))
lab.place(x=60, y=240,height=50,width=380)


lab_up = Label(sp, text=" 00.00 ", font=("calibri",20, "bold"),bg="white")
lab_up.place(x=60, y=290,height=50,width=380)


button = Button(sp, text=" Test ", font=("calibri",20, "bold"),bg="white",fg="dodgerblue",relief=RAISED,command=test)
button.place(x=60, y=390,height=50,width=380)

sp.mainloop()