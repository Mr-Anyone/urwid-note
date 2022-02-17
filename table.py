import urwid 
import logging 
logging.basicConfig(filename="log.log")

palette = [
    ('bg', 'black', 'black'), 
    ('text', 'white', 'dark red'),
]

def exit_on_q(key):
    if key in ('q', "Q"):
        raise urwid.ExitMainLoop() 
    
class ConversationText(urwid.Pile):
    def __init__(self):
        widget_list = [urwid.Edit("What is your name? "), urwid.Text("")]
        super().__init__(widget_list, focus_item=None)
        logging.critical(self.contents)
    
    def update_text(self, text):
        self.contents[1][0].set_text(text)

    
    def get_user_response(self):
        return self.contents[0][0].edit_text
        
    


class ConversationTable(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleListWalker([ConversationText()])
        super().__init__(body)
    
    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key == "q":
            raise urwid.ExitMainLoop()
        
        if key != 'enter':
            return key 
        
        text = self.focus.get_user_response()
        text = f"Hello {text}!"
        self.focus.update_text(text)
        
        # at the end of the list
        if self.focus_position + 1 >= len(self.body): 
            self.body.append(ConversationText())
            self.focus_position += 1
        
        return key


table = ConversationTable() 
loop = urwid.MainLoop(table, palette, unhandled_input=exit_on_q)
loop.run()