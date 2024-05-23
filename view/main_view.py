from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from model.database import DatabaseConnection


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
        self.controller = controller
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

    def toggle_first_run(self, event=None):
        self.first_run = not self.first_run
        self.login_page()

    def login_page(self):
        
        box = CTkFrame(self,height=788, width=1400,fg_color="white",bg_color="white")
        box.place(x=0,y=0)

        login_box = CTkFrame(self,height=731,width=1300
                              ,fg_color='#642424',bg_color="white",corner_radius=18)
        login_box.place(relx=0.5, rely=0.5,anchor=CENTER)

        login_field = CTkFrame(login_box,height=731,width=700
                              ,fg_color='grey20',bg_color="transparent",corner_radius=18)
        login_field.place(x=650, y=0)

        logo_directory = os.path.join(self.script_dir, 'assets', 'App_logo.png')
        logo = CTkImage(light_image=Image.open(logo_directory), size=(600,250))
        logo_placeholder = CTkButton(login_box,image=logo,fg_color='transparent',text='',state="diabled" ,border_width=0,border_color="white")
        logo_placeholder.place(x=30 , y=240)

        login_register_box = CTkFrame(login_field,height=550,width=450,fg_color="#e6e7df")
        login_register_box.place(rely=0.5,relx=0.5,anchor=CENTER)

        self.login_register_title = CTkLabel(login_register_box,text="",font=self.font(22),text_color="grey20")
        self.login_register_title.place(x=30,y=25)

        long_line = CTkFrame(login_register_box,width=390,height=5,fg_color='grey20',corner_radius=0)
        long_line.place(x=30,y=60)

        self.login_register_title1 = CTkLabel(login_register_box,text="",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=85)

        
        if self.first_run:
        
            
            self.login_register_title.configure(text="Sign In Responder")
            self.login_register_title1.configure(text="Badge ID")

            '''
            This section is for input to login account
            '''


            self.input_badge_id_signin = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                      text_color="grey20",border_width=0,placeholder_text="")
            self.input_badge_id_signin.place(x=30,y=120)

            self.input_password_id = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                      text_color="grey20",border_width=0,placeholder_text="",show="*")
            self.input_password_id.place(x=30,y=215)


            self.check_box = CTkCheckBox(self.input_password_id,height=15,width=15,text="",text_color="grey20",
                                         font=self.font(12),onvalue=0,offvalue=1,command=self.show_password,checkbox_height=30,
                                         checkbox_width=30)
            self.check_box.place(relx=0.9,rely=0.5,anchor=W)

            '''
            END SECTION
            '''

            self.login_register_title1 = CTkLabel(login_register_box,text="Password",font=self.font(18),text_color="grey20")
            self.login_register_title1.place(x=30,y=180)

            '''
            This section is login button
            '''            
            button_login = CTkButton(login_register_box, text="Login",fg_color='#2B70C9',font=self.font(18),hover_color='grey30', 
                                        command=  self.show_res,height=50,width=400)
            button_login.place(relx=0.5, rely=0.58, anchor=CENTER)

            self.long_line(login_register_box,170,3,30,385)
            self.text(login_register_box,"or",self.font(20),"grey20",215,370)
            self.long_line(login_register_box,170,3,250,385)

            self.button_register = CTkButton(login_register_box, text="Create New Account",fg_color='#642424',font=self.font(18),hover_color='grey30', 
                                            command=self.toggle_first_run,height=50,width=320)
            self.button_register.place(relx=0.5, rely=0.9, anchor=S)

    

        elif self.first_run == False :

            self.login_register_title.configure(text="Register Responder")
            self.login_register_title1.configure(text="Responder Name")

            self.input_responder_name_register = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                      text_color="grey20",border_width=0,placeholder_text="")
            self.input_responder_name_register.place(x=30,y=120)

            self.login_register_title1 = CTkLabel(login_register_box,text="Badge ID",font=self.font(18),text_color="grey20")
            self.login_register_title1.place(x=30,y=180)

            self.input_badge_id_register = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                      text_color="grey20",border_width=0,placeholder_text="")
            self.input_badge_id_register.place(x=30,y=215)

            self.login_register_title1 = CTkLabel(login_register_box,text="Password",font=self.font(18),text_color="grey20")
            self.login_register_title1.place(x=30,y=280)

            self.input_badge_password_register = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                      text_color="grey20",border_width=0,placeholder_text="",show='*')
            self.input_badge_password_register.place(x=30,y=310)

            self.check_box = CTkCheckBox(self.input_badge_password_register,height=15,width=15,text="",text_color="grey20",
                                         font=self.font(12),onvalue=0,offvalue=1,command=self.show_password,checkbox_height=30,
                                         checkbox_width=30)
            self.check_box.place(relx=0.9,rely=0.5,anchor=W)

            self.submit_register = CTkButton(login_register_box,height=50,width=400,fg_color='#42b72a',text_color="white",
                                             font=self.font(18),text='Submit')
            self.submit_register.place(x=30,y=380)

            self.long_line(login_register_box,170,3,30,460)
            self.text(login_register_box,"or",self.font(20),"grey20",215,446)
            self.long_line(login_register_box,170,3,250,460)

            have_account_label = CTkLabel(login_register_box,text="Have account?",font= (self.font_not_bold(16)),
                                          cursor='hand2',text_color='grey10')
            have_account_label.place(relx=0.5 ,rely=0.94, anchor=S)
            have_account_label.bind('<Button-1>',self.toggle_first_run)
            
            
            # login_field_title = CTkLabel(login_field,text="–✦– Register –✦–",font=self.font(48))
            # login_field_title.place(relx=0.5,rely=0.05,anchor=N)
            # button_signin = CTkButton(login_field, text="Switch to Sign In", command=self.toggle_first_run)
            # button_signin.place(relx=0.5, rely=0.1, anchor=N)

    def show_res(self):
        self.database = DatabaseConnection()
        self.database.connect()
        self.database.login_user(username=str(self.input_badge_id_signin.get()),
                                 password=str(self.input_password_id.get()))
        
        if self.database.login_user == True :
            self.controller.show_frame(StartPage)
        else : 
            print('Wrong Password')

            

        
        




        
    def text(self,position,teks,font,color,x,y):
        text = CTkLabel(position,text=teks,font=font,text_color=color)
        text.place(x=x,y=y)

    def long_line(self,position,width,height,x_position,y_position) :
        long_line = CTkFrame(position,width=width,height=height,fg_color='grey20',corner_radius=0)
        long_line.place(x=x_position,y=y_position)

    # def show_password(self):
    #     if self.check_box.get() == 1 :
    #         self.input_password_id.configure(show="*")
    #         self.input_badge_password_register.configure(show="*")
            
    #     elif self.check_box.get() == 0 :
    #         self.input_password_id.configure(show="")
    #         self.input_badge_password_register.configure(show="")

    def show_password(self):
        if hasattr(self, 'input_password_id') and self.input_password_id.winfo_exists():
            if self.check_box.get() == 1:
                self.input_password_id.configure(show="*")
            elif self.check_box.get() == 0:
                self.input_password_id.configure(show="")
        if hasattr(self, 'input_badge_password_register') and self.input_badge_password_register.winfo_exists():
            if self.check_box.get() == 1:
                self.input_badge_password_register.configure(show="*")
            elif self.check_box.get() == 0:
                self.input_badge_password_register.configure(show="")

    def font(self,ukuran) :
        return ("Arial Bold",ukuran)
    
    def font_not_bold(self,ukuran) :
        return ("Arial",ukuran)
    

