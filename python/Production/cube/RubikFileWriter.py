class RubikFileWriter:
    

        StreamWriter c_fileWriter
        //bool c_fileIsOK


        def __init__(self, String p_fileLocation):
            try
            
                c_fileWriter = new StreamWriter(p_fileLocation)
                //      c_fileIsOK = true
            
            catch (IOException ex)
            
                Console.WriteLine(ex.Message)
                //        c_fileIsOK = false
            
        

        def write(self, String p_string):
            try
            
                c_fileWriter.Write(p_string)
            
            catch (IOException ex): Console.WriteLine(ex.Message) 

        

        def close(self):
            try
            
                c_fileWriter.Close()
            
            catch (IOException ex): Console.WriteLine(ex.Message) 
        
    

