import urwid 

class Table(urwid.WidgetWrap):
    def __init__(self, rows, cols):
        count = 0 
        widget_list = []
        for y in range(cols): 
            body = []
            for x in range(rows):
                body.append(urwid.SelectableIcon(f"{count:.2f}"))
                count +=1
                
            widget_list.append(urwid.Columns(body))

        super().__init__(urwid.Pile(widget_list))
    
widgets = [
    urwid.Text("Title", align="center"),
    urwid.Divider(),
    urwid.Columns([
        ('weight', 2, urwid.Divider()), 
        ('weight', 10, Table(10, 10))
    ]),
    urwid.Divider(),
]
main_view = urwid.ListBox(urwid.SimpleFocusListWalker(widgets))

urwid.MainLoop(main_view).run()