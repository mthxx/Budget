from gi.repository import Gtk, Gio

class Projections():
        
    def __init__(self):
        self.grid = Gtk.Grid()

    def open_view(window, sidebar):
        window.add(sidebar.grid)


