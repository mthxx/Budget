from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Income():

    def __init__(self):
        values = ['Income 1','Income 2','Income 3','Income 4','Income 5']
        self.view = Sidebar(values) 

    def open_view(window, sidebar):
        window.add(sidebar.grid)
