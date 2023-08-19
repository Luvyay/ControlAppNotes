class ParsingInput:
    def __init__(self, input: str):
        self._string = input

    def parse_string(self) -> dict:
        dict_values = {"operator": "", "id": "", "title": "", "message": "", "trash": ""}

        parse_title = self._string.split("--title \"")
        if len(parse_title) == 2:
            parse_title = parse_title[1].split("\"")
            dict_values["title"] = parse_title[0]
        
        parse_message = self._string.split("-msg \"")
        if len(parse_message) == 2:
            parse_message = parse_message[1].split("\"")
            dict_values["message"] = parse_message[0]
        
        parse_id = self._string.split("id ")
        if len(parse_id) == 2:
            parse_id = parse_id[1].split(" ")
            dict_values["id"] = parse_id[0]
        
        parse_operator = self._string.split(" ", 1)
        dict_values["operator"] = parse_operator[0]
        
        if dict_values["operator"] == "" and dict_values["id"] == "" and\
        dict_values["title"] == "" and dict_values["message"] == "":
            dict_values["trash"] = self._string

        return dict_values