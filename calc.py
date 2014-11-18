from gi.repository import Gtk, Gio, Gdk
from decimal import *

class Calc():

    def __init__(self, data):
        self.data = data

    def sumTotalData(self,data_arr):
        total = 0
        for i in range (0,len(data_arr)):
            total += Decimal(data_arr[i][self.data.value])
        return total
    
    def sumCategoryData(self,data_arr, category):
        total = 0
        for i in range (0,len(data_arr)):
            if data_arr[i][self.data.category][self.data.category_index] == category:
                total += Decimal(data_arr[i][self.data.value])
        return total
    
    def sumMonthData(self,data_arr, month):
        total = 0
        for i in range (0,len(data_arr)):
            if data_arr[i][self.data.date][self.data.date_month] == month:
                total += Decimal(data_arr[i][self.data.value])
        return total
    
    def sumCategoryMonthData(self,data_arr, category, month):
        total = 0
        for i in range (0,len(data_arr)):
            if data_arr[i][self.data.category][self.data.category_index] == category and data_arr[i][self.data.date][self.data.date_month] == month:
                total += Decimal(data_arr[i][self.data.value])
        return total
