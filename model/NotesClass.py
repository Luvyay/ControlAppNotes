from datetime import datetime

class Notes:
    def __init__ (self, notes: list):
        self._notes = notes

    def get_notes(self) -> list:
        return self._notes

    def add_note(self, title: str, message: str) -> None:
        date = str(datetime.today().replace(microsecond=0))
        note_dict = {"id": self.get_max_id() + 1, "title": title, "message": message, "date": date}

        self._notes.append(note_dict)

    def get_max_id(self) -> int:
        if len(self._notes) > 0:
            return max([self._notes[index]["id"] for index in range(len(self._notes))])
        else:
            return 0

    def delete_note_by_id(self, id: int) -> None:
        for index in range(len(self._notes)):
            if self._notes[index]["id"] == id:
                self._notes.pop(index)
                break

    def edit_note_by_id(self, id: int, title: str, message: str) -> None:
        index_for_edit = 0

        for index in range(len(self._notes)):
            if self._notes[index]["id"] == id:
                index_for_edit = index
                break

        date = str(datetime.today().replace(microsecond=0))

        if title != "":
            self._notes[index_for_edit]["title"] = title
        
        if message != "":
            self._notes[index_for_edit]["message"] = message

        self._notes[index_for_edit]["date"] = date

    def get_all_id(self) -> list:
        return list(map(lambda note: note["id"], self._notes))

    def get_note_by_id(self, id: int) -> dict:
        search_index = -1

        for index in range(len(self._notes)):
            if self._notes[index]["id"] == id:
                search_index = index
                break
        
        if search_index != -1:
            return self._notes[index]
        else:
            return {}
