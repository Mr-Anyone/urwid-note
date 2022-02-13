import urwid 

def exit_or_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop() 

palette = [
    ("banner", "white", 'black'),
    ("streak", "dark blue", "dark blue"),
    ('bg', 'dark red', 'dark red')
]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_or_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(placeholder, 'bg')
loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

pile = loop.widget.base_widget 
for i in range(10):
    txt = urwid.Text(("banner", f"Hello World {i}"), align="center")
    map = urwid.AttrMap(txt, "streak")
    
    pile.contents.append((map, pile.options())) # (widget, options)


loop.run()
    