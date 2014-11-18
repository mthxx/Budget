from gi.repository import Gtk, Gio
from decimal import *
import os.path 

class Data():

    def __init__(self):
        #Indexes for data arrays
        self.category = 0
        self.category_index = 0
        self.category_text = 1

        self.date = 1
        self.date_month = 0
        self.date_day = 1
        self.date_year = 2
       
        self.value = 2
        self.description = 3

        self.incomeMenu = []
        self.expenseMenu = []
        self.currentMonthMenu = []
        self.allMonthMenu = []
        self.income = []
        self.expenses = []

        if(os.path.isfile('database.txt')):
            f = open('database.txt', 'r')
            for db in f.readlines():
                line = db.split(',')
                if line[0] == 'incomeMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.incomeMenu.append(self.arr)
                elif line[0] == 'expenseMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.expenseMenu.append(self.arr)
                elif line[0] == 'currentMonthMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.currentMonthMenu.append(self.arr)
                elif line[0] == 'allMonthMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.allMonthMenu.append(self.arr)
                elif line[0] == 'income':
                    self.arr = []
                    self.catArr = []
                    self.dateArr = []
                    self.catArr.append(int(line[1].strip()))
                    self.catArr.append(line[2].strip())
                    self.dateArr.append(int(line[3].strip()))
                    self.dateArr.append(int(line[4].strip()))
                    self.dateArr.append(int(line[5].strip()))
                    self.arr.append(self.catArr)
                    self.arr.append(self.dateArr)
                    self.arr.append(Decimal(line[6].strip()))
                    self.arr.append(line[7].strip())
                    self.income.append(self.arr)
                elif line[0] == 'expense':
                    self.arr = []
                    self.catArr = []
                    self.dateArr = []
                    self.catArr.append(int(line[1].strip()))
                    self.catArr.append(line[2].strip())
                    self.dateArr.append(int(line[3].strip()))
                    self.dateArr.append(int(line[4].strip()))
                    self.dateArr.append(int(line[5].strip()))
                    self.arr.append(self.catArr)
                    self.arr.append(self.dateArr)
                    self.arr.append(Decimal(line[6].strip()))
                    self.arr.append(line[7].strip())
                    self.expenses.append(self.arr)

            f.close()

    def translate_date(self,data,index):
        dateString = ""
        dateIndex = 1
        monthIndex = 0
        dayIndex = 1

        if data[index][dateIndex][monthIndex] == 1:
            dateString += ("January")
        elif data[index][dateIndex][monthIndex] == 2:
            dateString += ("February")
        elif data[index][dateIndex][monthIndex] == 3:
            dateString += ("March")
        elif data[index][dateIndex][monthIndex] == 4:
            dateString += ("April")
        elif data[index][dateIndex][monthIndex] == 5:
            dateString += ("May")
        elif data[index][dateIndex][monthIndex] == 6:
            dateString += ("June")
        elif data[index][dateIndex][monthIndex] == 7:
            dateString += ("July")
        elif data[index][dateIndex][monthIndex] == 8:
            dateString += ("August")
        elif data[index][dateIndex][monthIndex] == 9:
            dateString += ("September")
        elif data[index][dateIndex][monthIndex] == 10:
            dateString += ("October")
        elif data[index][dateIndex][monthIndex] == 11:
            dateString += ("November")
        elif data[index][dateIndex][monthIndex] == 12:
            dateString += ("December")
        else:
            dateString += ("Month Fail")

        dateString += (" " + str(data[index][dateIndex][dayIndex]))

        if data[index][dateIndex][dayIndex] == 1:
            dateString += ("st")
        elif data[index][dateIndex][dayIndex] == 21:
            dateString += ("st")
        elif data[index][dateIndex][dayIndex] == 31:
            dateString += ("st")
        elif data[index][dateIndex][dayIndex] == 2:
            dateString += ("nd")
        elif data[index][dateIndex][dayIndex] == 22:
            dateString += ("nd")
        elif data[index][dateIndex][dayIndex] == 3:
            dateString += ("rd")
        elif data[index][dateIndex][dayIndex] == 23:
            dateString += ("rd")
        else:
            dateString += ("th")
        return dateString
