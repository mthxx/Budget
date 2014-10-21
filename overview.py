from gi.repository import Gtk, Gio
from decimal import *
from data import Data

class Overview():

    def __init__(self):
        
        # Initialize Variables
        self.data = Data()
        self.index = 1

        # Create Layouts
        self.grid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        self.contentViewport = Gtk.Viewport()
       
        # Style Layouts
        self.contentScrolledWindow.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)

        # Build Layouts
        self.contentScrolledWindow.add(self.contentViewport)
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)
        self.contentViewport.add(self.contentGrid)
        
        # Print out Months
        for index in range(1,len(self.data.allMonthMenu)):
            self.label = Gtk.Label(self.data.allMonthMenu[index][1])
            self.label.set_property("height-request", 30)
            self.contentGrid.attach(self.label,index,0,1,1)

        self.display_info(self.data.incomeMenu, self.data.income)
        self.display_info(self.data.expenseMenu, self.data.expenses)

    
    def display_info(self,data_cat, data_arr):
        
        for index in range(1,len(data_cat)):
            self.label = Gtk.Label(data_cat[index][1])
            self.label.set_property("height-request", 30)
            self.index += 1
            self.contentGrid.attach(self.label, 0, self.index, 1, 1)
            
            for month in range(1,len(self.data.allMonthMenu)):
                self.total = 0
                for data in range(0,len(self.data.expenses)):
                    if self.data.expenses[data][0][0] == index:
                        if self.data.expenses[data][1] == self.data.allMonthMenu[month][0]:
                            self.total += Decimal(self.data.expenses[data][3])
                 
                self.totalLabel = Gtk.Label("$" + str(self.total))
                self.contentGrid.attach(self.totalLabel, month, self.index, 1, 1) 
        
        self.index += 1
        self.AllLabel = Gtk.Label(data_cat[0][1])
        self.AllLabel.set_property("height-request", 30)
        self.contentGrid.attach(self.AllLabel, 0, self.index, 1, 1)
        
        for month in range(1,len(self.data.allMonthMenu)):
            self.total = 0
            for data in range(0,len(data_arr)):
                if data_arr[data][1] == self.data.allMonthMenu[month][0]:
                    self.total += Decimal(data_arr[data][3])
            self.totalLabel = Gtk.Label("$" + str(self.total))
            self.contentGrid.attach(self.totalLabel, month, self.index, 1, 1) 
        
        self.index += 1
        self.dummyLabel = Gtk.Label()
        self.contentGrid.attach(self.dummyLabel, 0, self.index, 1, 1) 
        self.index += 1
