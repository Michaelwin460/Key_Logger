import datetime

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, data):
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.filename, "a") as file:
                file.write(f"{timestamp}: {data}\n")
                file.flush()
        except Exception as e:
            print(f"Error writing to file: {e}")

