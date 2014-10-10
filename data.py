from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Data():

    def __init__(self):
        self.currentMonthMenu = ['All','October','September','August','July','June','May','April','March','February','January']
        self.allMonthMenu = ['All','December','November','October','September','August','July','June','May','April','March','February','January']
        self.incomeSources = ['All','Income 1','Income 2','Income 3','Income 4','Income 5']
        self.expenseMenu = ['All','Rent','Monthly Bills','Insurance','Credit/Loans','Auto','Grocery','Restaurant','Media','Activities','Medical','Pet','Athletics','Donations','Gifts','Home Improvement','Technology','Travel','Clothing','Misc. Expenses','Wedding']
        
        self.income = [
                ['Income 2', 12, 15, '1500','Income 2']
                ,['Income 1', 12, 1, '1500','Income 1']
                ,['Income 2', 11, 15, '1500','Income 2']
                ,['Income 1', 11, 1, '1500','Income 1']
                ,['Income 2', 10, 15, '1500','Income 2']
                ,['Income 1', 10, 1, '1500','Income 1']
                ,['Income 2', 9, 15, '1500','Income 2']
                ,['Income 1', 9, 1, '1500','Income 1']
                ,['Income 2', 8, 15, '1500','Income 2']
                ,['Income 1', 8, 1, '1500','Income 1']
                ,['Income 2', 7, 15, '1500','Income 2']
                ,['Income 1', 7, 1, '1500','Income 1']
                ,['Income 2', 6, 15, '1500','Income 2']
                ,['Income 1', 6, 1, '1500','Income 1']
                ,['Income 2', 5, 15, '1500','Income 2']
                ,['Income 1', 5, 1, '1500','Income 1']
                ,['Income 2', 4, 15, '1500','Income 2']
                ,['Income 1', 4, 1, '1500','Income 1']
                ,['Income 2', 3, 15, '1500','Income 2']
                ,['Income 1', 3, 1, '1500','Income 1']
                ,['Income 2', 2, 15, '1500','Income 2']
                ,['Income 1', 2, 1, '1500','Income 1']
                ,['Income 2', 1, 15, '1500','Income 2']
                ,['Income 1', 1, 1, '1500','Income 1']
                ]
        
        self.expenses = [
                ['Restaurant', 10, 10, '1.66','Cafetaria']
                ,['Restaurant', 10, 9, '29.52','Pizza Hut']
                ,['Restaurant', 10, 8, '26.52','Chinese Buffet']
                ,['Credit/Loans', 10, 8, '453.20','Federal Loan']
                ,['Restaurant', 10, 7, '40.76','Hibachi Grill']
                ,['Auto', 10, 7, '40.45','Lumina Gas']
                ,['Restaurant', 10, 6, '10.55','Taco Bell']
                ,['Restaurant', 10, 5, '2.22','Cafetaria']
                ,['Auto', 10, 4, '29.45','Prius Gas']
                ,['Restaurant', 10, 4, '9.19','Bar']
                ,['Restaurant', 10, 3, '8.12','Burger King']
                ,['Restaurant', 10, 3, '15.20','Taco Bell']
                ,['Restaurant', 10, 2, '1.66','Cafetaria']
                ,['Rent', 10, 1, '1650','Rent']
                ]

    def translate_date(self,data,index):
        dateString = ""
        monthIndex = 1
        dayIndex = 2

        if data[index][monthIndex] == 1:
            dateString += ("January")
        elif data[index][monthIndex] == 2:
            dateString += ("February")
        elif data[index][monthIndex] == 3:
            dateString += ("March")
        elif data[index][monthIndex] == 4:
            dateString += ("April")
        elif data[index][monthIndex] == 5:
            dateString += ("May")
        elif data[index][monthIndex] == 6:
            dateString += ("June")
        elif data[index][monthIndex] == 7:
            dateString += ("July")
        elif data[index][monthIndex] == 8:
            dateString += ("August")
        elif data[index][monthIndex] == 9:
            dateString += ("September")
        elif data[index][monthIndex] == 10:
            dateString += ("October")
        elif data[index][monthIndex] == 11:
            dateString += ("November")
        elif data[index][monthIndex] == 12:
            dateString += ("December")
        else:
            dateString += ("Month Fail")

        dateString += (" " + str(data[index][dayIndex]))

        if data[index][dayIndex] == '1':
            dateString += ("st")
        elif data[index][dayIndex] == '21':
            dateString += ("st")
        elif data[index][dayIndex] == '31':
            dateString += ("st")
        elif data[index][dayIndex] == '2':
            dateString += ("nd")
        elif data[index][dayIndex] == '22':
            dateString += ("nd")
        elif data[index][dayIndex] == '3':
            dateString += ("rd")
        elif data[index][dayIndex] == '23':
            dateString += ("rd")
        else:
            dateString += ("th")
        return dateString
