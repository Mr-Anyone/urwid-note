import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', '', '', '', '#ffa', '#60d'), # (foreground, background) final two
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'),]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256) # set the proeprty of the terminal
loop.widget = urwid.AttrMap(placeholder, 'bg') # set the background # set the default widget
loop.widget.original_widget = urwid.Filler(urwid.Pile([])) # stacking widgets from top to bottom

div = urwid.Divider()
outside = urwid.AttrMap(div, 'outside')
inside = urwid.AttrMap(div, 'inside')
txt = urwid.Text(('banner', u" Hello World "), align='center')
streak = urwid.AttrMap(txt, 'streak')

txt2 = urwid.Text(("banner", u"What is this SHIT!"), align="center")
streak2 = urwid.AttrMap(txt2, "streak")


pile = loop.widget.base_widget # .base_widget skips the decorations
for item in [outside, inside, streak, streak2, inside, outside]:
    pile.contents.append((item, pile.options()))

loop.run()