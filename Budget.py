from gi.repository import Gtk, Gio
from window import Window
from data import Data

class main():

    def __init__(self):
        self.data = Data()
        self.data.import_data()
        self.win = Window(self.data)
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.show_all()
        Gtk.main()

if __name__=='__main__':
    main()
