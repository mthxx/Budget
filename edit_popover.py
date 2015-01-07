from gi.repository import Gtk, Gio, Gdk
from overview_menu import Overview_Menu

class Edit_Popover(Gtk.Window):

    def __init__(self, data):
        self.data = data

        # Content Grid
        self.LAYOUT_GRID_INDEX = 0           # Element

        # Layout Widgets
        self.LAYOUT_WIDGET_INDEX = 1         # Array
        self.CATEGORY_LABEL_INDEX = 0        # Element
        self.DATE_LABEL_INDEX = 1            # Element
        self.CURRENCY_LABEL_INDEX = 2        # Element
        self.COST_LABEL_INDEX = 3            # Element
        self.DESCRIPTION_LABEL_INDEX = 4     # Element
        self.EDIT_BUTTON_INDEX = 5
        
        # Additional Items
        self.ENTRY_GRID_INDEX = 2            # Element
        self.COST_GRID_INDEX = 3             # Element
        self.UNIQUE_ID_INDEX = 4             # Element
        
        #Initialize Data
        self.unique_id = 0
        self.entryRows = 0
        self.editPopover = ""
        self.contentGrid = 0

        # Create Widgets
        self.editGrid = Gtk.Grid()
        
        self.editButton = Gtk.Button("Edit")
        self.deleteButton = Gtk.Button("Delete")
        self.selectorBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        self.confirmLabelLine1 = Gtk.Label("Are you sure?")
        self.confirmLabelLine2 = Gtk.Label()
        self.deleteCancelButton = Gtk.Button("Cancel")
        self.deleteConfirmButton = Gtk.Button("Confirm")
        self.deleteSelectorBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        # Style Widgets
        self.editButton.set_size_request(100,32)
        self.deleteButton.set_size_request(100,32)
        self.deleteCancelButton.set_size_request(100,32)
        self.deleteConfirmButton.set_size_request(100,32)
        self.confirmLabelLine2.set_markup("<span foreground=\"red\"><b>This cannot be undone!</b></span>")
        Gtk.StyleContext.add_class(self.selectorBox.get_style_context(), "linked")
        Gtk.StyleContext.add_class(self.deleteSelectorBox.get_style_context(), "linked")
        self.selectorBox.set_margin_start(10)
        self.selectorBox.set_margin_top(10)
        self.selectorBox.set_margin_bottom(10)
        self.selectorBox.set_margin_end(5)
        self.confirmLabelLine1.set_margin_top(10)
        self.deleteSelectorBox.set_margin_start(10)
        self.deleteSelectorBox.set_margin_top(10)
        self.deleteSelectorBox.set_margin_bottom(10)
        self.deleteSelectorBox.set_margin_end(5)

        # Connect Widget Handlers
        self.editButton.connect("clicked", self.on_editButton_clicked)
        self.deleteButton.connect("clicked", self.on_deleteButton_clicked)
        self.deleteCancelButton.connect("clicked", self.on_deleteCancelButton_clicked)
        self.deleteConfirmButton.connect("clicked", self.on_deleteConfirmButton_clicked)

        # Add Widgets to Grid
        self.selectorBox.add(self.editButton)
        self.selectorBox.add(self.deleteButton)

        self.deleteSelectorBox.add(self.deleteCancelButton)
        self.deleteSelectorBox.add(self.deleteConfirmButton)
        
        self.editGrid.attach(self.selectorBox,0,0,2,1)
        self.editGrid.attach(self.confirmLabelLine1, 0, 1, 2, 1)
        self.editGrid.attach(self.confirmLabelLine2, 0, 2, 2, 1)
        self.editGrid.attach(self.deleteSelectorBox, 0, 3, 2, 1)
        
    def margin(self, widget, margin):
        widget.set_margin_start(margin)
        widget.set_margin_top(margin)
        widget.set_margin_bottom(margin)
    
    def on_calendarDropdown_clicked(self, button, calendarPopover):
        if calendarPopover.get_visible():
            calendarPopover.hide()
        else:
            calendarPopover.show_all()
    
    def on_calendarDropdown_closed(self, calendarPopover):
        dateString = self.data.translate_date(self.calendar.get_date(),"edit")
        self.calendarButton.set_label(dateString)

    def on_cancelButton_clicked(self, button):
        self.editGrid.hide()
        for i in range(0, len(self.entryRows)):
            if self.entryRows[i][self.UNIQUE_ID_INDEX] == self.unique_id:
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.EDIT_BUTTON_INDEX].show_all()
                self.entryRows[i][self.ENTRY_GRID_INDEX].show_all()
        self.contentGrid.queue_draw()
    
    def on_deleteButton_clicked(self, *args):
        self.selectorBox.hide()
        self.confirmLabelLine1.show()
        self.confirmLabelLine2.show()
        self.deleteSelectorBox.show_all()
    
    def on_deleteCancelButton_clicked(self, *args):
        self.confirmLabelLine1.hide()
        self.confirmLabelLine2.hide()
        self.deleteSelectorBox.hide()
        self.selectorBox.show()
    
    def on_deleteConfirmButton_clicked(self, *args):
        self.editPopover.hide()
        self.data.delete_data(self.unique_id)
    
    def on_editButton_clicked(self, *args):
        self.editPopover.hide()
        
        # Create editing widgets
        self.editGrid = Gtk.Grid()
        self.categoryLabel = Gtk.Label("Category:")
        self.calendarLabel = Gtk.Label("Date:")
        self.costLabel = Gtk.Label("Cost:")
        self.descriptionLabel = Gtk.Label("Description:")
        
        self.categoryComboBoxText = Gtk.ComboBoxText()
        self.costEntry = Gtk.Entry()
        self.descriptionEntry = Gtk.Entry()
        self.submitButton = Gtk.Button("Submit")
        self.cancelButton = Gtk.Button("Cancel")

        self.calendar = Gtk.Calendar()
        self.calendarButton = Gtk.Button()
        self.calendarPopover = Gtk.Popover.new(self.calendarButton)
        self.calendarPopover.add(self.calendar)
        
        # Connect Widgets
        self.calendarButton.connect("clicked", self.on_calendarDropdown_clicked, self.calendarPopover)
        self.calendarPopover.connect("closed", self.on_calendarDropdown_closed)
        self.cancelButton.connect("clicked", self.on_cancelButton_clicked)
        self.submitButton.connect("clicked", self.on_submitButton_clicked)

        # Style Editing Widgets
        self.categoryLabel.set_halign(Gtk.Align.END)
        self.categoryLabel.set_margin_top(20)
        
        self.categoryComboBoxText.set_margin_start(32)
        self.categoryComboBoxText.set_margin_top(20)
        
        self.calendarLabel.set_halign(Gtk.Align.END)
        self.calendarLabel.set_margin_top(8)

        self.calendarButton.set_margin_start(32)
        self.calendarButton.set_margin_top(8)
        
        self.costLabel.set_halign(Gtk.Align.END)
        self.costLabel.set_margin_top(8)

        self.costEntry.set_alignment(1)
        self.costEntry.set_margin_start(32)
        self.costEntry.set_margin_top(8)
        
        self.descriptionLabel.set_halign(Gtk.Align.END)
        self.descriptionLabel.set_margin_top(8)

        self.descriptionEntry.set_margin_start(32)
        self.descriptionEntry.set_margin_top(8)
        
        self.cancelButton.set_alignment(1, 1)
        self.cancelButton.set_margin_top(32)
        self.cancelButton.set_margin_bottom(32)

        self.submitButton.set_margin_start(32)
        self.submitButton.set_margin_top(32)
        self.submitButton.set_margin_bottom(20)

        self.cancelButton.set_margin_top(32)
        self.cancelButton.set_margin_bottom(20)
       
        # Set Calendar to currently set date
        self.set_calendar(self.data.transactions)
        
        # Replace label widgets with editing widgets
        for i in range(0, len(self.entryRows)):
            if self.entryRows[i][self.UNIQUE_ID_INDEX] == self.unique_id:
                for j in range(0,len(self.data.transactionsMenu)):
                    if self.data.transactionsMenu[j][1] != "Uncategorized":
                        self.categoryComboBoxText.append_text(self.data.transactionsMenu[j][1])
                    if self.data.transactionsMenu[j][1] == self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.CATEGORY_LABEL_INDEX].get_text():
                        self.categoryComboBoxText.set_active(j)
                
                # Style Edit Grid, Hide Entry Grid
                self.editGrid.set_halign(Gtk.Align.CENTER)
                self.editGrid.set_hexpand(True)
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.EDIT_BUTTON_INDEX].hide()
                self.entryRows[i][self.ENTRY_GRID_INDEX].hide()
                
                # Category
                self.editGrid.attach(self.categoryLabel, 1,0,1,1)
                self.editGrid.attach(self.categoryComboBoxText,2,0,1,1)
                
                # Date
                self.calendarButton.set_label(self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DATE_LABEL_INDEX].get_text())
                self.editGrid.attach(self.calendarLabel,1,1,1,1)
                self.editGrid.attach(self.calendarButton,2,1,1,1)
                
                # Cost
                self.costEntry.set_text(self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.COST_LABEL_INDEX].get_text())
                self.editGrid.attach(self.costLabel,1,3,1,1)
                self.editGrid.attach(self.costEntry,2,3,1,1)
                
                # Description
                self.descriptionEntry.set_text(self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.DESCRIPTION_LABEL_INDEX].get_text())
                self.editGrid.attach(self.descriptionLabel,1,4,1,1)
                self.editGrid.attach(self.descriptionEntry,2,4,1,1)
                
                # Add Submit/Cancel Button to popover
                self.editGrid.attach(self.cancelButton,1,5,1,1)
                self.editGrid.attach(self.submitButton,2,5,1,1)

                # Attach and Show Edit Grid
                self.entryRows[i][self.LAYOUT_GRID_INDEX].attach(self.editGrid, 0, 0, 1, 1)
                self.contentGrid.queue_draw()
                self.editGrid.show_all()
    
    def on_editDropdown_clicked(self, button, editPopover, unique_id, entryRows, contentGrid):
        if editPopover.get_visible():
            editPopover.hide()
        else:
            editPopover.show_all()
            self.confirmLabelLine1.hide()
            self.confirmLabelLine2.hide()
            self.deleteSelectorBox.hide()

        self.editPopover = editPopover
        self.unique_id = unique_id
        self.entryRows = entryRows
        self.contentGrid = contentGrid

    def on_submitButton_clicked(self, button):
        self.editGrid.hide()
        self.dateArr = self.calendar.get_date()
        self.year = str(self.dateArr[0])
        self.month = str(self.dateArr[1] + 1)
        self.day = str(self.dateArr[2])
        
        self.editString = self.data.create_data_string(self.categoryComboBoxText.get_active_text(),
                                        self.year, self.month, self.day, self.costEntry.get_text(), self.descriptionEntry.get_text(),
                                        self.unique_id)

        self.data.delete_data(self.unique_id)
        self.data.add_data(self.editString)
        
        for i in range(0, len(self.entryRows)):
            if self.entryRows[i][self.UNIQUE_ID_INDEX] == self.unique_id:
                self.entryRows[i][self.LAYOUT_WIDGET_INDEX][self.EDIT_BUTTON_INDEX].show_all()
                self.entryRows[i][self.ENTRY_GRID_INDEX].show_all()
        
        self.contentGrid.queue_draw()
    
    def set_calendar(self,data):
        for i in range(0, len(data)):
            if data[i][self.data.UNIQUE_ID] == self.unique_id:
                self.calendar.select_month(data[i][self.data.DATE][self.data.DATE_MONTH] - 1,
                                            data[i][self.data.DATE][self.data.DATE_YEAR])
                self.calendar.select_day(data[i][self.data.DATE][self.data.DATE_DAY])
