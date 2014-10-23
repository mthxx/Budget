from gi.repository import Gtk, Gio, Gdk
from decimal import *
from data import Data

class Overview():

    def __init__(self):
        
        # Initialize Variables
        self.data = Data()
        self.monthArr = []
        self.categoryArr = []
        self.entryRows = []
        self.index = 0
        self.monthIndex = 10000
        self.categoryIndex = 10000

        # Create Layouts
        self.grid = Gtk.Grid()
        
        self.monthGrid = Gtk.Grid()
        self.monthScrolledWindow = Gtk.ScrolledWindow()
        self.monthViewport = Gtk.Viewport()
        
        self.contentGrid = Gtk.Grid()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        self.contentViewport = Gtk.Viewport()
        
        self.categoryGrid = Gtk.Grid()
        self.categoryScrolledWindow = Gtk.ScrolledWindow()
        self.categoryViewport = Gtk.Viewport()
       
        # Style Layouts
        self.categoryScrolledWindow.set_vexpand(True)
        self.categoryGrid.set_column_homogeneous(True)
        self.categoryScrolledWindow.set_property("width-request",150)
        self.categoryVScrollBar = self.categoryScrolledWindow.get_vscrollbar()
        self.categoryVScrollBar.set_property("visible",False)
        self.categoryScrolledWindow.set_property("hscrollbar-policy",Gtk.PolicyType.NEVER)
        self.categoryScrolledWindow.set_vadjustment(self.contentScrolledWindow.get_vadjustment())
        
        self.monthGrid.set_column_homogeneous(True)
        self.monthGrid.set_hexpand(True)
        self.monthScrolledWindow.set_property("vscrollbar-policy",Gtk.PolicyType.NEVER)
        self.monthHScrollBar = self.monthScrolledWindow.get_hscrollbar()
        self.monthHScrollBar.set_property("visible",False)
        self.monthScrolledWindow.set_hadjustment(self.contentScrolledWindow.get_hadjustment())
        
        self.contentScrolledWindow.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        

        # Build Layouts
        self.monthViewport.add(self.monthGrid)
        self.monthScrolledWindow.add(self.monthViewport)
        self.grid.attach(self.monthScrolledWindow,1,0,1,1)
        
        self.categoryViewport.add(self.categoryGrid)
        self.categoryScrolledWindow.add(self.categoryViewport)
        self.grid.attach(self.categoryScrolledWindow,0,1,1,1)
       
        self.contentViewport.add(self.contentGrid)
        self.contentScrolledWindow.add(self.contentViewport)
        self.grid.attach(self.contentScrolledWindow,1,1,1,1)

        # Print out Months
        for index in range(1,len(self.data.allMonthMenu)):
            self.button = Gtk.Button(self.data.allMonthMenu[index][1])
            self.button.set_relief(Gtk.ReliefStyle.NONE)
            self.button.set_property("height-request", 30)
            self.button.set_property("width-request", 120)
            self.monthGrid.attach(self.button,index,0,1,1)
            self.monthArr.append([index, self.button])
            self.button.connect("clicked", self.month_clicked, index)
        

        self.display_info(self.data.incomeMenu, self.data.income)
        self.display_info(self.data.expenseMenu, self.data.expenses)

    
    def display_info(self,data_cat, data_arr):
        # Print out Categories
        for index in range(1,len(data_cat)):
            self.button = Gtk.Button(data_cat[index][1])
            self.button.set_relief(Gtk.ReliefStyle.NONE)
            self.button.set_property("height-request", 40)
            self.contentArr = []
            self.categoryArr.append([self.index, self.button])
            self.button.connect("clicked", self.category_clicked, self.index)
            self.categoryGrid.attach(self.button, 0, self.index, 1, 1)
            
            # Print out total values for each category for each month
            for month in range(1,len(self.data.allMonthMenu)):
                self.total = 0
                for data in range(0,len(data_arr)):
                    if data_arr[data][0][0] == index:
                        if data_arr[data][1] == self.data.allMonthMenu[month][0]:
                            self.total += Decimal(data_arr[data][3])
                self.totalLabel = Gtk.Label("$" + str(self.total))
                self.totalLabel.set_property("height-request", 40)
                self.totalLabel.set_property("width-request", 120)
                self.contentArr.append(self.totalLabel)
                self.contentGrid.attach(self.totalLabel, month - 1, self.index, 1, 1) 
            self.entryRows.append([self.index, self.contentArr])
            self.index += 1
        
        # Print out "All" Button
        self.AllButton = Gtk.Button(data_cat[0][1])
        self.AllButton.set_relief(Gtk.ReliefStyle.NONE)
        self.AllButton.set_property("height-request", 40)
        self.categoryArr.append([self.index, self.AllButton])
        self.AllButton.connect("clicked", self.category_clicked, self.index)
        self.categoryGrid.attach(self.AllButton, 0, self.index, 1, 1)

        # Print out total values of all categories for each month 
        self.contentArr = []
        for month in range(1,len(self.data.allMonthMenu)):
            self.total = 0
            for data in range(0,len(data_arr)):
                if data_arr[data][1] == self.data.allMonthMenu[month][0]:
                    self.total += Decimal(data_arr[data][3])
            self.totalLabel = Gtk.Label("$" + str(self.total))
            self.totalLabel.set_property("height-request", 40)
            self.contentArr.append(self.totalLabel)
            self.contentGrid.attach(self.totalLabel, month - 1, self.index, 1, 1) 
        self.entryRows.append([self.index, self.contentArr])
        self.index += 1
       
        # Set up empty Row
        self.contentArr = []
        self.dummyCategoryButton = Gtk.Button()
        self.dummyCategoryButton.set_relief(Gtk.ReliefStyle.NONE)
        self.dummyCategoryButton.set_property("height-request", 30)
        self.dummyCategoryButton.set_sensitive(False) 
        self.categoryArr.append([self.index, self.dummyCategoryButton])
       
        for month in range(1,len(self.data.allMonthMenu)):
            self.dummyContentLabel = Gtk.Label()
            self.dummyContentLabel.set_property("height-request", 30)
            self.contentArr.append(self.dummyContentLabel)
            self.contentGrid.attach(self.dummyContentLabel, month - 1, self.index, 1, 1) 
        self.entryRows.append([self.index, self.contentArr])
        
        self.categoryGrid.attach(self.dummyCategoryButton, 0, self.index, 1, 1) 
        self.index += 1

    def month_clicked(self, button, index):
        self.monthIndex = index - 1
        for i in range (0, len(self.monthArr)):
            if self.monthArr[i][0] == index:
                self.monthArr[i][1].set_relief(Gtk.ReliefStyle.HALF)
                for j in range(0, len(self.entryRows)):
                    if self.entryRows[j][0] == self.categoryIndex:
                        self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.5, .5, .5, .5));
                    else:
                        self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.1, .1, .1, .1));
            else:
                self.monthArr[i][1].set_relief(Gtk.ReliefStyle.NONE)
                for j in range(0, len(self.entryRows)):
                    if self.entryRows[j][0] != self.categoryIndex:
                       self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.0, .0, .0, .0));
                    else:
                        self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.1, .1, .1, .1));
    
    def category_clicked(self, button, index):
        self.categoryIndex = index
        for i in range (0, len(self.categoryArr)):
            if self.categoryArr[i][0] == index:
                self.categoryArr[i][1].set_relief(Gtk.ReliefStyle.HALF)
                for j in range(0, len(self.entryRows[i][1])):
                    if j == self.monthIndex:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.5, .5, .5, .5));
                    else:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.1, .1, .1, .1));
            else:
                self.categoryArr[i][1].set_relief(Gtk.ReliefStyle.NONE)
                for j in range(0, len(self.entryRows[i][1])):
                    if j != self.monthIndex:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.0, .0, .0, .0));
                    else:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.1, .1, .1, .1));
