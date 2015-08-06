from gi.repository import Gtk, Gio, Gdk

class Menu_Popover(Gtk.Window):
    
    def __init__(self):
        self.menuGrid = Gtk.Grid()
        self.aboutButton = Gtk.Button("About")


        self.aboutButton.set_relief(Gtk.ReliefStyle.NONE)
        self.aboutButton.set_margin_left(10)
        self.aboutButton.set_margin_right(10)
        
        self.menuGrid.attach(self.aboutButton,0,0,1,1)
    
    
    
    def on_menuButton_clicked(self, button, menuPopover):
        if menuPopover.get_visible():
            menuPopover.hide()
        else:
            menuPopover.show_all()
