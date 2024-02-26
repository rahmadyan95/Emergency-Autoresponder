from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from model.CTkSlideView import CTkSlideView 
from PIL import Image

class tkinterApp (ctk.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login_page,StartPage, Page1, Page2, Page3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame(Login_page)
        # self.show_frame(Page3)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
            

class Login_page(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.first_run = True
        '''
        Bagian ini digunakan untuk memberikan nama pada latar belakang dari
        login dan register box
        
        '''

        self.run()
    
    def run(self):
        self.login_page()

    def toggle_first_run(self):
        self.first_run = not self.first_run
        self.login_page()

    def login_page(self):
        
        box = CTkFrame(self,height=788, width=1400,fg_color="white",bg_color="white")
        box.place(x=0,y=0)

        login_box = CTkFrame(self,height=660,width=1244
                              ,fg_color='grey50',bg_color="white",border_width=8,border_color='grey40')
        login_box.place(relx=0.5, rely=0.5,anchor=CENTER)

        login_field = CTkFrame(login_box,height=630,width=450
                              ,fg_color='grey20',bg_color="grey50",
                              border_width=8,border_color="white")
        login_field.place(x=779, y=15)

        logo_directory = os.path.join(self.script_dir, 'assets', 'App_logo.png')
        logo = CTkImage(light_image=Image.open(logo_directory), size=(600,250))
        logo_placeholder = CTkButton(login_box,image=logo,fg_color='grey20',text='',state="diabled" ,border_width=4,border_color="white")
        logo_placeholder.place(x=100 , y=200)
    

        if self.first_run:

            login_field_title = CTkLabel(login_field,text="Automatic Emergency Responder",font=self.font(28))
            login_field_title.place(relx=0.5,rely=0.04,anchor=N)
            

            login_box = CTkFrame(login_field,height=360,width=390,fg_color='grey50'
                                 ,border_color='white',border_width=5)
            login_box.place(relx=0.5,rely=0.4, anchor=CENTER)
            
            login_title = CTkLabel(login_box,text="Responder Login",font=self.font(22),
                                   text_color='white')
            login_title.place(relx=0.5,rely=0.04,anchor=N)

            button_register = CTkButton(login_field, text="Register",fg_color='green', 
                                        command=self.toggle_first_run,height=40,width=280)
            button_register.place(relx=0.5, rely=0.93, anchor=S)

            self.badge_number = CTkEntry(login_box,placeholder_text="Input Badge Number",font=self.font(18),
                                         height=60,width=350,text_color='white',placeholder_text_color='grey50')
            self.badge_number.place(relx=0.5,rely=0.17,anchor=N)

            self.password = CTkEntry(login_box,placeholder_text="Input Password",font=self.font(18),
                                         height=60,width=350,text_color='white',placeholder_text_color='grey50')
            self.password.place(relx=0.5,rely=0.37,anchor=N)

            button_login = CTkButton(login_box, text="Login",fg_color='cyan', 
                                        command=self.toggle_first_run,height=40,width=280)
            button_login.place(relx=0.5, rely=0.93, anchor=S)
       
        elif self.first_run == False :
            login_field_title = CTkLabel(login_field,text="–✦– Register –✦–",font=self.font(48))
            login_field_title.place(relx=0.5,rely=0.05,anchor=N)
            button_signin = CTkButton(login_field, text="Switch to Sign In", command=self.toggle_first_run)
            button_signin.place(relx=0.5, rely=0.1, anchor=N)
            

        

           

    def font(self,ukuran) :
        return ("Bahnschrift SemiBold SemiConden",ukuran)

        
        
    
        
class StartPage(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")

        label = CTkLabel(self,text="Hello")
        label.place(x=10,y=10)

class Page1(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")

class Page2(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")

class Page3(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")

if __name__ == '__main__' :
    app = tkinterApp()
    app.title('Emergency System')
    app.geometry("1400x788")
    app._set_appearance_mode("Light")
    app.resizable(False,False)
    app.mainloop()
