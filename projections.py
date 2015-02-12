from gi.repository import Gtk, Gio
import datetime, calendar
from edit_popover import Edit_Popover

class Projections():
        
    def __init__(self, data):
        self.data = data
        self.grid = Gtk.Grid(name="projectionsGrid")
        
        self.sideGrid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
        self.entryRows = []
        
        # Side Grid Styling 
        self.sideGrid.set_vexpand(True)
        self.sideGrid.set_property("width-request",200)
        
        # Content Grid Styling 
        self.contentGrid.set_hexpand(True)
        self.contentGrid.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_row_homogeneous(True)
    
        # --- Notebooks ---
        # Create Grids
        self.dayViewGrid = Gtk.Grid()
        self.weekViewGrid = Gtk.Grid()
        self.monthViewGrid = Gtk.Grid()
        self.yearViewGrid = Gtk.Grid()
        self.transactionViewGrid = Gtk.Grid()
            
        # Style Grids
        self.monthViewGrid.set_column_homogeneous(True)
        self.monthViewGrid.set_margin_start(55)
        self.monthViewGrid.set_margin_end(55)
        self.monthViewGrid.set_margin_bottom(55)

        self.transactionViewGrid.set_hexpand(True)
        self.transactionViewGrid.set_halign(Gtk.Align.FILL)
        # self.transactionViewGrid.set_column_homogeneous(True)
        self.transactionViewGrid.set_margin_start(55)
        self.transactionViewGrid.set_margin_top(20)
        self.transactionViewGrid.set_margin_end(55)
        self.transactionViewGrid.set_margin_bottom(55)

        # Create Labels
        self.dayLabel = Gtk.Label("Day")
        self.weekLabel = Gtk.Label("Week")
        self.monthLabel = Gtk.Label("Month")
        self.yearLabel = Gtk.Label("Year")
        self.transactionLabel = Gtk.Label("Transactions")

        # Create Notebooks
        self.projectionsNotebook = Gtk.Notebook()
        self.projectionsNotebook.insert_page(self.dayViewGrid, self.dayLabel,0)
        self.projectionsNotebook.insert_page(self.weekViewGrid, self.weekLabel,1)
        self.projectionsNotebook.insert_page(self.monthViewGrid, self.monthLabel,2)
        self.projectionsNotebook.insert_page(self.yearViewGrid, self.yearLabel,3)
        self.projectionsNotebook.insert_page(self.transactionViewGrid, self.transactionLabel,4)
        self.projectionsNotebook.set_show_tabs(False)
        
        self.contentGrid.add(self.projectionsNotebook)
        self.generate_sidebar()
        self.generate_month_view()
        self.generate_transactions_view()

        self.grid.attach(self.sideGrid, 0, 0, 1, 1)
        self.grid.attach(self.contentGrid, 1, 0, 1, 1)

    def add_view_mode(self, boolean):
        if boolean == True:
            self.transactionTitleLabel.show()
            self.transactionTitleEntry.show()
            self.transactionAmountLabel.show()
            self.transactionAmountEntry.show()
            self.transactionDescriptionLabel.show()
            self.transactionDescriptionEntry.show()
            self.transactionTypeLabel.show()
            self.radioBox.show()
            self.addCategoryLabel.show()
            self.addCategoryComboBoxText.show()
            self.startDateLabel.show()
            self.startDate.show()
            self.frequencyLabel.show()
            self.frequencyComboBoxText.show()
            self.cancelButton.show()
        else:
            self.transactionTitleLabel.hide()
            self.transactionTitleEntry.hide()
            self.transactionAmountLabel.hide()
            self.transactionAmountEntry.hide()
            self.transactionDescriptionLabel.hide()
            self.transactionDescriptionEntry.hide()
            self.transactionTypeLabel.hide()
            self.radioBox.hide()
            self.addCategoryLabel.hide()
            self.addCategoryComboBoxText.hide()
            self.startDateLabel.hide()
            self.startDate.hide()
            self.frequencyLabel.hide()
            self.frequencyComboBoxText.hide()
            self.cancelButton.hide()
    
    def generate_month_view(self):
        
        self.monthTitleLabel = Gtk.Label()
        self.monthPreviousButton = Gtk.Button()
        self.monthNextButton = Gtk.Button()
        
        self.backIcon = Gio.ThemedIcon(name="go-previous-symbolic")
        self.backImage = Gtk.Image.new_from_gicon(self.backIcon, Gtk.IconSize.MENU)
        self.monthPreviousButton.add(self.backImage)
        
        self.forwardIcon = Gio.ThemedIcon(name="go-next-symbolic")
        self.forwardImage = Gtk.Image.new_from_gicon(self.forwardIcon, Gtk.IconSize.MENU)
        self.monthNextButton.add(self.forwardImage)
        
        self.monthPreviousButton.connect("clicked", self.on_monthPreviousButton_clicked)
        self.monthNextButton.connect("clicked", self.on_monthNextButton_clicked)

        self.monthPreviousButton.set_margin_top(10)
        self.monthPreviousButton.set_relief(Gtk.ReliefStyle.NONE)
        
        self.monthNextButton.set_margin_top(10)
        self.monthNextButton.set_relief(Gtk.ReliefStyle.NONE)

        self.monthTitleLabel.set_margin_top(10)
        self.monthTitleLabel.set_halign(Gtk.Align.CENTER)
        self.monthTitleLabel.set_hexpand(True)

        self.monthCalendarGrid = Gtk.Grid()        

        self.monthViewGrid.attach(self.monthPreviousButton, 2,0,1,1)
        self.monthViewGrid.attach(self.monthTitleLabel, 1,0,5,1)
        self.monthViewGrid.attach(self.monthNextButton, 4,0,1,1)
        self.monthViewGrid.attach(self.monthCalendarGrid, 0,1,7,1)
         
        self.currentDay = datetime.datetime.now().day
        self.currentMonth = datetime.datetime.now().month
        self.currentYear = datetime.datetime.now().year

        self.selectedMonth = self.currentMonth
        self.selectedYear = self.currentYear

        self.currentMonthStartDate = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[0]
        self.currentMonthEndDate = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1] 

        self.populate_month_grid(self.currentMonth, self.currentYear, self.currentMonthStartDate, self.currentMonthEndDate)

    def generate_sidebar(self):
        self.dayButton = Gtk.Button("Day")
        self.weekButton = Gtk.Button("Week")
        self.monthButton = Gtk.Button("Month")
        self.yearButton = Gtk.Button("Year")
        self.transactionsButton = Gtk.Button("Transactions")
        
        self.dayButton.set_property("width-request",60)
        self.dayButton.set_margin_start(20)
        self.dayButton.set_margin_top(80)
        
        self.weekButton.set_property("width-request",50)
        self.weekButton.set_margin_start(20)
        self.weekButton.set_margin_top(20)
        
        self.monthButton.set_property("width-request",50)
        self.monthButton.set_margin_start(20)
        self.monthButton.set_margin_top(20)
        
        self.yearButton.set_property("width-request",50)
        self.yearButton.set_margin_start(20)
        self.yearButton.set_margin_top(20)
        
        self.transactionsButton.set_property("width-request",50)
        self.transactionsButton.set_margin_start(20)
        self.transactionsButton.set_margin_top(50)
        
        # Connect to handler
        self.dayButton.connect("clicked", self.on_dayButton_clicked)
        self.weekButton.connect("clicked", self.on_weekButton_clicked)
        self.monthButton.connect("clicked", self.on_monthButton_clicked)
        self.yearButton.connect("clicked", self.on_yearButton_clicked)
        self.transactionsButton.connect("clicked", self.on_transactionsButton_clicked)
        
        self.sideGrid.attach(self.dayButton, 0,0,1,1)
        self.sideGrid.attach(self.weekButton, 0,1,1,1)
        self.sideGrid.attach(self.monthButton, 0,2,1,1)
        self.sideGrid.attach(self.yearButton, 0,3,1,1)
        self.sideGrid.attach(self.transactionsButton, 0,4,1,1)

    def on_addButton_clicked(self, *args):
        if self.cancelButton.get_visible():
            # self.transactionTitleEntry.set_text("")
            # self.transactionAmountEntry.set_text("")
        
            if self.transactionTitleEntry.get_text() == "":
                self.transactionTitleLabel.set_markup("<span foreground=\"red\"><b>* Title</b></span>")
            else:
                self.transactionTitleLabel.set_text("Title")

            if self.transactionAmountEntry.get_text() == "":
                self.transactionAmountLabel.set_markup("<span foreground=\"red\"><b>* Amount</b></span>")
            else:
                self.transactionAmountLabel.set_text("Amount")
            
            if self.addCategoryComboBoxText.get_active() < 0:
                self.addCategoryLabel.set_markup("<span foreground=\"red\"><b>* Category</b></span>")
            else:
                self.addCategoryLabel.set_text("Category")
            
            if self.frequencyComboBoxText.get_active() < 0:
                self.frequencyLabel.set_markup("<span foreground=\"red\"><b>* Frequency</b></span>")
            else:
                self.frequencyLabel.set_text("Frequency")
            
            if (self.transactionTitleEntry != "" 
                and self.transactionAmountEntry != "" 
                and self.addCategoryComboBoxText.get_active() >= 0 
                and self.frequencyComboBoxText.get_active() >= 0):
                self.dateArr = self.startDate.get_date()
                self.year = str(self.dateArr[0])
                self.month = str(self.dateArr[1] + 1)
                self.day = str(self.dateArr[2])
                if self.addIncomeRadio.get_active() == True:
                    self.selected = "income"
                elif self.addExpenseRadio.get_active() == True:
                    self.selected = "expense"

                self.data.LATEST_PROJECTION_ID += 1
                
                self.data.add_projection_data(self.transactionTitleEntry.get_text(),
                    self.transactionAmountEntry.get_text(), self.transactionDescriptionEntry.get_text(),
                    self.selected, self.addCategoryComboBoxText.get_active(), self.year, self.month, self.day, 
                    self.frequencyComboBoxText.get_active(), self.data.LATEST_PROJECTION_ID)

        else:
            self.add_view_mode(True)
            for i in range(0, len(self.data.transactionsMenu)):
                self.addCategoryComboBoxText.remove(0)

            if self.addIncomeRadio.get_active() == True:
                self.selected = "income"
            elif self.addExpenseRadio.get_active() == True:
                self.selected = "expense"
            for i in range(0,len(self.data.transactionsMenu)):
                if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == self.selected:
                    if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] != "Uncategorized":
                        self.addCategoryComboBoxText.append_text(self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX])
    
    def on_addRadio_toggled(self, *args):
        for i in range(0, len(self.data.transactionsMenu)):
            self.addCategoryComboBoxText.remove(0)
        if self.addIncomeRadio.get_active() == True:
            self.radioStatus = "income"
            for i in range(0,len(self.data.transactionsMenu)):
                if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "income":
                    if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] != "Uncategorized":
                        self.addCategoryComboBoxText.append_text(self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX])
        elif self.addExpenseRadio.get_active() == True:
            self.radioStatus = "expense"
            for i in range(0,len(self.data.transactionsMenu)):
                if self.data.transactionsMenu[i][self.data.MENU_TYPE_INDEX] == "expense":
                    if self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX] != "Uncategorized":
                        self.addCategoryComboBoxText.append_text(self.data.transactionsMenu[i][self.data.MENU_NAME_INDEX])
    
    def on_cancelButton_clicked(self, *args):
        self.add_view_mode(False)
        
        # Reset fields to default
        self.transactionTitleEntry.set_text("")
        self.transactionAmountEntry.set_text("")
        self.addIncomeRadio.set_active(True)
        self.addCategoryComboBoxText.set_active(-1)
        self.startDate.select_month(self.currentMonth - 1, self.currentYear)
        self.startDate.select_day(self.currentDay)
        self.frequencyComboBoxText.set_active(-1)

    def on_dayButton_clicked(self, *args):
        self.projectionsNotebook.set_current_page(0)
     
    def on_weekButton_clicked(self, *args):
        self.projectionsNotebook.set_current_page(1)
    
    def on_monthButton_clicked(self, *args):
        self.projectionsNotebook.set_current_page(2)
    
    def on_yearButton_clicked(self, *args):
        self.projectionsNotebook.set_current_page(3)
     
    def on_transactionsButton_clicked(self, *args):
        self.projectionsNotebook.set_current_page(4)
        
    def on_monthPreviousButton_clicked(self, *args):
        if self.selectedMonth == 1:
            self.selectedYear = self.selectedYear - 1
            self.selectedMonth = 12
        else:
            self.selectedMonth = self.selectedMonth - 1
        
        start = calendar.monthrange(self.selectedYear, self.selectedMonth)[0]
        end = calendar.monthrange(self.selectedYear, self.selectedMonth)[1] 
        self.populate_month_grid(self.selectedMonth, self.selectedYear, start, end)

    def on_monthNextButton_clicked(self, *args):
        if self.selectedMonth == 12:
            self.selectedYear = self.selectedYear + 1
            self.selectedMonth = 1
        else:
            self.selectedMonth = self.selectedMonth + 1
        start = calendar.monthrange(self.selectedYear, self.selectedMonth)[0]
        end = calendar.monthrange(self.selectedYear, self.selectedMonth)[1] 
        self.populate_month_grid(self.selectedMonth, self.selectedYear, start, end)
    
    def populate_month_grid(self, month, year, start, end):
        if month == 1:
            self.monthTitleLabel.set_text("January")
        elif month == 2:
            self.monthTitleLabel.set_text("February")
        elif month == 3:
            self.monthTitleLabel.set_text("March")
        elif month == 4:
            self.monthTitleLabel.set_text("April")
        elif month == 5:
            self.monthTitleLabel.set_text("May")
        elif month == 6:
            self.monthTitleLabel.set_text("June")
        elif month == 7:
            self.monthTitleLabel.set_text("July")
        elif month == 8:
            self.monthTitleLabel.set_text("August")
        elif month == 9:
            self.monthTitleLabel.set_text("September")
        elif month == 10:
            self.monthTitleLabel.set_text("October")
        elif month == 11:
            self.monthTitleLabel.set_text("November")
        elif month == 12:
            self.monthTitleLabel.set_text("December")

        self.monthTitleLabel.set_text(self.monthTitleLabel.get_text() + " " + str(self.selectedYear))
        
        if self.monthCalendarGrid.get_child_at(1,1) != None:
            for i in range(1,8):
                self.monthCalendarGrid.get_child_at(i,1).destroy()
                self.monthCalendarGrid.get_child_at(i,2).destroy()
                self.monthCalendarGrid.get_child_at(i,3).destroy()
                self.monthCalendarGrid.get_child_at(i,4).destroy()
                self.monthCalendarGrid.get_child_at(i,5).destroy()
                self.monthCalendarGrid.get_child_at(i,6).destroy()
        
        self.dayText = 1
        self.nextMonthDate = 1
        for i in range(1, 43):
            # Create Widgets 
            if i - 2 >= start and self.dayText <= end:
                if i == 7 or i == 14 or i == 21 or i == 28 or i == 35:
                    self.monthGrid = Gtk.Grid(name="monthGridRightActive")
                elif i > 35 and i < 42:
                    self.monthGrid = Gtk.Grid(name="monthGridBottomActive")
                elif i == 42:
                    self.monthGrid = Gtk.Grid(name="monthGridLastActive")
                else:            
                    self.monthGrid = Gtk.Grid(name="monthGridActive")
                
                self.dayLabel = Gtk.Label(self.dayText)
                self.dayText += 1

                self.expenseLabel = Gtk.Label()
                self.incomeLabel = Gtk.Label()
                self.totalLabel = Gtk.Label()

                self.expenseLabel.set_markup("<span foreground=\"red\">" + "-" + "$125" + "</span>")
                self.incomeLabel.set_markup("<span foreground=\"green\">" + "+" + "$600" + "</span>")
                self.totalLabel.set_markup("<span foreground=\"green\">" + "=" + "$1250" + "</span>")
                #
                self.monthGrid.attach(self.dayLabel,0,0,1,1)
                self.monthGrid.attach(self.expenseLabel,0,1,1,1)            
                self.monthGrid.attach(self.incomeLabel,0,2,1,1)
                self.monthGrid.attach(self.totalLabel,0,3,1,1)

            else:
                if i == 7 or i == 14 or i == 21 or i == 28 or i == 35:
                    self.monthGrid = Gtk.Grid(name="monthGridRightInactive")
                elif i > 35 and i < 42:
                    self.monthGrid = Gtk.Grid(name="monthGridBottomInactive")
                elif i == 42:
                    self.monthGrid = Gtk.Grid(name="monthGridLastInactive")
                else:            
                    self.monthGrid = Gtk.Grid(name="monthGridInactive")
                
                if i - 2 < start: 

                    if month != 1:
                        self.prevMonthEndDate = calendar.monthrange(year, month - 1)[1]
                        self.prevMonthDate = self.prevMonthEndDate - start + i - 1
                        self.dayLabel = Gtk.Label(self.prevMonthDate)
                        self.monthGrid.attach(self.dayLabel,0,0,1,1)
                    else:
                        self.prevMonthEndDate = calendar.monthrange(year, 12)[1]
                        self.prevMonthDate = self.prevMonthEndDate - start + i - 1
                        self.dayLabel = Gtk.Label(self.prevMonthDate)
                        self.monthGrid.attach(self.dayLabel,0,0,1,1)
                        
                elif self.dayText > end:
                    self.dayLabel = Gtk.Label(self.nextMonthDate)
                    self.monthGrid.attach(self.dayLabel,0,0,1,1)
                    self.nextMonthDate += 1
                    
                    

            # Style Widgets
            self.monthGrid.set_column_homogeneous(True)
            self.dayLabel.set_margin_end(10)
            self.dayLabel.set_margin_top(5)
            self.dayLabel.set_halign(Gtk.Align.END)
            self.monthCalendarGrid.set_column_homogeneous(True)
            self.monthCalendarGrid.set_row_homogeneous(True)
            self.monthCalendarGrid.set_vexpand(True)
            self.monthCalendarGrid.set_margin_top(20)
        
            if i <= 7:
                self.monthCalendarGrid.attach(self.monthGrid,i,1,1,1)
            elif i > 7 and i <= 14:
                self.monthCalendarGrid.attach(self.monthGrid,(i-7),2,1,1)
            elif i > 14 and i <= 21:
                self.monthCalendarGrid.attach(self.monthGrid,(i-14),3,1,1)
            elif i > 21 and i <= 28:
                self.monthCalendarGrid.attach(self.monthGrid,(i-21),4,1,1)
            elif i > 28 and i <= 35:
                self.monthCalendarGrid.attach(self.monthGrid,(i-28),5,1,1)
            elif i > 35:
                self.monthCalendarGrid.attach(self.monthGrid,(i-35),6,1,1)

            self.monthCalendarGrid.show_all()

    def generate_transactions_view(self):
        while len(self.transactionViewGrid) > 0:
            self.transactionViewGrid.remove_row(0)
            
        while len(self.entryRows) > 0:
                self.entryRows.pop(0)
        # Create Widgets
        self.transactionTitleLabel = Gtk.Label("Title:")
        self.transactionTitleEntry = Gtk.Entry()
        
        self.transactionAmountLabel = Gtk.Label("Amount:")
        self.transactionAmountEntry = Gtk.Entry()
        
        self.transactionDescriptionLabel = Gtk.Label("Description:")
        self.transactionDescriptionEntry = Gtk.Entry()

        self.transactionTypeLabel = Gtk.Label("Type:")
        self.addIncomeRadio = Gtk.RadioButton.new_with_label(None, "Income")
        self.addExpenseRadio = Gtk.RadioButton.new_with_label(None, "Expense")
        self.addExpenseRadio.join_group(self.addIncomeRadio)
        self.radioBox = Gtk.Box(Gtk.Orientation.HORIZONTAL,1)
        self.radioBox.pack_start(self.addIncomeRadio, True, True, 0)
        self.radioBox.pack_start(self.addExpenseRadio, True, True, 0)
        
        self.addCategoryLabel = Gtk.Label("Category:")
        self.addCategoryComboBoxText = Gtk.ComboBoxText()
        
        self.startDateLabel = Gtk.Label("Start Date:")
        self.startDate = Gtk.Calendar()

        self.frequencyLabel = Gtk.Label("Frequency:")
        self.frequencyComboBoxText = Gtk.ComboBoxText()

        self.cancelButton = Gtk.Button("Cancel")
        self.addButton = Gtk.Button("Add Transaction")
            
        # Add data to frequency
        self.frequencyComboBoxText.append_text("One Time")
        self.frequencyComboBoxText.append_text("Daily")
        self.frequencyComboBoxText.append_text("Weekly")
        self.frequencyComboBoxText.append_text("Bi-Weekly")
        self.frequencyComboBoxText.append_text("Monthly on Date")
        self.frequencyComboBoxText.append_text("Monthly on Weekday")
        self.frequencyComboBoxText.append_text("Yearly")

        # Style Widgets
        self.transactionTitleLabel.set_halign(Gtk.Align.END)
        self.transactionTitleEntry.set_margin_start(20)
        
        self.transactionAmountLabel.set_halign(Gtk.Align.END)
        self.transactionAmountLabel.set_margin_top(10)
        self.transactionAmountEntry.set_margin_start(20)
        self.transactionAmountEntry.set_margin_top(10)
        
        self.transactionDescriptionLabel.set_halign(Gtk.Align.END)
        self.transactionDescriptionLabel.set_margin_top(10)
        self.transactionDescriptionEntry.set_margin_start(20)
        self.transactionDescriptionEntry.set_margin_top(10)
        
        self.transactionTypeLabel.set_halign(Gtk.Align.END)
        self.transactionTypeLabel.set_margin_top(10)
        self.radioBox.set_margin_start(20)
        self.radioBox.set_margin_top(10)
        self.radioBox.set_property("height-request", 34)
        self.addIncomeRadio.set_property("draw-indicator",False)
        self.addExpenseRadio.set_property("draw-indicator",False)
        Gtk.StyleContext.add_class(self.radioBox.get_style_context(), "linked")

        self.addCategoryLabel.set_halign(Gtk.Align.END)
        self.addCategoryLabel.set_margin_top(10)
        self.addCategoryComboBoxText.set_margin_start(20)
        self.addCategoryComboBoxText.set_margin_top(10)
        self.addCategoryComboBoxText.set_property("height-request", 34)
        
        self.startDateLabel.set_halign(Gtk.Align.END)
        self.startDateLabel.set_margin_top(10)
        self.startDate.set_margin_start(20)
        self.startDate.set_margin_top(10)
        
        self.frequencyLabel.set_halign(Gtk.Align.END)
        self.frequencyLabel.set_margin_top(10)
        self.frequencyComboBoxText.set_margin_start(20)
        self.frequencyComboBoxText.set_margin_top(10)
        self.frequencyComboBoxText.set_property("height-request", 34)
        
        self.cancelButton.set_margin_top(10)
        self.cancelButton.set_margin_bottom(20)
        self.addButton.set_margin_start(20)
        self.addButton.set_margin_top(10)
        self.addButton.set_margin_bottom(20)
        
        # Connect Widgets
        self.cancelButton.connect("clicked", self.on_cancelButton_clicked)
        self.addButton.connect("clicked", self.on_addButton_clicked)
        self.addIncomeRadio.connect("toggled", self.on_addRadio_toggled)
        
        # Attach Widgets
        if len(self.data.projections) == 0:
            self.transactionViewGrid.set_halign(Gtk.Align.CENTER)
        else:
            self.transactionViewGrid.set_halign(Gtk.Align.FILL)

        self.transactionViewGrid.attach(self.transactionTitleLabel,1,0,1,1)
        self.transactionViewGrid.attach(self.transactionTitleEntry,2,0,1,1)
        self.transactionViewGrid.attach(self.transactionAmountLabel,1,1,1,1)
        self.transactionViewGrid.attach(self.transactionAmountEntry,2,1,1,1)
        self.transactionViewGrid.attach(self.transactionDescriptionLabel,1,2,1,1)
        self.transactionViewGrid.attach(self.transactionDescriptionEntry,2,2,1,1)
        self.transactionViewGrid.attach(self.transactionTypeLabel,1,3,1,1)
        self.transactionViewGrid.attach(self.radioBox,2,3,1,1)
        self.transactionViewGrid.attach(self.addCategoryLabel,1,4,1,1)
        self.transactionViewGrid.attach(self.addCategoryComboBoxText,2,4,1,1)
        self.transactionViewGrid.attach(self.startDateLabel,1,5,1,1)
        self.transactionViewGrid.attach(self.startDate,2,5,1,1)
        self.transactionViewGrid.attach(self.frequencyLabel,1,6,1,1)
        self.transactionViewGrid.attach(self.frequencyComboBoxText,2,6,1,1)
        self.transactionViewGrid.attach(self.cancelButton,1,7,1,1)
        self.transactionViewGrid.attach(self.addButton,2,7,1,1)
        
        self.index = 8
        for i in range (0,len(self.data.projections)):
            # Date String
            self.dateString = [self.data.projections[i][4],self.data.projections[i][5] - 1,self.data.projections[i][6]]
            self.dateString = self.data.translate_date(self.dateString, "edit")
            
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.entryGrid = Gtk.Grid()
            self.costGrid = Gtk.Grid()
     
            self.categoryLabel = Gtk.Label()
            self.dateLabel = Gtk.Label(self.dateString)
            self.descriptionLabel = Gtk.Label()
            
            self.currencyLabel = Gtk.Label("$")
            self.costLabel = Gtk.Label()
            
            #if int(self.data.projections[i][self.data.PROJECTIONS_TYPE = ransactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX]) == int(self.data.transactionsMenu[j][self.data.MENU_ID_INDEX]) and self.data.transactionsMenu[j][self.data.MENU_TYPE_INDEX] == "income":
            self.costLabel.set_markup("<span foreground=\"green\">" + str(self.data.projections[i][self.data.PROJECTIONS_VALUE]) + "</span>")
           
            # for j in range(0, len(self.data.transactionsMenu)):
            #     if int(self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX]) == int(self.data.transactionsMenu[j][self.data.MENU_ID_INDEX]) and self.data.transactionsMenu[j][self.data.MENU_TYPE_INDEX] == "expense":
            #         self.costLabel.set_markup("<span foreground=\"red\">" + str(self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]) + "</span>")

            self.descriptionLabel.set_markup("<i>" + self.data.projections[i][self.data.PROJECTIONS_DESCRIPTION] + "</i>")
            
            # Create Edit Popover
            self.editButton = Gtk.Button()
            self.editPopover = Gtk.Popover.new(self.editButton)
            self.edit_popover = Edit_Popover(self.data)
            self.editPopover.add(self.edit_popover.editGrid)
            # self.editButton.connect("clicked", self.edit_popover.on_editDropdown_clicked, self.editPopover, self.data.projections[i][self.data.PROJECTIONS_ID], self.entryRows,  self.contentGrid, "projection")
            
            # Style Widgets
            self.entryGrid.set_halign(Gtk.Align.CENTER)
            self.entryGrid.set_hexpand(True)
            self.categoryLabel.set_markup(self.data.projections[i][self.data.PROJECTIONS_TITLE])
            self.categoryLabel.set_property("height-request", 50)
            self.categoryLabel.set_property("xalign", 1)
            self.categoryLabel.set_width_chars(15)
            
            self.dateLabel.set_margin_start(30)
            self.dateLabel.set_margin_end(30)
            self.dateLabel.set_width_chars(15)
            
            self.costGrid.set_row_homogeneous(True)
            self.costLabel.set_property("xalign", .05)
            self.costLabel.set_width_chars(14)
            
            # Style Edit Button
            self.editIcon = Gio.ThemedIcon(name="go-down-symbolic")
            self.editImage = Gtk.Image.new_from_gicon(self.editIcon, Gtk.IconSize.MENU)
            self.editButton.add(self.editImage)
            self.editButton.set_relief(Gtk.ReliefStyle.NONE)
            self.editButton.set_valign(Gtk.Align.START)
            self.editButton.set_opacity(.5)

            # Attach Labels
            self.costGrid.attach(self.currencyLabel, 0,1,1,1)
            self.costGrid.attach(self.costLabel, 1,1,1,1)
            self.entryGrid.attach(self.categoryLabel, 0, 1, 1, 1)
            self.entryGrid.attach(self.dateLabel, 1, 1, 1, 1)
            self.entryGrid.attach(self.costGrid, 2, 0, 1, 2)

            if self.descriptionLabel.get_text() != "":
                self.entryGrid.attach(self.descriptionLabel, 0, 3, 3, 1)
                self.extraSpaceLabel = Gtk.Label()
                self.entryGrid.attach(self.extraSpaceLabel,0, 4, 1, 1)
                self.layoutGrid.attach(self.entryGrid, 0, 0, 1, 5)
            
            # Add Layout Grid to Content Grid. Increment index and apply whitespaces
            else:
                self.layoutGrid.attach(self.entryGrid, 0, 0, 1, 2)
            
            self.layoutGrid.attach(self.editButton, 1, 0, 1, 1)
            self.layoutGrid.set_margin_bottom(25)


            self.transactionViewGrid.attach(self.layoutGrid, 1, self.index, 3, 2)

            self.index = self.index + 2

            self.transactionType = ""
            # for j in range(0, len(self.data.projections)):
            #     if self.data.projections[j][self.data.MENU_ID_INDEX] == self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX]:
            #         self.transactionType = self.data.transactionsMenu[j][self.data.MENU_TYPE_INDEX]
            
            self.entryRows.append([self.layoutGrid, [self.categoryLabel, self.dateLabel, self.currencyLabel, self.costLabel, self.descriptionLabel, self.editButton], self.entryGrid, self.costGrid, self.data.projections[i][self.data.PROJECTIONS_ID]])
            self.transactionViewGrid.show_all() 
       
    def redisplay_info(self):
        self.generate_transactions_view()
        self.add_view_mode(False)
        self.transactionViewGrid.queue_draw()
