using System;

using System.IO;

namespace cube
{
    public class RubikFileReader
    {
        Boolean c_fileIsOK;

        StreamReader   c_fileReader;

        public RubikFileReader()
        {
        }

        public RubikFileReader(String p_fileLocation)
        {
            try
            {
                c_fileReader = new StreamReader(p_fileLocation);
                c_fileIsOK = true;
            }
            catch (IOException ex)
            {
                Console.WriteLine(ex.Message);
                c_fileIsOK = false;
            }
        }

        public int read()
        {
            if (!c_fileIsOK)
                return -1;
            else
                try
                {
                    int readChar = c_fileReader.Read();
                    return readChar;
                }
                catch (IOException ex)
                {
                    Console.WriteLine(ex);
                    return -1;
                }
        }

        public void close()
        {
            try
            {
                c_fileReader.Close();
            }
            catch (IOException ex) { Console.WriteLine(ex); }
        }
    }
}

