import matplotlib, numpy, sys
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure




try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1(root)
    unknown_support.init(root, top)
    root.mainloop()
    #root.geometry('600x850')

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1(w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        self.loopCount = 0
        self.rowCount = 0
        self.rowCountH = 0
        self.i = 0
        self.j = 0
        self.idleCount = 0
        self.update = 0
        self.conditionIdleLoop = True
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        white = '#ffffff'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background= [('selected', white), ('active',_ana2color)])

        top.geometry("850x850")
        top.title("CAOS Project")
        top.configure(background="#d9d9d9")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[('selected', white), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.03, rely=0.04, relheight=0.83, relwidth=0.94)
        self.TNotebook1.configure(width=564)
        self.TNotebook1.configure(takefocus="")

        self.TNotebook1_t1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="FCFS Scheduling",underline="-1",)
        self.TNotebook1_t2 =ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Non-Preemptive Scheduling", underline="-1", )
        self.TNotebook1_t3 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text="Main Memory Management",underline="-1",)

        self.Image1 = PhotoImage(file="bg2.png")

        self.Image1Label = Label(self.TNotebook1_t1, image=self.Image1)
        self.Image1Label.pack()

        self.Algorithm = Label(self.TNotebook1_t1)
        self.Algorithm.place(relx=0.02, rely=0.03, height=30, width=755)
        self.Algorithm.configure(background="#98D085")
        self.Algorithm.configure(disabledforeground="#a3a3a3")
        self.Algorithm.configure(foreground="#042038")
        self.Algorithm.configure(font= ("Helvetica", 14))
        self.Algorithm.configure(text='''First-Come, First Serve Scheduling''')

        self.Frame1 = ttk.Frame(self.TNotebook1_t1)
        self.Frame1.place(relx=0.02, rely=0.10, relheight=0.41, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=535)

        ####################### Shereif's code ######################

        self.Frame3 = Frame(self.Frame1)
        self.Frame3.place(relx=0.0, rely=0.0, relheight=0.73, relwidth=1.0)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        # self.Frame3.configure(background="#8FC97F")
        self.Frame3.configure(width=525)

        self.Canvas1 = Canvas(self.Frame3)
        # self.Canvas1.configure(background="#8FC97F")
        self.Canvas1.pack(side=LEFT, fill=BOTH, expand=True)

        self.Frame4 = Canvas(self.Canvas1)
        self.Frame4.pack(side=LEFT, fill=BOTH, expand=True)

        self.vbar = Scrollbar(self.Canvas1, orient=VERTICAL)
        self.vbar.config(command=self.Canvas1.yview)
        self.Canvas1.config(yscrollcommand=self.vbar.set)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.Canvas1.pack(side="left", fill="both", expand=True)
        self.Canvas1.create_window((4, 4), window=self.Frame4, anchor="nw", tags="self.frame")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.01, rely=0.76, height=50, width=150)
        self.Button1.configure(font= ("Helvetica", 12))
        self.Button1.configure(background="#609B76")
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Populate Chart''')
        self.Button1.configure(command=unknown_support.printConsole1)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.79, rely=0.76, height=50, width=150)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#609B76")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(font= ("Helvetica", 12))
        self.Button2.configure(text='''New Row''')
        self.Button2.configure(command=unknown_support.createRow)

        self.label4 = Label(self.Frame4, text="Processer", width=34, borderwidth=2, relief="sunken", height=2)
        self.label4.grid(row=0, column=0)

        self.label5 = Label(self.Frame4, text="Arrival Time", width=34, borderwidth=2, relief="sunken", height=2)
        self.label5.grid(row=0, column=1)

        self.label3 = Label(self.Frame4, text="Burst Time", width=33, borderwidth=2, relief="sunken", height=2)
        self.label3.grid(row=0, column=2)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.58, rely=0.76, height=50, width=150)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#609B76")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Delete Row''')
        self.Button3.configure(font= ("Helvetica", 12))
        self.Button3.configure(command=unknown_support.deleteRow)

        self.Frame2 = Frame(self.TNotebook1_t1)
        self.Frame2.place(relx=0.02, rely=0.55, relheight=0.21, relwidth=0.96)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=535)

        self.Canvas2 = Canvas(self.Frame2)
        self.Canvas2.pack(side=LEFT, fill=BOTH, expand=True)

        self.Frame5 = Canvas(self.Canvas2)
        # self.Frame5.configure(background="#8FC97F")
        self.Frame5.pack(side=LEFT, fill=BOTH, expand=True)

        self.f = Figure(figsize=(5, 4), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.f, master=self.Frame5)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.Frame5)
        # self.Canvas1.configure(scrollregion=self.Canvas1.bbox("all"))

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.23,rely=0.76, height=50, width=200)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#e1031e")
        self.Label6.configure(text='''''')
        self.Label6.configure(width=274)

        self.Frame9 = Frame(self.TNotebook1_t1)
        self.Frame9.place(relx=0.02, rely=0.78, relheight=0.16, relwidth=0.96)
        self.Frame9.configure(relief=GROOVE)
        self.Frame9.configure(borderwidth="2")
        self.Frame9.configure(relief=GROOVE)
        self.Frame9.configure(background="#d9d9d9")
        self.Frame9.configure(width=535)

        # self.ImageFrame9 = PhotoImage(file="bg2.png")
        #
        # self.Image1Label = Label(self.Frame9, image=self.ImageFrame9)
        # self.Image1Label.pack()

        self.Label9 = Label(self.Frame9)
        self.Label9.place(relx=0.01, rely=0.13, height=21, width=235)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(font= ("Helvetica", 12))
        self.Label9.configure(text=''' Average Waiting Time         =''')

        self.Label8 = Label(self.Frame9)
        self.Label8.place(relx=0.01, rely=0.53, height=21, width=235)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(font= ("Helvetica", 12))
        self.Label8.configure(text='''Average Turnaround Time   =''')

        self.aveWaitTime = Label(self.Frame9)
        self.aveWaitTime.place(relx=0.3, rely=0.13, height=21, width=29)
        self.aveWaitTime.configure(background="#d9d9d9")
        self.aveWaitTime.configure(disabledforeground="#a3a3a3")
        self.aveWaitTime.configure(foreground="#e1031e")
        self.aveWaitTime.configure(font= ("Helvetica", 12))
        self.aveWaitTime.configure(text='''''')

        self.aveTurnTime = Label(self.Frame9)
        self.aveTurnTime.place(relx=0.3, rely=0.53, height=21, width=29)
        self.aveTurnTime.configure(background="#d9d9d9")
        self.aveTurnTime.configure(disabledforeground="#a3a3a3")
        self.aveTurnTime.configure(font= ("Helvetica", 12))
        self.aveTurnTime.configure(foreground="#e1031e")
        self.aveTurnTime.configure(text='''''')

        # self.Canvas1.configure(scrollregion=self.Canvas1.bbox("all"))

        ######################################################




        ############### Nazrul's #####################


        self.Image1N = PhotoImage(file="bg2.png")

        self.Image1LabelN = Label(self.TNotebook1_t3, image=self.Image1N)
        self.Image1LabelN.pack()

        self.Frame1NN = ttk.Frame(self.TNotebook1_t3)
        self.Frame1NN.place(relx=0.02, rely=0.04, relheight=0.76, relwidth=0.3)
        self.Frame1NN.configure(relief=GROOVE)
        self.Frame1NN.configure(borderwidth="2")
        self.Frame1NN.configure(relief=GROOVE)
        self.Frame1NN.configure(width=535)


        self.Frame3NN = ttk.Frame(self.TNotebook1_t3)
        self.Frame3NN.place(relx=0.67, rely=0.04, relheight=0.76, relwidth=0.3)
        self.Frame3NN.configure(relief=GROOVE)
        self.Frame3NN.configure(borderwidth="2")
        self.Frame3NN.configure(relief=GROOVE)
        self.Frame3NN.configure(width=535)

        self.Frame4NN = ttk.Frame(self.TNotebook1_t3)
        self.Frame4NN.place(relx=0.02, rely=0.85, relheight=0.1, relwidth=0.95)
        self.Frame4NN.configure(relief=GROOVE)
        self.Frame4NN.configure(borderwidth="2")
        self.Frame4NN.configure(relief=GROOVE)
        self.Frame4NN.configure(width=535)



        self.ButtonN1 = Button(self.Frame1NN)
        self.ButtonN1.place(relx=0.7, rely=0.01, height=33, width=60)
        self.ButtonN1.configure(activebackground="#d9d9d9")
        self.ButtonN1.configure(activeforeground="#000000")
        self.ButtonN1.configure(background="#609B76")
        self.ButtonN1.configure(disabledforeground="#a3a3a3")
        self.ButtonN1.configure(foreground="#000000")
        self.ButtonN1.configure(highlightbackground="#d9d9d9")
        self.ButtonN1.configure(highlightcolor="black")
        self.ButtonN1.configure(pady="0")
        self.ButtonN1.configure(text='''Add''')
        self.ButtonN1.configure(command=unknown_support.printval)
        self.ButtonN1.configure(width=60)

        self.LabelN1 = Label(self.Frame1NN)
        self.LabelN1.place(relx=0.02, rely=0.15, height=26, width=130)
        self.LabelN1.configure(activebackground="#f9f9f9")
        self.LabelN1.configure(activeforeground="black")
        self.LabelN1.configure(background="#d9d9d9")
        self.LabelN1.configure(disabledforeground="#a3a3a3")
        self.LabelN1.configure(foreground="#000000")
        self.LabelN1.configure(highlightbackground="#d9d9d9")
        self.LabelN1.configure(highlightcolor="black")
        self.LabelN1.configure(text='''Add Memory Block''')

        self.EntryN1 = Entry(self.Frame1NN)
        self.EntryN1.place(relx=0.01, rely=0.01, height=26, width=130)
        self.EntryN1.configure(background="white")
        self.EntryN1.configure(disabledforeground="#a3a3a3")
        self.EntryN1.configure(font="TkFixedFont")
        self.EntryN1.configure(foreground="#000000")
        self.EntryN1.configure(highlightbackground="#d9d9d9")
        self.EntryN1.configure(highlightcolor="black")
        self.EntryN1.configure(insertbackground="black")
        self.EntryN1.configure(selectbackground="#c4c4c4")
        self.EntryN1.configure(selectforeground="black")

        self.FrameN1 = Frame(self.Frame1NN)
        self.FrameN1.place(relx=0.05, rely=0.2, relheight=0.75, relwidth=0.9)
        self.FrameN1.configure(relief=GROOVE)
        self.FrameN1.configure(borderwidth="2")
        self.FrameN1.configure(relief=GROOVE)
        self.FrameN1.configure(background="#d9d9d9")
        self.FrameN1.configure(width=185)

        self.CanvasN1 = Canvas(self.FrameN1, width=190, height=300)
        self.CanvasN1.pack(fill=BOTH, expand=True)

        self.vbarN = Scrollbar(self.CanvasN1, orient=VERTICAL)
        self.vbarN.pack(side=RIGHT, fill=Y)
        self.vbarN.config(command=self.CanvasN1.yview)
        self.CanvasN1.config(yscrollcommand=self.vbarN.set)
        self.CanvasN1.config(scrollregion=(0, 0, 1000, 1000), yscrollcommand=self.vbarN.set)

        self.ButtonN2 = Button(self.Frame4NN)
        self.ButtonN2.place(relx=0.02, rely=0.1, height=40, width=200)
        self.ButtonN2.configure(font= ("Helvetica", 12))
        self.ButtonN2.configure(activebackground="#d9d9d9")
        self.ButtonN2.configure(activeforeground="#000000")
        self.ButtonN2.configure(background="#609B76")
        self.ButtonN2.configure(disabledforeground="#a3a3a3")
        self.ButtonN2.configure(foreground="#000000")
        self.ButtonN2.configure(highlightbackground="#d9d9d9")
        self.ButtonN2.configure(highlightcolor="black")
        self.ButtonN2.configure(pady="0")
        self.ButtonN2.configure(text='''Clear Blocks''')
        self.ButtonN2.configure(command=unknown_support.clearAll)


        self.Frame2NN = ttk.Frame(self.TNotebook1_t3)
        self.Frame2NN.place(relx=0.35, rely=0.04, relheight=0.76, relwidth=0.3)
        self.Frame2NN.configure(relief=GROOVE)
        self.Frame2NN.configure(borderwidth="2")
        self.Frame2NN.configure(relief=GROOVE)
        self.Frame2NN.configure(width=535)
    #
        self.FrameN2 = Frame(self.Frame2NN)
        self.FrameN2.place(relx=0.05, rely=0.02, relheight=0.3, relwidth=0.9)
        self.FrameN2.configure(relief=GROOVE)
        self.FrameN2.configure(borderwidth="2")
        self.FrameN2.configure(relief=GROOVE)
        self.FrameN2.configure(background="#d9d9d9")
        self.FrameN2.configure(width=185)

        self.EntryN2 = Entry(self.FrameN2)
        self.EntryN2.place(relx=0.05, rely=0.28, relheight=0.17, relwidth=0.69)
        self.EntryN2.configure(background="white")
        self.EntryN2.configure(disabledforeground="#a3a3a3")
        self.EntryN2.configure(font=10)
        self.EntryN2.configure(foreground="#000000")
        self.EntryN2.configure(insertbackground="black")
        self.EntryN2.configure(width=134)

        self.EntryN3 = Entry(self.FrameN2)
        self.EntryN3.place(relx=0.05, rely=0.69, relheight=0.17, relwidth=0.69)
        self.EntryN3.configure(background="white")
        self.EntryN3.configure(disabledforeground="#a3a3a3")
        self.EntryN3.configure(font=10)
        self.EntryN3.configure(foreground="#000000")
        self.EntryN3.configure(insertbackground="black")
        self.EntryN3.configure(width=134)

        self.LabelN2 = Label(self.FrameN2)
        self.LabelN2.place(relx=0.01, rely=0.07, height=26, width=70)
        self.LabelN2.configure(background="#d9d9d9")
        self.LabelN2.configure(disabledforeground="#a3a3a3")
        self.LabelN2.configure(foreground="#000000")
        self.LabelN2.configure(text='''Sequence''')

        self.LabelN3 = Label(self.FrameN2)
        self.LabelN3.place(relx=0.03, rely=0.48, height=26, width=70)
        self.LabelN3.configure(background="#d9d9d9")
        self.LabelN3.configure(disabledforeground="#a3a3a3")
        self.LabelN3.configure(foreground="#000000")
        self.LabelN3.configure(text='''Process Size''')

        self.ButtonN3 = Button(self.FrameN2)
        self.ButtonN3.place(relx=0.77, rely=0.66, height=29, width=35)
        self.ButtonN3.configure(activebackground="#d9d9d9")
        self.ButtonN3.configure(activeforeground="#000000")
        self.ButtonN3.configure(background="#609B76")
        self.ButtonN3.configure(disabledforeground="#a3a3a3")
        self.ButtonN3.configure(foreground="#000000")
        self.ButtonN3.configure(highlightbackground="#d9d9d9")
        self.ButtonN3.configure(highlightcolor="black")
        self.ButtonN3.configure(pady="0")
        self.ButtonN3.configure(command=unknown_support.addProcess)
        self.ButtonN3.configure(text='''Add''')

        self.FrameN3 = Frame(self.Frame2NN)
        self.FrameN3.place(relx=0.05, rely=0.4, relheight=0.5, relwidth=0.9)
        self.FrameN3.configure(relief=GROOVE)
        self.FrameN3.configure(borderwidth="2")
        self.FrameN3.configure(relief=GROOVE)
        self.FrameN3.configure(background="#d9d9d9")
        self.FrameN3.configure(width=140)

        self.FrameN4 = Frame(self.FrameN3)
        self.FrameN4.place(relx=0.0, rely=0.0, relheight=0.9, relwidth=0.5)
        self.FrameN4.configure(relief=GROOVE)
        self.FrameN4.configure(borderwidth="2")
        self.FrameN4.configure(relief=GROOVE)
        self.FrameN4.configure(background="#d9d9d9")
        self.FrameN4.configure(width=55)

        self.ListboxN1 = Listbox(self.FrameN4)
        self.ListboxN1.place(relx=0.0, rely=0.0, relheight=0.9, relwidth=1.0)
        self.ListboxN1.pack(side=LEFT, fill=BOTH, expand=True)
        self.ListboxN1.configure(background="white")
        self.ListboxN1.configure(disabledforeground="#a3a3a3")
        self.ListboxN1.configure(font=10)
        self.ListboxN1.configure(foreground="#000000")
        self.ListboxN1.configure(width=50)
        self.ListboxN1.grid(row=0, column=0)

        self.FrameN5 = Frame(self.FrameN3)
        self.FrameN5.place(relx=0.50, rely=0.0, relheight=1.0, relwidth=0.5)

        self.FrameN5.configure(relief=GROOVE)
        self.FrameN5.configure(borderwidth="2")
        self.FrameN5.configure(relief=GROOVE)
        self.FrameN5.configure(background="#d9d9d9")
        self.FrameN5.configure(width=55)

        self.ListboxN2 = Listbox(self.FrameN5)
        self.ListboxN2.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.ListboxN2.pack(side=LEFT, fill=BOTH, expand=True)
        self.ListboxN2.configure(background="white")
        self.ListboxN2.configure(disabledforeground="#a3a3a3")
        self.ListboxN2.configure(font=10)
        self.ListboxN2.configure(foreground="#000000")
        self.ListboxN2.configure(width=55)
        self.ListboxN2.grid(row=0, column=0)

        self.LabelN4 = Label(self.Frame2NN)
        self.LabelN4.place(relx=0.05, rely=0.33, height=26, width=79)
        self.LabelN4.configure(background="#d9d9d9")
        self.LabelN4.configure(disabledforeground="#a3a3a3")
        self.LabelN4.configure(foreground="#000000")
        self.LabelN4.configure(text='''Process No''')

        self.LabelN5 = Label(self.Frame2NN)
        self.LabelN5.place(relx=0.55, rely=0.33, height=26, width=33)
        self.LabelN5.configure(background="#d9d9d9")
        self.LabelN5.configure(disabledforeground="#a3a3a3")
        self.LabelN5.configure(foreground="#000000")
        self.LabelN5.configure(text='''Size''')

        self.ButtonN4 = Button(self.Frame4NN)
        self.ButtonN4.place(relx=0.37, rely=0.1, height=40, width=200)
        self.ButtonN4.configure(font= ("Helvetica", 12))
        self.ButtonN4.configure(activebackground="#d9d9d9")
        self.ButtonN4.configure(activeforeground="#000000")
        self.ButtonN4.configure(background="#609B76")
        self.ButtonN4.configure(disabledforeground="#a3a3a3")
        self.ButtonN4.configure(foreground="#000000")
        self.ButtonN4.configure(highlightbackground="#d9d9d9")
        self.ButtonN4.configure(highlightcolor="black")
        self.ButtonN4.configure(pady="0")
        self.ButtonN4.configure(text='''Clear Process''')
        self.ButtonN4.configure(command=unknown_support.clearProcess)

        self.FrameN6 = Frame(self.Frame3NN)
        self.FrameN6.place(relx=0.05, rely=0.05, relheight=0.7, relwidth=0.9)
        self.FrameN6.configure(relief=GROOVE)
        self.FrameN6.configure(borderwidth="2")
        self.FrameN6.configure(relief=GROOVE)
        self.FrameN6.configure(background="#d9d9d9")
        self.FrameN6.configure(highlightbackground="#d9d9d9")
        self.FrameN6.configure(highlightcolor="black")
        self.FrameN6.configure(width=275)

        self.CanvasN2 = Canvas(self.FrameN6)
        self.CanvasN2.place(relx=-0.275, rely=0.0, relheight=1.01, relwidth=1.49)
        self.CanvasN2.pack(side=LEFT, fill=BOTH, expand=True)

        self.vbarN3 = Scrollbar(self.CanvasN2, orient=VERTICAL)
        self.vbarN3.pack(side=RIGHT, fill=Y)
        self.vbarN3.config(command=self.CanvasN2.yview)
        self.CanvasN2.config(yscrollcommand=self.vbarN3.set)
        self.CanvasN2.config(scrollregion=(0, 0, 1000, 1000), yscrollcommand=self.vbarN3.set)

        self.ButtonN5 = Button(self.Frame2NN)
        self.ButtonN5.place(relx=0.15, rely=0.92, height=33, width=172)
        self.ButtonN5.configure(activebackground="#d9d9d9")
        self.ButtonN5.configure(activeforeground="#000000")
        self.ButtonN5.configure(background="#609B76")
        self.ButtonN5.configure(disabledforeground="#a3a3a3")
        self.ButtonN5.configure(foreground="#000000")
        self.ButtonN5.configure(highlightbackground="#d9d9d9")
        self.ButtonN5.configure(highlightcolor="black")
        self.ButtonN5.configure(pady="0")
        self.ButtonN5.configure(text='''Best-Fit''')
        self.ButtonN5.configure(command=unknown_support.BestFit)

        self.LabelN7 = Label(self.Frame3NN)
        self.LabelN7.place(relx=0.05, rely=0.85, height=36, width=157)
        self.LabelN7.configure(activebackground="#f9f9f9")
        self.LabelN7.configure(activeforeground="black")
        self.LabelN7.configure(background="#d9d9d9")
        self.LabelN7.configure(disabledforeground="#a3a3a3")
        self.LabelN7.configure(foreground="#000000")
        self.LabelN7.configure(highlightbackground="#d9d9d9")
        self.LabelN7.configure(highlightcolor="black")
        self.LabelN7.configure(text='''Internal Fragmentation:''')
        self.LabelN7.configure(width=167)

        self.cpdN39 = Label(self.Frame3NN)
        self.cpdN39.place(relx=0.05, rely=0.78, height=36, width=162)
        self.cpdN39.configure(activebackground="#f9f9f9")
        self.cpdN39.configure(activeforeground="black")
        self.cpdN39.configure(background="#d9d9d9")
        self.cpdN39.configure(disabledforeground="#a3a3a3")
        self.cpdN39.configure(foreground="#000000")
        self.cpdN39.configure(highlightbackground="#d9d9d9")
        self.cpdN39.configure(highlightcolor="black")
        self.cpdN39.configure(text='''External Fragmentation:''')

        self.LabelN8 = Label(self.Frame3NN)
        self.LabelN8.place(relx=0.76, rely=0.78, height=36, width=30)
        self.LabelN8.configure(background="#d9d9d9")
        self.LabelN8.configure(disabledforeground="#a3a3a3")
        self.LabelN8.configure(foreground="#000000")
        self.LabelN8.configure(text="0")

        self.LabelN9 = Label(self.Frame3NN)
        self.LabelN9.place(relx=0.76, rely=0.85, height=36, width=30)
        self.LabelN9.configure(background="#d9d9d9")
        self.LabelN9.configure(disabledforeground="#a3a3a3")
        self.LabelN9.configure(foreground="#000000")
        self.LabelN9.configure(text="0")

        self.butN42 = Button(self.Frame4NN)
        self.butN42.place(relx=0.71, rely=0.1, height=40, width=200)
        self.butN42.configure(font= ("Helvetica", 12))
        self.butN42.configure(activebackground="#d9d9d9")
        self.butN42.configure(activeforeground="#000000")
        self.butN42.configure(background="#609B76")
        self.butN42.configure(disabledforeground="#a3a3a3")
        self.butN42.configure(foreground="#000000")
        self.butN42.configure(highlightbackground="#d9d9d9")
        self.butN42.configure(highlightcolor="black")
        self.butN42.configure(pady="0")
        self.butN42.configure(text='''Clear Diagram''')
        self.butN42.configure(command=unknown_support.clearDiagram)


        ####################################################



        ################ Haikal's ##############################




        self.Image1H = PhotoImage(file="bg2.png")

        self.Image1LabelH = Label(self.TNotebook1_t2, image=self.Image1H)
        self.Image1LabelH.pack()

        self.AlgorithmH = Label(self.TNotebook1_t2)
        self.AlgorithmH.place(relx=0.02, rely=0.03, height=30, width=755)
        self.AlgorithmH.configure(background="#98D085")
        self.AlgorithmH.configure(disabledforeground="#a3a3a3")
        self.AlgorithmH.configure(foreground="#042038")
        self.AlgorithmH.configure(font= ("Helvetica", 14))
        self.AlgorithmH.configure(text='''Non-Preemptive SJF Scheduling''')

        self.Frame1H = Frame(self.TNotebook1_t2)
        self.Frame1H.place(relx=0.02, rely=0.10, relheight=0.43, relwidth=0.96)
        self.Frame1H.configure(relief=GROOVE)
        self.Frame1H.configure(borderwidth="2")
        self.Frame1H.configure(relief=GROOVE)
        self.Frame1H.configure(background="#d9d9d9")
        self.Frame1H.configure(width=535)

        self.Frame3H = Frame(self.Frame1H)
        self.Frame3H.place(relx=0.0, rely=0.0, relheight=0.73, relwidth=1.0)
        self.Frame3H.configure(relief=GROOVE)
        self.Frame3H.configure(borderwidth="2")
        self.Frame3H.configure(relief=GROOVE)
        self.Frame3H.configure(background="#d9d9d9")
        self.Frame3H.configure(width=425)

        self.Canvas1H = Canvas(self.Frame3H, width=300, height=300)
        self.Canvas1H.pack(side=LEFT, fill=BOTH, expand=True)

        self.Frame4H = Canvas(self.Canvas1H, width=300, height=300)
        self.Frame4H.pack(side=LEFT, fill=BOTH, expand=True)

        self.vbarH = Scrollbar(self.Canvas1H, orient=VERTICAL)
        self.vbarH.config(command=self.Canvas1H.yview)
        self.Canvas1H.config(yscrollcommand=self.vbarH.set)
        self.vbarH.pack(side=RIGHT, fill=Y)
        self.Canvas1H.pack(side="left", fill="both", expand=True)
        self.Canvas1H.create_window((4, 4), window=self.Frame4H, anchor="nw", tags="self.frame")

        # self.Canvas1.configure(scrollregion=self.Canvas1.bbox("all"))

        self.Button1H = Button(self.Frame1H)
        self.Button1H.place(relx=0.01, rely=0.76, height=50, width=150)
        self.Button1H.configure(font= ("Helvetica", 12))
        self.Button1H.configure(background="#609B76")
        # self.Button1H.place(relx=0.09, rely=0.81, height=24, width=33)
        self.Button1H.configure(activebackground="#d9d9d9")
        self.Button1H.configure(activeforeground="#000000")
        # self.Button1H.configure(background="#d9d9d9")
        self.Button1H.configure(disabledforeground="#a3a3a3")
        self.Button1H.configure(foreground="#000000")
        self.Button1H.configure(highlightbackground="#d9d9d9")
        self.Button1H.configure(highlightcolor="black")
        self.Button1H.configure(pady="0")
        self.Button1H.configure(text='''Populate Chart''')
        self.Button1H.configure(command=unknown_support.printConsole1H)

        self.Button2H = Button(self.Frame1H)
        self.Button2H.place(relx=0.79, rely=0.76, height=50, width=150)
        self.Button2H.configure(font= ("Helvetica", 12))
        self.Button2H.configure(background="#609B76")
        self.Button2H.configure(activebackground="#d9d9d9")
        self.Button2H.configure(activeforeground="#000000")
        # self.Button2H.configure(background="#d9d9d9")
        self.Button2H.configure(disabledforeground="#a3a3a3")
        self.Button2H.configure(foreground="#000000")
        self.Button2H.configure(highlightbackground="#d9d9d9")
        self.Button2H.configure(highlightcolor="black")
        self.Button2H.configure(pady="0")
        self.Button2H.configure(text='''New Row''')
        self.Button2H.configure(command=unknown_support.createRowH)

        self.label4H = Label(self.Frame4H, text="Processer", width=34, borderwidth=2, relief="sunken", height=2)
        self.label4H.grid(row=0, column=0)

        self.label5H = Label(self.Frame4H, text="Arrival Time", width=34, borderwidth=2, relief="sunken", height=2)
        self.label5H.grid(row=0, column=1)

        self.label3H = Label(self.Frame4H, text="Burst Time", width=34, borderwidth=2, relief="sunken", height=2)
        self.label3H.grid(row=0, column=2)

        self.Button3H = Button(self.Frame1H)
        self.Button3H.place(relx=0.58, rely=0.76, height=50, width=150)
        self.Button3H.configure(activebackground="#d9d9d9")
        self.Button3H.configure(activeforeground="#000000")
        # self.Button3H.configure(background="#d9d9d9")
        self.Button3H.configure(font= ("Helvetica", 12))
        self.Button3H.configure(background="#609B76")
        self.Button3H.configure(disabledforeground="#a3a3a3")
        self.Button3H.configure(foreground="#000000")
        self.Button3H.configure(highlightbackground="#d9d9d9")
        self.Button3H.configure(highlightcolor="black")
        self.Button3H.configure(pady="0")
        self.Button3H.configure(text='''Delete Row''')
        self.Button3H.configure(command=unknown_support.deleteRowH)

        self.Label6H = Label(self.Frame1H)
        self.Label6H.place(relx=0.23,rely=0.76, height=50, width=200)
        self.Label6H.configure(background="#d9d9d9")
        self.Label6H.configure(disabledforeground="#a3a3a3")
        self.Label6H.configure(foreground="#e1031e")
        self.Label6H.configure(text='''''')
        self.Label6H.configure(width=274)

        self.Frame2H = Frame(self.TNotebook1_t2)
        self.Frame2H.place(relx=0.02, rely=0.55, relheight=0.21, relwidth=0.96)
        self.Frame2H.configure(relief=GROOVE)
        self.Frame2H.configure(borderwidth="2")
        self.Frame2H.configure(relief=GROOVE)
        self.Frame2H.configure(background="#d9d9d9")
        self.Frame2H.configure(width=425)

        self.Canvas2H = Canvas(self.Frame2H, width=300, height=300)
        self.Canvas2H.pack(side=LEFT, fill=BOTH, expand=True)

        self.Frame5H = Canvas(self.Canvas2H, width=300, height=300)
        self.Frame5H.pack(side=LEFT, fill=BOTH, expand=True)

        # self.vbar2H = Scrollbar(self.Canvas2H, orient=HORIZONTAL)
        # self.vbar2H.config(command=self.Canvas2H.yview)
        # self.Canvas2H.config(yscrollcommand=self.vbar2H.set)
        # self.vbar2H.pack(side=BOTTOM, fill=X)
        # self.Canvas2H.pack(side="left", fill="both", expand=True)
        # self.Canvas2H.config(yscrollcommand=self.vbarH.set)
        # self.Canvas2H.config(scrollregion=(0, 0, 1000, 1000), yscrollcommand=self.vbar2H.set)

        # self.Canvas2H.configure(scrollregion=self.Canvas2.bbox("all"))


        self.fH = Figure(figsize=(5, 4), dpi=100)

        self.canvasH = FigureCanvasTkAgg(self.fH, master=self.Frame5H)
        self.toolbarH = NavigationToolbar2TkAgg(self.canvasH, self.Frame5H)

        self.Frame9H = Frame(self.TNotebook1_t2)
        self.Frame9H.place(relx=0.02, rely=0.78, relheight=0.16, relwidth=0.96)
        self.Frame9H.configure(relief=GROOVE)
        self.Frame9H.configure(borderwidth="2")
        self.Frame9H.configure(relief=GROOVE)
        self.Frame9H.configure(background="#d9d9d9")
        self.Frame9H.configure(width=535)

        # self.ImageFrame9 = PhotoImage(file="bg2.png")
        #
        # self.Image1Label = Label(self.Frame9, image=self.ImageFrame9)
        # self.Image1Label.pack()

        self.Label9H = Label(self.Frame9H)
        self.Label9H.place(relx=0.01, rely=0.13, height=21, width=235)
        self.Label9H.configure(background="#d9d9d9")
        self.Label9H.configure(disabledforeground="#a3a3a3")
        self.Label9H.configure(foreground="#000000")
        self.Label9H.configure(font=("Helvetica", 12))
        self.Label9H.configure(text=''' Average Waiting Time         =''')

        self.Label8H = Label(self.Frame9H)
        self.Label8H.place(relx=0.01, rely=0.53, height=21, width=235)
        self.Label8H.configure(background="#d9d9d9")
        self.Label8H.configure(disabledforeground="#a3a3a3")
        self.Label8H.configure(foreground="#000000")
        self.Label8H.configure(font=("Helvetica", 12))
        self.Label8H.configure(text='''Average Turnaround Time   =''')

        self.aveWaitTimeH = Label(self.Frame9H)
        self.aveWaitTimeH.place(relx=0.3, rely=0.13, height=21, width=29)
        self.aveWaitTimeH.configure(background="#d9d9d9")
        self.aveWaitTimeH.configure(disabledforeground="#a3a3a3")
        self.aveWaitTimeH.configure(foreground="#e1031e")
        self.aveWaitTimeH.configure(font=("Helvetica", 12))
        self.aveWaitTimeH.configure(text='''''')

        self.aveTurnTimeH = Label(self.Frame9H)
        self.aveTurnTimeH.place(relx=0.3, rely=0.53, height=21, width=29)
        self.aveTurnTimeH.configure(background="#d9d9d9")
        self.aveTurnTimeH.configure(disabledforeground="#a3a3a3")
        self.aveTurnTimeH.configure(font=("Helvetica", 12))
        self.aveTurnTimeH.configure(foreground="#e1031e")
        self.aveTurnTimeH.configure(text='''''')

        # self.Canvas1.configure(scrollregion=self.Canvas1.bbox("all"))

        #########################################################

if __name__ == '__main__':
    vp_start_gui()

