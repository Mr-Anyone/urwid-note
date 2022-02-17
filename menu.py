from fileinput import filename
import urwid 
import logging 
logging.basicConfig(filename="log.log")


choices = "Apple Banna Grape".split() 
def exit_on_q(key):
    if key in ('q', "Q"):
        raise urwid.ExitMainLoop() 

def menu(choices):
    body = []
    for choice in choices: 
        button = urwid.Button(choice)
        urwid.connect_signal(button, 'click', on_click)
        body.append(button)
    
    return urwid.ListBox(body)

def on_click(button):
    logging.log(f"Button was clicked {button}")

palette = [ 
    ('bg', 'dark blue', 'dark blue'), 
]

background = urwid.SolidFill("/")
menu_view = menu(choices)

overlay_view = urwid.Overlay(menu_view, background, align='center',  width=('relative', 80), valign='middle', height=('relative', 80))
loop = urwid.MainLoop(overlay_view, palette, unhandled_input=exit_on_q)
loop.run()