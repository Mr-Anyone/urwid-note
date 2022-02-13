import urwid
import logging 
logging.basicConfig(filename="log.log") 

def make_question():
    return urwid.Pile([urwid.Edit(('text', "What is your name?\n"))])

def make_textui(text):
    return urwid.Text(('text', f"{text} response"), align='center')

class ConversationList(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleFocusListWalker([make_question()])
        super().__init__(body)    

    def keypress(self, size, key):
        key = super(ConversationList, self).keypress(size, key)
        if key != "enter":
            return key
        
        name = self.focus[0].edit_text # The current selection in the pile 
        if not name:
            raise urwid.ExitMainLoop() 

        #insert or replace into list 
        self.focus.contents[1: ] = [(make_textui(name), self.focus.options())] # the format of pile is (widget, options)

        # inserting a new question
        pos = self.focus_position
        if pos +1 >= len(self.body):
            self.body.insert(pos + 1, make_question())
        self.focus_position += 1 # always goes to the next line
    

palette = [
    ('text', 'white', '')
]

loop = urwid.MainLoop(ConversationList(), palette)
loop.run()