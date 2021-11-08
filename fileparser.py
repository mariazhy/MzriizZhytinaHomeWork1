import json


class Parser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        raise NotImplementedError("Please notice: something went wrong")


class JsonParse(Parser):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path

    def parse(self):
        with open(self.file_path) as json_file:
            my_file = json.load(json_file)
        return my_file


class TxtParser(Parser):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path

    def parse(self):
        open_my_file = open(self.file_path, 'r')
        read_my_file = open_my_file.read()
        return read_my_file


class FileParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        """
        parse a file based on the file format using `JsonParser` and `TxtParser` classes. If file format is not
        supported - raise ValueError.
        """
        my_path = self.file_path
        supported_methods = self.get_supported_file_formats()
        if "json" in my_path and "json" in supported_methods:
            my_file = JsonParse(my_path)
            return my_file.parse()
        elif "txt" in my_path and "txt" in supported_methods:
            my_file = TxtParser(my_path)
            return my_file.parse()
        else:
            return ValueError("This format could not be parsed. 'txt and 'json' are the only supported formats")

    def get_supported_file_formats(self):
        """
        returns a tuple of supported file format. In our case ("txt", "json")
        """
        supported_formats = ("txt", "json")
        return supported_formats
