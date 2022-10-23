import numpy as np
import cv2 as cv
from tkinter import *
import requests
from bs4 import BeautifulSoup


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='GENDER')
        self.lbl2=Label(win,text='Age')
        self.lbl3=Label(win, text='HEIGHT(in metre)')
        self.lbl4=Label(win,text='Required BMI index')
        self.lbl5=Label(win, text='Weight in kgs')
        self.lbl6=Label(win, text='Calculated BMI index ')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6=Entry()
        self.t7=Entry(win, width=50)
        self.t8 = Entry(win, width=300,)
        self.t9 = Entry(win, width=300)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=400, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=400, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=400, y=150)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=400, y=200)
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=400, y=250)
        self.lbl6.place(x=100, y=300)
        self.t6.place(x=400, y=300)
        self.btn1 = Button(win, text='SHOW RESULT')
        self.b1=Button(win, text='SHOW RESULT', command=self.bmi)
        self.b1.place(x=250, y=550)
        self.t7.place(x=50,y=400)
        self.t8.place(x=50,y=450)
        self.t9.place(x=50,y=500)
    def bmi(self):
        self.t6.delete(0,'end')
        self.t4.delete(0, 'end')
        num1 = self.t1.get()
        num2 = float(self.t3.get())
        num3 = float(self.t5.get())
        result = num3/(num2*num2)
        self.t6.insert(END, str(result))
        BMI = float(self.t6.get())
        for t1, t2, t3 in [(16, 'severely underweight','https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/underweight/faq-20058429'),
                       (18.5, 'underweight','https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/underweight/faq-20058429#:~:text=Eat%20five%20to%20six%20smaller,Try%20smoothies%20and%20shakes.'),
                       (25, 'normal','YOU ARE FIT KEEP GOING'),
                        (30, 'overweight','https://www.mayoclinic.org/diseases-conditions/obesity/diagnosis-treatment/drc-20375749'),
                       (35, 'moderately obese','https://www.mayoclinic.org/diseases-conditions/obesity/diagnosis-treatment/drc-20375749'),
                       (float('inf'), 'severely obese','https://www.mayoclinic.org/diseases-conditions/obesity/diagnosis-treatment/drc-20375749')]:

            if BMI <= t1:
                str1 = ('Your BMI is', BMI)
                str2 = ('and the person is :', t2)
                str3 = str(t3)
                str4 = str(t1)

                break
        self.t4.insert(END,str4)
        self.t7.insert(END,str1)
        self.t8.insert(END,str2)
        self.t9.insert(END,str3)

window=Tk()
mywin=MyWindow(window)
window.title('BMI CALCULATOR')
window.geometry("1000x1000+10+10")
window.mainloop()