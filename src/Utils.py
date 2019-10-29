# -*- coding: utf-8 -*-


def read_file(file_name_to_read):
    """
    This function reads the file given the file name as an input
    
    Inputs: 
        file_name_to_read - string, name of file you want to read
    
    outputs:
        content_of_file - string, the content of the file
    """

    # this way of doing it is disgusting, but honestly I don't think there
    # is a better way...
    file_name_to_read = '../put_files_to_read_here/' + file_name_to_read

    file_obj = open(file_name_to_read,'r')

    content_of_file = file_obj.read()
    
    file_obj.close()
    
    return content_of_file



if __name__ == "__main__":
    
    
    print('the file contains: ',read_file('temp_file.txt'))