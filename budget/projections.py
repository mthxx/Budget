from gi.repository import Gtk, Gio
import datetime, calendar
from edit_mode import Edit_Entry

class Projections():
        
    def __init__(self, data):
        self.data = data
        self.projections = []
        self.defaultLoadOut = 180
        self.grid = Gtk.Grid(name="projectionsGrid")        
        self.entryRows = []
        self.totalSum = 0  
        
        self.currentDay = datetime.datetime.now().day
        self.currentMonth = datetime.datetime.now().month
        self.currentYear = datetime.datetime.now().year

        # Create Grids
        self.sideGrid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
        self.headerGrid = Gtk.Grid(name="headerGrid")
        self.dayViewGrid = Gtk.Grid()
        self.weekViewGrid = Gtk.Grid()
        self.monthViewGrid = Gtk.Grid()
        self.yearViewGrid = Gtk.Grid()
        self.transactionViewGrid = Gtk.Grid( name="transactionViewGrid")
        
        self.gridScrolledWindow = Gtk.ScrolledWindow()
        self.gridViewport = Gtk.Viewport(name="transactionViewport")
        
        # Side Grid Styling 
        self.sideGrid.set_vexpand(True)
        self.sideGrid.set_property("width-request",279)
        
        # Content Grid Styling 
        self.contentGrid.set_hexpand(True)
        self.contentGrid.set_vexpand(True)
        self.contentGrid.set_column_homogeneous(True)
    
        # --- Notebooks ---
        # Style Grids
        self.monthViewGrid.set_column_homogeneous(True)
        self.monthViewGrid.set_margin_start(55)
        self.monthViewGrid.set_margin_end(55)
        self.monthViewGrid.set_margin_bottom(55)

        self.transactionViewGrid.set_hexpand(True)
        self.transactionViewGrid.set_halign(Gtk.Align.FILL)
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
        #self.projectionsNotebook.insert_page(self.dayViewGrid, self.dayLabel,0)
        #self.projectionsNotebook.insert_page(self.weekViewGrid, self.weekLabel,1)
        self.projectionsNotebook.insert_page(self.monthViewGrid, self.monthLabel,2)
        #self.projectionsNotebook.insert_page(self.yearViewGrid, self.yearLabel,3)
        self.projectionsNotebook.set_show_tabs(False)
        
        self.gridScrolledWindow.add(self.gridViewport)
        self.gridViewport.add(self.contentGrid)
 
        self.generate_sidebar()
        self.generate_transactions_view()
        self.generate_month_view()
        self.create_header_grid()

        self.contentGrid.attach(self.headerGrid, 1, 0, 1, 1)
        self.contentGrid.attach(self.projectionsNotebook, 1, 1, 1, 1)
        self.contentGrid.attach(self.transactionViewGrid, 1, 2, 1, 1)
        #self.grid.attach(self.sideGrid,0,0,1,1)
        self.grid.attach(self.gridScrolledWindow,1,0,1,1)

    def active_day_cell(self, dayText, incomeSum, expenseSum, totalSum, incomeLabel, expenseLabel, totalLabel):
        if incomeSum != 0:
            incomeLabel.set_markup("<span foreground=\"green\">" + "+" + str("%0.2f" % (incomeSum,)) + "</span>")
        if expenseSum != 0:
            expenseLabel.set_markup("<span foreground=\"red\">" + "-" + str("%0.2f" % (expenseSum,)) + "</span>")
        if incomeSum != 0 or expenseSum != 0:
            self.totalSum += incomeSum 
            self.totalSum -= expenseSum
            if self.totalSum < 0:
                totalLabel.set_markup("<span foreground=\"red\">" + "=" + str("%0.2f" % (self.totalSum,)) + "</span>")
            if self.totalSum >= 0:
                totalLabel.set_markup("<span foreground=\"green\">" + "=" + str("%0.2f" % (self.totalSum,)) + "</span>")
    
    def add_projection(self, i, startYear, startMonth, startDay):
        self.arr = []
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_TITLE])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_VALUE])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_DESCRIPTION])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_CATEGORY_ID])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_CATEGORY_NAME])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_CATEGORY_TYPE])
        self.arr.append(startYear)
        self.arr.append(startMonth)
        self.arr.append(startDay)
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_END_YEAR])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_END_MONTH])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_END_DAY])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_FREQUENCY])
        self.arr.append(self.data.projections[i][self.data.PROJECTIONS_ID])
        
        self.projections = self.data.sort_projections(self.projections, self.arr)

    def create_header_grid(self):
        self.viewLabel = Gtk.Label("View:")
        self.viewCombo = Gtk.ComboBoxText()
        self.addButton = Gtk.Button("Add Projection")
        
        # Generate Months
        self.viewCombo.append_text("Day")
        self.viewCombo.append_text("Week")
        self.viewCombo.append_text("Month")
        self.viewCombo.append_text("Year")
        
        # Connect to handler    
        self.viewCombo.connect("changed",self.view_selected)
        
        self.viewCombo.set_active(0)

        self.viewLabel.set_margin_start(30)
        self.viewLabel.set_margin_end(5)
        
        self.viewCombo.set_margin_top(10)
        self.viewCombo.set_margin_bottom(10)
        self.viewCombo.set_margin_end(10)
        
        self.addButton.set_margin_start(20)
        self.addButton.set_margin_top(10)
        self.addButton.set_margin_bottom(10)
   
        self.headerGrid.attach(self.viewLabel,0,0,1,1)
        self.headerGrid.attach(self.viewCombo,1,0,1,1)
        self.headerGrid.attach(self.addButton,2,0,1,1)
       
        # Create Widgets
        self.addPopover = Gtk.Popover.new(self.addButton)
        self.addPopoverGrid = Gtk.Grid()
        self.addPopover.add(self.addPopoverGrid)
        self.addButton.connect("clicked", self.on_addButton_clicked)


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
        
        self.frequencyLabel = Gtk.Label("Frequency:")
        self.frequencyComboBoxText = Gtk.ComboBoxText()
            
        self.startDateLabel = Gtk.Label("Date:")
        self.startDate = Gtk.Calendar()
        
        self.neverRadio = Gtk.RadioButton.new_with_label(None, "Never")
        self.selectDateRadio = Gtk.RadioButton.new_with_label(None, "Select Date")
        self.selectDateRadio.join_group(self.neverRadio)

        self.endDateLabel = Gtk.Label("End Date:")
        self.endDate = Gtk.Calendar()

        self.cancelButton = Gtk.Button("Cancel")
        self.submitButton = Gtk.Button("Submit")
            
        # Add data to frequency
        for j in range(0, len(self.data.frequencyMenu)):
            self.frequencyComboBoxText.append_text(self.data.frequencyMenu[j][0])        

        self.transactionAmountEntry.connect("insert-text", self.data.check_amount_value)
        self.frequencyComboBoxText.connect("changed",self.frequency_selected)
        self.selectDateRadio.connect("toggled", self.on_selectDateRadio_toggled)
        
        # Style Widgets
        self.transactionTitleLabel.set_halign(Gtk.Align.END)
        self.transactionTitleLabel.set_margin_start(20)
        self.transactionTitleLabel.set_margin_top(10)
        self.transactionTitleEntry.set_margin_start(20)
        self.transactionTitleEntry.set_margin_top(10)
        self.transactionTitleEntry.set_margin_end(20)
        
        self.transactionAmountLabel.set_halign(Gtk.Align.END)
        self.transactionAmountLabel.set_margin_start(20)
        self.transactionAmountLabel.set_margin_top(10)
        self.transactionAmountEntry.set_margin_start(20)
        self.transactionAmountEntry.set_margin_top(10)
        self.transactionAmountEntry.set_margin_end(20)
        
        self.transactionDescriptionLabel.set_halign(Gtk.Align.END)
        self.transactionDescriptionLabel.set_margin_start(20)
        self.transactionDescriptionLabel.set_margin_top(10)
        self.transactionDescriptionEntry.set_margin_start(20)
        self.transactionDescriptionEntry.set_margin_top(10)
        self.transactionDescriptionEntry.set_margin_end(20)
        
        self.transactionTypeLabel.set_halign(Gtk.Align.END)
        self.transactionTypeLabel.set_margin_start(20)
        self.transactionTypeLabel.set_margin_top(10)
        self.radioBox.set_margin_start(20)
        self.radioBox.set_margin_top(10)
        self.radioBox.set_margin_end(20)
        self.radioBox.set_property("height-request", 34)
        self.addIncomeRadio.set_property("draw-indicator",False)
        self.addExpenseRadio.set_property("draw-indicator",False)
        Gtk.StyleContext.add_class(self.radioBox.get_style_context(), "linked")

        self.addCategoryLabel.set_halign(Gtk.Align.END)
        self.addCategoryLabel.set_margin_start(20)
        self.addCategoryLabel.set_margin_top(10)
        self.addCategoryComboBoxText.set_margin_start(20)
        self.addCategoryComboBoxText.set_margin_top(10)
        self.addCategoryComboBoxText.set_margin_end(20)
        self.addCategoryComboBoxText.set_property("height-request", 34)
        
        self.frequencyLabel.set_halign(Gtk.Align.END)
        self.frequencyLabel.set_margin_start(20)
        self.frequencyLabel.set_margin_top(10)
        self.frequencyComboBoxText.set_margin_start(20)
        self.frequencyComboBoxText.set_margin_top(10)
        self.frequencyComboBoxText.set_margin_end(20)
        self.frequencyComboBoxText.set_property("height-request", 34)
        
        self.startDateLabel.set_halign(Gtk.Align.END)
        self.startDateLabel.set_margin_start(20)
        self.startDateLabel.set_margin_top(10)
        self.startDate.set_margin_start(20)
        self.startDate.set_margin_top(10)
        self.startDate.set_margin_end(20)
        
        self.endDateLabel.set_halign(Gtk.Align.END)
        self.endDateLabel.set_margin_start(20)
        self.endDateLabel.set_margin_top(10)
        
        self.selectDateRadio.set_margin_start(20)
        self.selectDateRadio.set_margin_top(10)
        
        self.neverRadio.set_margin_start(20)
        self.neverRadio.set_margin_top(10)
        self.neverRadio.set_margin_end(20)
        
        self.endDate.set_margin_start(20)
        self.endDate.set_margin_top(10)
        self.endDate.set_margin_end(20)
        
        self.cancelButton.set_margin_start(20)
        self.cancelButton.set_margin_top(30)
        self.cancelButton.set_margin_bottom(20)
        self.submitButton.set_margin_start(20)
        self.submitButton.set_margin_top(30)
        self.submitButton.set_margin_bottom(20)
        self.submitButton.set_margin_end(20)
        
        # Connect Widgets
        self.cancelButton.connect("clicked", self.on_cancelButton_clicked)
        self.submitButton.connect("clicked", self.on_submitButton_clicked)
        self.addIncomeRadio.connect("toggled", self.on_addRadio_toggled)
        
        # Attach Widgets
        if len(self.projections) == 0:
            self.transactionViewGrid.set_halign(Gtk.Align.CENTER)
        else:
            self.transactionViewGrid.set_halign(Gtk.Align.FILL)

        self.addPopoverGrid.attach(self.transactionTitleLabel,1,1,1,1)
        self.addPopoverGrid.attach(self.transactionTitleEntry,2,1,2,1)
        self.addPopoverGrid.attach(self.transactionAmountLabel,1,2,1,1)
        self.addPopoverGrid.attach(self.transactionAmountEntry,2,2,2,1)
        self.addPopoverGrid.attach(self.transactionDescriptionLabel,1,3,1,1)
        self.addPopoverGrid.attach(self.transactionDescriptionEntry,2,3,2,1)
        self.addPopoverGrid.attach(self.transactionTypeLabel,1,4,1,1)
        self.addPopoverGrid.attach(self.radioBox,2,4,2,1)
        self.addPopoverGrid.attach(self.addCategoryLabel,1,5,1,1)
        self.addPopoverGrid.attach(self.addCategoryComboBoxText,2,5,2,1)
        self.addPopoverGrid.attach(self.frequencyLabel,1,6,1,1)
        self.addPopoverGrid.attach(self.frequencyComboBoxText,2,6,2,1)
        self.addPopoverGrid.attach(self.startDateLabel,4,1,1,4)
        self.addPopoverGrid.attach(self.startDate,5,1,2,4)
        self.addPopoverGrid.attach(self.endDateLabel,4,5,1,1)
        self.addPopoverGrid.attach(self.neverRadio,5,5,1,1)
        self.addPopoverGrid.attach(self.selectDateRadio,6,5,1,1)
        self.addPopoverGrid.attach(self.endDate,5,6,2,4)
        self.addPopoverGrid.attach(self.cancelButton,4,10,1,1)
        self.addPopoverGrid.attach(self.submitButton,5,10,2,1)        
    
    def frequency_selected(self, listbox, *args):
        # To catch calls before widget exists.
        if listbox == None:
            return
        else:
            self.row = self.data.frequencyMenu[listbox.get_active()][0]
            if listbox.get_active() == 0:
                self.startDateLabel.set_text("Date:")
                self.endDateLabel.hide()
                self.selectDateRadio.hide()
                self.neverRadio.hide()
                self.endDate.hide()
                self.transactionViewGrid.queue_draw()
            else:
                self.startDateLabel.set_text("Start Date:")
                self.selectDateRadio.show()
                self.neverRadio.show()
                self.endDateLabel.show()
                self.transactionViewGrid.queue_draw()

    def generate_transactions_view(self):
        # Create new array full of projections
        for i in range(0,len(self.data.projections)):
            startYear = self.data.projections[i][self.data.PROJECTIONS_START_YEAR]
            startMonth = self.data.projections[i][self.data.PROJECTIONS_START_MONTH]
            startDay = self.data.projections[i][self.data.PROJECTIONS_START_DAY]
            currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
            
            start = datetime.date(self.data.projections[i][self.data.PROJECTIONS_START_YEAR],
                    self.data.projections[i][self.data.PROJECTIONS_START_MONTH],
                    self.data.projections[i][self.data.PROJECTIONS_START_DAY])
            
            if self.data.projections[i][self.data.PROJECTIONS_END_YEAR] != 0:
                end = datetime.date(self.data.projections[i][self.data.PROJECTIONS_END_YEAR],
                        self.data.projections[i][self.data.PROJECTIONS_END_MONTH],
                        self.data.projections[i][self.data.PROJECTIONS_END_DAY])
                days = (end-start).days
                if days > self.defaultLoadOut:
                    days = self.defaultLoadOut
            else:
                days = self.defaultLoadOut
            
            # Create Daily Projections
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "One Time":
                self.add_projection(i, startYear, startMonth, startDay)
           
            # Create Daily Projections
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "Daily":
                for j in range(days):
                    self.add_projection(i, startYear, startMonth, startDay)
                    if startDay >= currentMonthEndDate:
                        startDay = 1
                        if startMonth == 12:
                            startMonth = 1
                            startYear += 1
                        else:
                            startMonth += 1
                        currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
                    startDay += 1
            
            # Create Weekly Projections
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "Weekly":
                dayOfWeek = datetime.datetime(startYear, startMonth, startDay).weekday()
                for j in range(days):
                    if dayOfWeek == datetime.datetime(startYear, startMonth, startDay).weekday():
                        self.add_projection(i, startYear, startMonth, startDay)
                    if startDay >= currentMonthEndDate:
                        startDay = 1
                        if startMonth == 12:
                            startMonth = 1
                            startYear += 1
                        else:
                            startMonth += 1
                        currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
                    startDay += 1
            
            # Create Bi-Weekly Projections
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "Bi-Weekly":
                dayOfWeek = datetime.datetime(startYear, startMonth, startDay).weekday()
                self.flag = True;
                for j in range(days):
                    if dayOfWeek == datetime.datetime(startYear, startMonth, startDay).weekday():
                        if self.flag == True:
                            self.add_projection(i, startYear, startMonth, startDay)
                            self.flag = False
                        else:
                            self.flag = True
                    if startDay >= currentMonthEndDate:
                        startDay = 1
                        if startMonth == 12:
                            startMonth = 1
                            startYear += 1
                        else:
                            startMonth += 1
                        currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
                    startDay += 1
            
            # Create Monthly On Date Projections
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "Monthly on Date":
                recurringDate = startDay
                for j in range(days):
                    if startDay == recurringDate:
                        self.add_projection(i, startYear, startMonth, startDay)
                    if startDay >= currentMonthEndDate:
                        startDay = 1
                        if startMonth == 12:
                            startMonth = 1
                            startYear += 1
                        else:
                            startMonth += 1
                        currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
                    startDay += 1
                        
            # Create Monthly on Weekday
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "Monthly on Weekday":
                dayOfWeek = datetime.datetime(startYear, startMonth, startDay).weekday()
                self.count = 0;
                for j in range(days):
                    if dayOfWeek == datetime.datetime(startYear, startMonth, startDay).weekday():
                        if self.count == 0:
                            self.add_projection(i, startYear, startMonth, startDay)
                            self.count += 1
                        elif self.count != 3:
                            self.count += 1
                        elif self.count == 3:
                            self.count = 0;
                    if startDay >= currentMonthEndDate:
                        startDay = 1
                        if startMonth == 12:
                            startMonth = 1
                            startYear += 1
                        else:
                            startMonth += 1
                        currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
                    startDay += 1
            
            # Create Monthly on Weekday
            if self.data.projections[i][self.data.PROJECTIONS_FREQUENCY] == "Yearly":
                dayOfWeek = datetime.datetime(startYear, startMonth, startDay).weekday()
                self.recurringYear = startYear
                self.recurringMonth = startMonth
                self.recurringDay = startDay
                for j in range(days):
                    if self.recurringMonth == startMonth and self.recurringDay == startDay:
                            self.add_projection(i, startYear, startMonth, startDay)
                    if startDay >= currentMonthEndDate:
                        startDay = 1
                        if startMonth == 12:
                            startMonth = 1
                            startYear += 1
                        else:
                            startMonth += 1
                        currentMonthEndDate = calendar.monthrange(startYear, startMonth)[1] 
                    startDay += 1

        # Code from transactions.py
        while len(self.transactionViewGrid) > 0:
            self.transactionViewGrid.remove_row(0)
            
        while len(self.entryRows) > 0:
                self.entryRows.pop(0)
        self.index = 10
        self.count = 0
        for i in reversed(range(0,len(self.projections))):
            if self.projections[i][6] >= self.currentYear:
                if self.projections[i][7] >= self.currentMonth:
                    if self.projections[i][8] >= self.currentDay:
                        # Date String
                        self.dateString = [self.projections[i][self.data.PROJECTIONS_START_YEAR],self.projections[i][self.data.PROJECTIONS_START_MONTH] - 1,self.projections[i][self.data.PROJECTIONS_START_DAY]]
                        self.dateString = self.data.translate_date(self.dateString, "edit")
                        
                        self.layoutGrid = Gtk.Grid(name="layoutGrid")
                        self.entryGrid = Gtk.Grid()
                        self.costGrid = Gtk.Grid()
                 
                        self.titleLabel = Gtk.Label()
                        self.categoryLabel = Gtk.Label()
                        self.dateLabel = Gtk.Label(self.dateString)
                        self.descriptionLabel = Gtk.Label()
                        
                        self.currencyLabel = Gtk.Label("$")
                        self.costLabel = Gtk.Label()
                        
                        self.costLabel.set_markup("<span foreground=\"green\">" + str(self.projections[i][self.data.PROJECTIONS_VALUE]) + "</span>")
                       
                        self.titleLabel.set_markup("<b>" + self.projections[i][self.data.PROJECTIONS_TITLE] + "</b>")
                        self.descriptionLabel.set_markup("<i>" + self.projections[i][self.data.PROJECTIONS_DESCRIPTION] + "</i>")
                        self.categoryLabel.set_markup(self.projections[i][self.data.PROJECTIONS_CATEGORY_NAME])
                        
                        # Create Edit Popover
                        self.editButton = Gtk.Button()
                        self.editView = Gtk.Popover.new(self.editButton)
                        self.edit_view = Edit_Entry(self.data, "projection")
                        self.editView.add(self.edit_view.editGrid)
                        
                        # Style Widgets
                        self.entryGrid.set_halign(Gtk.Align.CENTER)
                        self.entryGrid.set_hexpand(True)
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
                        
                        self.entryGrid.attach(self.titleLabel, 0, 0, 3, 1)
                        self.entryGrid.attach(self.categoryLabel, 0, 2, 1, 1)
                        self.entryGrid.attach(self.dateLabel, 1, 2, 1, 1)
                        self.entryGrid.attach(self.costGrid, 2, 1, 1, 2)

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


                        self.transactionViewGrid.attach(self.layoutGrid, 1, self.index, 4, 2)

                        self.index = self.index + 2

                        self.transactionType = ""
                        
                        self.entryRows.append([self.layoutGrid, [self.categoryLabel, self.dateLabel, self.currencyLabel, self.costLabel, self.descriptionLabel, self.editButton, self.titleLabel], self.entryGrid, self.costGrid, self.projections[i][self.data.PROJECTIONS_ID]])
                        self.editButton.connect("clicked", self.edit_view.on_editDropdown_clicked, self.editView, self.projections[i][self.data.PROJECTIONS_ID], self.entryRows[self.count],  self.transactionViewGrid, self.projections[i])
                        self.count += 1
                        self.transactionViewGrid.show_all() 
 
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
         
        self.selectedMonth = self.currentMonth
        self.selectedYear = self.currentYear

        self.currentMonthStartDate = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[0]
        self.currentMonthEndDate = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1] 

        self.populate_month_grid(self.currentMonth, self.currentYear, self.currentMonthStartDate, self.currentMonthEndDate)

    def generate_sidebar(self):
        return
 
    def inactive_day_cell(self, dayText, incomeSum, expenseSum, totalSum, incomeLabel, expenseLabel, totalLabel):
        if incomeSum != 0:
            incomeLabel.set_markup("<span foreground=\"gray\">" + "+" + str("%0.2f" % (incomeSum,)) + "</span>")
        if expenseSum != 0:
            expenseLabel.set_markup("<span foreground=\"gray\">" + "-" + str("%0.2f" % (expenseSum,)) + "</span>")

    def on_addButton_clicked(self, *args):
        if self.addPopover.get_visible():
            self.addPopover.hide()
        else:
            self.reset_fields()
            self.addPopover.show_all()
            self.neverRadio.hide()
            self.selectDateRadio.hide()
            self.endDateLabel.hide()
            self.endDate.hide()
        
    def on_submitButton_clicked(self, *args):
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
        
        if (self.transactionTitleEntry.get_text() != "" 
            and self.transactionAmountEntry.get_text() != "" 
            and self.addCategoryComboBoxText.get_active() >= 0 
            and self.frequencyComboBoxText.get_active() >= 0):
            
            self.dateArr = self.startDate.get_date()
            self.startYear = str(self.dateArr[0])
            self.startMonth = str(self.dateArr[1] + 1)
            self.startDay = str(self.dateArr[2])
            
            if self.frequencyComboBoxText.get_active() == 0:
                self.dateArr = self.startDate.get_date()
                self.endYear = str(self.dateArr[0])
                self.endMonth = str(self.dateArr[1] + 1)
                self.endDay = str(self.dateArr[2])
            else:
                if self.selectDateRadio.get_active() == True:
                    self.dateArr = self.endDate.get_date()
                    self.endYear = str(self.dateArr[0])
                    self.endMonth = str(self.dateArr[1] + 1)
                    self.endDay = str(self.dateArr[2])
                elif self.neverRadio.get_active() == True:
                    self.endYear = str(0)
                    self.endMonth = str(0)
                    self.endDay = str(0)
            
            if self.addIncomeRadio.get_active() == True:
                self.selected = "income"
            elif self.addExpenseRadio.get_active() == True:
                self.selected = "expense"

            self.data.LATEST_PROJECTION_ID += 1
            
            self.data.add_projection(self.transactionTitleEntry.get_text(),
                self.transactionAmountEntry.get_text(), self.transactionDescriptionEntry.get_text(),
                self.selected, self.addCategoryComboBoxText.get_active(), self.startYear, self.startMonth, self.startDay, 
                self.endYear, self.endMonth, self.endDay, self.frequencyComboBoxText.get_active(), self.data.LATEST_PROJECTION_ID)
            
            self.reset_fields()
            self.addPopover.hide()

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
        if self.addPopover.get_visible():
            self.addPopover.hide()
        else:
            self.addPopover.show_all()

    def on_selectDateRadio_toggled(self, *args):
        if self.selectDateRadio.get_active() == True:
            self.endDate.show()
            self.frequencyLabel.set_margin_bottom(103)
            self.frequencyComboBoxText.set_margin_bottom(103)
            self.transactionViewGrid.queue_draw()
        if self.neverRadio.get_active() == True:
            self.endDate.hide()
            self.frequencyLabel.set_margin_bottom(0)
            self.frequencyComboBoxText.set_margin_bottom(0)
            self.transactionViewGrid.queue_draw()
    
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

        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.data.incomeMenu)):
                if self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == self.data.incomeMenu[j]:
                    self.totalSum += self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]
       
        for i in range(0, len(self.data.transactions)):
            for j in range(0, len(self.data.expenseMenu)):
                if self.data.transactions[i][self.data.TRANSACTION_MENU_INDEX][self.data.TRANSACTION_MENU_ID_INDEX] == self.data.expenseMenu[j]:
                    self.totalSum -= self.data.transactions[i][self.data.TRANSACTION_VALUE_INDEX]

        for i in range(1, 43):
            # Create Widgets 
            if i - 2 >= start and self.dayText <= end:
                if self.selectedYear == self.currentYear and self.selectedMonth == self.currentMonth and int(self.dayText) == self.currentDay:
                    if i == 7 or i == 14 or i == 21 or i == 28 or i == 35:
                        self.monthGrid = Gtk.Grid(name="monthGridRightCurrent")
                    elif i > 35 and i < 42:
                        self.monthGrid = Gtk.Grid(name="monthGridBottomCurrent")
                    elif i == 42:
                        self.monthGrid = Gtk.Grid(name="monthGridLastCurrent")
                    else:            
                        self.monthGrid = Gtk.Grid(name="monthGridCurrent")
                else:
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
                
                self.incomeSum = 0
                self.expenseSum = 0

                for j in range(0,len(self.projections)):
                    if self.projections[j][self.data.PROJECTIONS_START_YEAR] == self.selectedYear:
                        if self.projections[j][self.data.PROJECTIONS_START_MONTH] == self.selectedMonth:
                            if self.projections[j][self.data.PROJECTIONS_START_DAY] == self.dayText - 1:
                                if self.projections[j][self.data.PROJECTIONS_CATEGORY_TYPE] == 0:
                                    self.incomeSum += self.projections[j][self.data.PROJECTIONS_VALUE]
                                if self.projections[j][self.data.PROJECTIONS_CATEGORY_TYPE] == 1:
                                    self.expenseSum += self.projections[j][self.data.PROJECTIONS_VALUE]
                
                if self.currentYear == self.selectedYear:
                    if self.currentMonth == self.selectedMonth:
                        if int(self.dayText) >= self.currentDay:
                            self.active_day_cell(self.dayText, self.incomeSum, self.expenseSum, self.totalSum, self.incomeLabel, self.expenseLabel, self.totalLabel)
                        elif int(self.dayText) < self.currentDay:
                            self.inactive_day_cell(self.dayText, self.incomeSum, self.expenseSum, self.totalSum, self.incomeLabel, self.expenseLabel, self.totalLabel)
                    if self.currentMonth < self.selectedMonth:                
                        self.active_day_cell(self.dayText, self.incomeSum, self.expenseSum, self.totalSum, self.incomeLabel, self.expenseLabel, self.totalLabel)
                    elif self.currentMonth > self.selectedMonth:                
                        self.inactive_day_cell(self.dayText, self.incomeSum, self.expenseSum, self.totalSum, self.incomeLabel, self.expenseLabel, self.totalLabel)
                elif self.currentYear < self.selectedYear: 
                    self.active_day_cell(self.dayText, self.incomeSum, self.expenseSum, self.totalSum, self.incomeLabel, self.expenseLabel, self.totalLabel)
                elif self.currentYear > self.selectedYear:
                    self.inactive_day_cell(self.dayText, self.incomeSum, self.expenseSum, self.totalSum, self.incomeLabel, self.expenseLabel, self.totalLabel)

                self.monthGrid.attach(self.dayLabel,0,0,1,1)
                self.monthGrid.attach(self.incomeLabel,0,1,1,1)
                self.monthGrid.attach(self.expenseLabel,0,2,1,1)            
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
            #self.monthCalendarGrid.set_vexpand(True)
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
    
    def redisplay_info(self):
        self.projections = []
        self.generate_transactions_view()
        self.populate_month_grid(self.currentMonth, self.currentYear, self.currentMonthStartDate, self.currentMonthEndDate)
        self.transactionViewGrid.queue_draw()
        
    def reset_fields(self):
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
        
        # Reset fields to default
        self.transactionTitleEntry.set_text("")
        self.transactionAmountEntry.set_text("")
        self.transactionDescriptionEntry.set_text("")
        self.addIncomeRadio.set_active(True)
        self.addCategoryComboBoxText.set_active(-1)
        self.frequencyComboBoxText.set_active(-1)
        self.startDateLabel.set_text("Date:")
        self.startDate.select_month(self.currentMonth - 1, self.currentYear)
        self.startDate.select_day(self.currentDay)
        self.neverRadio.set_active(True)
        self.endDate.select_month(self.currentMonth - 1, self.currentYear)
        self.endDate.select_day(self.currentDay)
        
    
    def view_selected(self, listbox, *args):
        self.projectionsNotebook.set_current_page(listbox.get_active())
        
        