class StartPage(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.dashboard()
        self.notification_field()
        self.responder_status()
        self.navbar()

    def navbar(self):
        navbar_box = CTkLabel(self,height=80,width=400,bg_color="#642424",corner_radius=8,fg_color='#642424')
        navbar_box.place(x=15,y=15)

    def responder_status(self):
        title = CTkLabel(self.box,height=35,width=300,fg_color='#642424',text='',corner_radius=5)
        title.place(relx=0.982,rely=0.075,anchor=NE)

        title_1 = CTkLabel(title,text='Responder Profiles',text_color='white',font=('Arial Bold',14))
        title_1.place(relx=0.5,rely=0.5,anchor=E)

        responder_profile_box = CTkLabel(self.box,height=160,width=300,fg_color='white',text='',corner_radius=5)
        responder_profile_box.place(relx=0.768,rely=0.23,anchor=W)

        name = CTkLabel(responder_profile_box, text="Name", font=('Arial',14), text_color='grey40')
        name.place(x=150, y = 15)

        self.inputname = CTkLabel(responder_profile_box,text="Umam Madura",font=('Arial Bold',16),
                                  text_color='grey10')
        self.inputname.place(x=150, y = 35)

        name = CTkLabel(responder_profile_box, text="Division", font=('Arial',14), text_color='grey40')
        name.place(x=150, y = 60)

        self.input_divison = CTkLabel(responder_profile_box,text="69 Division",font=('Arial Bold',16),
                             text_color='grey10')
        self.input_divison.place(x = 150, y = 83)

    def dashboard(self) :
        self.box = CTkFrame(self,height=788, width=1400,fg_color="#E5E4E2",bg_color="white")
        self.box.place(x=0,y=0)

        # dashboard_title = CTkLabel(self.box,text='Main Dashboard',text_color="grey20",font=('Arial Bold',22))
        # dashboard_title.place(relx=0.34, rely= 0.04, anchor=NE)

        # dashboard_title_1 = CTkLabel(self.box,text='Available Camera',text_color="grey20",font=('Arial Bold',20))
        # dashboard_title_1.place(relx=0.339, rely= 0.09, anchor=NE)

        self.search = CTkEntry(self.box,height=30,width=200, fg_color="white",font=('Arial',16),
                                      text_color="grey20",border_width=0,placeholder_text="Search",border_color="black")
        self.search.place(relx=0.91,rely=0.02,anchor=NE)

        # sidebar(self)
        # self.camera_available()
        


    def notification_field(self):
        notification_title = CTkLabel(self.box,text='Accident Notification',text_color="grey20",font=('Arial Bold',20))
        notification_title.place(relx=0.91,rely=0.35,anchor=NE)

        AER_box = CTkLabel(self.box,height=250,width=300,fg_color='#642424',text='',corner_radius=5)
        AER_box.place(relx=0.768,rely=0.55,anchor=W)


    

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

# if __name__ == '__main__' :
#     app = tkinterApp()
#     app.title('Emergency System')
#     app.geometry("1400x788")
#     app._set_appearance_mode("Light")
#     app.resizable(False,False)
#     app.mainloop()
