from gi.repository import Gtk, Gio
from sidebar import Sidebar
from calc import Calc

class Expense():

    def __init__(self, data):
        # Define Sidebar Menu
        self.data = data
        self.calc = Calc(self.data)
        self.view = Sidebar(self.data, "expense") 
        
        self.view.generate_sidebars(self.data.expenseMenu)
        self.view.display_content(self.data.expenses, self.data.expenseMenu)
        
        # Add Signal Handling
        self.view.menuListBox.connect("row-selected",self.view.menu_clicked, self.data.expenses, self.data.expenseMenu)
        self.view.subMenuListBox.connect("row-selected",self.view.subMenu_clicked, self.data.expenses, self.data.expenseMenu)
