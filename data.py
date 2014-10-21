from gi.repository import Gtk, Gio

class Data():

    def __init__(self):
        self.incomeMenu = [
                        [0, 'All']
                        ,[1, 'Income 1']
                        ,[2, 'Income 2']
                        ,[3, 'Income 3']
                        ,[4, 'Income 4']
                        ,[5, 'Income 5']]
        
        self.expenseMenu = [
                        [0, 'All']
                        ,[1, 'Rent']
                        ,[2, 'Monthly Bills']
                        ,[3, 'Insurance']
                        ,[4, 'Credit/Loans']
                        ,[5, 'Auto']
                        ,[6, 'Grocery']
                        ,[7, 'Restaurant']
                        ,[8, 'Media']
                        ,[9, 'Activities']
                        ,[10, 'Medical']
                        ,[11, 'Pet']
                        ,[12, 'Athletics']
                        ,[13, 'Donations']
                        ,[14, 'Gifts']
                        ,[15, 'Home Improvement']
                        ,[16, 'Technology']
                        ,[17, 'Travel']
                        ,[18, 'Clothing']
                        ,[19, 'Misc. Expenses']
                        ,[20, 'Wedding']]
        
        self.currentMonthMenu = [
                        [0, 'All']
                        ,[1, 'October']
                        ,[2, 'September']
                        ,[3, 'August']
                        ,[4, 'July']
                        ,[5, 'June']
                        ,[6, 'May']
                        ,[7, 'April']
                        ,[8, 'March']
                        ,[9, 'February']
                        ,[10, 'January']
                        ]

        self.allMonthMenu = [
                        [0, 'All']
                        ,[1, 'January']
                        ,[2, 'February']
                        ,[3, 'March']
                        ,[4, 'April']
                        ,[5, 'May']
                        ,[6, 'June']
                        ,[7, 'July']
                        ,[8, 'August']
                        ,[9, 'September']
                        ,[10, 'October']
                        ,[11, 'November']
                        ,[12, 'December']
                        ]
        
        self.income = [
                [[2, 'Income 2'], 12, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 12, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 11, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 11, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 10, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 10, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 9, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 9, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 8, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 8, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 7, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 7, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 6, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 6, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 5, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 5, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 4, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 4, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 3, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 3, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 2, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 2, 1, '1500','Income 1']
                ,[[2, 'Income 2'], 1, 15, '1500','Income 2']
                ,[[1, 'Income 1'], 1, 1, '1500','Income 1']
                ]
        
        self.expenses = [
                [[7, 'Restaurant'], 10, 10, '1.66','Cafetaria']
                ,[[7, 'Restaurant'], 10, 9, '29.52','Pizza Hut']
                ,[[7, 'Restaurant'], 10, 8, '26.52','Chinese Buffet']
                ,[[4, 'Credit/Loans'], 10, 8, '453.20','Federal Loan']
                ,[[7, 'Restaurant'], 10, 7, '40.76','Hibachi Grill']
                ,[[5, 'Auto'], 10, 7, '40.45','Lumina Gas']
                ,[[7, 'Restaurant'], 10, 6, '10.55','Taco Bell']
                ,[[7, 'Restaurant'], 10, 5, '2.22','Cafetaria']
                ,[[5, 'Auto'], 10, 4, '29.45','Prius Gas']
                ,[[7, 'Restaurant'], 10, 4, '9.19','Bar']
                ,[[7, 'Restaurant'], 10, 3, '8.12','Burger King']
                ,[[7, 'Restaurant'], 10, 3, '15.20','Taco Bell']
                ,[[7, 'Restaurant'], 10, 2, '1.66','Cafetaria']
                ,[[1, 'Rent'], 10, 1, '1650','Rent']
                ,[[7, 'Restaurant'], 9, 10, '1.66','Cafetaria']
                ,[[7, 'Restaurant'], 9, 9, '29.52','Pizza Hut']
                ,[[7, 'Restaurant'], 9, 8, '26.52','Chinese Buffet']
                ,[[4, 'Credit/Loans'], 8, 8, '453.20','Federal Loan']
                ,[[7, 'Restaurant'], 8, 7, '40.76','Hibachi Grill']
                ,[[5, 'Auto'], 8, 7, '40.45','Lumina Gas']
                ,[[7, 'Restaurant'], 7, 6, '10.55','Taco Bell']
                ,[[7, 'Restaurant'], 7, 5, '2.22','Cafetaria']
                ,[[5, 'Auto'], 7, 4, '29.45','Prius Gas']
                ,[[7, 'Restaurant'], 6, 4, '9.19','Bar']
                ,[[7, 'Restaurant'], 6, 3, '8.12','Burger King']
                ,[[7, 'Restaurant'], 6, 3, '15.20','Taco Bell']
                ,[[7, 'Restaurant'], 5, 2, '1.66','Cafetaria']
                ,[[1, 'Rent'], 5, 1, '1650','Rent']
                ,[[7, 'Restaurant'], 5, 10, '1.66','Cafetaria']
                ,[[7, 'Restaurant'], 4, 9, '29.52','Pizza Hut']
                ,[[7, 'Restaurant'], 4, 8, '26.52','Chinese Buffet']
                ,[[4, 'Credit/Loans'], 4, 8, '453.20','Federal Loan']
                ,[[7, 'Restaurant'], 3, 7, '40.76','Hibachi Grill']
                ,[[5, 'Auto'], 3, 7, '40.45','Lumina Gas']
                ,[[7, 'Restaurant'], 3, 6, '10.55','Taco Bell']
                ,[[7, 'Restaurant'], 2, 5, '2.22','Cafetaria']
                ,[[5, 'Auto'], 7, 2, '29.45','Prius Gas']
                ,[[7, 'Restaurant'], 2, 4, '9.19','Bar']
                ,[[7, 'Restaurant'], 1, 3, '8.12','Burger King']
                ,[[7, 'Restaurant'], 1, 3, '15.20','Taco Bell']
                ,[[7, 'Restaurant'], 1, 2, '1.66','Cafetaria']
                ,[[1, 'Rent'], 1, 1, '1650','Rent']
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
