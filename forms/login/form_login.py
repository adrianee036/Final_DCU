import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner
from db.repository.auth_user_repositary import AuthUserRepositroy
from db.model import Auth_User
import util.encoding_decoding as end_dec
from forms.registro.form_registro import Registro

class FormLogin(FormLoginDesigner):
    
    def __init__(self):
        self.auth_repository = AuthUserRepositroy()
        super().__init__()


    def verificar(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)  

    def registrar(self):
        Registro().mainloop()
                      
    def isUser(self, user: Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe por favor registrese", title="Mensaje",parent=self.ventana)            
        return status
    
    def isUserRegister(self, user: Auth_User):
        status: bool = False
        if(user != None):
            status = True
            messagebox.showerror(
                message="El usuario ya existe", title="Mensaje")
        return status
    

    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.ventana.destroy()
            nuevo_archivo = open("remember.txt", "w")
            nuevo_archivo.write("master")
            nuevo_archivo.close()
            MasterPanel()
            
            
        else:
            messagebox.showerror(
                message="La contraseña no es correcta", title="Mensaje")