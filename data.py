from gi.repository import Gtk, Gio
from decimal import *
import os.path 

class Data():
    CATEGORY = 0
    CATEGORY_INDEX = 0
    CATEGORY_TEXT = 1

    DATE = 1
    DATE_YEAR = 0
    DATE_MONTH = 1
    DATE_DAY = 2
   
    VALUE = 2
    DESCRIPTION = 3
    UNIQUE_ID = 4

    LATEST_MENU_ID = 0
    LATEST_ID = 0

    def __init__(self):
        #Indexes for data arrays

        self.transactionsMenu = []
        self.transactions = []

        self.transaction_view = 0
        self.overview = 0
        
        self.allMonthMenu = [[0, "All"],
                            [1, "January"],
                            [2, "February"],
                            [3, "March"],
                            [4, "April"],
                            [5, "May"],
                            [6, "June"],
                            [7, "July"],
                            [8, "August"],
                            [9, "September"],
                            [10, "October"],
                            [11, "November"],
                            [12, "December"],
                            ]
    def import_data(self):
        if(os.path.isfile('database.txt')):
            f = open('database.txt', 'r')
            for db in f.readlines():
                line = db.split(',')
                if line[0] == 'menu':
                    self.arr = []
                    self.arr.append(int(line[3].strip()))
                    self.arr.append(line[2].strip())
                    self.arr.append(line[1].strip())
                    if self.LATEST_MENU_ID < int(line[3].strip()):
                        self.LATEST_MENU_ID = int(line[3].strip())
                    #self.arr.append(line[3].strip())
                    self.transactionsMenu.append(self.arr)
               
                elif line[0] == 'transaction':
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
                    if self.LATEST_ID < int(line[8].strip()):
                        self.LATEST_ID = int(line[8].strip())
                    self.sort_data(self.transactions, self.arr)

            f.close()

    def sort_data(self, data, arr):
        if len(data) == 0:
            data.append(arr)
        else:
            flag = False
            for i in range(len(data)):
                # If entry's year is equal to array's year
                if data[i][self.DATE][self.DATE_YEAR] == int(arr[self.DATE][self.DATE_YEAR]):
                    # If entry's month is equal to array's month
                    if data[i][self.DATE][self.DATE_MONTH] == int(arr[self.DATE][self.DATE_MONTH]):
                        # If entry's day is equal to array's day
                        if data[i][self.DATE][self.DATE_DAY] == int(arr[self.DATE][self.DATE_DAY]):
                            data.insert(i, arr)
                            flag = True
                            break
                        # If entry's day is less than array's day
                        elif data[i][self.DATE][self.DATE_DAY] > int(arr[self.DATE][self.DATE_DAY]):
                            for j in range(i, len(data)):
                                if data[j][self.DATE][self.DATE_MONTH] == int(arr[self.DATE][self.DATE_MONTH]):
                                    if data[j][self.DATE][self.DATE_DAY] <= int(arr[self.DATE][self.DATE_DAY]):
                                        data.insert(j, arr)
                                        flag = True
                                        break
                                else:
                                    data.insert(j , arr)
                                    flag = True
                                    break
                            break
                        # If entry's day is greater than array's day
                        elif data[i][self.DATE][self.DATE_DAY] < int(arr[self.DATE][self.DATE_DAY]):
                            data.insert(i , arr)
                            flag = True
                            break
                    # If entry's month is less than array's month
                    elif data[i][self.DATE][self.DATE_MONTH] < int(arr[self.DATE][self.DATE_MONTH]):
                        data.insert(i , arr)
                        flag = True
                        break
                # If entry's year is less than income array's year
                elif data[i][self.DATE][self.DATE_YEAR] < int(arr[self.DATE][self.DATE_YEAR]):
                    data.insert(i , arr)
                    flag = True
                    break

            if flag == False:
                data.append(arr)
            
    def connect_data_views(self, transaction_view, overview):
        self.transaction_view = transaction_view
        self.overview = overview

    def create_data_string(self,category, year, month, day, cost, description, uniqueID):
        self.editString = "transaction" + ","
        for i in range(0,len(self.transactionsMenu)):
            if category == self.transactionsMenu[i][1]:
                self.editString += str(self.transactionsMenu[i][0]) +","
        self.editString += str(category) + ","
        self.editString += str(year) + ","
        self.editString += str(month) + ","
        self.editString += str(day) + ","
        self.editString += str(cost) + ","
        self.editString += str(description) + ","
        self.editString += str(uniqueID) + "\n"
       
        return self.editString
    
    def create_category_string(self, menu, category):
        self.editString = "menu" + ","
        self.editString += str(menu) + ", "
        self.editString += str(category.get_text()) + ","
        self.LATEST_MENU_ID += 1
        self.editString += str(self.LATEST_MENU_ID) + "\n"

        return self.editString

    def add_data(self, entryString):
        if(os.path.isfile('database.txt')):
            self.transactionsMenu = []
            self.transactions = []
            f = open('database.txt', 'a')
            f.write(entryString)
            f.close()
            
            # Refresh data and views
            self.import_data()
            self.transaction_view.generate_sidebars()
            self.transaction_view.display_content()
            self.overview.redisplay_info()
    
    def delete_data(self, uniqueID):
        if(os.path.isfile('database.txt')):
            self.transactionsMenu = []
            self.transactions = []
            f = open('database.txt', 'r')
            output = []
            for line in f:
                cur = line.split(",")
                cur[0].strip()
                if cur[0] == "transaction":
                    if cur[8].strip() != uniqueID:
                        output.append(line)
                else:
                    output.append(line)
            
            f.close()
            
            f = open('database.txt', 'w')
            f.writelines(output)
            f.close()
           
            # Refresh data and views
            self.import_data()
            self.transaction_view.generate_sidebars()
            self.transaction_view.display_content()
            self.overview.redisplay_info()
            

    def translate_date(self,data,index):
        dateString = ""
        
        if index == "edit":
            if data[1] == 0:
                dateString += ("January")
            elif data[1] == 1:
                dateString += ("February")
            elif data[1] == 2:
                dateString += ("March")
            elif data[1] == 3:
                dateString += ("April")
            elif data[1] == 4:
                dateString += ("May")
            elif data[1] == 5:
                dateString += ("June")
            elif data[1] == 6:
                dateString += ("July")
            elif data[1] == 7:
                dateString += ("August")
            elif data[1] == 8:
                dateString += ("September")
            elif data[1] == 9:
                dateString += ("October")
            elif data[1] == 10:
                dateString += ("November")
            elif data[1] == 11:
                dateString += ("December")
            else:
                dateString += ("Month Fail")
            
            dateString += (" " + str(data[2]))

            if data[2] == 1:
                dateString += ("st")
            elif data[2] == 21:
                dateString += ("st")
            elif data[2] == 31:
                dateString += ("st")
            elif data[2] == 2:
                dateString += ("nd")
            elif data[2] == 22:
                dateString += ("nd")
            elif data[2] == 3:
                dateString += ("rd")
            elif data[2] == 23:
                dateString += ("rd")
            else:
                dateString += ("th")
        else:
            if data[index][self.DATE][self.DATE_MONTH] == 1:
                dateString += ("January")
            elif data[index][self.DATE][self.DATE_MONTH] == 2:
                dateString += ("February")
            elif data[index][self.DATE][self.DATE_MONTH] == 3:
                dateString += ("March")
            elif data[index][self.DATE][self.DATE_MONTH] == 4:
                dateString += ("April")
            elif data[index][self.DATE][self.DATE_MONTH] == 5:
                dateString += ("May")
            elif data[index][self.DATE][self.DATE_MONTH] == 6:
                dateString += ("June")
            elif data[index][self.DATE][self.DATE_MONTH] == 7:
                dateString += ("July")
            elif data[index][self.DATE][self.DATE_MONTH] == 8:
                dateString += ("August")
            elif data[index][self.DATE][self.DATE_MONTH] == 9:
                dateString += ("September")
            elif data[index][self.DATE][self.DATE_MONTH] == 10:
                dateString += ("October")
            elif data[index][self.DATE][self.DATE_MONTH] == 11:
                dateString += ("November")
            elif data[index][self.DATE][self.DATE_MONTH] == 12:
                dateString += ("December")
            else:
                dateString += ("Month Fail")

            dateString += (" " + str(data[index][self.DATE][self.DATE_DAY]))

            if data[index][self.DATE][self.DATE_DAY] == 1:
                dateString += ("st")
            elif data[index][self.DATE][self.DATE_DAY] == 21:
                dateString += ("st")
            elif data[index][self.DATE][self.DATE_DAY] == 31:
                dateString += ("st")
            elif data[index][self.DATE][self.DATE_DAY] == 2:
                dateString += ("nd")
            elif data[index][self.DATE][self.DATE_DAY] == 22:
                dateString += ("nd")
            elif data[index][self.DATE][self.DATE_DAY] == 3:
                dateString += ("rd")
            elif data[index][self.DATE][self.DATE_DAY] == 23:
                dateString += ("rd")
            else:
                dateString += ("th")
        return dateString
