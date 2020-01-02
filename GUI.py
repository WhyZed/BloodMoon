from tkinter import *
import player




window = Tk()
window.geometry("1700x749")
window.title ("FIGHT!")

#ph = Label(text = str(player.health))
#ph.pack

zombie = PhotoImage(file = "C:\\Users\\123\\Pictures\\zomb.png")
zbel = Label(image = zombie)
zbel.pack()



Slash_image = PhotoImage(file = "C:\\Users\\123\\Pictures\\Slash_image.gif")

slash = Button(window, image = Slash_image)
slash.pack(side = LEFT)



Stab_image = PhotoImage(file = "C:\\Users\\123\\Pictures\\Stab_image.png")

stab = Button(window, image = Stab_image)
stab.pack(side = LEFT)


Throw_image = PhotoImage(file = "C:\\Users\\123\\Pictures\\Throw_image.png")

throw = Button(window, image = Throw_image)
throw.pack(side = LEFT)




window.mainloop()