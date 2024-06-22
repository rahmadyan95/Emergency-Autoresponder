from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from model.database import DatabaseConnection
from CTkMessagebox import *
from model.add_camera_db import camera_db
from tkintermapview import TkinterMapView as CTkMap
import cv2
from ultralytics import YOLO
import pandas as pd
from PIL import Image, ImageTk
from view.tracker import*
import datetime
import json

class tkinterApp (ctk.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login_page,StartPage, Page1, Page2, Page3, Page4):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        # self.show_frame(Login_page)
        self.show_frame(Login_page)
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

    def login(self):
        self.login_register_title.configure(text="Sign In Responder")
        self.login_register_title1.configure(text="Badge ID")

        '''
        This section is for input to login account
        '''


        self.input_badge_id_signin = CTkEntry(self.login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                    text_color="grey20",border_width=0,placeholder_text="")
        self.input_badge_id_signin.place(x=30,y=120)

        self.input_password_id = CTkEntry(self.login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                    text_color="grey20",border_width=0,placeholder_text="",show="*")
        self.input_password_id.place(x=30,y=215)


        self.check_box = CTkCheckBox(self.input_password_id,height=15,width=15,text="",text_color="grey20",
                                        font=self.font(12),onvalue=0,offvalue=1,command=self.show_password,checkbox_height=30,
                                        checkbox_width=30)
        self.check_box.place(relx=0.9,rely=0.5,anchor=W)

        '''
        END SECTION
        '''

        self.login_register_title1 = CTkLabel(self.login_register_box,text="Password",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=180)

        '''
        This section is login button
        '''            
        button_login = CTkButton(self.login_register_box, text="Login",fg_color='#2B70C9',font=self.font(18),hover_color='grey30', 
                                    command=  self.show_res,height=50,width=400)
        button_login.place(relx=0.5, rely=0.58, anchor=CENTER)

        self.long_line(self.login_register_box,170,3,30,385)
        self.text(self.login_register_box,"or",self.font(20),"grey20",215,370)
        self.long_line(self.login_register_box,170,3,250,385)

        self.button_register = CTkButton(self.login_register_box, text="Create New Account",fg_color='#642424',font=self.font(18),hover_color='grey30', 
                                        command=self.toggle_first_run,height=50,width=320)
        self.button_register.place(relx=0.5, rely=0.9, anchor=S)

    def register(self):
        self.login_register_title.configure(text="Register Responder")
        self.login_register_title1.configure(text="Responder Name")

        self.login_register_box.configure(height=680)


        '''
        This Field for entry credential of dispactcher
        '''
        self.input_responder_name_register = CTkEntry(self.login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                    text_color="grey20",border_width=0,placeholder_text="")
        self.input_responder_name_register.place(x=30,y=120)

        self.input_badge_id_register = CTkEntry(self.login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                    text_color="grey20",border_width=0,placeholder_text="")
        self.input_badge_id_register.place(x=30,y=215)

        self.input_badge_password_register = CTkEntry(self.login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                    text_color="grey20",border_width=0,placeholder_text="",show='*')
        self.input_badge_password_register.place(x=30,y=380+25)

        self.input_badge_repassword_register = CTkEntry(self.login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                    text_color="grey20",border_width=0,placeholder_text="",show='*')
        self.input_badge_repassword_register.place(x=30,y=380+110)

        self.sctructural_ranks = CTkComboBox(self.login_register_box,height=50,width=400,fg_color="white",font=('Arial',18),text_color="grey20",
                                                dropdown_font=self.font_not_bold(16),
                                                values=['Dispatch Director','Dispatch Deputy Director',
                                                        'Senior Operator','Operator II','Operator I','Dispatch Cadet'],
                                                        button_color='#642424',border_width=2,border_color='grey20')
        self.sctructural_ranks.place(x=30,y=330-20)

        
    
        '''
        End Field
        '''

        self.login_register_title1 = CTkLabel(self.login_register_box,text="Badge ID",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=180)

    
        self.login_register_title1 = CTkLabel(self.login_register_box,text="Password",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=350+20)

        self.login_register_title1 = CTkLabel(self.login_register_box,text="Confirm Password",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=350+110)

        

        self.check_box = CTkCheckBox(self.input_badge_password_register,height=15,width=15,text="",text_color="grey20",
                                        font=self.font(12),onvalue=0,offvalue=1,command=self.show_password,checkbox_height=30,
                                        checkbox_width=30)
        self.check_box.place(relx=0.9,rely=0.5,anchor=W)

        self.check_box2 = CTkCheckBox(self.input_badge_repassword_register,height=15,width=15,text="",text_color="grey20",
                                        font=self.font(12),onvalue=0,offvalue=1,command=self.show_password,checkbox_height=30,
                                        checkbox_width=30)
        self.check_box2.place(relx=0.9,rely=0.5,anchor=W)

        self.submit_register = CTkButton(self.login_register_box,height=50,width=400,fg_color='#42b72a',text_color="white",
                                            font=self.font(18),text='Submit',command=self.show_res)
        self.submit_register.place(x=30,y=560)

        self.login_register_title1 = CTkLabel(self.login_register_box,text="Dispatcher Structural Ranks",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=330-55)

        # self.long_line(self.login_register_box,170,3,30,560)
        # self.text(self.login_register_box,"or",self.font(20),"grey20",215,560)
        # self.long_line(self.login_register_box,170,3,250,560)

        have_account_label = CTkLabel(self.login_register_box,text="Have account?",font= (self.font_not_bold(16)),
                                        cursor='hand2',text_color='grey10')
        have_account_label.place(relx=0.5 ,rely=0.96, anchor=S)
        have_account_label.bind('<Button-1>',self.toggle_first_run)


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

        self.login_register_box = CTkFrame(login_field,height=550,width=450,fg_color="#e6e7df")
        self.login_register_box.place(rely=0.5,relx=0.5,anchor=CENTER)

        self.login_register_title = CTkLabel(self.login_register_box,text="",font=self.font(22),text_color="grey20")
        self.login_register_title.place(x=30,y=25)

        long_line = CTkFrame(self.login_register_box,width=390,height=5,fg_color='grey20',corner_radius=0)
        long_line.place(x=30,y=60)

        self.login_register_title1 = CTkLabel(self.login_register_box,text="",font=self.font(18),text_color="grey20")
        self.login_register_title1.place(x=30,y=85)

        # escape_button = CTkButton(self.login_register_box,height=20,width=50,command=lambda : self.controller.show_frame(StartPage))
        # escape_button.place(x=100,y=400)


        
        if self.first_run:
            self.login()
        

        elif self.first_run == False :
            self.register()

            
            
            
    def show_res(self):
        
    
        if self.first_run:
            self.database = DatabaseConnection()
            self.database.connect()

            login_success = self.database.login_user(username=str(self.input_badge_id_signin.get()),
                                    password=str(self.input_password_id.get()))
            
            if login_success:
                self.controller.show_frame(StartPage)
            else : 
                print('Wrong Password')
                msg_2 = CTkMessagebox(title="Warning",message="Wrong Dispatcher ID Or Password",icon='cancel',
                                      option_1="Return")
                
                if msg_2.get() == 'Return' :
                    return

        elif self.first_run == False:

            self.database = DatabaseConnection()
            self.database.connect()

            if (len(self.input_badge_password_register.get()) >= 12) and (self.input_badge_repassword_register.get() == self.input_badge_password_register.get()):
                self.database.register_user(
                    username=self.input_badge_id_register.get(),
                    password=self.input_badge_password_register.get(),
                    name=self.input_responder_name_register.get(),
                    job_position=self.sctructural_ranks.get()
                )


                if self.database.register_user:
                    msg1 = CTkMessagebox(title='Register',message="Register register success",icon='check',
                                         option_1='OK')
                    
                    if msg1.get() == 'OK' :
                        self.toggle_first_run()
                else : 
                    print('Register Failed')
                    
                    
            
            else:
                print("Not 12 and Not same")
                msg = CTkMessagebox(title="Warning",message="Password not same or Password less than 12 Characters",
                                        icon='cancel',option_1='Return')
                    
                if msg.get() == 'Return':
                    return


    def text(self,position,teks,font,color,x,y):
        text = CTkLabel(position,text=teks,font=font,text_color=color)
        text.place(x=x,y=y)

    def long_line(self,position,width,height,x_position,y_position) :
        long_line = CTkFrame(position,width=width,height=height,fg_color='grey20',corner_radius=0)
        long_line.place(x=x_position,y=y_position)

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

        if hasattr(self, 'input_badge_repassword_register') and self.input_badge_repassword_register.winfo_exists():
            if self.check_box2.get() == 1:
                self.input_badge_repassword_register.configure(show="*")
            elif self.check_box2.get() == 0:
                self.input_badge_repassword_register.configure(show="")


    def font(self,ukuran) :
        return ("Arial Bold",ukuran)
    
    def font_not_bold(self,ukuran) :
        return ("Arial",ukuran)
    
    
        
    

