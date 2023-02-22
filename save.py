import json
import os

class Saver:
    def __init__(self, file):
        self.file = file  # We will Save the password here

    def save(self, data):
        with open(self.file, "w") as file: # "w" is called write access
            json.dump(data, file, indent=4) # This will put the data into the file and format it to amke it readable

    def read(self):
        with open(self.file, "r") as file:
            data = file.read()

            if os.stat(self.file).st_size == 0:  # If there's nothing inside file and we will still try to load the data then it will return empty array
                return []

            return json.loads(data) # Otherwise we will continue the loading operation   

                    
