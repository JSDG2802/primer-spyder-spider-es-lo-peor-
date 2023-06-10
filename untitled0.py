
from tkinter import * 
root = Tk() 
root.title("SPYDER DEBERIA DE TENER VIRRUS") 
root.geometry("800x400") 

show_label=Label(root,text="12",font=("courier",20))
show_label.pack()
show_label2=Label(root,text="10",font=("courier",20))
show_label2.pack()
show_resultado=Label(root,font=("courier",20))

def multi():
    resultado=12*10
    show_resultado["text"]=resultado
    show_resultado.pack()
    bg="red"
    
btn = Button(root,text="X",font=("courier",20),bg="yellow",command=multi);
btn.pack()



def mashimas():
    resultado=12+10
    show_resultado["text"]=resultado
    show_resultado.pack()
    
btn = Button(root,text="+",font=("courier",20),bg="blue",command=mashimas);
btn.pack()



def menos():
    resultado=12-10
    show_resultado["text"]=resultado
    show_resultado.pack()
btn = Button(root,text="-",font=("courier",20),bg="red",command=menos);
btn.pack()



def dividivi():
    resultado=12//10
    show_resultado["text"]=resultado
    show_resultado.pack()
    
btn = Button(root,text="÷",font=("courier",20),bg="green",command=dividivi);
btn.pack()
root.mainloop()



