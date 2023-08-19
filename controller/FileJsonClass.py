import controller.config as config
import json
import os

class FileJson:
    def read_file_json(self) -> list:
        if os.path.exists(config.PATH):
            try:
                with open(config.PATH, "r", encoding="utf-8") as file:
                    notes = json.load(file)
            
            except json.decoder.JSONDecodeError as e:
                notes = list()
                with open(config.PATH, "w") as file:
                    json.dump(notes, file, indent=2)
            
            return notes
    
    def save(self, notes: list) -> None:
        if os.path.exists(config.PATH):
            with open(config.PATH, "w", encoding="utf-8") as file:
                json.dump(notes, file, indent=2, ensure_ascii=False)