#
# hw0pr2.py ~ phonebook analysis
#
# Name(s):Tiancheng(Tony) Jiang 
#

#
# be sure your file runs from this location, 
# relative to the "phonebook" directories
#


#
# hw0pr2.py ~ phonebook analysis
#
# Name(s): Tiancheng(Tony) Jiang 

# The Main may take a while to run all the main tests

#
# be sure your file runs from this location, 
# relative to the "phonebook" directories
#

import os
import os.path
import shutil



def how_many_txt_files(path):
    """ walks a whole directory structure
        and returns how many txt files are in it!

        call it with: how_many_txt_files(".")

        the (v1) (v2) etc. are different versions, to illustrate
        the process of _trying things out_ and _taking small steps_
    """
    # return 42  # just to check that it's working (v1)    

    AllFiles = list(os.walk(path))
    # print(AllFiles)    # just to check out what's up (v2)

    #print("AllFiles has length: ", len(AllFiles), "\n")
    totalCount = 0

    for item in AllFiles:
        # print("item is", item, "\n")    (v3)
        foldername, LoDirs, LoFiles = item   # cool!
        #print("In", foldername, "there are", end=" ")

        count = 0
        for filename in LoFiles:
            if filename[-3:] == "txt":
                count += 1
        #print(count, ".txt files")
        totalCount += count

    return totalCount   # this is not _quite_ correct!

def countdepth(s):
    """return the number of '/' contained in the path to find how deep the path is 
    """
    count = 0
    for i in range(len(s)):
        if (s[i] == '/'):
            count += 1
    return count 

def max_depth_dir(path):
    """returns the maximum number of times that it's possible 
    to move deeper into subdirectory
    """
    AllFiles = list(os.walk(path))
    longestPath = AllFiles[0][0]
    print(longestPath)
    for i in range(len(AllFiles)-1):
        if (countdepth(longestPath) < countdepth(AllFiles[i+1][0])):
            longestPath = AllFiles[i+1][0]
    return longestPath

def count_numInstring(s):
    """Returns the number is digits in a string
    """
    count = 0
    for i in range(len(s)):
        if (s[i].isdigit()):
            count += 1
    return count

def find_files_with10dig_phonenum(path):
    """return the number files that have 10 digit phonenumber in its content 
    """
    fileWith10dig = 0
    ListOfContents = os.listdir(path)

    for item in ListOfContents:
        newPath = path + "/" + item
        if os.path.isdir(newPath):
            fileWith10dig = fileWith10dig + find_files_with10dig_phonenum(newPath)
        else:
            filepath = os.path.join(path, item)
            try:
                f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
                data = f.readline()   # read all of the file's data
                if (count_numInstring(data) == 10):
                    fileWith10dig = fileWith10dig + 1
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""   
    return fileWith10dig


def find_files_909areacode_phonenum(path):
    """return the number files that have 909 as the phone number's area code 
    """
    count = 0
    ListOfContents = os.listdir(path)

    for item in ListOfContents:
        newPath = path + "/" + item
        if os.path.isdir(newPath):
            count = count + find_files_909areacode_phonenum(newPath)
        else:
            filepath = os.path.join(path, item)
            try:
                f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
                data = f.readline()   # read all of the file's data
                if (data[0:3] == "909" and count_numInstring(data) == 10):
                    count = count + 1
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""
 
    return count

def how_many_lastname(s, path):
    """ returns the number of files that contain the last name s(a string) in this path
    """
    AllFiles = list(os.walk(path))
    
    count = 0

    for item in AllFiles:
        
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename 
            
            try:
                f = open(filepath,"r", encoding="latin1") 
                data = f.readlines()[1]   # read all of the file's data
                if(',' in data):
                    if (data.startswith(s)):
                        count += 1
                else:
                    if (data.endswith(s)):
                        count += 1   
                f.close()         

            except PermissionError:  
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""
       

    return count   


def how_many_firstname(s, path):
    """ returns the number of files that contain the first name s(a string) in this path
    """
       

    AllFiles = list(os.walk(path))
    
    count = 0

    for item in AllFiles:
        
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename 
            try:
                f = open(filepath,"r", encoding="latin1") 
                data = f.readlines()[1]   
                if(',' in data):
                    if (data.endswith(s)):
                        count += 1
                else:
                    if (data.startswith(s)):
                        count += 1   
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""

    return count   



def how_many_more_than_10dig(path):
    """ returns the number of files that contain phone number with greater than 10 digits 
    """
       

    AllFiles = list(os.walk(path))
    
    count = 0

    for item in AllFiles:
       
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename 
            try:
                f = open(filepath,"r", encoding="latin1") 
                data = f.readlines()[0]   # read all of the file's data
                if(count_numInstring(data) > 10):
                    count += 1
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""

    return count   

