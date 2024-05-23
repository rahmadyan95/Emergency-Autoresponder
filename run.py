import view.main_view as main_view

if __name__ == '__main__' :
    app = main_view.tkinterApp()
    app.title('Emergency System')
    app.geometry("1400x788")
    app._set_appearance_mode("Light")
    app.resizable(False,False)
    app.mainloop()
