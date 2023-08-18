import tkinter as tk
from forms.registro.form_registro_designer import RegistroDesigner
from db.repository.auth_user_repositary import AuthUserRepositroy
from db.model import Auth_User
import util.encoding_decoding as end_dec
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl



class Registro(RegistroDesigner):
   

    def __init__(self):  
        self.auth_repository = AuthUserRepositroy()      
        super().__init__()
    
    def registrar(self):                   
            user = Auth_User()
            user.matricula = self.matricula.get()
            user_db: Auth_User = self.auth_repository.getUserByUserName(
                self.matricula.get())
            if not (self.isUserRegister(user_db)):
                user.password = end_dec.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showinfo(
                    message="Se registro el usuario", title="Mensaje")     
                self.ventana.destroy()


    def isUserRegister(self, user: Auth_User):
        status: bool = False
        if(user != None):
            status = True
            messagebox.showerror(
                message="El usuario ya existe", title="Mensaje")
        return status