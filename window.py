from gi.repository import Gtk, Gio
from sidebar import Sidebar

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Budget")
        self.set_default_size(1000, 700)

        
        # --- Header Bar ---
        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.set_titlebar(self.hb)

        # --- Date Range Buttons (Left Side of Header Bar) ---
            
            # Create Buttons
        self.dayButton = Gtk.Button("Day")
        self.weekButton = Gtk.Button("Week")
        self.monthButton = Gtk.Button("Month")
            # Set Size
        self.dayButton.set_size_request(65,32)
        self.weekButton.set_size_request(65,32)
        self.monthButton.set_size_request(65,32)
            # Connect to handler
        self.dayButton.connect("clicked", self.on_dayButton_clicked)
        self.weekButton.connect("clicked", self.on_weekButton_clicked)
        self.monthButton.connect("clicked", self.on_monthButton_clicked)
            # Pack into Box 
        self.rangeBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.rangeBox.get_style_context(), "linked")
        self.rangeBox.add(self.dayButton)
        self.rangeBox.add(self.weekButton)
        self.rangeBox.add(self.monthButton)
        
        # --- Navigation Buttons (Center of Header Bar) ---
            
            # Create Buttons
        self.overviewButton = Gtk.Button("Overview")
        self.incomeButton = Gtk.Button("Income")
        self.expensesButton = Gtk.Button("Expenses")
        self.projectionsButton = Gtk.Button("Projections")
            # Set Size
        self.overviewButton.set_size_request(100,32)
        self.incomeButton.set_size_request(100,32)
        self.expensesButton.set_size_request(100,32)
        self.projectionsButton.set_size_request(100,32)
            # Connect to handler
        self.overviewButton.connect("clicked", self.on_overviewButton_clicked)
        self.incomeButton.connect("clicked", self.on_incomeButton_clicked)
        self.expensesButton.connect("clicked", self.on_expensesButton_clicked)
        self.projectionsButton.connect("clicked", self.on_projectionsButton_clicked)
            # Pack into Box 
        self.navBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.navBox.get_style_context(), "linked")
        self.navBox.add(self.overviewButton)
        self.navBox.add(self.incomeButton)
        self.navBox.add(self.expensesButton)
        self.navBox.add(self.projectionsButton)
        
        # --- Action Buttons (Right of Header Bar) ---
        
            # Create Buttons
        self.addButton = Gtk.Button()
        self.menuButton = Gtk.MenuButton();
            # Add Image
        self.addIcon = Gio.ThemedIcon(name="list-add-symbolic")
        self.menuIcon = Gio.ThemedIcon(name="emblem-system-symbolic")
        self.addImage = Gtk.Image.new_from_gicon(self.addIcon, Gtk.IconSize.MENU)
        self.menuImage = Gtk.Image.new_from_gicon(self.menuIcon, Gtk.IconSize.MENU)
        self.addButton.add(self.addImage)
        self.menuButton.add(self.menuImage)
            # Set Size
        self.addButton.set_size_request(32,32)
        self.menuButton.set_size_request(32,32)
            # Connect to handler
        self.addButton.connect("clicked", self.on_addButton_clicked)
        self.menuButton.connect("clicked", self.on_menuButton_clicked)
        
        # --- Header Bar Packing ---
        self.hb.set_custom_title(self.navBox)
        self.hb.pack_start(self.rangeBox)
        self.hb.pack_end(self.menuButton)
        self.hb.pack_end(self.addButton)

        self.sidebar = Sidebar()
        self.add(self.sidebar.grid) 
    

    def on_dayButton_clicked(self, *args):
        print("Day Button Working!")
    
    def on_weekButton_clicked(self, *args):
        print("Week Button Working!")

    def on_monthButton_clicked(self, *args):
        print("Month Button Working!")

    def on_overviewButton_clicked(self, *args):
        print("Overview Button Working!")

    def on_incomeButton_clicked(self, *args):
        print("Income Button Working!")

    def on_expensesButton_clicked(self, *args):
        print("Expenses Button Working!")
        sidebar = Sidebar()
        self.add(sidebar.grid) 

    def on_projectionsButton_clicked(self, *args):
        print("Projections Button Working!")

    def on_addButton_clicked(self, *args):
        print("Add Button Working!")

    def on_menuButton_clicked(self, *args):
        print("Menu Button Working!")


win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
