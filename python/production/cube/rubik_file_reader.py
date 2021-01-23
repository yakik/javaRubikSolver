class Rubik_file_reader:

        def __init__(self, p_fileLocation):
            self.c_fileReader = open(p_fileLocation,"r")
            self.c_fileIsOK = True

        def read(self):
            if not self.c_fileIsOK:
                return -1
            else:
                readChar = self.c_fileReader.read(1)
                return readChar

        def close(self):
            self.c_fileReader.close()
