import psutil
import os
import random
from menu import Menu
from dataStruct import DataStruct
from filemanager import TextFileManager, ZipFileManager, JsonFileManager, XmlFileManager, FileManager


#----------------------ИНФОРМАЦИЯ О СИСТЕМЕ------------------------------------------------------------------------------


def ejectSysInfo():
    disk_info = []
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '': continue
        usage = psutil.disk_usage(part.mountpoint)
        print("Device:", part.device)
        print("Total space:", round(usage.total / (2 ** 30), 2), "Gb")
        print("Used space:", round(usage.used / (2 ** 30), 2), "Gb")
        print("Free space:", round(usage.free / (2 ** 30), 2), "Gb")
        print("Percent used:", usage.percent)
        print("Filesystem type:", part.fstype)
        print("Mountpoint:", part.mountpoint)


def startMainMenu():
    mainMenu = Menu(name='ГЛАВНОЕ МЕНЮ')
    mainMenu.addElement(text='Вывести информацию о системе', action=ejectSysInfo)
    mainMenu.addElement(text='Работа с текстовым файлом', action=startTextFileMenu, decorate=False)
    mainMenu.addElement(text='Работа с JSON файлом', action=startJsonFileMenu, decorate=False)
    mainMenu.addElement(text='Работа с XML файлом', action=startXmlFileMenu, decorate=False)
    mainMenu.addElement(text='Работа с ZIP файлом', action=startZipFileMenu, decorate=False)
    mainMenu.addElement(text='Выйти', action=Menu.quitMenu, decorate=False)
    mainMenu.startWork()


def startTextFileMenu():
    textfileMenu = Menu(name='РАБОТА С ТЕКСТОВЫМ ФАЙЛОМ')
    textfileMenu.addElement(text='Создать файл', action=FileManager.createFile)
    textfileMenu.addElement(text='Запись в файл', action=TextFileManager.writeToFile)
    textfileMenu.addElement(text='Содержимое файла', action=TextFileManager.readFile)
    textfileMenu.addElement(text='Удалить файл', action=FileManager.deleteFile)
    textfileMenu.addElement(text='Выйти', action=Menu.quitMenu, decorate=False)
    textfileMenu.startWork()


def startJsonFileMenu():
    jsonFileMenu = Menu(name='РАБОТА С JSON ФАЙЛОМ')
    jsonFileMenu.addElement(text='Создать файл', action=FileManager.createFile)
    jsonFileMenu.addElement(text='Записать объект в файл', action=JsonFileManager.writeToFile)
    jsonFileMenu.addElement(text='Содержимое файла', action=JsonFileManager.readFile)
    jsonFileMenu.addElement(text='Удалить файл', action=FileManager.deleteFile)
    jsonFileMenu.addElement(text='Выйти', action=Menu.quitMenu, decorate=False)
    jsonFileMenu.startWork()


def startXmlFileMenu():
    xmlFileMenu = Menu(name='РАБОТА С XML ФАЙЛОМ')
    xmlFileMenu.addElement(text='Создать файл', action=FileManager.createFile)
    xmlFileMenu.addElement(text='Запись в файл', action=XmlFileManager.writeToFile)
    xmlFileMenu.addElement(text='Содержимое файла', action=XmlFileManager.readFile)
    xmlFileMenu.addElement(text='Удалить файл', action=FileManager.deleteFile)
    xmlFileMenu.addElement(text='Выйти', action=Menu.quitMenu, decorate=False)
    xmlFileMenu.startWork()


def startZipFileMenu():
    zipFileMenu = Menu(name='РАБОТА С ZIP ФАЙЛОМ')
    zipFileMenu.addElement(text='Создать архив', action=ZipFileManager.createFile)
    zipFileMenu.addElement(text='Добавить файл в архив', action=ZipFileManager.writeToFile)
    zipFileMenu.addElement(text='Разархивировать файл и вывести данные', action=ZipFileManager.readFile)
    zipFileMenu.addElement(text="Удалить файл и архив", action=FileManager.deleteFile)
    zipFileMenu.addElement(text="Выйти", action=Menu.quitMenu, decorate=False)
    zipFileMenu.startWork()


def repairConsoleEncoding():
    #os.system("chcp 65001 > nul")
    pass


def main():
    repairConsoleEncoding()
    startMainMenu()


if __name__ == "__main__":
    main()