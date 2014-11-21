from gi.repository import Gtk, Gio, Gdk
from sidebar import Sidebar
from calc import Calc

class Income():

    def __init__(self, data):
        # Define Sidebar Menu
        self.data = data 
        self.calc = Calc(self.data)
        self.view = Sidebar(self.data) 

        self.view.monthTotalLabel.set_text("$" + str(self.calc.sumTotalData(self.data.income)))

        self.view.generate_sidebars(self.data.incomeMenu)
        self.view.display_content(self.data.income)

        # Add Signal Handling
        self.view.menuListBox.connect("row-activated",self.view.menu_clicked, self.data.income, self.data.incomeMenu)
        self.view.subMenuListBox.connect("row-activated",self.view.subMenu_clicked, self.data.income, self.data.incomeMenu)
