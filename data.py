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
        self.date_year = 0
        self.date_month = 1
        self.date_day = 2
       
        self.value = 2
        self.description = 3
        
        self.unique_id = 4 

        self.latest_id = 0

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
                    self.arr.append(line[3].strip())
                    self.incomeMenu.append(self.arr)
                elif line[0] == 'expenseMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.arr.append(line[3].strip())
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
                    self.arr.append(line[8].strip())
                    if self.latest_id < int(line[8].strip()):
                        self.latest_id = int(line[8].strip())
                    self.sort_data(self.income)

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
                    self.arr.append(line[8].strip())
                    if self.latest_id < int(line[8].strip()):
                        self.latest_id = int(line[8].strip())
                    self.sort_data(self.expenses)
            f.close()

    def sort_data(self, data):
        if len(data) == 0:
            data.append(self.arr)
        else:
            flag = False
            for i in range(len(data)):
                # If entry's year is equal to array's year
                if data[i][self.date][self.date_year] == int(self.arr[self.date][self.date_year]):
                    # If entry's month is equal to array's month
                    if data[i][self.date][self.date_month] == int(self.arr[self.date][self.date_month]):
                        # If entry's day is equal to array's day
                        if data[i][self.date][self.date_day] == int(self.arr[self.date][self.date_day]):
                            #self.expenses.insert(i, self.arr)
                            flag = True
                            break
                        # If entry's day is less than array's day
                        elif data[i][self.date][self.date_day] < int(self.arr[self.date][self.date_day]):
                            data.insert(i , self.arr)
                            flag = True
                            break
                    # If entry's month is less than array's month
                    elif data[i][self.date][self.date_month] < int(self.arr[self.date][self.date_month]):
                        data.insert(i - 1 , self.arr)
                        flag = True
                        break
                # If entry's year is less than income array's year
                elif data[i][self.date][self.date_year] < int(self.arr[self.date][self.date_year]):
                    data.insert(i , self.arr)
                    flag = True
                    break

            if flag == False:
                data.append(self.arr)
            

    def add_data(self, entryString):
        if(os.path.isfile('database.txt')):
            f = open('database.txt', 'a')
            f.write(entryString)
            f.close()

    def translate_date(self,data,index):
        dateString = ""
        
        if data[index][self.date][self.date_month] == 1:
            dateString += ("January")
        elif data[index][self.date][self.date_month] == 2:
            dateString += ("February")
        elif data[index][self.date][self.date_month] == 3:
            dateString += ("March")
        elif data[index][self.date][self.date_month] == 4:
            dateString += ("April")
        elif data[index][self.date][self.date_month] == 5:
            dateString += ("May")
        elif data[index][self.date][self.date_month] == 6:
            dateString += ("June")
        elif data[index][self.date][self.date_month] == 7:
            dateString += ("July")
        elif data[index][self.date][self.date_month] == 8:
            dateString += ("August")
        elif data[index][self.date][self.date_month] == 9:
            dateString += ("September")
        elif data[index][self.date][self.date_month] == 10:
            dateString += ("October")
        elif data[index][self.date][self.date_month] == 11:
            dateString += ("November")
        elif data[index][self.date][self.date_month] == 12:
            dateString += ("December")
        else:
            dateString += ("Month Fail")

        dateString += (" " + str(data[index][self.date][self.date_day]))

        if data[index][self.date][self.date_day] == 1:
            dateString += ("st")
        elif data[index][self.date][self.date_day] == 21:
            dateString += ("st")
        elif data[index][self.date][self.date_day] == 31:
            dateString += ("st")
        elif data[index][self.date][self.date_day] == 2:
            dateString += ("nd")
        elif data[index][self.date][self.date_day] == 22:
            dateString += ("nd")
        elif data[index][self.date][self.date_day] == 3:
            dateString += ("rd")
        elif data[index][self.date][self.date_day] == 23:
            dateString += ("rd")
        else:
            dateString += ("th")
        return dateString
