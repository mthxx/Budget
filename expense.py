from gi.repository import Gtk, Gio
from sidebar import Sidebar
from data import Data

class Expense():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data()
        self.view = Sidebar() 
        
        self.view.topLeftLabel.set_markup("<b>Total Spent</b>")
        self.view.topMiddleLabel.set_markup("<b>Total Remaining</b>")
        self.view.topRightLabel.set_markup("<b>% of Budget</b>")
        
        self.view.monthTotalLabel.set_text( "$" + str(self.view.sumTotalData(self.data.expenses)))
        
        self.view.generate_sidebars(self.data.expenseMenu)
        self.view.generate_content(self.data.expenses)

        # Add Signal Handling
        self.view.menuListBox.connect("row-activated",self.view.menu_clicked, self.data.expenses, self.data.expenseMenu)
        self.view.subMenuListBox.connect("row-activated",self.view.subMenu_clicked, self.data.expenses, self.data.expenseMenu)
