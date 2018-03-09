#
# hw0pr3.py ~ recipe analysis
#
# Name(s): Tiancheng(Tony) Jiang 
#

#
# be sure your file runs from this location, 
# relative to the "recipes" files and directories
#


import os
import os.path
import shutil

def is_savory(filepath):
    """ returns true or false whether the recipe of this filepath is a sweet pie or not  
    """
    f = open(filepath,"r", encoding="latin1") 
    data = f.readlines()[2]   
    return ("Savory Pie" in data)
    f.close() 

def is_sweet(filepath):
    """ returns true or false whether the recipe of this filepath is a sweet pie or not  
    """
    f = open(filepath,"r", encoding="latin1") 
    data = f.readlines()[2]   
    return ("Sweet Pie" in data)
    f.close() 

def is_vegetarian(filepath):
    """ returns true or false whether the recipe of this filepath is savory or not  
    """
    f = open(filepath,"r", encoding="latin1") 
    data = f.readlines()   
    if ("Sweet Pie" in data[2]):
        for i in range(len(data)):
            if (('chicken' in data[i]) or ('beef' in data[i]) or ('pork' in data[i])):
                return False
            else:
                return True
    else:
        return False
    f.close()   

def listpies(path):
        

    AllFiles = list(os.walk(path))
    

    savory_pies = []
    sweet_pies = []
    vegetarian_pies = []


    for item in AllFiles:
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename 
            
            try:
                if (is_savory(filepath)):
                    savory_pies.insert(len(savory_pies), filepath)
                if (is_sweet(filepath)):
                    sweet_pies.insert(len(sweet_pies), filepath)
                if (is_vegetarian(filepath)):
                    vegetarian_pies.insert(len(vegetarian_pies), filepath)

            except PermissionError:  
                print("file", item, "couldn't be opened: permission error")
                data = ""

            except UnicodeDecodeError:
                print("file", item, "couldn't be opened: encoding error")
                data = "" 

            except FileNotFoundError:  
                print("file", item, "couldn't be opened: not found!")
                print("Check that you have the correct path...")
                data = ""
    return savory_pies, sweet_pies, vegetarian_pies   

def reorganize_pies():
    """copy all savory pie recipes into a directory called savory_recipes, 
    and all sweet pie recipes into a directory called sweet_recipes etc
    """
    path = "."
    os.mkdir('./savory_recipes')
    savories = './savory_recipes'
    os.mkdir('./sweet_recipes')
    sweets = './sweet_recipes'
    os.mkdir('./sweet_recipes/vegetarian_pies')
    vegetarians = './sweet_recipes/vegetarian_pies'

    savory_p, sweet_p, vegetarian_p = listpies(path)
    for files in savory_p:
        shutil.copy(files, savories)
    for files in sweet_p:
        shutil.copy(files, sweets)
    for files in vegetarian_p:
        shutil.copy(files, vegetarians) 

def find_num(s):
    """find string measurement of ingredient into number
    """
    measure = "" 
    if (s != ""  and isinstance(s, str)):
        if (s[0] == " "):
            return ""
        elif(s[0].isdigit()):
            return measure + s[0] + find_num(s[1:])
        else:
            return ""
    else:
        return ""
def find_ingredient(s):
    """find string measurement of ingredient into number
    """
    ingredient = "" 
    if (s != ""  and isinstance(s, str)):
        if (s[-1] == " "):
            return ""
        else:
            return ingredient + s[-1] + find_ingredient(s[:-1])
    else:
        return ""

            
def find_maxkilo(filepath):
    """ returns the maximum kilograms values in a recipe   
    """
    f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
    data = f.readlines()   # read all of the file's data
    max_kilo = 0
    max_ingredient = ""
    for i in range(len(data)):
        if ("kilograms" in data[i] and find_num(data[i]) != ''):
            kilo = int(find_num(data[i]))
            if (kilo > max_kilo):
                max_kilo = kilo
                max_ingredient = find_ingredient(data[i])[::-1]

    f.close()   
    return max_kilo, max_ingredient[:-1]

def find_max_kilo_recipe(path):
    """ returns the recipe with max kilogram values in all recipes 
    """

    AllFiles = list(os.walk(path))
    # print(AllFiles)    # just to check out what's up (v2)

    max_kilo_recipe = ""
    max_kilo_allfiles = 0
    max_kilo_ing = ""

    for item in AllFiles:
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            try:
                if (filename[-4:] == '.txt'):
                    max_kilo_file, max_kilo_file_ing = find_maxkilo(filepath) 
                    if (max_kilo_file > max_kilo_allfiles):
                        max_kilo_allfiles = max_kilo_file
                        max_kilo_recipe = filename
                        max_kilo_ing = max_kilo_file_ing


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
    return max_kilo_recipe, max_kilo_allfiles, max_kilo_ing

