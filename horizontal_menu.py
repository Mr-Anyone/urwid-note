# this will be my implementation  of the horizontal menu 
# original implementation: https://urwid.org/tutorial/index.htmlr
import urwid 
import urwid.web_display
import logging 

logging.basicConfig(filename="log.log")

class Choice(urwid.WidgetWrap):
    def __init__(self, choice_label, sub_menu=None):
        button = urwid.Button(('button', choice_label))
    
        if sub_menu is not None:
            urwid.connect_signal(button, "click", self.open_menu)
            self.sub_menu = sub_menu
    
        button_map = urwid.AttrMap(button, 'button')
        botton_focus = urwid.AttrMap(button_map, None, focus_map=focus_map)
        super().__init__(botton_focus)
        
    def open_menu(self, key):
        main_view.open_menu(self.sub_menu)
        

class Heading(urwid.WidgetWrap):
    def __init__(self, label):
        divider = urwid.AttrMap(urwid.Divider(), "line")
        text = urwid.AttrMap(urwid.Text(label, align="center"), "heading-title")
        w = urwid.Pile([divider, text, divider])
        super().__init__(w)
    
class Menu(urwid.WidgetWrap):
    def __init__(self, captions, choices, max_choice=10 ):
        body = [Heading(captions)]
        
        # adding adding choices in
        for i in range(max_choice):
            if i  + 1 <= len(choices):
                body.append(choices[i])
            else: 
                body.append(Choice(""))
        
        menu = urwid.ListBox(urwid.SimpleFocusListWalker(body))
        menu_map = urwid.AttrMap(menu, "menu")
        super().__init__(menu_map)

class MainView(urwid.Columns):
    def __init__(self,dividechars=0):
        widget_list = []
        
        super().__init__(widget_list, dividechars)
    
    def open_menu(self, menu):
        if self.contents:
            del self.contents[self.focus_position + 1:]
        
        self.contents.append((menu, self.options('given', 30)))
        
        self.focus_position = len(self.contents) - 1
        
        

palette = [
    (None, "black", "black"),
    ('button', 'dark cyan', 'white'),
    ('menu', 'black', 'black'),
    ('options', 'white', 'white'),
    # For Heading 
    ("line", "dark red", "dark red"),
    ("heading-title", "white,bold", "dark red"),
    # for focus 
    ("button_foucs", "white", 'dark blue')
]
focus_map = {
    "button" : "button_foucs"
    
}
menus = Menu("Main Menu", [
    Choice("Choice One", Menu("Choice One", [Choice("Choice Three", Menu("Choice Three", []))])), 
    Choice("Choice Two", Menu("Choice Two", [Choice("Choice Four")]))
])

main_view = MainView(1)
main_view.open_menu(menus)
loop = urwid.MainLoop(main_view, palette).run()