using System
using System.IO
using System.Collections.Generic
using System.Linq
using System.Text
using System.Threading.Tasks

namespace CSharpRubikSolver



    class RubikFileWriter
    

        StreamWriter c_fileWriter
        //bool c_fileIsOK


        RubikFileWriter(String p_fileLocation):
            try
            
                c_fileWriter = new StreamWriter(p_fileLocation)
                //      c_fileIsOK = true
            
            catch (IOException ex)
            
                Console.WriteLine(ex.Message)
                //        c_fileIsOK = false
            
        

        write(String p_string):
            try
            
                c_fileWriter.Write(p_string)
            
            catch (IOException ex): Console.WriteLine(ex.Message) 

        

        close():
            try
            
                c_fileWriter.Close()
            
            catch (IOException ex): Console.WriteLine(ex.Message) 
        
    