class StartPage(ctk.CTkFrame):

    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.controller = controller

        self.box = CTkFrame(self,height=788, width=1400,fg_color="#E5E4E2",bg_color="white")
        self.box.place(x=0,y=0)

        self.camera_db = camera_db()
        self.warning_status = False

        
        # self.dashboard()
        self.notification_warning()
        self.responder_status()
        create_navbar(self.box, self.script_dir, self.controller)
        self.warning_sign()
        self.accident_notification_details()
        self.camere_status()
        self.map_view()

        self.dispacther_location("Standby Hospital","152",115,285, photo_name='redcross.png')
        self.dispacther_location("Police Station","253",418,285, photo_name='police_logo.jpg')
        self.dispacther_location("Fire Station","129",721,285, photo_name='fireman.jpg')

        self.input_nama_camera('1','CGDK331','-6.34224, 11.4234',True,self.scrollable)
        self.input_nama_camera('2','CGDK332','-6.34224 12.3223',False,self.scrollable)
        
        

    def map_view(self):

        title = CTkLabel(self.box,height=35,width=910,fg_color='#642424',text='',corner_radius=5)
        title.place(x=115,y=445)

        title_1 = CTkLabel(title,text='Map Availability Responder',text_color='white',font=('Arial Bold',14))
        title_1.place(relx=0.38,rely=0.5,anchor=E)


        self.map = CTkMap(self.box,width=1800,height=540,corner_radius=10)
        self.map.place(x=230,y=980)

        self.map.set_position(-6.2079558,106.7968640)
        self.map.set_zoom(15)


    

    def responder_status(self):
        title = CTkLabel(self.box,height=35,width=300,fg_color='#642424',text='',corner_radius=5)
        title.place(relx=0.982,rely=0.075,anchor=NE)

        title_1 = CTkLabel(title,text='Responder Profiles',text_color='white',font=('Arial Bold',14))
        title_1.place(relx=0.5,rely=0.5,anchor=E)

        responder_profile_box = CTkLabel(self.box,height=160,width=300,fg_color='white',text='',corner_radius=5)
        responder_profile_box.place(relx=0.768,rely=0.23,anchor=W)

        name = CTkLabel(responder_profile_box, text="Name", font=('Arial',14), text_color='grey40')
        name.place(x=150, y = 15)

        self.inputname = CTkLabel(responder_profile_box,text="Dispactcher",font=('Arial Bold',16),
                                  text_color='grey10')
        self.inputname.place(x=150, y = 35)

        name = CTkLabel(responder_profile_box, text="Division", font=('Arial',14), text_color='grey40')
        name.place(x=150, y = 60)

        self.input_divison = CTkLabel(responder_profile_box,text="69 Division",font=('Arial Bold',16),
                             text_color='grey10')
        self.input_divison.place(x = 150, y = 83)


        self.search = CTkEntry(self.box,height=30,width=200, fg_color="white",font=('Arial',16),
                                      text_color="grey20",border_width=0,placeholder_text="Search",border_color="black")
        self.search.place(relx=0.91,rely=0.02,anchor=NE)

        logo_directory_home = os.path.join(self.script_dir, 'assets', 'dummy.jpg')
        logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(110,115))
        logo_placeholder_home = CTkButton(responder_profile_box, image=logo_home, fg_color='transparent', text='',
                                        hover_color='#926565', height=110, width=115, state='disabled',border_width=3,border_color='#642424')
        logo_placeholder_home.place(x=15, y=15)

    def notification_warning(self):
        notification_title = CTkLabel(self.box,text='Accident Notification',text_color="grey20",font=('Arial Bold',20))
        notification_title.place(relx=0.91,rely=0.35,anchor=NE)

        self.AER_box = CTkLabel(self.box,height=100,width=300,fg_color='#642424',text='',corner_radius=5)
        self.AER_box.place(relx=0.768,rely=0.46,anchor=W)

        # logo_directory_home = os.path.join(self.script_dir, 'assets', 'Warning.png')
        # self.logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(70,70))
        # logo_placeholder_home = CTkButton(self.AER_box, image=self.logo_home, fg_color='transparent', text='',
        #                                 hover_color='#926565', height=70, width=70, state='disabled',border_width=3,border_color='#642424')
        # logo_placeholder_home.place(x=10, y=5)

        self.status = CTkLabel(self.AER_box,text="",font=('Arial Bold',20),
                                  text_color='white')
        self.status.place(x=95, y = 25)

    def warning_sign(self):
        if self.warning_status == True :
            logo_directory_home = os.path.join(self.script_dir, 'assets', 'warning.png')
            self.logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(70,70))
            logo_placeholder_home = CTkButton(self.AER_box, image=self.logo_home, fg_color='transparent', text='',
                                            hover_color='#926565', height=70, width=70, state='disabled',border_width=3,border_color='#642424')
            logo_placeholder_home.place(x=10, y=5)

            self.status.configure(text="AN ACCIDENT\nOCCURRED !!!")
        
        else :
            logo_directory_home = os.path.join(self.script_dir, 'assets', 'checklist.png')
            self.logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(70,70))
            logo_placeholder_home = CTkButton(self.AER_box, image=self.logo_home, fg_color='transparent', text='',
                                            hover_color='#926565', height=70, width=70, state='disabled',border_width=3,border_color='#642424')
            logo_placeholder_home.place(x=10, y=10)

            self.status = CTkLabel(self.AER_box,text="STANDBY",font=('Arial Bold',20),
                                  text_color='white')
            self.status.place(x=115, y = 35)

            self.accidental_detail = CTkLabel(self.box,height=335,width=300,fg_color='white',text='',corner_radius=5)
            self.accidental_detail.place(relx=0.768,rely=0.745,anchor=W)

            long_line = CTkFrame(self.box, width=6, height=745, fg_color='#642424', corner_radius=4)
            long_line.place(x=1045, y=15)

    def accident_notification_details(self):
        # self.coordinates = CTkLabel(self.accidental_detail,text="Coordinates",font=('Arial Bold',20),text_color='grey10')
        # self.coordinates.place(x=15,y=15)

        # self.address = CTkLabel(self.accidental_detail,text="Address",font=('Arial Bold',20),text_color='grey10')
        # self.address.place(x=15,y=45)

        scrollable = CTkScrollableFrame(self.accidental_detail,width=260,height=290,bg_color='transparent',fg_color='transparent',
                                             orientation='vertical',border_color='#642424',border_width=3)
        scrollable.place(x=10,y=10)

        placeholder = CTkButton(scrollable,height=270,width=250,fg_color='white',text='',border_color='black',border_width=5,state='disabled')
        placeholder.pack(side = LEFT,padx=5,pady=5)

        latlong = CTkLabel(placeholder,text_color='black',font=('Arial bold',16),text='Latitude Longitude')
        latlong.place(x=15,y=10)

        latlong_loc = CTkLabel(placeholder,text_color='grey10',font=('Arial ',15),text='-6.190071,106.797188')
        latlong_loc.place(x=15,y=35)

        day = CTkLabel(placeholder,text_color='black',font=('Arial bold',16),text='Day')
        day.place(x=15,y=60)

        day_val = CTkLabel(placeholder,text_color='grey10',font=('Arial ',15),text='Monday')
        day_val.place(x=15,y=85)

        date = CTkLabel(placeholder,text_color='black',font=('Arial bold',16),text='Date')
        date.place(x=15,y=110)

        date_val = CTkLabel(placeholder,text_color='grey10',font=('Arial ',15),text='26-06-2024')
        date_val.place(x=15,y=135)

        hour = CTkLabel(placeholder,text_color='grey10',font=('Arial bold',16),text='Time')
        hour.place(x=15,y=160)

        hour_val = CTkLabel(placeholder,text_color='grey10',font=('Arial ',15),text='18:25:14')
        hour_val.place(x=15,y=185)




    def camere_status(self):
        title = CTkLabel(self.box,height=35,width=910,fg_color='#642424',text='',corner_radius=5)
        title.place(x=115,y=18)

        title_1 = CTkLabel(title,text='Camera Status',text_color='white',font=('Arial Bold',14))
        title_1.place(relx=0.13,rely=0.5,anchor=E)

        self.scrollable = CTkScrollableFrame(self.box,width=885,height=190,bg_color='transparent',fg_color='transparent',
                                             orientation='horizontal',border_color='#642424',border_width=3)
        self.scrollable.place(x=115,y=60)



        

        '''
        This section is used to make make camera status placeholder
        '''
        # camera_data = self.camera_db.get_all_camera_data()

       
    def dispacther_location(self,title_text,num_value,posisi_x,posisi_y,photo_name):
        # x=115 y=285
        box = CTkLabel(self.box,height=150,width=295)
        box.place(x=posisi_x,y=posisi_y)

        title = CTkLabel(box,height=35,width=295,fg_color='#642424',text='',corner_radius=5)
        title.place(x=0,y=0)

        title_1 = CTkLabel(title,text=f'{title_text}',text_color='white',font=('Arial Bold',14))
        title_1.place(x=20,y=4)

        self.value_box = CTkButton(box,height=100,width=295,bg_color='transparent',fg_color='white',state='disabled',text='',text_color_disabled='black',font=('Arial Bold',20))
        self.value_box.place(x=0,y=40)

        self.value = CTkLabel(self.value_box,text=num_value,text_color='black',font=('Arial Bold',45))
        self.value.place(x=170,y=20)

        path = os.path.join(self.script_dir, 'assets', photo_name)
        logo_home = CTkImage(light_image=Image.open(path), size=(75,75))
        logo_placeholder_home = CTkButton(self.value_box, image=logo_home, fg_color='transparent', text='',
                                        hover_color='#926565', height=90, width=100, state='disabled')
        logo_placeholder_home.place(x=15, y=5)


    # def map_on_dashboard(self):
        

    def input_nama_camera(self,num_cam,idcam,coordinate,status,scrollable):

        placeholder = CTkButton(scrollable,height=240,width=350,fg_color='white',text='',border_color='green',border_width=5,state='disabled')
        placeholder.pack(side = LEFT,padx=10,pady=10) 

        logo_directory_home = os.path.join(self.script_dir, 'assets', 'cctv.png')
        logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(90,100))
        logo_placeholder_home = CTkButton(placeholder, image=logo_home, fg_color='transparent', text='',
                                        hover_color='#926565', height=90, width=100, state='disabled')
        logo_placeholder_home.place(x=15, y=10)

        logo_directory_home = os.path.join(self.script_dir, 'assets', 'cctv.png')
        logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(90,100))
        logo_placeholder_home = CTkButton(placeholder, image=logo_home, fg_color='transparent', text='',
                                        hover_color='#926565', height=90, width=100, state='disabled')
        logo_placeholder_home.place(x=15, y=10)

        long_line = CTkFrame(placeholder, width=3, height=140, fg_color='black', corner_radius=0)
        long_line.place(x=130, y=15)

        long_line = CTkFrame(placeholder, width=180, height=3, fg_color='black', corner_radius=0)
        long_line.place(x=130, y=65)

        long_line = CTkFrame(placeholder, width=180, height=3, fg_color='black', corner_radius=0)
        long_line.place(x=130, y=120)

        long_line = CTkFrame(placeholder, width=3, height=140, fg_color='black', corner_radius=0)
        long_line.place(x=130, y=15)

        long_line = CTkFrame(placeholder, width=180, height=3, fg_color='black', corner_radius=0)
        long_line.place(x=130, y=65)

        long_line = CTkFrame(placeholder, width=180, height=3, fg_color='black', corner_radius=0)
        long_line.place(x=130, y=120)
        
        logo_directory_home = os.path.join(self.script_dir, 'assets', 'cctv.png')
        logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(90,100))
        logo_placeholder_home = CTkButton(placeholder, image=logo_home, fg_color='transparent', text='',
                                        hover_color='#926565', height=90, width=100, state='disabled')
        logo_placeholder_home.place(x=15, y=10)

        self.status = CTkLabel(placeholder,text=f"CCTV {num_cam}",font=('Arial Bold',25),text_color='black',fg_color='transparent',
                               bg_color='transparent')
        self.status.place(x=20, y=115)

        self.id_camera = CTkLabel(placeholder,text=f"Camera ID",font=('Arial Bold',18),text_color='black',fg_color='transparent',
                               bg_color='transparent')
        self.id_camera.place(x=145, y=15)

        self.id_camera_value = CTkLabel(placeholder,text=f"{idcam}",font=('Arial Bold',16),text_color='#642424',fg_color='transparent',
                               bg_color='transparent')
        self.id_camera_value.place(x=145, y=35)

        '''
        Coordinates Placeholder
        '''

        self.coordinat = CTkLabel(placeholder,text=f"Coordinate",font=('Arial Bold',18),text_color='black',fg_color='transparent',
                               bg_color='transparent')
        self.coordinat.place(x=145, y=70)
        
        self.id_camera_value = CTkLabel(placeholder,text=f"{coordinate}",font=('Arial Bold',16),text_color='#642424',fg_color='transparent',
                               bg_color='transparent')
        self.id_camera_value.place(x=145, y=90)

        if status:
            self.status = CTkLabel(placeholder,text=f"STANDBY",font=('Arial Bold',16),text_color='green',fg_color='transparent',
                               bg_color='transparent')
            self.status.place(x=180, y=125)

            placeholder.configure(border_color='green')

            

            
            

        else :
            self.status = CTkLabel(placeholder,text=f"SHUTDOWN",font=('Arial Bold',16),text_color='#642424',fg_color='transparent',
                               bg_color='transparent')
            self.status.place(x=180, y=125)

            placeholder.configure(border_color='#642424')


