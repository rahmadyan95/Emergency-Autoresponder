from customtkinter import *
import customtkinter as ctk
import tkinter as tk
from model.CTkSlideView import CTkSlideView 

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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        '''
        Bagian ini digunakan untuk memberikan nama pada latar belakang dari
        login dan register box
        
        '''
        
        box = CTkFrame(self,height=788, width=1400,fg_color="white",bg_color="white")
        box.place(x=0,y=0)

        login_box = CTkFrame(self,height=660,width=1244
                              ,fg_color='grey50',bg_color="white",border_width=8,border_color='grey40')
        login_box.place(relx=0.5, rely=0.5,anchor=CENTER)

        login_field = CTkFrame(login_box,height=630,width=450
                              ,fg_color='grey20',bg_color="grey50",
                              border_width=8,border_color="white")
        login_field.place(x=779, y=15)

        login_field_title = CTkLabel(login_field,text="–✦– 𝙎𝙄𝙂𝙉 𝙐𝙋 –✦–",font=self.font(48))
        login_field_title.place(relx=0.5,rely=0.05,anchor=N)

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
