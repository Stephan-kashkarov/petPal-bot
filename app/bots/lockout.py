import re

class Bot:
    def __init__(self, state="NO QUERY", text=None):
        self.state = state
        self.functions = {
            'NO QUERY': self.no_query,
            'LOOKING': self.looking,
            'SEND': self.send,
        }
        self.text = text
        self.places = text.split()

    def no_query(self):
        if re.search(r".*help.*", self.text, re.I):
            self.state = "LOOKING"
            return self.looking()
        return "Hi say help to get some help!"
    
    def looking(self):
        # check = [re.search(r".*{}.*".format(x), self.text, re.I) for x in self.places]
        if True: #in check:
            self.state = "SEND"
            place = self.text #self.places[check.index('True')]
            return self.send(place)
        return "Where are you?"

    def send(self, place):
        self.state = "NO QUERY"
        return f"Sending a tutor to {place}!"
    
    def get_func(self):
        return self.functions[self.state](), self.state