from gi.repository import Gtk, Gio, Gdk
from overview import Overview
from transactions import Transactions
from reports import Reports
from projections import Projections
from add_popover import Add_Popover

class Window(Gtk.Window):

    def __init__(self, data):
        self.data = data 
        self.provider = Gtk.CssProvider()
        self.provider.load_from_path("style.css")
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        Gtk.Window.__init__(self, title="Budget")
        self.set_default_size(1000, 700)
        
        # Initialize Views
        self.overview = Overview(self.data)
        self.transactions = Transactions(self.data)
        self.reports = Reports()
        self.projections = Projections(self.data)

        # --- Header Bar ---
        # Create Header Bar
        self.headerBox = Gtk.Box(name="headerBox")
        self.hb = Gtk.HeaderBar(name="hb")
       
        # Style Header Bar
        self.hb.set_show_close_button(True)
        self.hb.set_hexpand(True)

        self.headerBox.add(self.hb)
        self.set_titlebar(self.headerBox)

        # --- Navigation Buttons ---
        # Create Navigation Buttons
        self.overviewButton = Gtk.Button("Overview")
        self.transactionsButton = Gtk.Button("Transactions")
        self.projectionsButton = Gtk.Button("Projections")
        self.navBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        # Style Navigation Buttons
        self.overviewButton.set_size_request(100,32)
        self.transactionsButton.set_size_request(100,32)
        self.projectionsButton.set_size_request(100,32)
        Gtk.StyleContext.add_class(self.navBox.get_style_context(), "linked")

        # Connect Buttons to handler
        self.overviewButton.connect("clicked", self.on_overviewButton_clicked)
        self.transactionsButton.connect("clicked", self.on_transactionsButton_clicked)
        self.projectionsButton.connect("clicked", self.on_projectionsButton_clicked)

        # Add Buttons to Navigation Box
        self.navBox.add(self.overviewButton)
        self.navBox.add(self.transactionsButton)
        self.navBox.add(self.projectionsButton)
        self.hb.set_custom_title(self.navBox)
        
        # --- Action Buttons ---
        # Create Widgets
        self.addButton = Gtk.Button()
        self.menuButton = Gtk.MenuButton();
        
        self.addPopover = Gtk.Popover.new(self.addButton)
        self.add_popover = Add_Popover(self.data)
        self.addPopover.add(self.add_popover.addGrid)
       
        # Add Images
        self.addIcon = Gio.ThemedIcon(name="list-add-symbolic")
        self.menuIcon = Gio.ThemedIcon(name="open-menu-symbolic")
        self.addImage = Gtk.Image.new_from_gicon(self.addIcon, Gtk.IconSize.MENU)
        self.menuImage = Gtk.Image.new_from_gicon(self.menuIcon, Gtk.IconSize.MENU)
        self.addButton.add(self.addImage)
        self.menuButton.add(self.menuImage)
       
        # Style Action Buttons
        self.addButton.set_size_request(32,32)
        self.menuButton.set_size_request(32,32)
        
        # Connect to handler
        self.addButton.connect("clicked", self.add_popover.on_addButton_clicked, self.addPopover)
        self.menuButton.connect("clicked", self.on_menuButton_clicked)
        
        # Pack Header Bar 
        self.hb.pack_end(self.menuButton)
        self.hb.pack_end(self.addButton)
        
        # --- Notebooks ---
        # Create Labels
        self.overviewLabel = Gtk.Label("Overview")
        self.transactionsLabel = Gtk.Label("Transactions")
        self.projectionsLabel = Gtk.Label("Projections")

        # Style Notebook 
        self.overviewLabel.set_hexpand(True)
        self.transactionsLabel.set_hexpand(True)
        self.projectionsLabel.set_hexpand(True)
       
        # Create Notebook
        self.notebook = Gtk.Notebook()
        self.notebook.insert_page(self.overview.grid, self.overviewLabel, 0)
        self.notebook.insert_page(self.transactions.grid, self.transactionsLabel, 1)
        self.notebook.insert_page(self.projections.grid, self.projectionsLabel, 3)
        self.add(self.notebook)
        self.notebook.set_show_tabs(False)
        
        # Connect to handler
        # self.notebook.connect("switch-page", self.on_notebook_switch)
      
        # Connect views to data
        self.data.connect_data_views(self.transactions, self.overview)
    
    def on_addButton_clicked(self, *args):
        if self.addPopover.get_visible():
            self.addPopover.hide()
        else:
            self.addPopover.show_all()
    
    def on_menuButton_clicked(self, *args):
        print("Menu Button Working!")

    # def on_notebook_switch(self, notebook, page, index, *args):
    #     if index == 0:
    #         self.hb.queue_draw()
    #     if index == 1:
    #         self.hb.queue_draw()
    #     if index == 2:
    #         self.hb.queue_draw()
    #     if index == 3:
    #         self.hb.queue_draw()
    #     if index == 4:
    #         self.hb.queue_draw()

    def on_overviewButton_clicked(self, *args):
        self.notebook.set_current_page(0)
     
    def on_transactionsButton_clicked(self, *args):
        self.notebook.set_current_page(1)
    
    def on_projectionsButton_clicked(self, *args):
        self.notebook.set_current_page(2)
