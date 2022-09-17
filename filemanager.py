import json
import os
import random
import xml
import zipfile
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from json import JSONDecodeError
import shutil

from dataStruct import DataStruct
from random import *


class FileManager(ABC):
    @staticmethod
    def deleteFile():
        try:
            os.remove(input("Введите имя файла: "))
            print("Файл успешно удалён")
        except FileNotFoundError:
            print("Файл с данным именем не существует")

    @staticmethod
    def createFile():
        filename = input("Введите имя файла: ")
        if not os.path.exists(filename):
            open(filename, 'w+').close()
            print(f"Файл {filename} успешно создан!")
        else:
            print(f"Ошибка! Файл {filename} уже существует!")

    @abstractmethod
    def writeToFile(self):
        pass

    @abstractmethod
    def readFile(self):
        pass


class TextFileManager(FileManager):
    @staticmethod
    def writeToFile():
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            with open(filename, 'w+') as file:
                file.write(input("Введите текст на ввод: "))
                print("Запись в файл прошла успешно")
        else:
            print("Такого файла не существует!")

    @staticmethod
    def readFile():
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                print(f"\nФайл {file.name}", file.read(), sep='\n')
        else:
            print("Такого файла не существует!")


class JsonFileManager(FileManager):
    @staticmethod
    def writeToFile():
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            with open(filename, 'w+') as file:
                jsonStructure = makeStruct()
                file.write(json.dumps(jsonStructure.__dict__))
                print("Запись в файл прошла успешно")
        else:
            print("Такого файла не существует!")

    @staticmethod
    def readFile():
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            with open(filename, encoding='utf-8', mode='r') as file:
                try:
                    filetext = json.load(file)
                    print(f'''{filetext["name"]} {filetext["surname"]}\nID: {filetext['id']}\nОценки: {filetext['marks']}''')
                except (JSONDecodeError, KeyError) as e:
                    if e == JSONDecodeError:
                        print("Откройте файл формата JSON!")
                    else:
                        print("Содержимое файла не соответствует требуемой структуре")

        else:
            print("Такого файла не существует!")


class XmlFileManager(FileManager):
    @staticmethod
    def writeToFile():
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            with open(filename, 'a') as file:
                xmlStruct = makeStruct()
                pupils = ET.Element("Pupils")
                pupil = ET.SubElement(pupils, "Pupil", attrib={"id": str(xmlStruct.id)})
                structName = ET.SubElement(pupil, "name")
                structName.text = xmlStruct.name
                structName = ET.SubElement(pupil, "surname")
                structName.text = xmlStruct.surname
                structMarks = ET.SubElement(pupil, "marks")
                for mark in xmlStruct.marks:
                    structMark = ET.SubElement(structMarks, "mark")
                    structMark.text = str(mark)
                file.write(ET.tostring(pupils).decode())
        else:
            print("Такого файла не существует!")

    @staticmethod
    def readFile():
        filename = input("Введите имя файла: ")
        if os.path.exists(filename):
            with open(filename, encoding='utf-8', mode='r') as file:
                try:
                    root = ET.parse(file).getroot()
                    for pupil in root.findall('Pupil'):
                        print(f'Cтудент: {pupil[0].text} {pupil[1].text}')
                        print(f'ID: {pupil.attrib.get("id")}')
                        print("Оценки: ", end='')
                        for mark in pupil.find('marks'):
                            print(f"{mark.text} ", end='')
                            continue
                        print('\n')
                except xml.etree.ElementTree.ParseError:
                    print("Откройте файл нужного формата!")
        else:
            print("Такого файла не существует!")


class ZipFileManager(FileManager):
    @staticmethod
    def createFile():
        filename = input("Введите имя архива: ")
        if not os.path.exists(filename):
            with zipfile.ZipFile(filename + '.zip', 'w') as file:
                pass
            print(f"Архив {filename} успешно создан!")
        else:
            print(f"Ошибка! Файл {filename} уже существует!")

    @staticmethod
    def writeToFile():
        archname = input("Введите имя архива: ")
        archname = archname + '.zip'
        if os.path.exists(archname):
            archive = zipfile.ZipFile(archname, "a")
            filename = input("Введите имя файла: ")
            if os.path.exists(filename):
                archive.write(filename, os.path.basename(filename))
                print(f"Файл {filename} успешно добавлен в архив {archname}")
            else:
                print("Такого файла не существует!")
        else:
            print("Такого архива не существует!")

    @staticmethod
    def readFile():
        archname = input("Введите имя архива: ")
        archname = archname + '.zip'
        if os.path.exists(archname):
            archive = zipfile.ZipFile(archname, "r")
            filename = input("Введите имя файла: ")
            data = archive.read(filename)
            archive.close()
            file = open(filename, "w+b")
            file.write(data)
            file.close()
            print("size:", os.path.getsize(filename))
            print("modify timestamp:", os.path.getmtime(filename))
        else:
            print("Такого архива не существует!")


def makeStruct():
    id = int(input("id = "))
    name = input("Имя = ")
    surname = input("Фамилия = ")
    marks = []
    for i in range(0, 5):
        marks.append(randint(2, 5))
    return DataStruct(id, name, surname, marks)
