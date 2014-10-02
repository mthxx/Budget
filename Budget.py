from gi.repository import Gtk, Gio
from window import Window


class main():

    def __init__(self):
        win = Window()
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()

if __name__=='__main__':
    main()
