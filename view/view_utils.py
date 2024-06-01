from customtkinter import *
from PIL import Image


class view_utilites():
    def __init__(self) -> None:
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        

    # def navbar(self,div):
    #     navbar_box = CTkLabel(div,height=750,width=80,corner_radius=10,fg_color='#642424',text='')
    #     navbar_box.place(x=20,rely=0.02)

    #     logo_directory = os.path.join(self.script_dir, 'assets', 'EAS_logo.png')
    #     logo = CTkImage(light_image=Image.open(logo_directory), size=(35,50))
    #     logo_placeholder = CTkButton(navbar_box,image=logo,fg_color='transparent',text='',corner_radius=5,state='disabled',
    #                                  border_color='white',border_width=3,height=80,width=60,command=lambda : self.controller.show_frame(StartPage))
    #     logo_placeholder.place(x=10 , y=10)

    #     '''
    #     Home logo PlaceHolder
    #     '''

    #     logo_directory = os.path.join(self.script_dir, 'assets', 'home.png')
    #     logo_home = CTkImage(light_image=Image.open(logo_directory), size=(40,40))
    #     logo_placeholder_home = CTkButton(navbar_box,image=logo_home,fg_color='transparent',text='',
    #                                       hover_color='#926565',height=50,width=50)
    #     logo_placeholder_home.place(x=12 , y=130)

    #     logo_directory = os.path.join(self.script_dir, 'assets', 'kamera.png')
    #     logo_camera = CTkImage(light_image=Image.open(logo_directory), size=(40,40))
    #     logo_placeholder_camera = CTkButton(navbar_box,image=logo_camera,fg_color='transparent',text='',
    #                                       hover_color='#926565',height=50,width=50)
    #     logo_placeholder_camera.place(x=12 , y=200)

    #     logo_directory = os.path.join(self.script_dir, 'assets', 'map.png')
    #     logo_map = CTkImage(light_image=Image.open(logo_directory), size=(45,45))
    #     logo_placeholder_map = CTkButton(navbar_box,image=logo_map,fg_color='transparent',text='',
    #                                       hover_color='#926565',height=45,width=45)
    #     logo_placeholder_map.place(x=12 , y=270)

    #     logo_directory = os.path.join(self.script_dir, 'assets', 'logout.png')
    #     logo_logout = CTkImage(light_image=Image.open(logo_directory), size=(40,40))
    #     logo_placeholder_logout = CTkButton(navbar_box,image=logo_logout,fg_color='transparent',text='',
    #                                       hover_color='#926565',height=50,width=50)
    #     logo_placeholder_logout.place(x=12 , y=680)

    #     logo_directory = os.path.join(self.script_dir, 'assets', 'gear.png')
    #     logo_gear = CTkImage(light_image=Image.open(logo_directory), size=(40,40))
    #     logo_placeholder_gear = CTkButton(navbar_box,image=logo_gear,fg_color='transparent',text='',
    #                                       hover_color='#926565',height=50,width=50)
    #     logo_placeholder_gear.place(x=12 , y=610)


        

    #     long_line = CTkFrame(navbar_box,width=65,height=4,fg_color='white',corner_radius=3)
    #     long_line.place(x=6,y=110)

    #     long_line_2 = CTkFrame(navbar_box,width=65,height=4,fg_color='white',corner_radius=3)
    #     long_line_2.place(x=6,y=590)
        