class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.controller = controller

        self.box = ctk.CTkFrame(self, height=788, width=1400, fg_color="#E5E4E2", bg_color="white")
        self.box.place(x=0, y=0)

        create_navbar(self.box, self.script_dir, self.controller)


        self.setup_ui()
        
        
       

        self.processing = False  # Flag to indicate if processing is active

        # self.start_processing()

        title = CTkLabel(self.box,height=35,width=1000,fg_color='#642424',text='',corner_radius=5)
        title.place(x=130,y=20)

        title_1 = CTkLabel(title,text='CCTV Live Camera',text_color='white',font=('Arial Bold',14))
        title_1.place(relx=0.18,rely=0.5,anchor=E)

        self.videobox_1 = ctk.CTkLabel(self.box, height=563, width=1000,bg_color="transparent",fg_color='white',text='Start Video',corner_radius=10)
        self.videobox_1.place(x=130, y=65)

        
        
        title_2 = CTkLabel(self.box,height=35,width=235,fg_color='#642424',text='',corner_radius=5)
        title_2.place(x=1145,y=20)
        title_3 = CTkLabel(title_2,text='Camera Configuration',text_color='white',font=('Arial Bold',14))
        title_3.place(relx=0.8,rely=0.5,anchor=E)



        self.videobox_str = ctk.CTkLabel(self.box, height=150, width=235,bg_color="transparent",fg_color='white',text='',corner_radius=10)
        self.videobox_str.place(x=1145, y=65)
        
        self.button_start = CTkButton(self.videobox_str,height=50,width=215,command=self.start_processing,fg_color='#C1E1C1'
                                      ,hover_color='#b8d8be',text='START DETECT',font=('Arial Bold',18),text_color='grey10')
        self.button_start.place(x=10,y=10 )

        self.button_stop = CTkButton(self.videobox_str,height=50,width=215,command=self.stop_processing,fg_color='#fdaaaa'
                                      ,hover_color='#ee6969',text='STOP DETECT',font=('Arial Bold',18),text_color='grey10')
        self.button_stop.place(x=10,y=70)

        self.button_stop.configure(state='disabled')

        


        
        
    def setup_ui(self):

        self.videobox = ctk.CTkLabel(self, height=563, width=1000,bg_color="#E5E4E2",fg_color='white',text='Start Video',corner_radius=10)
        self.videobox.place(x=130, y=65)

        self.model = YOLO('C:\\Users\\Rahmadyan\\Documents\\Project\\traffic_accident_detector\\p.pt')

        self.cap = cv2.VideoCapture('C:\\Users\\Rahmadyan\\Documents\\Project\\traffic_accident_detector\\dataset3.mp4')

        with open("C:\\Users\\Rahmadyan\\Documents\\Project\\traffic_accident_detector\\coco.txt", "r") as my_file:
            data = my_file.read()
            self.class_list = data.split("\n")

        self.count = 0
        self.tracker = Tracker()

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 1
        self.font_color = (255, 255, 0)
        self.font_thickness = 2

        self.cy1 = 194
        self.cy2 = 220
        self.offset = 6
        self.coord_y_line1, selfoffset = 700, 40

        self.data, self.counter1 = {}, []
        self.x = datetime.datetime.now()

    def start_processing(self):
        if not self.processing:
            self.processing = True
            
            self.button_start.configure(state='disabled')
            self.button_stop.configure(state='normal')
            self.update_frame()

    def stop_processing(self):
        self.processing = False
        
        self.button_start.configure(state='normal')
        self.button_stop.configure(state='disabled')  # Release the video capture
        self.cap.release()
        self.videobox.destroy()

    def update_frame(self):
        if self.processing:
            ret, frame = self.cap.read()
            if not ret:
                self.stop_processing()
                return

            self.count += 1
            if self.count % 3 == 0:
                frame = cv2.resize(frame, (1020, 500))

                results = self.model.predict(frame)
                a = results[0].boxes.data
                px = pd.DataFrame(a).astype("float")


                list = []
                for index, row in px.iterrows():
                    x1 = int(row[0])
                    y1 = int(row[1])
                    x2 = int(row[2])
                    y2 = int(row[3])
                    d = int(row[5])

                    c = self.class_list[d]
                    if 'accident' in c:
                        print(x1)
                        list.append([x1, y1, x2, y2])

                bbox_id = self.tracker.update(list)
                for bbox in bbox_id:
                    x3, y3, x4, y4, id = bbox
                    cx = int(x3 + x4) // 2
                    cy = int(y3 + y4) // 2
                    cv2.circle(frame, (cx, cy), 4, (255, 0, 255), -1)
                    cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)

                    if y3 <= self.cy1 + self.offset and y4 >= self.cy1 - self.offset:
                        # accident_data = f"Accident detected at Line 1: ID {id} at {datetime.datetime.now()}\n"
                        # self.log_accident(accident_data)

                        if self.counter1.count(id) == 0:
                            self.data[id] = {
                                'latitude' : -6.190071,
                                'longitude' : 106.797188,
                                'day' : f'{self.x.strftime("%A")}',
                                'date' : f'{self.x.day},{self.x.month},{self.x.year}',
                                'time': f'{self.x.strftime("%H:%M:%S")}'
                            }
                            self.counter1.append(id) 
                            self.log_accident(self.data)
                    

                cv2.line(frame, (3, self.cy1), (1018, self.cy1), (0, 255, 0), 2)
                cv2.line(frame, (5, self.cy2), (1019, self.cy2), (0, 255, 255), 2)
                cv2.putText(frame, "Cam2", (20, 30), self.font, self.font_scale, self.font_color, self.font_thickness)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                self.imgtk = ctk.CTkImage(img, size=(930, 530))
                self.videobox.imgtk = self.imgtk
                self.videobox.configure(image=self.imgtk)
                self.videobox.image = self.imgtk

            self.after(10, self.update_frame)

    def log_accident(self, data):
        with open("C:\\Users\\Rahmadyan\\Documents\\Project\\traffic_accident_detector\\accident_log.json", "w") as log_file:
            json.dump(data, log_file, indent=4)



        
        