#my own three questions
#1 what is the most common area code here
from collections import defaultdict      # be sure to import it!

def most_common_areacode(path):
    """ 
    Question: what is the most common area code here?
    Answer: to this question is area code (442)

    I did this question by creating defaultdict with all the areacodes as key 
    by looping through all files. Then I pick the area code have the most values to find 
    the one that appears the most often

    """
       

    AllFiles = list(os.walk(path))
    
    
    areacodes = defaultdict(int)
    for item in AllFiles:
        
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            try:
                f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
                data = f.readlines()[0]   # read all of the file's data
                ac = data[0:3]
                areacodes[ac] += 1
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""
    counter = 0
    mc = ""
    for code in areacodes.keys():
        if (areacodes[code] > counter):
            mc = code
            counter = areacodes[code]
    return  mc  

#2 
def how_many_substring42(path):
    """ 
    Question: How many phone numbers have substring 42 in it
    Answer: 2500

    I looped through all the phonebook files and check if each phone number contains 42 or not

    """

    AllFiles = list(os.walk(path))
    
    
    count = 0
    for item in AllFiles:
       
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            try:
                f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
                data = f.readlines()[0]   # read all of the file's data
                if ("42" in data):
                    count += 1
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""

    return count   

#3
def firstnamesize(s):
    """return the number of letters for the first name
    """
    if(s == ""):
        return 0
    else:
        if(',' in s):
            if (s[-1] == ' ' ):
                return -1
            else:
                return 1 + firstnamesize(s[:-1])
        else:
            if (s[0] == ' ' ):
                return 0
            else:
                return 1 + firstnamesize(s[1:])

def size_longest_firstname(path):
    """ 
    Question: what is the name with longest firstname in phonebook?
    Answer: Providencia Hamlett and has length 11 for firstname 

    I did this question by creating defaultdict with all the names as key 
    by looping through all files. Then I pick the name that has the longest 
    first name by using the helper function above

    """

    AllFiles = list(os.walk(path))
    
    
    longest = 0
    names = defaultdict(int)
    for item in AllFiles:
        
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            try:
                f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
                data = f.readlines()[1]   # read all of the file's data
                names[data] = firstnamesize(data)
                
                
                f.close()         # close the file

            except PermissionError:  # example of "exceptions": atypical errors
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" # no data

            except FileNotFoundError:  # try it with and without this block...
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""
    
    counter = 0
    n = ""
    for i in names.keys():
        if (names[i] > counter):
            n = i
            counter = names[i]
    return n, counter 

def main():
    """ overall function to run all examples """

    print("Start of main()\n")

    num_txt_files = how_many_txt_files(".")
    print("num_txt_files in . is:", num_txt_files)
    print('\n')
    max_depth_directories = countdepth(max_depth_dir("."))
    print("max_depth_directories in . is:", max_depth_directories)
    print('\n')
    path_deepest_directory = max_depth_dir(".")
    print("path_deepest_directory in . is:", path_deepest_directory)
    print('\n')
    num_files_with10dig_phone_number = find_files_with10dig_phonenum('.')
    print("num_files_with10dig_phone_numer in . is:", num_files_with10dig_phone_number)
    print('\n')
    num_files_with10dig_with909areacode = find_files_909areacode_phonenum('.')
    print("num_files_with10dig_with909areacode in . is:", num_files_with10dig_with909areacode)
    print('\n')
    result = how_many_lastname('Davis', '.')
    print("number of people with last name 'Davis':", result)
    print('\n')
    result0 = how_many_lastname('Canel', '.')
    print("number of people with last name 'Canel':", result0)
    print('\n')
    result1 = how_many_firstname('Davis','.')
    print("number of people with first name 'Davis':", result1)
    print('\n')
    result3 = how_many_firstname('Oliva','.')
    print("number of people with first name 'Oliva':", result3)
    print('\n')
    result4 = how_many_more_than_10dig('.')
    print("number of people with phonenumber of greater than 10 digits :", result4)
    print('\n')
    print("THE FOLLOWING ARE MY OWN QUESTIONS:")
    print("1. How many people have substring 42 in his or her phone number?")
    result5 = how_many_substring42('.')
    print("number of people with phonenumber that has '42' in it :", result5)
    print('\n')
    result6 = most_common_areacode('.')
    print("2. what is the most common area code out of all phone numbers?")
    print("The most common area code of all phonenumbers is :", result6)
    print('\n')
    result7, size = size_longest_firstname('.')
    print("3. what is the longest firstname in the phonebook and its length?")
    print("The size of longest firstname is:", result7, "with length", size)
    print('\n')




if __name__ == "__main__":
    main()



