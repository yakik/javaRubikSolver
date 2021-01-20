class RubikFileReader:
    

        def __init__(self,p_fileLocation):
            try
            
                self.c_fileReader = new StreamReader(p_fileLocation)
                self.c_fileIsOK = true
            
            catch (IOException ex)
            
                Console.WriteLine(ex.Message)
                self.c_fileIsOK = false
            
        

        def read(self):
            if !self.c_fileIsOK)
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
        
    


