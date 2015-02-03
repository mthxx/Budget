from gi.repository import Gtk, Gio
import datetime, calendar

class Projections():
        
    def __init__(self):
        self.grid = Gtk.Grid(name="projectionsGrid")
        
        self.sideGrid = Gtk.Grid()
        self.contentGrid = Gtk.Grid()
        
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

        self.grid.attach(self.sideGrid, 0, 0, 1, 1)
        self.grid.attach(self.contentGrid, 1, 0, 1, 1)

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

                # self.expenseLabel = Gtk.Label()
                # self.incomeLabel = Gtk.Label()
                # self.totalLabel = Gtk.Label()
                #
                # self.expenseLabel.set_markup("<span foreground=\"red\">" + "-" + "$125" + "</span>")
                # self.incomeLabel.set_markup("<span foreground=\"green\">" + "+" + "$600" + "</span>")
                # self.totalLabel.set_markup("<span foreground=\"green\">" + "=" + "$1250" + "</span>")
                #
                self.monthGrid.attach(self.dayLabel,0,0,1,1)
                # self.monthGrid.attach(self.expenseLabel,0,1,1,1)            
                # self.monthGrid.attach(self.incomeLabel,0,2,1,1)
                # self.monthGrid.attach(self.totalLabel,0,3,1,1)

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
