import urwid 

def exit_on_q(key):
    if key in ('q', "Q"):
        raise urwid.ExitMainLoop() 

class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != "enter": # call parent such that nothing will happen
            return super().keypress(size, key)

        self.original_widget = urwid.Text(f"Nice to meet you,\n{edit.edit_text}.\n\nPress Q to exit.")



palette = [
    ("qb", "black", "dark blue")
]
edit = urwid.Edit(u"What is your name?\n")
map = urwid.AttrMap(edit, "qb")
filler = QuestionBox(map, valign="middle")

loop = urwid.MainLoop(filler, palette, unhandled_input=exit_on_q)
loop.run()