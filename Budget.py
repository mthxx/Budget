from gi.repository import Gtk, Gio, Gdk
from window import Window
from data import Data

class main():

    def __init__(self):
        self.data = Data()
        self.data.import_data()
        self.win = Window(self.data)
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.show_all()
        self.win.connect('key-press-event', self.on_key_function)
        Gtk.main()

    def on_key_function(self, wodget, event):
        if Gdk.ModifierType.CONTROL_MASK & event.state:# & event.keyval == 113:
            if event.keyval == 113:
                Gtk.main_quit()

if __name__=='__main__':
    main()
