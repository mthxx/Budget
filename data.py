from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Data():

    def __init__(self):
        self.monthMenu = ['All','December','November','October','September','August','July','June','May','April','March','February','January']
        self.incomeSources = ['All','Income 1','Income 2','Income 3','Income 4','Income 5']
        
        self.income = [
                [12, 15, '1500','Income 2']
                ,[12, 1, '1500','Income 1']
                ,[11, 15, '1500','Income 2']
                ,[11, 1, '1500','Income 1']
                ,[10, 15, '1500','Income 2']
                ,[10, 1, '1500','Income 1']
                ,[9, 15, '1500','Income 2']
                ,[9, 1, '1500','Income 1']
                ,[8, 15, '1500','Income 2']
                ,[8, 1, '1500','Income 1']
                ,[7, 15, '1500','Income 2']
                ,[7, 1, '1500','Income 1']
                ,[6, 15, '1500','Income 2']
                ,[6, 1, '1500','Income 1']
                ,[5, 15, '1500','Income 2']
                ,[5, 1, '1500','Income 1']
                ,[4, 15, '1500','Income 2']
                ,[4, 1, '1500','Income 1']
                ,[3, 15, '1500','Income 2']
                ,[3, 1, '1500','Income 1']
                ,[2, 15, '1500','Income 2']
                ,[2, 1, '1500','Income 1']
                ,[1, 15, '1500','Income 2']
                ,[1, 1, '1500','Income 1']
                ]

    def translate_date(self,data,index):
        dateString = ""
        if data[index][0] == 1:
            dateString += ("January")
        elif data[index][0] == 2:
            dateString += ("February")
        elif data[index][0] == 3:
            dateString += ("March")
        elif data[index][0] == 4:
            dateString += ("April")
        elif data[index][0] == 5:
            dateString += ("May")
        elif data[index][0] == 6:
            dateString += ("June")
        elif data[index][0] == 7:
            dateString += ("July")
        elif data[index][0] == 8:
            dateString += ("August")
        elif data[index][0] == 9:
            dateString += ("September")
        elif data[index][0] == 10:
            dateString += ("October")
        elif data[index][0] == 11:
            dateString += ("November")
        elif data[index][0] == 12:
            dateString += ("December")
        else:
            dateString += ("Month Fail")

        dateString += (" " + str(data[index][1]))

        if data[index][1] == '1':
            dateString += ("st")
        elif data[index][1] == '21':
            dateString += ("st")
        elif data[index][1] == '31':
            dateString += ("st")
        elif data[index][1] == '2':
            dateString += ("nd")
        elif data[index][1] == '22':
            dateString += ("nd")
        elif data[index][1] == '3':
            dateString += ("rd")
        elif data[index][1] == '23':
            dateString += ("rd")
        else:
            dateString += ("th")
        return dateString
