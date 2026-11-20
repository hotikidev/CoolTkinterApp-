def A_cool_GUI_APP():
    import tkinter as t
    window_root_GUI_py = t.Tk()
    window_root_GUI_py.title('A cool thing😁')
    window_root_GUI_py.geometry('780x780')
    window_root_GUI_py.configure(bg='#2F3FCC')

    enterable = t.Entry(
    window_root_GUI_py,
    font=('arial',40)
    )
    enterable.pack(pady=50)

    buttons = t.Button(
    window_root_GUI_py,
    text='Car🚘 !😁',
    font=('Algerian',25),
    bg='#B332A4',
    fg="#000000"
    )
    buttons.pack(pady=50)

    buttons2 = t.Button(
    window_root_GUI_py,
    text='Car🚘!😁',
    font=('Algerian',25),
    bg='#B332A4',
    fg="#000000"
    )
    buttons2.pack(pady=50)

    buttons3 = t.Button(
    window_root_GUI_py,
    text='Car🚘!😁',
    font=('Algerian',25),
    bg='#B332A4',
    fg="#000000"
    )
    buttons3.pack(pady=50)

    buttons4 = t.Button(
    window_root_GUI_py,
    text='Car🚘 !😁',
    font=('Algerian',25),
    bg='#B332A4',
    fg="#000000"
    )
    buttons4.pack(pady=50)

    window_root_GUI_py.mainloop()
A_cool_GUI_APP()

#==========================================================CREATED BY (@hotikidev) WITH LOVE========================================