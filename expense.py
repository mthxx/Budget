from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Expense():

    def __init__(self):
        values = ['Rent','Monthly Bills','Insurance','Credit/Loans','Auto','Grocery','Restaurant','Media','Activities','Medical','Pet','Athletics','Donations','Gifts','Home Improvement','Technology','Travel','Clothing','Misc. Expenses','Wedding']
        self.view = Sidebar(values) 

    def open_view(window, sidebar):
        window.add(sidebar.grid)
