from gi.repository import Gtk, Gio

class Data():

    def __init__(self):
        self.incomeMenu = [
                        [0, 'All Income']
                        ,[1, 'Income 1']
                        ,[2, 'Income 2']
                        ,[3, 'Income 3']
                        ,[4, 'Income 4']
                        ,[5, 'Income 5']]
        
        self.expenseMenu = [
                        [0, 'All Expenses']
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
                        ,[1, 'November']
                        ,[2, 'October']
                        ,[3, 'September']
                        ,[4, 'August']
                        ,[5, 'July']
                        ,[6, 'June']
                        ,[7, 'May']
                        ,[8, 'April']
                        ,[9, 'March']
                        ,[10, 'February']
                        ,[11, 'January']
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
                [[2, 'Income 2'], [10, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [10, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [9, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [9, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [8, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [8, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [7, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [7, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [6, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [6, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [5, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [5, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [4, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [4, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [3, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [3, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [2, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [2, 1, 2014], '1500','']
                ,[[2, 'Income 2'], [1, 15, 2014], '1500','']
                ,[[1, 'Income 1'], [1, 1, 2014], '1500','']
                ]
        
        self.expenses = [
                [[7, 'Restaurant'], [10, 10, 2014], '1.66','Cafetaria']
                ,[[7, 'Restaurant'], [10, 9, 2014], '29.52','Pizza Hut']
                ,[[7, 'Restaurant'], [10, 8, 2014], '26.52','Chinese Buffet']
                ,[[4, 'Credit/Loans'], [10, 8, 2014], '453.20','Federal Loan']
                ,[[7, 'Restaurant'], [10, 7, 2014], '40.76','Hibachi Grill']
                ,[[5, 'Auto'], [10, 7, 2014], '40.45','Lumina Gas']
                ,[[7, 'Restaurant'], [10, 6, 2014], '10.55','Taco Bell']
                ,[[7, 'Restaurant'], [10, 5, 2014], '2.22','Cafetaria']
                ,[[5, 'Auto'], [10, 4], '29.45','Prius Gas']
                ,[[7, 'Restaurant'], [10, 4, 2014], '9.19','Bar']
                ,[[7, 'Restaurant'], [10, 3, 2014], '8.12','Burger King']
                ,[[7, 'Restaurant'], [10, 3, 2014], '15.20','Taco Bell']
                ,[[7, 'Restaurant'], [10, 2, 2014], '1.66','Cafetaria']
                ,[[1, 'Rent'], [10, 1, 2014], '1650','Rent']
                ,[[7, 'Restaurant'], [9, 10, 2014], '1.66','Cafetaria']
                ,[[7, 'Restaurant'], [9, 9, 2014], '29.52','Pizza Hut']
                ,[[7, 'Restaurant'], [9, 8, 2014], '26.52','Chinese Buffet']
                ,[[4, 'Credit/Loans'], [8, 8, 2014], '453.20','Federal Loan']
                ,[[7, 'Restaurant'], [8, 7, 2014], '40.76','Hibachi Grill']
                ,[[5, 'Auto'], [8, 7, 2014], '40.45','Lumina Gas']
                ,[[7, 'Restaurant'], [7, 6, 2014], '10.55','Taco Bell']
                ,[[7, 'Restaurant'], [7, 5, 2014], '2.22','Cafetaria']
                ,[[5, 'Auto'], [7, 4, 2014], '29.45','Prius Gas']
                ,[[7, 'Restaurant'], [6, 4, 2014], '9.19','Bar']
                ,[[7, 'Restaurant'], [6, 3, 2014], '8.12','Burger King']
                ,[[7, 'Restaurant'], [6, 3, 2014], '15.20','Taco Bell']
                ,[[7, 'Restaurant'], [5, 2, 2014], '1.66','Cafetaria']
                ,[[1, 'Rent'], [5, 1, 2014], '1650','Rent']
                ,[[7, 'Restaurant'], [5, 10, 2014], '1.66','Cafetaria']
                ,[[7, 'Restaurant'], [4, 9, 2014], '29.52','Pizza Hut']
                ,[[7, 'Restaurant'], [4, 8, 2014], '26.52','Chinese Buffet']
                ,[[4, 'Credit/Loans'], [4, 8, 2014], '453.20','Federal Loan']
                ,[[7, 'Restaurant'], [3, 7, 2014], '40.76','Hibachi Grill']
                ,[[5, 'Auto'], [3, 7, 2014], '40.45','Lumina Gas']
                ,[[7, 'Restaurant'], [3, 6, 2014], '10.55','Taco Bell']
                ,[[7, 'Restaurant'], [2, 5, 2014], '2.22','Cafetaria']
                ,[[5, 'Auto'], [7, 2, 2014], '29.45','Prius Gas']
                ,[[7, 'Restaurant'], [2, 4, 2014], '9.19','Bar']
                ,[[7, 'Restaurant'], [1, 3, 2014], '8.12','Burger King']
                ,[[7, 'Restaurant'], [1, 3, 2014], '15.20','Taco Bell']
                ,[[7, 'Restaurant'], [1, 2, 2014], '1.66','Cafetaria']
                ,[[1, 'Rent'], [1, 1, 2014], '1650','Rent']
                ]

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

        if data[index][dateIndex][dayIndex] == '1':
            dateString += ("st")
        elif data[index][dateIndex][dayIndex] == '21':
            dateString += ("st")
        elif data[index][dateIndex][dayIndex] == '31':
            dateString += ("st")
        elif data[index][dateIndex][dayIndex] == '2':
            dateString += ("nd")
        elif data[index][dateIndex][dayIndex] == '22':
            dateString += ("nd")
        elif data[index][dateIndex][dayIndex] == '3':
            dateString += ("rd")
        elif data[index][dateIndex][dayIndex] == '23':
            dateString += ("rd")
        else:
            dateString += ("th")
        return dateString
