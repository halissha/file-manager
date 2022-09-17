import os
import string
from quit import QuitException
from six.moves import input as raw_input


class Menu:
    def __init__(self, name):
        self.name = name
        self.elements = []
        self.currentid = 1

    def addElement(self, text, action, decorate=True):
        self.elements.append({'id':self.currentid, 'text':text, 'func':action, 'decorate':decorate})
        self.currentid += 1

    def startWork(self):
        while True:
            self.ejectMenu()
            try:
                self.conductChoice()
            except QuitException:
                return

    def ejectMenu(self):
        print(f'\n---{self.name}---')
        for element in self.elements:
            print(str(element['id']) + '. ' + element['text'])

    def conductChoice(self):
        choice = input('\nВыберите пункт меню: ')
        try:
            choice = int(choice)
        except ValueError:
            print(f'\033[1;31mВведите номер пункта меню для выбора действия\033[0;0m'.ljust(2))
            return
        if 0 < int(choice) <= self.currentid:
            self.decorateMenu(choice, self.elements[choice - 1]['text'])
            self.elements[int(choice) - 1]['func']()
            self.decorateMenu(choice)
            #os.system('pause')
            raw_input("Press enter to continue...")
        else:
            print(f'\033[1;31mВведите корректный пункт меню\033[0;0m'.ljust(2))

    @staticmethod
    def quitMenu():
        raise QuitException

    def decorateMenu(self, choice, text=''):
        if self.elements[int(choice) - 1]['decorate']:
            if text:
                print(f'\n\033[1;31m{text}\033[0;0m'.ljust(2))
            print('-----------------------------------------------')