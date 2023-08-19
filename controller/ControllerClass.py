from controller.FileJsonClass import FileJson
from model.NotesClass import Notes


class Controller:
    def __init__(self):
        self._file_json = FileJson()
        self._notes = Notes(self._file_json.read_file_json())
    
    def get_notes(self) -> list:
        return self._notes.get_notes()
    
    def add_note(self, title: str, message: str) -> None:
        self._notes.add_note(title, message)
    
    def del_by_id(self, id: int) -> None:
        self._notes.delete_note_by_id(id)
    
    def edit_by_id(self, id: int, title: str, message: str) -> None:
        self._notes.edit_note_by_id(id, title, message)
    
    def save_in_file(self) -> None:
        self._file_json.save(self._notes.get_notes())

    def get_all_id(self) -> list:
        return self._notes.get_all_id()
    
    def get_note_by_id(self, id: int) -> dict:
        return self._notes.get_note_by_id(id)

