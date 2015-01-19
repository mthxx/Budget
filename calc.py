from gi.repository import Gtk, Gio, Gdk
from decimal import *

class Calc():

    def __init__(self, data):
        self.data = data

    def sumCategoryData(self,data_arr, category):
        total = 0
        for i in range (0,len(data_arr)):
            if data_arr[i][self.data.CATEGORY][self.data.CATEGORY_INDEX] == category:
                total += Decimal(data_arr[i][self.TRANSACTION_VALUE_INDEX])
        return total
    
    def sumCategoryMonthData(self,data_arr, category, month):
        total = 0
        for i in range (0,len(data_arr)):
            if data_arr[i][self.data.CATEGORY][self.data.CATEGORY_INDEX] == category and data_arr[i][self.data.DATE][self.data.DATE_MONTH] == month:
                total += Decimal(data_arr[i][self.TRANSACTION_VALUE_INDEX])
        return total
    
    def sumMonthData(self,data_arr, month):
        total = 0
        for i in range (0,len(data_arr)):
            if data_arr[i][self.data.DATE][self.data.DATE_MONTH] == month:
                total += Decimal(data_arr[i][self.TRANSACTION_VALUE_INDEX])
        return total
    
    def sumTotalData(self,data_arr):
        total = 0
        for i in range (0,len(data_arr)):
            total += Decimal(data_arr[i][self.data.TRANSACTION_VALUE_INDEX])
            print(total)
            #total = "%.2f" % total
        return total
