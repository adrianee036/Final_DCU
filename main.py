nuevo_archivo = open("remember.txt", "r")


if(nuevo_archivo.read() == "master"):
    from forms.master.form_master import MasterPanel
    MasterPanel()

else:
    from forms.login.form_login import FormLogin
    FormLogin()
