import tkinter as tk
from tkinter import Grid
root=tk.Tk()
var =tk.StringVar()
#var.set("initial")
def clear():
    var.set('')
    
def bk_clear():
    text =var.get()
    if text:
        var.set(text[:-1])
        
def evalute():
    expr=var.get()
    try:
        ans=eval(expr)
    except Exception as e:
        ans="invalid input"
    finally:
        var.set(ans)

def add_char(label):
    new_str=var.get()+label
    var.set(new_str)
    
    
    
labels=[
    ['AC', False, False, False, 'BK'],
    ['1','2','3','-','/'],
    ['4','5','6',"*",'%'],
    ['7','8','9',False,'**'],
    ['00','0','.',False,' '],]

buttons=[]
extra=[]

for row in range(6):
    for col in range(5):
        if row==0 and col<=3 and col>0:
            if col==1:
                entry=tk.Entry(root, textvariable=var)
                entry.config(bg='#123456',fg='White')
                entry.config(font=('Time',40,'bold'))
                entry.grid(row=row,column=col,columnspan=3,sticky=tk.N+tk.W+tk.S+tk.E)
                
        elif row>2 and row<5 and col==3:
            if row==3:
                bt=tk.Button(root,text='+')
                bt.config(font=('monospace',20,'bold'))
                bt.config(bg='#333333',fg='#eeeeee',height=1,width=10)
                bt.grid(row=row,column=col,rowspan=2,padx=5,pady=5,sticky=tk.N+tk.S+tk.E+tk.W)
                buttons.append(bt)
                label="+"
                bt.config(command=lambda char=label: add_char(char))
                
        elif row<5:
            bt=tk.Button(root,text=labels[row][col])
            bt.config(font=('monospace',20,'bold'))
            bt.config(bg='#333333',fg='#eeeeee',height=1,width=10)
            bt.grid(row=row,column=col,padx=5,pady=5,sticky=tk.N+tk.S+tk.E+tk.W)
            buttons.append(bt)
            label=labels[row][col]
            if label=="AC":
                bt.config(command=lambda: clear())
            elif label=="BK":
                bt.config(command=lambda: bk_clear())
            else:
                bt.config(command=lambda char=label: add_char(char))
                
        else:
            if col==0:
                bt=tk.Button(root,text='Exit')
                #bt.config(command= root.destroy)#bt.config(command=lambda:root.quit())
                bt.config(font=('monospace',20,'bold'))
                bt.config(bg='#333333',fg='#eeeeee',height=1,width=10)
                bt.grid(row=row,column=col,padx=5,pady=5,sticky=tk.N+tk.S+tk.E+tk.W,columnspan=3)
                buttons.append(bt)
                
            if col==3:
                bt=tk.Button(root,text='=')
                bt.config(font=('monospace',20,'bold'))
                bt.config(bg='#333333',fg='#eeeeee',height=1,width=10)
                bt.grid(row=row,column=col,padx=5,pady=5,sticky=tk.N+tk.S+tk.E+tk.W,columnspan=2)
                buttons.append(bt)
                bt.config(command=lambda: evalute())
                
        Grid.rowconfigure(root,row,weight=1)
        Grid.columnconfigure(root,col,weight=1)
root.mainloop()
