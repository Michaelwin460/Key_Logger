

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, data):
        try:
            with open(self.filename, "a+") as file:
                file.write(f"{data}\n")
                file.flush()
        except Exception as e:
            print(f"Error writing to file: {e}")

    def getFileName(self):
        return self.filename

