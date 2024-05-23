from customtkinter import *

def login_utility(self,login_register_box,controller):
    self.login_register_title.configure(text="Sign In Responder")
    self.login_register_title1.configure(text="Badge ID")

    self.input_badge_id_signin = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                text_color="grey20",border_width=0,placeholder_text="")
    self.input_badge_id_signin.place(x=30,y=120)

    self.login_register_title1 = CTkLabel(login_register_box,text="Password",font=self.font(18),text_color="grey20")
    self.login_register_title1.place(x=30,y=180)


    self.input_password_id = CTkEntry(login_register_box,height=50,width=400, fg_color="white",font=self.font_not_bold(18),
                                text_color="grey20",border_width=0,placeholder_text="",show="*")
    self.input_password_id.place(x=30,y=215)

    self.check_box = CTkCheckBox(self.input_password_id,height=15,width=15,text="",text_color="grey20",
                                    font=self.font(12),onvalue=0,offvalue=1,command=self.show_password,checkbox_height=30,
                                    checkbox_width=30)
    self.check_box.place(relx=0.9,rely=0.5,anchor=W)

    
    button_login = CTkButton(login_register_box, text="Login",fg_color='#2B70C9',font=self.font(18),hover_color='grey30', 
                                command=  lambda: controller,height=50,width=400)
    button_login.place(relx=0.5, rely=0.58, anchor=CENTER)

    self.long_line(login_register_box,170,3,30,385)
    self.text(login_register_box,"or",self.font(20),"grey20",215,370)
    self.long_line(login_register_box,170,3,250,385)

    self.button_register = CTkButton(login_register_box, text="Create New Account",fg_color='#642424',font=self.font(18),hover_color='grey30', 
                                    command=self.toggle_first_run,height=50,width=320)
    self.button_register.place(relx=0.5, rely=0.9, anchor=S)