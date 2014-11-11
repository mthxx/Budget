from gi.repository import Gtk, Gio
from sidebar import Sidebar
from data import Data
from calc import Calc

class Expense():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data()
        self.calc = Calc()
        self.view = Sidebar() 
        
        self.view.monthTotalLabel.set_text( "$" + str(self.calc.sumTotalData(self.data.expenses)))
        
        self.view.generate_sidebars(self.data.expenseMenu)
        self.view.generate_content(self.data.expenses)
        self.view.generate_add_popover(self.data.expenseMenu)
        
        # Connect Button Handlers
        self.view.addEntryButton.connect("clicked", self.view.add_entry)

        # Add Signal Handling
        self.view.menuListBox.connect("row-activated",self.view.menu_clicked, self.data.expenses, self.data.expenseMenu)
        self.view.subMenuListBox.connect("row-activated",self.view.subMenu_clicked, self.data.expenses, self.data.expenseMenu)
