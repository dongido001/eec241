#Developed by Onwuka Gideon [ Dongido ],
#For EEE department 2013/2014 federal polytechnic nekede EEC 241 ND2...
#Just for Business!,
#Atfer Business it later went Open Source!, enjoy, cheers!!
#dongidomed@gmail.com
#www.facebook.com/dongidomed
#phone : 08059794251
#leachers stay off...
 
import os,sys
import shutil
 
print '''
-------------------------------------------
!        developed  BY  D O N G I D O     !
!                                         !
!                    ENJOY!               !
-------------------------------------------
     '''
#function to check if 2 important folders are available[import & export]
def check_folders():
    print ""
    exit(1)
 
 
#writes to the file
def fix1(files,txt):
    fp = open(files,"a+")
    fp.seek(0,0)
    fp.write(txt)
    fp.write("\n")
    fp.close
 
#read files from the input folder, no be small thinking man...
def fix2(files):
    fp = open (files,"r")
    fp.seek(0,0)
    return_str = fp.readlines()
    fp.close
    return return_str
 
strd = raw_input("please, put the guy Name here >> ");
reg = raw_input("please, put the guy Reg No here >> ");
if strd == "":
    print "I cant continue, You can not have an empty name, bye!"
    exit(1)
if reg == "":
    print "hmmm, Till now you dont have reg No. u sure u come school ????"
   
#array that holds the code description...
s1 = """
'[question 1]
'This program will print "EEEE" 3 times ...
'Using Input statement
    """
s2 = """
'[question 2]
'using READ ... DATA state to calculate the volume of a
'cubiod...
'the program assumed
' cuboid lenght = 3, height = 4, height = 5
    """
s3 = """
'[question 3a]
'A program that converts a written formular into
'a qbasic equivalent and prints the result...
    """
s4 = """
'[question 3b]
'A program that converts a written formular into
    """
s5 = """
'[question 3c]
'A program that converts a written formular into
'a qbasic equivalent and prints the result...
    """
s6 = """
'[question 3d]
'A program that converts a written formular into
'a qbasic equivalent and prints the result...
    """
s7 = """
'[question 4]
'a program that stores the names,height,weight and age of 3 persons then prints it in a tabbular form
'it prints also the average of their height , weight and age...
    """
s8 = """
'[question 5]
' a program that print the first nine powers of 2
    """
s9 = """
'[question 6]
'A program for a cinema hall that decide the amount of ticket
'that a person will pay according to the person's age...
    """
s10 = """
'[question 7]
'prints a pyramid using the word below...
    """
s11 = """
REM [question 8]
REM prints the name and phone number of my 3 best friend :v
    """
s12 = """
'[question 9]
'I corrected the syntax error of the code and printed the results
    """
s13 = """
'[question 10]
'made some corection on the original program
    """
original_file = ["1.bas","2.bas","3a.bas","3b.bas","3c.bas","3d.bas","4.bas","5.bas","6.bas","7.bas","8.bas","9.bas","10.bas"]
txt = [s1,s13,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]
#checks if some important folders are available
#TODO
 
#gets the current working directory
inputf = os.getcwd() + "/import/" #input of the files
output = os.getcwd() + "/export/" #output of the files
 
#open a new directory for the user
cont = output + strd
os.mkdir( cont )
print "[+] New Folder \" %s \" Created Successfully!...\n" % strd
 
#change directory
os.chdir(cont) # to export directory
 
#create new empty file in the new created folder
#sorry if i did the below wrongly,
#I gat no internet connection so i couldnt check if there is a function that can handle it :D
#just used a tweak,, mine ..
 
for i in original_file:
    fp = open(strd + " " +i, "w")
    fp.close
   
print "[+] Creation done!................................\n"
 
print "[+] Now Writing your Name and Reg no to the files ...pls wait [+]"
 
listdir = os.getcwd()
det = os.listdir(listdir)
co = 0
lent = len(strd) + 1
 
for sd in det:
    strings = txt[co] +  "\n'BY " + strd + "\n'" + reg + "\n"
    fix1(sd,strings)
    sdf = fix2(inputf + sd[lent:] )
    for each in sdf:
        fix1(sd,each)
    print " [+]  " , sd , " => [success!]"
    co = co + 1
