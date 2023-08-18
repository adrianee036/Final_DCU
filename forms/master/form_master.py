import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
    def deslogear(self):
        nuevo_archivo = open("remember.txt", "w")
        nuevo_archivo.write("login")
        nuevo_archivo.close()
        self.ventana.destroy()
        from forms.login.form_login import FormLogin
        FormLogin().mainloop()
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)            
        
        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='#023875' )
        label.place(x=0,y=0,relwidth=1, relheight=1)

        title = tk.Label(self.ventana, text="Sesion iniciada",font=('Times', 30), fg="#fcfcfc",bg='#023875',pady=10)
        title.pack()

        inicio = tk.Button(self.ventana, text="Cerrar Sesión", font=(
            'Times', 15), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.deslogear)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.deslogear()))
        
        self.ventana.mainloop()
