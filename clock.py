'''RUTUJA PAWAR
    PYTHON TASK1: DIGITAL CLOCK.
'''
from tkinter import *
from time import strftime

def time():
    # Get current time
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM indicator
    lab_hr.config(text=current_time[:2])  # Update hour label
    lab_min.config(text=current_time[3:5])  # Update minute label
    lab_sec.config(text=current_time[6:8])  # Update second label
    lab_am.config(text=current_time[-2:])  # Update AM/PM label
    # Schedule the time function to run again after 1000 milliseconds (1 second)
    lab_hr.after(1000, time)

#Setting up the GUI for the Digital clock
clock = Tk()
clock.title('   DIGITAL CLOCK      ')
clock.geometry('1000x300')
clock.config(bg= 'black')

#Hour  label and text
lab_hr =  Label(clock,  text = "00", font=('Time New Roman',60, "bold"), bg='black', fg= '#E3DAC9' )
lab_hr.place(x=120, y=50, height=110, width=100)
lab_hr_txt =  Label(clock,  text = "Hr", font=('Time New Roman',25, "bold"), bg='black', fg= '#E3DAC9' )
lab_hr_txt.place(x=120, y=190, height=40, width=100)

#Minute  label and text
lab_min =  Label(clock,  text = "00", font=('Time New Roman',60, "bold"), bg='black', fg= '#E3DAC9' )
lab_min.place(x=345, y= 40, height=110, width=100)
lab_min_txt =  Label(clock,  text = "Min", font=('Time New Roman',25, "bold"), bg='black', fg= '#E3DAC9' )
lab_min_txt.place(x=340, y=190, height=40, width=100)

#Sec  label and text
lab_sec =  Label(clock,  text = "00", font=('Time New Roman',60, "bold"), bg='black', fg= '#E3DAC9' )
lab_sec.place(x=560, y= 40, height=110, width=100)
lab_sec_txt =  Label(clock,  text = "Sec", font=('Time New Roman',25, "bold"), bg='black', fg= '#E3DAC9' )
lab_sec_txt.place(x=560, y=190, height=40, width=100)

#Am/Pm  label and text
lab_am =  Label(clock,  text = "00", font=('Time New Roman',60, "bold"), bg='black', fg= '#E3DAC9' )
lab_am.place(x=780, y= 40, height=110, width=100)
lab_am_txt =  Label(clock,  text = "Am/Pm", font=('Time New Roman',20, "bold"), bg='black', fg= '#E3DAC9' )
lab_am_txt.place(x=780, y=190, height=40, width=100)

time()

clock.mainloop()