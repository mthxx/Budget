from gi.repository import Gtk, Gio, Gdk
from window import Window
from data import Data
import os.path

class main():

    def __init__(self):
        # If a database file doesn't exist, create one
        # This should run only on the first launch of the application
        if(os.path.isfile('database.txt')) == False:
            uncategorizedIncomeString = "menu,income,Uncategorized,-1\n"
            uncategorizedExpenseString = "menu,expense,Uncategorized,-2\n"
            
            f = open('database.txt', 'w')
            f.write(uncategorizedIncomeString)
            f.write(uncategorizedExpenseString)
            f.close()

        self.data = Data()
        self.data.import_data()
        self.win = Window(self.data)
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.show_all()
        
        self.win.hbLeft.hide()

        for i in range(0, len(self.win.transactions.menuListBox)):
            if self.win.transactions.editable_category(i):
                self.win.transactions.category_view_mode(i)
        
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
