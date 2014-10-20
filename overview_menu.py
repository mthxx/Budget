from gi.repository import Gtk, Gio
from overview import Overview
from reports import Reports
from projections import Projections

class Overview_Menu():

    def __init__(self):


        # Notebook Views
        self.overview = Overview()
        self.reports = Reports()
        self.projections = Projections()
        
        self.overviewLabel = Gtk.Label("Overview")
        self.reportsLabel = Gtk.Label("Reports")
        self.projectionsLabel = Gtk.Label("Projections")

        self.notebook = Gtk.Notebook()
        self.notebook.insert_page(self.overview.grid, self.overviewLabel, 0)
        self.notebook.append_page(self.reports.grid, self.reportsLabel)
        self.notebook.append_page(self.projections.grid, self.projectionsLabel)
        self.notebook.set_show_tabs(True)
        
        self.overviewLabel.set_hexpand(True)
        self.reportsLabel.set_hexpand(True)
        self.projectionsLabel.set_hexpand(True)
        
        self.notebook.child_set_property(self.overviewLabel,"tab-expand",True)
        self.notebook.child_set_property(self.reportsLabel,"tab-expand",True)
        self.notebook.child_set_property(self.projectionsLabel,"tab-expand",True)
