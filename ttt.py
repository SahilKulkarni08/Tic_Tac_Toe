#author : Sahil Kulkarni

from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("Tic Tac Toe")
click = 1
total_moves = 0


def disableButton():
    btn1.configure(state=DISABLED)
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
    btn4.configure(state=DISABLED)
    btn5.configure(state=DISABLED)
    btn6.configure(state=DISABLED)
    btn7.configure(state=DISABLED)
    btn8.configure(state=DISABLED)
    btn9.configure(state=DISABLED)
def btnClick(buttons):
    global click, total_moves
    if buttons["text"] == " " and click == 1:
        buttons["text"] = "X"
        click = 0


        total_moves += 1
        checkForWin()

    elif buttons["text"] == " " and click == 0:
        buttons["text"] = "O"
        click = 1

        checkForWin()
        total_moves += 1

    else:
        tkinter.messagebox.showinfo("TTT", "Button already Clicked!")
def checkForWin():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
        btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X'):

        disableButton()
        tkinter.messagebox.showinfo("TTT", "first player wins(X)")
    elif(total_moves==9):
        tkinter.messagebox.showinfo("TTT", "It is a Tie")
    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' ):
        disableButton()
        tkinter.messagebox.showinfo("TTT", "second player wins(O)")




buttons = StringVar()
btn1 = Button(root, text=" ", font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn1))
btn1.grid(row=1, column=1)
btn2 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn2))
btn2.grid(row=1, column=2)
btn3 = Button(root, text=' ',font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn3))
btn3.grid(row=1, column=3)
btn4 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn4))
btn4.grid(row=2, column=1)
btn5 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn5))
btn5.grid(row=2, column=2)
btn6 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn6))
btn6.grid(row=2, column=3)
btn7 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn7))
btn7.grid(row=3, column=1)
btn8 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn8))
btn8.grid(row=3, column=2)
btn9 = Button(root, text=' ', font='Times 20 bold', bg='red', fg='blue', height=4, width=8, command=lambda: btnClick(btn9))
btn9.grid(row=3, column=3)

root.mainloop()