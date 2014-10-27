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
        
        self.menuColor = .5
        self.totalColor = .75
        self.highlightColor = .1
        
        # Create Layouts
        self.grid = Gtk.Grid()
        self.overviewGrid = Gtk.Grid()
        self.headerGrid = Gtk.Grid()
        
        self.monthGrid = Gtk.Grid()
        self.monthScrolledWindow = Gtk.ScrolledWindow()
        self.monthViewport = Gtk.Viewport()
        
        self.contentGrid = Gtk.Grid()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        self.contentViewport = Gtk.Viewport()
        
        self.categoryGrid = Gtk.Grid()
        self.categoryScrolledWindow = Gtk.ScrolledWindow()
        self.categoryViewport = Gtk.Viewport()
        
        # Build Master Grid
        self.grid.attach(self.headerGrid,0,0,1,1)
        self.grid.attach(self.overviewGrid,0,1,1,1)
        
        # Style Master Grid
        
        self.build_header()
        self.build_overview()    
        self.display_info(self.data.incomeMenu, self.data.income)
        self.empty_row()
        self.display_info(self.data.expenseMenu, self.data.expenses)

    def build_header(self):
        # Build Header Grid
        self.blankLabel = Gtk.Label()
        
        self.balanceLabel = Gtk.Label("Balance:  ")
        self.balanceLabel.set_halign(Gtk.Align.END)
        self.balanceTotalLabel = Gtk.Label( "$" + str(self.sumData(self.data.income) - self.sumData(self.data.expenses)))
        self.balanceTotalLabel.set_halign(Gtk.Align.START)
        
        self.varianceLabel = Gtk.Label("Variance:  ")
        self.varianceLabel.set_halign(Gtk.Align.END)
        self.varianceTotalLabel = Gtk.Label( "$" + str(self.sumData(self.data.income)))
        self.varianceTotalLabel.set_halign(Gtk.Align.START)
        
        self.incomeTotalLabel = Gtk.Label("Total Income:  ")
        self.incomeTotalLabel.set_halign(Gtk.Align.END)
        self.incomeTotalValueLabel = Gtk.Label( "$" + str(self.sumData(self.data.income)))
        self.incomeTotalValueLabel.set_halign(Gtk.Align.START)
        
        self.expensesTotalLabel = Gtk.Label("Total Expenses:  ")
        self.expensesTotalLabel.set_halign(Gtk.Align.END)
        self.expensesTotalValueLabel = Gtk.Label( "$" + str(self.sumData(self.data.expenses)))
        self.expensesTotalValueLabel.set_halign(Gtk.Align.START)
        
        self.headerGrid.attach(self.blankLabel,0,0,5,1)
        
        self.headerGrid.attach(self.balanceLabel,0,1,1,1)
        self.headerGrid.attach(self.balanceTotalLabel,1,1,1,1)
        
        self.headerGrid.attach(self.varianceLabel,0,2,1,1)
        self.headerGrid.attach(self.varianceTotalLabel,1,2,1,1)
        
        self.headerGrid.attach(self.expensesTotalLabel,3,1,1,1)
        self.headerGrid.attach(self.expensesTotalValueLabel,4,1,1,1)
        
        self.headerGrid.attach(self.incomeTotalLabel,3,2,1,1)
        self.headerGrid.attach(self.incomeTotalValueLabel,4,2,1,1)
        
        for i in range(0,5):
            self.dummyHeaderLabel = Gtk.Label()
            self.headerGrid.attach(self.dummyHeaderLabel,i,4,1,1)
        
        # Style Header Grid
        self.headerGrid.set_column_homogeneous(True)
        self.headerGrid.set_hexpand(True)
       

    def build_overview(self):
        # Build Overview Grid
        self.clearButton = Gtk.Button("Clear Selection")
        self.clearButton.connect("clicked", self.clear_selection)
        self.overviewGrid.attach(self.clearButton,0,0,1,1)
        
        self.monthViewport.add(self.monthGrid)
        self.monthScrolledWindow.add(self.monthViewport)
        self.overviewGrid.attach(self.monthScrolledWindow,1,0,1,1)
        
        self.categoryViewport.add(self.categoryGrid)
        self.categoryScrolledWindow.add(self.categoryViewport)
        self.overviewGrid.attach(self.categoryScrolledWindow,0,1,1,1)
       
        self.contentViewport.add(self.contentGrid)
        self.contentScrolledWindow.add(self.contentViewport)
        self.overviewGrid.attach(self.contentScrolledWindow,1,1,1,1)
        
        # Print out Months
        for index in range(1,len(self.data.allMonthMenu) + 1):
            # Total Header
            if index == len(self.data.allMonthMenu):
                self.button = Gtk.Button("Total")
                self.button.set_relief(Gtk.ReliefStyle.NONE)
                self.button.set_property("height-request", 30)
                self.button.set_property("width-request", 120)
                self.monthGrid.attach(self.button,index,0,1,1)
                self.monthArr.append([index, self.button])
                self.button.connect("clicked", self.month_clicked, 13)
            else:
                self.button = Gtk.Button(self.data.allMonthMenu[index][1])
                self.button.set_relief(Gtk.ReliefStyle.NONE)
                self.button.set_property("height-request", 30)
                self.button.set_property("width-request", 120)
                self.monthGrid.attach(self.button,index,0,1,1)
                self.monthArr.append([index, self.button])
                self.button.connect("clicked", self.month_clicked, index)
        
        # Style Overview Grid
        self.clearButton.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.menuColor, self.menuColor, self.menuColor, self.menuColor))
        
        self.categoryGrid.set_column_homogeneous(True)
        self.categoryGrid.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.menuColor, self.menuColor, self.menuColor, self.menuColor))
        
        self.categoryScrolledWindow.set_vexpand(True)
        self.categoryScrolledWindow.set_property("width-request",150)
        self.categoryScrolledWindow.set_property("hscrollbar-policy",Gtk.PolicyType.NEVER)
        self.categoryScrolledWindow.set_vadjustment(self.contentScrolledWindow.get_vadjustment())
        
        self.categoryVScrollBar = self.categoryScrolledWindow.get_vscrollbar()
        self.categoryVScrollBar.set_property("visible",False)
        
        self.monthGrid.set_column_homogeneous(True)
        self.monthGrid.set_hexpand(True)
        self.monthGrid.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.menuColor, self.menuColor, self.menuColor, self.menuColor))        
        self.monthScrolledWindow.set_property("vscrollbar-policy",Gtk.PolicyType.NEVER)
        self.monthScrolledWindow.set_hadjustment(self.contentScrolledWindow.get_hadjustment())
        
        self.monthHScrollBar = self.monthScrolledWindow.get_hscrollbar()
        self.monthHScrollBar.set_property("visible",False)
        
        self.contentScrolledWindow.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
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
            for month in range(1,len(self.data.allMonthMenu) + 1):
                self.total = 0
                # Total Column
                if month == len(self.data.allMonthMenu):
                    for data in range(0,len(data_arr)):
                        if data_arr[data][0][0] == index:
                            self.total += Decimal(data_arr[data][2])
                    self.totalLabel = Gtk.Label()
                    self.totalLabel.set_markup("<b>$" + str(self.total) + "</b>")
                    self.totalLabel.set_property("height-request", 40)
                    self.totalLabel.set_property("width-request", 120)
                    self.totalLabel.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
                    self.contentArr.append(self.totalLabel)
                    self.contentGrid.attach(self.totalLabel, month - 1, self.index, 1, 1) 
                else:
                    for data in range(0,len(data_arr)):
                        if data_arr[data][0][0] == index:
                            if data_arr[data][1][0] == self.data.allMonthMenu[month][0]:
                                self.total += Decimal(data_arr[data][2])
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
        for month in range(1,len(self.data.allMonthMenu) + 1):
            self.total = 0
            # Total Label
            if month == len(self.data.allMonthMenu):
                for data in range(0,len(data_arr)):
                    self.total += Decimal(data_arr[data][2])
                self.totalLabel = Gtk.Label()
                self.totalLabel.set_markup("<b>$" + str(self.total) + "</b>")
                self.totalLabel.set_property("height-request", 40)
                self.totalLabel.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
                self.contentArr.append(self.totalLabel)
                self.contentGrid.attach(self.totalLabel, month - 1, self.index, 1, 1) 
            else:
                for data in range(0,len(data_arr)):
                    if data_arr[data][1][0] == self.data.allMonthMenu[month][0]:
                        self.total += Decimal(data_arr[data][2])
                self.totalLabel = Gtk.Label()
                self.totalLabel.set_markup("<b>$" + str(self.total) + "</b>")
                self.totalLabel.set_property("height-request", 40)
                self.totalLabel.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
                self.contentArr.append(self.totalLabel)
                self.contentGrid.attach(self.totalLabel, month - 1, self.index, 1, 1) 
        self.entryRows.append([self.index, self.contentArr])
        self.index += 1
       
    def empty_row(self):
        # Set up empty Row
        self.contentArr = []
        self.dummyCategoryButton = Gtk.Button()
        self.dummyCategoryButton.set_relief(Gtk.ReliefStyle.NONE)
        self.dummyCategoryButton.set_property("height-request", 30)
        self.dummyCategoryButton.set_sensitive(False) 
        self.categoryArr.append([self.index, self.dummyCategoryButton])
       
        for month in range(1,len(self.data.allMonthMenu) + 1):
            self.dummyContentLabel = Gtk.Label()
            self.dummyContentLabel.set_property("height-request", 30)
            if month == len(self.data.allMonthMenu):
                self.dummyContentLabel.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
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
                        self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.menuColor, self.menuColor, self.menuColor, self.menuColor))
                    else:
                        self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.highlightColor, self.highlightColor, self.highlightColor, self.highlightColor))
            else:
                self.monthArr[i][1].set_relief(Gtk.ReliefStyle.NONE)
                for j in range(0, len(self.entryRows)):
                    if self.entryRows[j][0] != self.categoryIndex:
                       self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.0, .0, .0, .0));
                    else:
                        self.entryRows[j][1][i].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.highlightColor, self.highlightColor, self.highlightColor, self.highlightColor))
    
    def category_clicked(self, button, index):
        self.categoryIndex = index
        for i in range (0, len(self.categoryArr)):
            if self.categoryArr[i][0] == index:
                self.categoryArr[i][1].set_relief(Gtk.ReliefStyle.HALF)
                for j in range(0, len(self.entryRows[i][1])):
                    if j == self.monthIndex:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.menuColor, self.menuColor, self.menuColor, self.menuColor))
                    else:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.highlightColor, self.highlightColor, self.highlightColor, self.highlightColor))
            else:
                self.categoryArr[i][1].set_relief(Gtk.ReliefStyle.NONE)
                for j in range(0, len(self.entryRows[i][1])):
                    if j != self.monthIndex:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.0, .0, .0, .0));
                    else:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.highlightColor, self.highlightColor, self.highlightColor, self.highlightColor))
    
    def clear_selection(self, button):
        self.categoryIndex = 10000
        self.monthIndex = 10000
        for i in range (0, len(self.categoryArr)):
            self.categoryArr[i][1].set_relief(Gtk.ReliefStyle.NONE)
        for i in range (0, len(self.monthArr)):
            self.monthArr[i][1].set_relief(Gtk.ReliefStyle.NONE)
        for i in range(0, len(self.entryRows)):
            for j in range(0, len(self.entryRows[i][1])):
                if self.entryRows[i][0] == self.categoryArr[len(self.data.incomeMenu) - 1][0]:
                    self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
                elif self.entryRows[i][0] == self.categoryArr[len(self.data.incomeMenu) + len(self.data.expenseMenu)][0]:
                    self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
                else:
                    if j == len(self.data.allMonthMenu) - 1:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(self.totalColor, self.totalColor, self.totalColor, self.totalColor))
                    else:
                        self.entryRows[i][1][j].override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(.0, .0, .0, .0));
         
    def sumData(self,data_arr):
        total = 0
        for i in range (0,len(data_arr)):
            total += Decimal(data_arr[i][2])
        return total
