class RubikFileReader:
    

        def __init__(self,p_fileLocation):
            try
            
                self.c_fileReader = StreamReader(p_fileLocation)
                self.c_fileIsOK = True
            
            catch (IOException ex)
            
                Console.WriteLine(ex.Message)
                self.c_fileIsOK = False
            
        

        def read(self):
            if not self.c_fileIsOK:
                return -1
            else
                try
                
                    readChar = self.c_fileReader.Read()
                    return readChar
                
                catch (IOException ex):
                    Console.WriteLine(ex)
                    return -1
                
        

        def close(self):
            try
            
                self.c_fileReader.Close()
            
            catch (IOException ex): Console.WriteLine(ex) 
        
    


