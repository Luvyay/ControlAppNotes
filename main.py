'''
    Реализовать консольное приложение заметки, с сохранением, чтением,
    добавлением, редактированием и удалением заметок. Заметка должна
    содержать идентификатор, заголовок, тело заметки и дату/время создания или
    последнего изменения заметки. Сохранение заметок необходимо сделать в
    формате json или csv формат (разделение полей рекомендуется делать через
    точку с запятой). Реализацию пользовательского интерфейса студент может
    делать как ему удобнее, можно делать как параметры запуска программы
    (команда, данные), можно делать как запрос команды с консоли и
    последующим вводом данных, как-то ещё, на усмотрение студента.Например:
    python notes.py add --title "новая заметка" -msg "тело новой заметки"
    Или так:
    python note.py
    Введите команду: add
    Введите заголовок заметки: новая заметка
    Введите тело заметки: тело новой заметки
    Заметка успешно сохранена
    Введите команду:

    При чтении списка заметок реализовать фильтрацию по дате

    Команды для примера:
    add
    print-all
    edit id 4 --title "title" -msg "message"
    print-all
    delete id 4
    print-all
    print-by-date
    print id 1
    help
'''

from controller.ControllerClass import Controller
from ValidationClass import Validation
from ParsingInputClass import ParsingInput
from datetime import datetime


def print_note(note: dict) -> None:
    if note:
        print("id: " + str(note["id"]) + "; Date: " + note["date"] + "; Title: " + note["title"] + "\n" + 
                "Text: \n" +
                note["message"] + "\n")
    else:
        print("Ничего нет!")

def print_all(notes: list) -> None:
    print("\n----------вывод всех заметов----------\n")

    for element in notes:
        print_note(element)
    
    print("--------------------------------------\n")

def print_by_date(notes: list) -> None:
    notes_by_date = sorted(notes, key=lambda note: datetime.strptime(note["date"], '%Y-%m-%d %H:%M:%S'))

    print("\n----------вывод всех заметов по дате----------\n")

    for element in notes_by_date:
        print_note(element)

    print("----------------------------------------------\n")

def print_available_commands() -> None:
    print("\nДанная программа позволяет добавлять, редактировать, удалять и выводить заметки.")
    print("Доступные команды:\n" +\
          "add --title \"title\" -msg \"message\"\n" +\
            "edit id 1 --title \"title\" -msg \"message\"\n" +\
                "delete id 1\n" +\
                    "print id 1\n" +\
                        "print-all\n" +\
                            "print-by-date\n")

def main():

    controller = Controller()

    print_available_commands()

    string_input = input("Введите команду: ")

    while string_input != "exit":
        
        comand = ParsingInput(string_input).parse_string()
        check_input = Validation(comand)

        if check_input.check_operator():
            if check_input.check_arguments(controller.get_all_id()):
                if comand["operator"] == "add":
                    controller.add_note(comand["title"], comand["message"])
                    controller.save_in_file()

                if comand["operator"] == "print-all":
                    print_all(controller.get_notes())

                if comand["operator"] == "print-by-date":
                    print_by_date(controller.get_notes())

                if comand["operator"] == "print":
                    print_note(controller.get_note_by_id(int(comand["id"])))

                if comand["operator"] == "delete":
                    controller.del_by_id(int(comand["id"]))
                    controller.save_in_file()

                if comand["operator"] == "edit":
                    controller.edit_by_id(int(comand["id"]), comand["title"], comand["message"])
                    controller.save_in_file()

                if comand["operator"] == "help":
                    print_available_commands()

            else:
                print(f"Параметры команды \"{comand['operator']}\" должны быть следующими:\n" +
                    check_input.get_spelling_rule())

        else:
            print("Нет такой команды!")
        
        string_input = input("Введите команду: ")



if __name__ == "__main__":
    main()