import urwid
import logging 
logging.basicConfig(filename="log.log")

choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()

def menu(title, choices):
    body = [urwid.Text(title, align="center"), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c) # Clicked or something

        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text(f"You have choosen {choice}! ") 
    button = urwid.Button("Done")
    urwid.connect_signal(button, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response, urwid.Divider(), button]))

def exit_program(button):
    raise urwid.ExitMainLoop()



main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u"\\"), 'center', ('relative', 70),'middle',  ('relative', 70))
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()