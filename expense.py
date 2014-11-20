from gi.repository import Gtk, Gio
from sidebar import Sidebar
from calc import Calc

class Expense():

    def __init__(self, data):
        # Define Sidebar Menu
        self.data = data
        self.calc = Calc(self.data)
        self.view = Sidebar(self.data) 
        
        self.view.monthTotalLabel.set_text( "$" + str(self.calc.sumTotalData(self.data.expenses)))
        
        self.view.generate_sidebars(self.data.expenseMenu)
        self.view.display_content(self.data.expenses)
        self.view.generate_add_popover("expense")
        
        # Add Signal Handling
        self.view.menuListBox.connect("row-activated",self.view.menu_clicked, self.data.expenses, self.data.expenseMenu)
        self.view.subMenuListBox.connect("row-activated",self.view.subMenu_clicked, self.data.expenses, self.data.expenseMenu)