def find_cooktime(filepath):
    """return the cooking time in integer for each recipe. Parameter is the filepath 
    of a recipe
    """
    f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
    data = f.readlines()   # read all of the file's data
    last_line = data[len(data)-1]
    cook_time = ""
    
    if ("minutes" in last_line and last_line != ''):
        cook_time = last_line[-12:-9]
    f.close()   
    return int(cook_time)

def find_num_file_cook_greater40(path):
    """return number of recipes that cook over 40 minutes
    """
    # return 42  # just to check that it's working (v1)    

    AllFiles = list(os.walk(path))

    num_file_cooktime_under40 = 0

    for item in AllFiles:
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            try:
                if (filename[-4:] == '.txt'):
                    recipe_cooking_time = find_cooktime(filepath) 
                    if (recipe_cooking_time > 40):
                       num_file_cooktime_under40 += 1 

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
    return num_file_cooktime_under40

def find_maxcups(filepath):
    """ returns the recipe with max cupes values in one recipe
    """
    f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
    data = f.readlines()   # read all of the file's data
    max_cups = 0
    max_ingredient = ""
    for i in range(len(data)):
        if ("cups" in data[i] and find_num(data[i]) != ''):
            cups = int(find_num(data[i]))
            if (cups > max_cups):
                max_cups = cups
                max_ingredient = find_ingredient(data[i])[::-1]
    f.close()   
    return max_cups, max_ingredient[:-1]

def find_max_cups_recipe(path):
    """returns the recipe with max kilogram values in all recipes 
    """

    AllFiles = list(os.walk(path))

    max_cups_recipe = ""
    max_cups_allfiles = 0
    max_cups_ing = ""

    for item in AllFiles:
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            #print (filepath)
            try:
                if (filename[-4:] == '.txt'):
                    max_cups_file, max_cups_file_ing = find_maxcups(filepath) 
                    if (max_cups_file > max_cups_allfiles):
                        #print (max_kilo_file)
                        max_cups_allfiles = max_cups_file
                        max_cups_recipe = filename
                        max_cups_ing = max_cups_file_ing


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
    return max_cups_recipe, max_cups_allfiles, max_cups_ing

def find_recipe_size(filepath):
    """return the number of lines in a recipe 
    """
    f = open(filepath,"r", encoding="latin1") # latin1 is a very safe encoding
    data = f.readlines()   # read all of the file's data
    recipe_size = len(data)
    f.close()   
    return recipe_size

def find_recipe_longest_size(path):
    """return filename of largest recipe 
    """

    AllFiles = list(os.walk(path))

    recipe_longest = ""
    recipe_longest_size_all = 0

    for item in AllFiles:
        
        for filename in item[2]:
            filepath = item[0] + '/' + filename #os.path.join(path, item)
            try:
                if (filename[-4:] == '.txt'):
                    recipe_size = find_recipe_size(filepath) 
                    if (recipe_size > recipe_longest_size_all):
                       recipe_longest_size_all = recipe_size
                       recipe_longest = filename 

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
    return recipe_longest,recipe_longest_size_all


def main():
    """ overall function to run all examples """
    #reorganize_pies() reorganize pies into files of savories and sweets, and vegetarians within sweets 
    print("reorganize_pies organizes pies into files of savories and sweets, and vegetarians within sweets")
    reorganize_pies()

    #test find_max_kilo_recipe
    max_recipe, num_kilo, what_ing = find_max_kilo_recipe(".")
    print("The recipe that calls for the most kilograms of one ingredient is: ", max_recipe)
    print('\n')
    print("The recipe calls for: ", num_kilo, " of ", what_ing)
    print("\n")
    #personal question1:
    print("The followings are three of my own questions regarding the recipe folder\n")
    print("1. How many recipes have a cooking time greater than 40 minutes\n")
    q1_result = find_num_file_cook_greater40('.')
    print("The number of recipes that have a cooking time greater than 40 minutes is: ", q1_result,"\n")
    #personal question2: 
    print("2.Across all recipes, which recipe calls for the most cups of one ingredient?")
    q2_result1, q2_result2, q2_result3 = find_max_cups_recipe('.')
    print("The recipe that uses the most of cups of any ingredient is: ",q2_result1,". The ingredient is: ", q2_result3, "and it needs ", q2_result2, "many cups.\n")
    #personal question3: 
    print("3. What recipe is the longest? How many lines are there?")
    q3_result1, q3_result2 = find_recipe_longest_size('.')
    print("The longest recipe is: ", q3_result1, "and it has ", q3_result2, "lines.")




if __name__ == "__main__":
    main()

