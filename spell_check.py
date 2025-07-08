from spellchecker import SpellChecker #default spell-check module of python

#create class and define spell-check function
class SpellCheckerApp:
    def __init__(self):
        self.spell=SpellChecker()
    
    def corrected_text(self,text):
        words=text.split()
        corrected_word=[]
