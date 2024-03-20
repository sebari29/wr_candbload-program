import cantools
import can
import csv
from pprint import pprint
from tkinter import *
import subprocess

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()
        
        def dbcButtonClick():
            from tkinter.filedialog import askopenfilename
            filename = askopenfilename(initialdir=":c/", filetypes=(("DBC Files", "*.dbc*"),))
            #print(filename)
            
            from datetime import datetime
            current_time = datetime.now()
            date_time = str(current_time.date()) + "_" + str(current_time.timestamp())
            #print(date_time)
            
            command = "python -m cantools dump " + filename + " > " + 'DBC_' + date_time #+ ".csv"
            print(command)
            #command = "python -m cantools dump MV_HVPTC.dbc > out324.txt"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)
            quit()

        self.blfButton = Button(master, text="DBC Load", width=15, height=2,command=dbcButtonClick)
        self.blfButton.grid()
        
        def blfButtonClick():
            from tkinter.filedialog import askopenfilename
            filename = askopenfilename(initialdir=":c/", filetypes=(("BLF Files", "*.blf*"),))
            #print(filename)
            
            from datetime import datetime
            current_time = datetime.now()
            date_time = str(current_time.date()) + "_" + str(current_time.timestamp())
            #print(date_time)
            file = open('BLF_' + date_time + '.csv', 'w')
            with can.BLFReader(filename) as can_log:
                for msg in can_log:
                    content = str(msg) + "\r"
                    file.write(content)
            file.close();
            quit()

        self.blfButton = Button(master, text="BLF Load", width=15, height=2,command=blfButtonClick)
        self.blfButton.grid()

if __name__ == "__main__":
    guiFrame = GUI()  
    guiFrame.mainloop()