from gi.repository import Gtk, Gio, Gdk
from sidebar import Sidebar
from data import Data
from calc import Calc

class Income():

    def __init__(self):
        # Define Sidebar Menu
        self.data = Data() 
        self.calc = Calc()
        self.view = Sidebar() 

        self.view.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(self.data.income)))

        self.view.generate_sidebars(self.data.incomeMenu)
        self.view.generate_content(self.data.income)
        self.view.generate_add_popover("income")

        # Add Signal Handling
        self.view.menuListBox.connect("row-activated",self.view.menu_clicked, self.data.income, self.data.incomeMenu)
        self.view.subMenuListBox.connect("row-activated",self.view.subMenu_clicked, self.data.income, self.data.incomeMenu)
