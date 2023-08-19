class Validation:
    _commands = ["add", "print-all", "print-by-date", "print", "delete", "edit", "help"]

    def __init__(self, command: dict):
        self._command = command
    
    def check_operator(self) -> bool:
        if self._command["operator"] in self._commands:
            return True
        else:
            return False
    
    def check_arguments(self, array_id: list) -> bool:

        # Проверка корректности аргументов для команды add
        if self._command["operator"] == self._commands[0]:
            return True

        # Проверка корректности аргументов для команды print-all и print-by-date
        if self._command["operator"] == self._commands[1] or\
             self._command["operator"] == self._commands[2] :
            if self._command["id"] == "" and self._command["title"] == ""\
            and self._command["message"] == "":
                return True
            else:
                return False

        # Проверка корректности аргументов для команды print и delete
        if self._command["operator"] == self._commands[3] or\
        self._command["operator"] == self._commands[4]:
            if self.check_id(array_id) and self._command["title"] == ""\
            and self._command["message"] == "":
                return True
            else:
                return False

        # Проверка корректности аргументов для команды edit
        if self._command["operator"] == self._commands[5]:
            if self.check_id(array_id):
                return True
            else:
                return False
        
        # Проверка корректности аргументов для команды help
        if self._command["operator"] == self._commands[6]:
            return True

    def check_id(self, array_id: list) -> bool:
        if self._command["id"] == "":
            return False
        
        if not self._command["id"].isdigit():
            return False
        
        if int(self._command["id"]) not in array_id:
            return False
        
        return True

    def get_spelling_rule(self) -> str:
        # Корректные аргументы для команды add
        if self._command["operator"] == self._commands[0]:
            return "--title \"текст заголовка\" -msg \"текст заметки\"\n" +\
            "(заголовок и текст заметки не обязательные параметры)\n" +\
            "Пример: add --title \"title\" -msg \"message\""

        # Корректные аргументы для команды print-all
        if self._command["operator"] == self._commands[1]:
            return "Нет параметров\n" +\
            "Пример: print-all"
        
        # Корректные аргументы для команды print-by-date
        if self._command["operator"] == self._commands[2]:
            return "Нет параметров\n" +\
            "Пример: print-by-date"

        # Корректные аргументы для команды print
        if self._command["operator"] == self._commands[3]:
            return "id номер заметки\n" +\
            "(айди является обязательным параметром)\n" +\
            "Пример: print id 5"
        
        # Корректные аргументы для команды delete
        if self._command["operator"] == self._commands[4]:
            return "id номер заметки\n" +\
            "(айди является обязательным параметром)\n" +\
            "Пример: delete id 5"

        # Корректные аргументы для команды edit
        if self._command["operator"] == self._commands[5]:
            return "id номер заметки --title \"текст заголовка\" -msg \"текст заметки\"\n" +\
            "(заголовок и текст заметки не обязательные параметры, а айди обязательный)\n" +\
            "Пример: edit id 5 --title \"title\" -msg \"message\""
        
        # Корректные аргументы для команды help
        if self._command["operator"] == self._commands[1]:
            return "Нет параметров\n" +\
            "Пример: help"
