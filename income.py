from gi.repository import Gtk, Gio, Gdk
from sidebar import Sidebar
from data import Data

class Income():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data() 
        self.view = Sidebar() 
        self.index = 3
        
        self.view.topLeftLabel.set_markup("<b>All Income</b>")
        self.view.topMiddleLabel.set_markup("<b>All Remaining</b>")
        self.view.topRightLabel.set_markup("<b>% Remaining</b>")
        
        #Build Content Area
        for i in range (0,len(self.data.income)):
            
            self.layoutGrid = Gtk.Grid(name="layoutGrid")
            self.layoutGrid.set_column_homogeneous(True)
            self.layoutGrid.set_hexpand(True)
            
            self.whiteSpaceLabel = Gtk.Label()
            self.index = self.index + 2
            self.view.contentGrid.attach(self.whiteSpaceLabel,0, self.index, 5, 1)
            self.index = self.index + 3
            
            self.dateString = ""
            self.dateString = Data.translate_date(self.dateString,self.data.income, i)

            self.categoryLabel = Gtk.Label()
            self.categoryLabel.set_markup("<b>" + self.data.income[i][0][1] + "</b>")
            self.dateLabel = Gtk.Label(self.dateString)
            self.costLabel = Gtk.Label("$" + self.data.income[i][2])
            self.descriptionLabel = Gtk.Label(self.data.income[i][3])
            #self.whiteSpaceLabel = Gtk.Label()
            
            self.costLabel.set_property("height-request", 35)
            
            #self.layoutGrid.attach(self.whiteSpaceLabel,0, 1, 3, 1)
            self.layoutGrid.attach(self.categoryLabel, 0, 1, 1, 1)
            self.layoutGrid.attach(self.dateLabel, 1, 1, 1, 1)
            self.layoutGrid.attach(self.costLabel, 2, 1, 1, 1)
            
            if self.descriptionLabel.get_text() != "":
                self.layoutGrid.attach(self.descriptionLabel, 0, 3, 3, 1)
                self.whiteSpaceLabel = Gtk.Label()
                self.layoutGrid.attach(self.whiteSpaceLabel,0, 4, 3, 1)

            self.layoutGrid.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1, 1, 1, 1))
            self.view.contentGrid.attach(self.layoutGrid, 1, self.index, 3, 2)
            self.view.entryRows.append([self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel])
        
        #for i in range (0,len(self.data.income)):
        #    self.dateString = ""
        #    self.dateString = Data.translate_date(self.dateString,self.data.income, i)
#
#            self.categoryLabel = Gtk.Label(self.data.income[i][0][1])
#            self.dateLabel = Gtk.Label(self.dateString)
#            self.costLabel = Gtk.Label("$" + self.data.income[i][2])
#            self.descriptionLabel = Gtk.Label(self.data.income[i][3])
#            
#            self.costLabel.set_property("height-request", 35)
#            
#            self.view.contentGrid.attach(self.categoryLabel, self.view.categoryOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
#            self.view.contentGrid.attach(self.dateLabel, self.view.dateOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
#            self.view.contentGrid.attach(self.costLabel, self.view.costOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
#            self.view.contentGrid.attach(self.descriptionLabel, self.view.descriptionOffsetLeft, self.view.entryOffsetTop + i, 1, 1)
#            
#            self.view.entryRows.append([self.categoryLabel,self.dateLabel,self.costLabel,self.descriptionLabel])
        
        # Build Sidebars
        for i in range(0,len(self.data.incomeMenu)):
            self.label = Gtk.Label(self.data.incomeMenu[i][1])
            self.label.set_property("height-request", 60)
            self.view.menuListBox.add(self.label)
        
        for i in range(0,len(self.data.currentMonthMenu)):
            self.label = Gtk.Label(self.data.currentMonthMenu[i][1])
            self.label.set_property("height-request", 60)
            self.view.subMenuListBox.add(self.label)
        
        # Add Signal Handling
        self.view.menuListBox.connect("row-activated",self.view.menu_clicked, self.data.income, self.data.incomeMenu)
        self.view.subMenuListBox.connect("row-activated",self.view.subMenu_clicked, self.data.income, self.data.incomeMenu)
