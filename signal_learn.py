from re import L
import urwid 

def exit_on_q(key):
    if key in ('q', "Q"):
        raise urwid.ExitMainLoop()

palette = [
    ('I say', 'default,bold', 'default', 'bold')
]

ask = urwid.Edit(("I say", "What is your name?\n"))
reply = urwid.Text(u"")
button = urwid.Button(u'Exit')

div = urwid.Divider() 
pile = urwid.Pile([ask, div, reply, div, button]) # stakcing stuff together

top = urwid.Filler(pile, valign="top")
loop = urwid.MainLoop(top, palette=palette, unhandled_input=exit_on_q)

def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)

loop.run()