class Page2(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.controller = controller

        self.box = CTkFrame(self,height=788, width=1400,fg_color="#E5E4E2",bg_color="white")
        self.box.place(x=0,y=0)

        create_navbar(self.box, self.script_dir, self.controller)

        self.mapping()

    def mapping(self):
        title = CTkLabel(self.box,height=35,width=1240,fg_color='#642424',text='',corner_radius=5)
        title.place(x=115,y=20)

        title_1 = CTkLabel(title,text='Overall Map',text_color='white',font=('Arial Bold',14))
        title_1.place(relx=0.18,rely=0.5,anchor=E)

        self.peta = CTkMap(self.box,width=2480,height=1400,corner_radius=10)
        self.peta.place(x=230,y=130)

        self.peta.set_position(-6.2079558,106.7968640)
        self.peta.set_zoom(15)




class Page3(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.controller = controller

        self.box = CTkFrame(self,height=788, width=1400,fg_color="#E5E4E2",bg_color="white")
        self.box.place(x=0,y=0)

        create_navbar(self.box, self.script_dir, self.controller)

class Page4(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self._set_appearance_mode("Light")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.controller = controller

        self.box = CTkFrame(self,height=788, width=1400,fg_color="#E5E4E2",bg_color="white")
        self.box.place(x=0,y=0)

        create_navbar(self.box, self.script_dir, self.controller)

    


def create_navbar(parent, script_dir, controller):
    navbar_box = CTkLabel(parent, height=750, width=80, corner_radius=10, fg_color='#642424', text='')
    navbar_box.place(x=20, rely=0.02)

    logo_directory = os.path.join(script_dir, 'assets', 'EAS_logo.png')
    logo = CTkImage(light_image=Image.open(logo_directory), size=(35,50))
    logo_placeholder = CTkButton(navbar_box, image=logo, fg_color='transparent', text='', corner_radius=5, state='disabled',
                                 border_color='white', border_width=3, height=80, width=60)
    logo_placeholder.place(x=10, y=10)

    '''
    Home logo PlaceHolder
    '''
    logo_directory_home = os.path.join(script_dir, 'assets', 'home.png')
    logo_home = CTkImage(light_image=Image.open(logo_directory_home), size=(40,40))
    logo_placeholder_home = CTkButton(navbar_box, image=logo_home, fg_color='transparent', text='',
                                      hover_color='#926565', height=50, width=50, command=lambda: controller.show_frame(StartPage))
    logo_placeholder_home.place(x=12, y=130)

    logo_directory_cameralogo = os.path.join(script_dir, 'assets', 'kamera.png')
    logo_camera = CTkImage(light_image=Image.open(logo_directory_cameralogo), size=(40,40))
    logo_placeholder_camera = CTkButton(navbar_box, image=logo_camera, fg_color='transparent', text='',
                                        hover_color='#926565', height=50, width=50, command=lambda: controller.show_frame(Page1))
    logo_placeholder_camera.place(x=12, y=200)

    logo_directory_map = os.path.join(script_dir, 'assets', 'map.png')
    logo_map = CTkImage(light_image=Image.open(logo_directory_map), size=(45,45))
    logo_placeholder_map = CTkButton(navbar_box, image=logo_map, fg_color='transparent', text='',
                                     hover_color='#926565', height=45, width=45, command=lambda: controller.show_frame(Page2))
    logo_placeholder_map.place(x=12, y=270)

    logo_directory_logoticon = os.path.join(script_dir, 'assets', 'logout.png')
    logo_logout = CTkImage(light_image=Image.open(logo_directory_logoticon), size=(40,40))
    logo_placeholder_logout = CTkButton(navbar_box, image=logo_logout, fg_color='transparent', text='',
                                        hover_color='#926565', height=50, width=50, command=lambda: controller.show_frame(Login_page))
    logo_placeholder_logout.place(x=12, y=680)

    logo_directory_gear = os.path.join(script_dir, 'assets', 'gear.png')
    logo_gear = CTkImage(light_image=Image.open(logo_directory_gear), size=(40,40))
    logo_placeholder_gear = CTkButton(navbar_box, image=logo_gear, fg_color='transparent', text='',
                                      hover_color='#926565', height=50, width=50, command=lambda: controller.show_frame(StartPage))
    logo_placeholder_gear.place(x=12, y=610)

    long_line = CTkFrame(navbar_box, width=65, height=4, fg_color='white', corner_radius=3)
    long_line.place(x=6, y=110)

    long_line_2 = CTkFrame(navbar_box, width=65, height=4, fg_color='white', corner_radius=3)
    long_line_2.place(x=6, y=590)

    



# if __name__ == '__main__' :
#     app = tkinterApp()
#     app.title('Emergency System')
#     app.geometry("1400x788")
#     app._set_appearance_mode("Light")
#     app.resizable(False,False)
#     app.mainloop()
