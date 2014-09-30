from gi.repository import Gtk, Gio

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Budget")
        self.set_default_size(1000, 800)

        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.set_titlebar(self.hb)

        # Date Range Buttons
        self.day_button = Gtk.Button("Day")
        self.week_button = Gtk.Button("Week")
        self.month_button = Gtk.Button("Month")
        
        # Navigation Buttons
        self.overview_button = Gtk.Button("Overview")
        self.income_button = Gtk.Button("Income")
        self.expenses_button = Gtk.Button("Expenses")
        self.reports_button = Gtk.Button("Reports")
        self.projections_button = Gtk.Button("Projections")
        
        self.overview_button.halign = Gtk.Align.CENTER;
        self.income_button.halign = Gtk.Align.CENTER;
        self.expenses_button.halign = Gtk.Align.CENTER;
        self.reports_button.halign = Gtk.Align.CENTER;
        self.projections_button.halign = Gtk.Align.CENTER;
        
        # Quick Add Buttons
        self.quick_add_button = Gtk.Button()
        self.icon = Gio.ThemedIcon(name="list-add-symbolic")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.MENU)
        self.quick_add_button.set_size_request(32,32)
        self.quick_add_button.valign = Gtk.Align.CENTER;
        self.quick_add_button.add(self.image)
        
        # Date Range Box
        self.range_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.range_box.get_style_context(), "linked")
        self.range_box.add(self.day_button)
        self.range_box.add(self.week_button)
        self.range_box.add(self.month_button)
        
        # Navigation Box
        self.nav_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(self.nav_box.get_style_context(), "linked")
        self.nav_box.add(self.overview_button)
        self.nav_box.add(self.income_button)
        self.nav_box.add(self.expenses_button)
        self.nav_box.add(self.reports_button)
        self.nav_box.add(self.projections_button)
       
        # Header Bar Packing
        self.hb.pack_start(self.range_box)
        self.hb.pack_start(self.nav_box)
        self.hb.pack_end(self.quick_add_button)


        #self.quick_add_button = Gtk.Button()
        #self.add_button.add(Gtk.Arrow(Gtk.ArrowType.plus, Gtk.ShadowType.NONE))

#        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
#        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

#        button = Gtk.Button()
#        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
#        box.add(button)

#        button = Gtk.Button()
#        button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
#        box.add(button)

#        hb.pack_start(box)


win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
