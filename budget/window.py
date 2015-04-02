from gi.repository import Gtk, Gio, Gdk
from overview import Overview
from transactions import Transactions
from projections import Projections
from add_popover import Add_Entry_Popover

class Window(Gtk.Window):

    def __init__(self, data):
        self.data = data 
        self.provider = Gtk.CssProvider()
        self.provider.load_from_path("style.css")
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        Gtk.Window.__init__(self, title="Budget")
        self.set_default_size(500, 500)
        
        # Initialize Views
        self.overview = Overview(self.data)
        self.transactions = Transactions(self.data)
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
        self.overviewRadio = Gtk.RadioButton.new_with_label(None, "Overview")
        self.transactionsRadio = Gtk.RadioButton.new_with_label(None, "Transactions")
        self.projectionsRadio = Gtk.RadioButton.new_with_label(None, "Projections")
        
        self.transactionsRadio.join_group(self.overviewRadio)
        self.projectionsRadio.join_group(self.overviewRadio)
        
        self.radioNavBox = Gtk.Box(Gtk.Orientation.HORIZONTAL,1)
        #self.radioNavBox.pack_start(self.overviewRadio, True, True, 0)
        self.radioNavBox.pack_start(self.transactionsRadio, True, True, 0)
        self.radioNavBox.pack_start(self.projectionsRadio, True, True, 0)
        
        # Style Navigation Buttons
        self.radioNavBox.set_homogeneous(True)
        self.radioNavBox.set_property("height-request", 32)
        #self.overviewRadio.set_property("draw-indicator",False)
        self.transactionsRadio.set_property("draw-indicator",False)
        self.projectionsRadio.set_property("draw-indicator",False)
        Gtk.StyleContext.add_class(self.radioNavBox.get_style_context(), "linked")

        # Connect Radio Buttons to handler
        #self.overviewRadio.connect("toggled", self.on_navRadio_toggled)
        self.transactionsRadio.connect("toggled", self.on_navRadio_toggled)
        self.projectionsRadio.connect("toggled", self.on_navRadio_toggled)
        
        self.radioStatus = "transactions"

        # Add Navigation Radio Buttons to Navigation Box
        self.hb.set_custom_title(self.radioNavBox)
        
        # --- Action Buttons ---
        # Create Widgets
        self.addButton = Gtk.Button()
        self.menuButton = Gtk.MenuButton();
        
        self.addEntryPopover = Gtk.Popover.new(self.addButton)
        self.add_entry_popover = Add_Entry_Popover(self.data)
        self.addEntryPopover.add(self.add_entry_popover.addGrid)
       
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
        self.addButton.connect("clicked", self.add_entry_popover.on_addButton_clicked, self.addEntryPopover)
        self.menuButton.connect("clicked", self.on_menuButton_clicked)
        
        # Pack Header Bar 
        self.hb.pack_end(self.menuButton)
        self.hb.pack_end(self.addButton)
        
        # --- Notebooks ---
        # Create Labels
        #self.overviewLabel = Gtk.Label("Overview")
        self.transactionsLabel = Gtk.Label("Transactions")
        self.projectionsLabel = Gtk.Label("Projections")

        # Style Notebook 
        #self.overviewLabel.set_hexpand(True)
        self.transactionsLabel.set_hexpand(True)
        self.projectionsLabel.set_hexpand(True)
       
        # Create Notebook
        self.notebook = Gtk.Notebook()
        #self.notebook.insert_page(self.overview.grid, self.overviewLabel, 0)
        self.notebook.insert_page(self.transactions.grid, self.transactionsLabel, 1)
        self.notebook.insert_page(self.projections.grid, self.projectionsLabel, 2)
        self.add(self.notebook)
        self.notebook.set_show_tabs(False)
        
        # Connect to handler
        # self.notebook.connect("switch-page", self.on_notebook_switch)
      
        # Connect views to data
        self.data.connect_data_views(self.transactions, self.overview, self.projections)
    
    def on_addButton_clicked(self, *args):
        if self.addEntryPopover.get_visible():
            self.addEntryPopover.hide()
        else:
            self.addEntryPopover.show_all()
    
    def on_menuButton_clicked(self, *args):
        print("Menu Button Working!")
    
    def on_navRadio_toggled(self, *args):
        if self.overviewRadio.get_active() == True:
            self.radioStatus = "overview"
            self.switch_to_overview()
        elif self.transactionsRadio.get_active() == True:
            self.radioStatus = "transactions"
            self.switch_to_transactions()
        elif self.projectionsRadio.get_active() == True:
            self.radioStatus = "projections"
            self.switch_to_projections()

    def switch_to_overview(self):
        self.notebook.set_current_page(0)
     
    def switch_to_transactions(self):
        self.notebook.set_current_page(0)
    
    def switch_to_projections(self):
        self.notebook.set_current_page(1)
