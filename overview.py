from gi.repository import Gtk, Gio
from decimal import *
from data import Data

class Overview():

    def __init__(self):
        
        self.data = Data()
        self.entryRows = []

        # Create Grids
        self.grid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        self.contentViewport = Gtk.Viewport()
        
        self.contentScrolledWindow.set_vexpand(True)
        
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)
        
        
        self.incomeIndex = 1
        self.expensesIndex = 0
        
        # Print out Months
        for index in range(1,len(self.data.allMonthMenu)):
            self.label = Gtk.Label(self.data.allMonthMenu[index][1])
            self.label.set_property("height-request", 30)
            self.contentGrid.attach(self.label,index,0,1,1)

        # Print out income categories and values
        for index in range(1,len(self.data.incomeMenu)):
            self.label = Gtk.Label(self.data.incomeMenu[index][1])
            self.label.set_property("height-request", 30)
            self.incomeIndex = index
            
            self.contentGrid.attach(self.label,0,index,1,1)
            
            for month in range(1,len(self.data.allMonthMenu)):
                self.total = 0
                for data in range(0,len(self.data.income)):
                    if self.data.income[data][0][0] == index:
                        if self.data.income[data][1] == self.data.allMonthMenu[month][0]:
                            self.total += Decimal(self.data.income[data][3])
                 
                self.totalLabel = Gtk.Label("$" + str(self.total))
                self.contentGrid.attach(self.totalLabel, month, index, 1, 1) 
            
        # Print out category "All Income" and Values
        self.incomeIndex += 1
        self.incomeAllLabel = Gtk.Label(self.data.incomeMenu[0][1])
        self.incomeAllLabel.set_property("height-request", 30)
        self.contentGrid.attach(self.incomeAllLabel,0, self.incomeIndex,1,1)
        
        for month in range(1,len(self.data.allMonthMenu)):
            self.total = 0
            for data in range(0,len(self.data.income)):
                if self.data.income[data][1] == self.data.allMonthMenu[month][0]:
                    self.total += Decimal(self.data.income[data][3])
            self.totalLabel = Gtk.Label("$" + str(self.total))
            self.contentGrid.attach(self.totalLabel, month, self.incomeIndex, 1, 1) 

        self.incomeIndex += 1
        
        self.dummyLabel = Gtk.Label()
        self.contentGrid.attach(self.dummyLabel, month, self.incomeIndex, 1, 1) 
        
        self.incomeIndex += 1
        
        # Print out Expense Categories and Values
        for index in range(1,len(self.data.expenseMenu)):
            self.label = Gtk.Label(self.data.expenseMenu[index][1])
            self.label.set_property("height-request", 30)
            self.expensesIndex = index
            
            self.contentGrid.attach(self.label,0, self.incomeIndex + index,1,1)
            
            for month in range(1,len(self.data.allMonthMenu)):
                self.total = 0
                for data in range(0,len(self.data.expenses)):
                    if self.data.expenses[data][0][0] == index:
                        if self.data.expenses[data][1] == self.data.allMonthMenu[month][0]:
                            self.total += Decimal(self.data.expenses[data][3])
                 
                self.totalLabel = Gtk.Label("$" + str(self.total))
                self.contentGrid.attach(self.totalLabel, month, self.incomeIndex + index, 1, 1) 
            
        
        # Print out category "All Expenses" and Values
        self.expensesIndex += 1
        self.expensesAllLabel = Gtk.Label(self.data.expenseMenu[0][1])
        self.expensesAllLabel.set_property("height-request", 30)
        self.contentGrid.attach(self.expensesAllLabel,0,self.expensesIndex + self.incomeIndex,1,1)
        
        for month in range(1,len(self.data.allMonthMenu)):
            self.total = 0
            for data in range(0,len(self.data.expenses)):
                if self.data.expenses[data][1] == self.data.allMonthMenu[month][0]:
                    self.total += Decimal(self.data.expenses[data][3])
            self.totalLabel = Gtk.Label("$" + str(self.total))
            self.contentGrid.attach(self.totalLabel, month, self.incomeIndex + self.expensesIndex, 1, 1) 
        

        
        self.contentViewport.add(self.contentGrid)
