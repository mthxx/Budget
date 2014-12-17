from gi.repository import Gtk, Gio, Gdk
from overview import Overview
from transactions import Transactions
from reports import Reports
from projections import Projections
from sidebar import Sidebar
from add_popover import Add_Popover
from add_category_popover import Add_Category_Popover

class Window(Gtk.Window):

    def __init__(self, data):
        self.data = data 
        self.provider = Gtk.CssProvider()
        self.provider.load_from_path("style.css")
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        Gtk.Window.__init__(self, title="Budget")
        self.set_default_size(1000, 700)
        
        # --- Header Bars ---
        self.headerBox = Gtk.Box(name="headerBox")
        self.hbLeft = Gtk.HeaderBar()
        self.hbRight = Gtk.HeaderBar(name="hbRight")
       
        # Style Header Bars
        self.hbLeft.set_show_close_button(False)
        self.hbLeft.set_property("width-request", 100)
        
        self.hbRight.set_show_close_button(True)
        self.hbRight.set_hexpand(True)
        

        self.headerBox.add(self.hbLeft)
        self.headerBox.add(self.hbRight)
        self.set_titlebar(self.headerBox)

        # --- Action Buttons (Left Header Bar) ---
        # Create Buttons
        self.addCategoryButton = Gtk.Button()
        self.selectButton = Gtk.Button()
        self.selectIcon = Gio.ThemedIcon(name="object-select-symbolic")
        self.selectImage = Gtk.Image.new_from_gicon(self.selectIcon, Gtk.IconSize.MENU)
        self.selectButton.add(self.selectImage)
        self.addCategoryPopover = Gtk.Popover.new(self.addCategoryButton)
        
        # Create Popover
        self.add_category_popover = Add_Category_Popover(self.data)
        self.addCategoryPopover.add(self.add_category_popover.addGrid)
        # Connect to handler
        #self.selectButton.connect("clicked", self.on_selectButton_clicked)
        self.addCategoryButton.connect("clicked", self.add_category_popover.on_addCategoryButton_clicked, self.addCategoryPopover)
        
        # Add Image
        self.addCategoryIcon = Gio.ThemedIcon(name="list-add-symbolic")
        self.addCategoryImage = Gtk.Image.new_from_gicon(self.addCategoryIcon, Gtk.IconSize.MENU)
        self.addCategoryButton.add(self.addCategoryImage)
        
        # --- Action Buttons (Right Header Bar) ---
        # Create Buttons
        self.addButton = Gtk.Button()
        self.menuButton = Gtk.MenuButton();
        self.addPopover = Gtk.Popover.new(self.addButton)
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
        # Create Popovers
        self.add_popover = Add_Popover(self.data)
        self.addPopover.add(self.add_popover.addGrid)
        # Connect to handler
        self.addButton.connect("clicked", self.add_popover.on_addButton_clicked, self.addPopover)
        self.menuButton.connect("clicked", self.on_menuButton_clicked)
        
        # --- Header Bar Packing ---
        self.hbLeft.pack_start(self.addCategoryButton)
        self.hbLeft.pack_end(self.selectButton)
        self.hbRight.pack_end(self.menuButton)
        self.hbRight.pack_end(self.addButton)
        
        # --- Notebooks
        # Initialize Views
        self.overview = Overview(self.data)
        self.transactions = Transactions(self.data)
        self.reports = Reports()
        self.projections = Projections()

        # Create Labels
        self.overviewLabel = Gtk.Label("Overview")
        self.transactionsLabel = Gtk.Label("Transactions")
        self.reportsLabel = Gtk.Label("Reports")
        self.projectionsLabel = Gtk.Label("Projections")

        # Style Notebook 
        self.overviewLabel.set_hexpand(True)
        self.transactionsLabel.set_hexpand(True)
        self.reportsLabel.set_hexpand(True)
        self.projectionsLabel.set_hexpand(True)
       
        # Create Notebook
        self.notebook = Gtk.Notebook()
        self.notebook.insert_page(self.overview.grid, self.overviewLabel, 0)
        self.notebook.insert_page(self.transactions.view.grid, self.transactionsLabel, 1)
        self.notebook.insert_page(self.reports.grid, self.reportsLabel, 3)
        self.notebook.insert_page(self.projections.grid, self.projectionsLabel, 4)
        self.add(self.notebook)
        
        # Connect to handler
        self.notebook.connect("switch-page", self.on_notebook_switch)
      
        # Connect views to data
        self.data.connect_data_views(self.transactions, self.overview)
        self.add_popover.addSubmitButton.connect("clicked", self.add_popover.on_addSubmitButton_clicked)
    
    def on_addButton_clicked(self, *args):
        if self.addPopover.get_visible():
            self.addPopover.hide()
        else:
            self.addPopover.show_all()

        
    def on_notebook_switch(self, notebook, page, index, *args):
        if index == 0:
            self.hbLeft.hide()
            self.hbRight.queue_draw()
            #self.notebook.set_current_page(0)
        if index == 1:
            self.hbLeft.show()
            self.hbRight.queue_draw()
        if index == 2:
            self.hbLeft.show()
            self.hbRight.queue_draw()
        if index == 3:
            self.hbLeft.hide()
            self.hbRight.queue_draw()
        if index == 4:
            self.hbLeft.hide()
            self.hbRight.queue_draw()

    def on_menuButton_clicked(self, *args):
        print("Menu Button Working!")
