from gi.repository import Gtk, Gio
from basic import Basic

class Projections():

    def __init__(self):
      self.view = Basic() 

    def open_view(window, sidebar):
        window.add(sidebar.grid)


