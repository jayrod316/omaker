# omaker
A tool to split, rename, and organize CNC machine programs
 ## Description
 The quickest way to output all the programs on many modern CNC machines lumps all of the programs into one large file. This is quick and convenient, but this makes it difficult to extract individual programs to organize them into folders on a server for instance.
 ## Vision
This tool will take as input a directory of CNC programs dumped from a machine, and ouput the individual programs with names specified in the comment of the program name i.e. O1234(PROGRAM-NAME) will be named "PROGRAM-NAME" in a new directory. If no comment exists, the file in this example will be named O1234.
---
Some CNC controllers allow a "<PROGRAM-NAME>(COMMENT)" naming convention. In this case, the new file will be named as the contents between < and > and nothing will be done with the comment.

