from tkinter import *
Tik = Tk()
size=60
Tik.title("Jeu de dames")
BG = Frame(Tik, bg = 'maroon')
BG.grid()
can = Canvas(BG, width = 600,height = 600, bg = "white")
can.grid(row = 0, column = 0, columnspan = 2)
[[can.create_rectangle(60*j,60*i,60*(j+1),60*(i + 1),width=2,fill="red",state='disabled')and can.create_rectangle(60*(j + 1),60*(i + 1),60*(j + 2),60*(i + 2),width=2,fill="red",state='disabled')for j in range(0, 10, 2)]for i in range(1, 10, 2)]
exit = Button(BG, text = "  Exit  ",bg = 'grey', fg = 'yellow',relief = 'ridge', bd = 3,command = Tik.destroy)
exit.grid(row = 1, column = 1, padx = 8, pady = 8, sticky = 'w')
for i in range(1, 10, 2) :
    if i<=6:
        Fill='blue'
    else:
        Fill='black'
    for j in range(0,10,2):
        if(i<=3 or i>=7):
            can.create_oval((60*j)+10,(60*i)+10,(60*(j+1))-10,(60*(i+1))-10,width=2,fill=Fill)
            can.create_oval((60*(j+1))+10,(60*(i+1))+10,(60*(j+2))-10,(60*(i+2))-10,width=2,fill=Fill)
Tik.mainloop()