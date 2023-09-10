from tkinter import *
from tkinter import messagebox


class Play:
  global listo
  global listx

  listo = []
  listx = []
  
  def show (self):
    global turn
    turn = ""

    lo=len(listo)
    lx=len(listx)

    if lo==lx:
      turn="x"
    if lx>lo:
      turn="o"

  
    if turn=="o":
      if self not in listx:
        listo.append(self)

    if turn=="x":
      if self not in listo:
        listx.append(self)


    print(listo)
    print(listx)








#blue

    if turn=="x" and self==1:
      btn1=Button(root,bg="lightblue",text=" ",padx=40,pady=34,state="disabled")
      btn1.grid(row=0,column=0)

    if turn=="x" and self==2:
      btn2=Button(root,bg="lightblue",text=" ",padx=40,pady=34,state="disabled")
      btn2.grid(row=0,column=1)

    if turn=="x" and self==3:
      btn3=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn3.grid(row=0,column=2)


    if turn=="x" and self==4:
      btn4=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn4.grid(row=1,column=0)


    if turn=="x" and self==5:
      btn5=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn5.grid(row=1,column=1)


    if turn=="x" and self==6:
      btn6=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn6.grid(row=1,column=2)


    if turn=="x" and self==7:
      btn7=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn7.grid(row=2,column=0)


    if turn=="x" and self==8:
      btn8=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn8.grid(row=2,column=1)


    if turn=="x" and self==9:
      btn9=Button(root,bg="lightblue",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn9.grid(row=2,column=2)




#red

    if turn=="o" and self==1:
      btn1=Button(root,bg="red",text=" ",padx=40,pady=34,state="disabled")
      btn1.grid(row=0,column=0)

    if turn=="o" and self==2:
      btn2=Button(root,bg="red",text=" ",padx=40,pady=34,state="disabled")
      btn2.grid(row=0,column=1)

    if turn=="o" and self==3:
      btn3=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn3.grid(row=0,column=2)


    if turn=="o" and self==4:
      btn4=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn4.grid(row=1,column=0)


    if turn=="o" and self==5:
      btn5=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn5.grid(row=1,column=1)


    if turn=="o" and self==6:
      btn6=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn6.grid(row=1,column=2)


    if turn=="o" and self==7:
      btn7=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn7.grid(row=2,column=0)


    if turn=="o" and self==8:
      btn8=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn8.grid(row=2,column=1)


    if turn=="o" and self==9:
      btn9=Button(root,bg="red",text=" ",padx=40,pady=34, command = lambda : Play.show(1),state="disabled")
      btn9.grid(row=2,column=2)


#winner winner chicken dinner





    if 1 in listo:
        if 2 in listo:
          if 3 in listo:
            messagebox.showinfo("Win","well done O you won")
            root.destroy()

    if 4 in listo:
      if 5 in listo:
        if  6 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    if 7 in listo:
      if 8 in listo:
        if 9 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    if 1 in listo:
      if 4 in listo:
        if 7 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    if 2 in listo:
       if 5 in listo:
        if 8 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    if 3 in listo:
       if 6 in listo:
        if 9 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    if 1 in listo:
       if 5 in listo:
        if 9 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    if 3 in listo:
       if 5 in listo:
        if 7 in listo:
          messagebox.showinfo("Win","well done O you won")
          root.destroy()

    
    if lo > 3:
      messagebox.showinfo("nobody wins","Try again")
    if lx > 3:
      messagebox.showinfo("nobody wins","Try again")


    if 1 in listx:
        if 2 in listx:
          if 3 in listx:
            messagebox.showinfo("Win","well done x you won")
            root.destroy()

    if 4 in listx:
      if 5 in listx:
        if  6 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    if 7 in listx:
      if 8 in listx:
        if 9 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    if 1 in listx:
      if 4 in listx:
        if 7 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    if 2 in listx:
       if 5 in listx:
        if 8 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    if 3 in listx:
       if 6 in listx:
        if 9 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    if 1 in listx:
       if 5 in listx:
        if 9 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    if 3 in listx:
       if 5 in listx:
        if 7 in listx:
          messagebox.showinfo("Win","well done x you won")
          root.destroy()

    
    if lo > 3:
      messagebox.showinfo("nobody wins","Try again")
    if lx > 3:
      messagebox.showinfo("nobody wins","Try again")



  # x blue
  # o red





root = Tk()

btn1=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(1))
btn2=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(2))
btn3=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(3))
btn4=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(4))
btn5=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(5))
btn6=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(6))
btn7=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(7))
btn8=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(8))
btn9=Button(root,text=" ",padx=40,pady=34, command = lambda : Play.show(9))



btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

root.mainloop()
