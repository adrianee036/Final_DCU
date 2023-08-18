import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl


class RegistroDesigner:

    def registrar():
            pass
   

    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Registrar')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventanas(self.ventana,400,400)
        
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de estudiante",font=('Times', 18), fg="#666a88",bg='#fcfcfc',pady=10)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_matricula = tk.Label(frame_form_fill, text="Matricula", font=('Times', 12) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_matricula.pack(fill=tk.X, padx=20,pady=5)
        self.matricula = ttk.Entry(frame_form_fill, font=('Times', 10))
        self.matricula.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_nombre = tk.Label(frame_form_fill, text="Nombre", font=('Times', 12) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20,pady=5)
        self.nombre = ttk.Entry(frame_form_fill, font=('Times', 10))
        self.nombre.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 12),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 10))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        registrar = tk.Button(frame_form_fill,text="Registrar",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.registrar)
        registrar.pack(fill=tk.X, padx=20,pady=20)        
        registrar.bind("<Return>", (lambda event: self.registrar()))

        #end frame_form_fill
        self.ventana.mainloop()

        