class RubikFileWriter:
        def __init__(self,p_fileLocation):
                self.c_fileWriter = open(p_fileLocation,"a")

        def write(self,p_string):
                self.c_fileWriter.Write(p_string)

        def close(self):
                self.c_fileWriter.close()
        
    

