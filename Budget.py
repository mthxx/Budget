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
        
        self.win.hbLeft.hide()
        for i in range(0, len(self.win.transactions.menuListBox) - 1):
            if (self.win.transactions.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.win.transactions.transactionsLabel 
                and self.win.transactions.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.win.transactions.incomeLabel
                and self.win.transactions.menuListBox.get_row_at_index(i).get_child().get_children()[0] != self.win.transactions.expenseLabel):
                
                self.win.transactions.menuListBox.get_row_at_index(i).get_child().get_children()[2].hide()
        
        self.win.connect('key-press-event', self.on_key_function)
        self.win.set_icon_from_file("logo.png")
        Gtk.main()

    def on_key_function(self, widget, event):
        # If ctrl is pressed
        if Gdk.ModifierType.CONTROL_MASK & event.state:
            # ctrl+q to quit
            if event.keyval == 113:
                Gtk.main_quit()

if __name__=='__main__':
    main()
