using System

using System.IO

namespace cube
{
    class RubikFileReader
    {
        Boolean c_fileIsOK

        StreamReader   c_fileReader

        RubikFileReader():
        }

        RubikFileReader(String p_fileLocation):
            try
            {
                c_fileReader = new StreamReader(p_fileLocation)
                c_fileIsOK = true
            }
            catch (IOException ex)
            {
                Console.WriteLine(ex.Message)
                c_fileIsOK = false
            }
        }

        read():
            if !c_fileIsOK)
                return -1
            else
                try
                {
                    readChar = c_fileReader.Read()
                    return readChar
                }
                catch (IOException ex):
                    Console.WriteLine(ex)
                    return -1
                }
        }

        close():
            try
            {
                c_fileReader.Close()
            }
            catch (IOException ex): Console.WriteLine(ex) }
        }
    }
}

