# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:35:43 2020

@author: Hp
"""
from tkinter import *
from PIL import ImageTk, Image 
import sqlite3

root2 = Tk()


con = sqlite3.connect("user1.db")
curr = con.cursor()
'''
con.execute("""CREATE TABLE worker (
              Name text,
              skillset text,
              city text,
              state text,
              pincode int
             )""")

con.execute("""CREATE TABLE Employer (
                Emp_Name text,
                Req_skill text,
                pincode int
                )""")        
'''



def submit():
     
    con = sqlite3.connect("user1.db")
    curr = con.cursor()
    curr.execute("Insert into worker values (:name, :skill, :place, :stat, :pin)",
                 { 
                      'name':name.get(),
                      'skill':skill.get(),
                      'place':place.get(),
                      'stat':stat.get(),
                      'pin': pin.get()
                      
                }) 
    
    
    con.commit()
    con.close()
    
    name.delete(0, END)
    skill.delete(0, END)
    place.delete(0, END)
    stat.delete(0, END)
    pin.delete(0, END)
    
def query():
    con = sqlite3.connect("user1.db")
    curr = con.cursor()
    curr.execute("Insert into Employer values (:emp_name, :req_skill, :req_pin)",
                 { 
                      'emp_name':emp_name.get(),
                      'req_skill':req_skill.get(),
                      
                      'req_pin': req_pin.get()
                      
                }) 
    curr.execute("select *from worker, Employer where (worker.skillset == Employer.Req_skill && worker.pincode == Employer.pincode)")
    record = curr.fetchall()
    print(record)
    
    
    con.commit()
    con.close()
    
    emp_name.delete(0, END)
    req_skill.delete(0, END)
    req_pin.delete(0, END)
    
    

def work():
    root = Tk()
    name = Entry(root, width = 30)
    name.grid(row = 0, column = 1, padx = 20)
    skill = Entry(root, width = 30)
    skill.grid(row = 1, column = 1)
    place = Entry(root, width = 30)
    place.grid(row = 2, column = 1)
    stat = Entry(root, width = 30)
    stat.grid(row = 3, column = 1)
    pin = Entry(root, width = 30)
    pin.grid(row = 4, column = 1)
    
    name_label = Label(root, text = "Name")
    name_label.grid(row = 0, column = 0)
    skill_label = Label(root, text = "Skillset")
    skill_label.grid(row = 1, column = 0)
    place_label = Label(root, text = "City")
    place_label.grid(row = 2, column = 0)  
    stat_label = Label(root, text = "State")
    stat_label.grid(row = 3, column = 0)
    pin_label = Label(root, text = "pincode")
    pin_label.grid(row = 4, column = 0)
    
    submit_bt = Button(root, text = "submit worker info", command = submit)
    submit_bt.grid(row = 5, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 100)

def emp():
    
    root1 = Tk()
    emp_name = Entry(root1, width = 30)
    emp_name.grid(row = 0, column = 1, padx = 20)
    req_skill = Entry(root1, width = 30)
    req_skill.grid(row = 1, column = 1)
    req_pin = Entry(root1, width = 30)
    req_pin.grid(row = 2, column = 1)
    
    emp_name_label = Label(root1, text = "Emp_name")
    emp_name_label.grid(row = 0, column = 0)
    req_skill_label = Label(root1, text = "Req_skill")
    req_skill_label.grid(row = 1, column = 0) 
    req_pin_label = Label(root1, text = "Pincode")
    req_pin_label.grid(row = 2, column = 0)
    
    query_bt = Button(root1, text = "Display workers", command = query)
    query_bt.grid(row = 3, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 50) 
#query_btn = Button(root, text = "display workers", command = query)
#query_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 50)

  
enter_label = Label(root2, text = "Select Employer or Worker")
enter_label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 150)

submit_btn = Button(root2, text = "worker", command = work)
submit_btn.grid(row = 1, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 100)

submit_bt = Button(root2, text = "Employer", command = emp)
submit_bt.grid(row = 2, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 100)
        
con.commit()
con.close()

root2.mainloop()