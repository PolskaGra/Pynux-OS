import os
import getpass
import time
import sys
import shutil
import platform

os.system('cls')

def Loadnig():
    Loading = '''
   .-..    ___  ___   ___ .-.    ___  ___   ___  ___      .--.       .--.    
  /    \  (   )(   ) (   )   \  (   )(   ) (   )(   )    /    \    /  _  \   
 ' .-,  ;  | |  | |   |  .-. .   | |  | |   | |  | |    |  .-. ;  . .' `. ;  
 | |  . |  | |  | |   | |  | |   | |  | |    \ `' /     | |  | |  | '   | |  
 | |  | |  | '  | |   | |  | |   | |  | |    / ,. \     | |  | |  _\_`.(___) 
 | |  | |  '  `-' |   | |  | |   | |  | |   ' .  ; .    | |  | | (   ). '.   
 | |  ' |   `.__. |   | |  | |   | |  ; '   | |  | |    | '  | |  | |  `\ |  
 | `-'  '   ___ | |   | |  | |   ' `-'  /   | |  | |    '  `-' /  ; '._,' '  
 | \__.'   (   )' |  (___)(___)   '.__.'   (___)(___)    `.__.'    '.___.'   V.1.2.3
 | |        ; `-' '                                                          
(___)        .__.'                                                           
'''
    print(Loading)
    print('CREATED BY PĄCZEK')
    print("COMMAND LIST = HELP")
    
Loadnig()                      

Current_Dir = os.getcwd()
HostName = platform.node()
Username = getpass.getuser()
HostUserName = str(Username) + "@" + str(HostName)
Default_Dir = Current_Dir

while True:
    first = False
    def Dir_Check(Command):
        global first
        if Command.startswith("C:\\", 0, 3):
            first = True
        elif Command.startswith("c:\\", 0, 3):
            first = True
        elif Command.startswith("B:\\", 0, 3):
            first = True
        elif Command.startswith("b:\\", 0, 3):
            first = True
        elif Command.startswith("D:\\", 0, 3):
            first = True
        elif Command.startswith("d:\\", 0, 3):
             first = True
        elif Command.startswith("E:\\", 0, 3):
            first = True
        elif Command.startswith("e:\\", 0, 3):
            first = True
        elif Command.startswith("F:\\", 0, 3):
            first = True
        elif Command.startswith("f:\\", 0, 3):
            first = True
        elif Command.startswith("G:\\", 0, 3):
            first = True
        elif Command.startswith("g:\\", 0, 3):
            first = True
        elif Command.startswith("H:\\", 0, 3):
            first = True
        elif Command.startswith("h:\\", 0, 3):
            first = True
        elif Command.startswith("I:\\", 0, 3):
            first = True
        elif Command.startswith("i:\\", 0, 3):
            first = True
        elif Command.startswith("J:\\", 0, 3):
            first = True
        elif Command.startswith("j:\\", 0, 3):
            first = True
        elif Command.startswith("K:\\", 0, 3):
            first = True
        elif Command.startswith("k:\\", 0, 3):
            first = True
        elif Command.startswith("L:\\", 0, 3):
            first = True
        elif Command.startswith("l:\\", 0, 3):
            first = True
        elif Command.startswith("M:\\", 0, 3):
            first = True
        elif Command.startswith("m:\\", 0, 3):
            first = True
        elif Command.startswith("N:\\", 0, 3):
            first = True
        elif Command.startswith("n:\\", 0, 3):
            first = True
        elif Command.startswith("O:\\", 0, 3):
            first = True
        elif Command.startswith("o:\\", 0, 3):
            first = True
        elif Command.startswith("P:\\", 0, 3):
            first = True
        elif Command.startswith("p:\\", 0, 3):
            first = True
        elif Command.startswith("Q:\\", 0, 3):
            first = True
        elif Command.startswith("q:\\", 0, 3):
            first = True
        elif Command.startswith("R:\\", 0, 3):
            first = True
        elif Command.startswith("r:\\", 0, 3):
            first = True
        elif Command.startswith("S:\\", 0, 3):
            first = True
        elif Command.startswith("s:\\", 0, 3):
            first = True
        elif Command.startswith("T:\\", 0, 3):
            first = True2
        elif Command.startswith("t:\\", 0, 3):
            first = True
        elif Command.startswith("U:\\", 0, 3):
            first = True
        elif Command.startswith("u:\\", 0, 3):
            first = True
        elif Command.startswith("V:\\", 0, 3):
            first = True
        elif Command.startswith("v:\\", 0, 3):
            first = True
        elif Command.startswith("W:\\", 0, 3):
            first = True
        elif Command.startswith("w:\\", 0, 3):
            first = True
        elif Command.startswith("X:\\", 0, 3):
            first = True
        elif Command.startswith("x:\\", 0, 3):
            first = True
        elif Command.startswith("Y:\\", 0, 3):
            first = True
        elif Command.startswith("y:\\", 0, 3):
            first = True
        elif Command.startswith("Z:\\", 0, 3):
            first = True
        elif Command.startswith("z:\\", 0, 3):
            first = True
        else:
            first = False
            
    Default_Cmd = HostUserName + " " + Default_Dir + '''
$ ''' 
    print(" ")
    Cmd = input(Default_Cmd)
    if Cmd.startswith("cd "):
        PATH = Cmd.replace("cd ", "", 1) 
        Dir_Check(PATH)
        czy_istnieje = os.path.exists(PATH)
        
        if first == True and czy_istnieje == True:
            Default_Dir = PATH
        elif first == False and czy_istnieje == False:
            Full_Path = Default_Dir + "\\" + PATH
            czy_istnieje = os.path.exists(Full_Path)
            if czy_istnieje == True:
                Default_Dir = Full_Path
            else:
                print("DIR DOESN'T EXIST")
        else:
            print("DIR DOESN'T EXIST")
            
    elif Cmd.startswith("open "):
        File_Name = Cmd.replace('open ', '', 1)
        try:
            f = open(Default_Dir + "\\" + File_Name, "r", encoding="utf8")
            print(f.read())
        except OSError:
            print("OPENING FILE %s FAILED" % File_Name)
            
    elif Cmd.startswith("cpfile "):
        FileAndDir = Cmd.replace('cpfile ', '', 1)
        File_and_Dir = FileAndDir.split(", ")
        File = File_and_Dir[0]
        Dir = File_and_Dir[1]
        Old_Copy_File_Path = Default_Dir + "\\" + File
        Dir_Check(Dir)            
        if first == True:
            New_Copy_File_Path = Dir + "\\" + File
            try:
                shutil.copy(Old_Copy_File_Path, New_Copy_File_Path)
            except OSError:
                print("COPYING A FILE FAILED")
            else:
                print("SUCCESSFULLY COPIED A FILE")

        elif first == False:
            dla_czy_istnieje = Default_Dir + "\\" + Dir
            czy_istnieje = os.path.exists(dla_czy_istnieje)
            if czy_istnieje == True:
                New_Copy_File_Path = Default_Dir + "\\" + Dir + "\\" + File
                try:
                    shutil.copy(Old_Copy_File_Path, New_Copy_File_Path)
                except OSError:
                    print("COPYING A FILE FAILED")
                else:
                    print("SUCCESSFULLY COPIED A FILE")
            else:
                print("DIR %s DOESN'T EXIST" % dla_czy_istnieje) 
            
    elif Cmd.startswith('cpdir '):
        DirAndDir = Cmd.replace('cpdir ', '', 1)
        Dir_and_Dir = DirAndDir.split(", ")
        DirToCopy = Dir_and_Dir[0]
        CopyThere = Dir_and_Dir[1]
        Old_Copy_Dir_Path = Default_Dir + "\\" + DirToCopy
        Dir_Check(CopyThere)            
        if first == True:
            New_Copy_Dir_Path = CopyThere + "\\"  +DirToCopy
            try:
                shutil.copytree(Old_Copy_Dir_Path, New_Copy_Dir_Path)
            except OSError:
                print("COPYING A DIR FAILED")
            else:
                print("SUCCESSFULLY COPIED A DIR")
            
        elif first == False:
            dla_czy_istnieje = Default_Dir + CopyThere
            czy_istnieje = os.path.exists(dla_czy_istnieje)
            if czy_istnieje == True:
                New_Copy_Dir_Path = Default_Dir + CopyThere + "\\" + DirToCopy
                try:
                    shutil.copytree(Old_Copy_Dir_Path, New_Copy_Dir_Path)
                except OSError:
                    print("COPYING A DIR FAILED")
                else:
                    print("SUCCESSFULLY COPIED A DIR")
            else:
                print("DIR %s DOESN'T EXIST" % dla_czy_istnieje) 
        
    elif Cmd.startswith("rnfile "):
        File_Names = Cmd.replace("rnfile ", "", 1)
        File_Names_List = File_Names.split(", ")
        Old_File_Path = Default_Dir + "\\" + File_Names_List[0]
        New_File_Path = Default_Dir + "\\" + File_Names_List[1]
        try:
            os.rename(Old_File_Path, New_File_Path)
        except OSError:
            print ("RENAMING OF THE FILE %s FAILED" % File_Names_List[0])
        else:
            print("SUCCESSFULLY RENAMED THE FILE %s" % File_Names_List[0])

    elif Cmd.startswith("rndir "):
        DirNames = Cmd.replace("rndir ", "", 1)
        Dir_Names_List = DirNames.split(", ")
        Old_Dir_Path = Default_Dir + "\\" + Dir_Names_List[0]
        New_Dir_Path = Default_Dir + "\\" + Dir_Names_List[1]
        try:
            os.rename(Old_Dir_Path, New_Dir_Path)
        except OSError:
            print ("RENAMING OF THE DIR %s FAILED" % Dir_Names_List[0])
        else:
            print("SUCCESSFULLY RENAMED THE DIR %s" % Dir_Names_List[0])
            
    elif Cmd.startswith("mvfile "):
        FileAndDir = Cmd.replace('mvfile ', '', 1)
        File_and_Dir = FileAndDir.split(", ")
        FileToCopy = File_and_Dir[0]
        WhereCopyFile = File_and_Dir[1]
        Old_File_Path = Default_Dir + "\\" + FileToCopy
        Dir_Check(WhereCopyFile)            
        if first == True:
            New_File_Path = WhereCopyFile + "\\" + FileToCopy
            try:
                shutil.copy(Old_File_Path, New_File_Path)
                os.remove(Old_File_Path)
            except OSError:
                print("MOVING A FILE FAILED")
            else:
                print("SUCCESSFULLY MOVE A FILE")

        elif first == False:
            dla_czy_istnieje = Default_Dir + "\\" + WhereCopyFile
            czy_istnieje = os.path.exists(dla_czy_istnieje)
            if czy_istnieje == True:
                New_File_Path = Default_Dir + "\\" + WhereCopyFile + "\\" + FileToCopy
                try:
                    shutil.copy(Old_File_Path, New_File_Path)
                    os.remove(Old_File_Path)
                except OSError:
                    print("MOVING A FILE FAILED")
                else:
                    print("SUCCESSFULLY MOVED A FILE")
            else:
                print("DIR %s DOESN'T EXIST" % dla_czy_istnieje)
        
    elif Cmd.startswith("mvdir "):
        DirAndDir = Cmd.replace('mvdir ', '', 1)
        Dir_and_Dir = DirAndDir.split(", ")
        DirToMove = Dir_and_Dir[0]
        WhereMoveDir = Dir_and_Dir[1]
        Old_Dir_Path = Default_Dir + "\\" + DirToMove
        Dir_Check(Old_Dir_Path)            
        if first == True:
            New_Dir_Path = WhereMoveDir + DirToMove
            try:
                shutil.copytree(Old_Dir_Path, New_Dir_Path)
                shutil.rmtree(Old_Dir_Path)
            except OSError:
                print("MOVING A DIR FAILED")
            else:
                print("SUCCESSFULLY MOVED A DIR")
            
        elif first == False:
            dla_czy_istnieje = Default_Dir + "\\" +  Command
            czy_istnieje = os.path.exists(dla_czy_istnieje)
            if czy_istnieje == True:
                New_Dir_Path = Default_Dir + "\\" + Command + "\\" + Dir
                try:
                    shutil.copytree(Old_Dir_Path, New_Dir_Path)
                    shutil.rmtree(Old_Dir_Path)
                except OSError:
                    print("MOVING A DIR FAILED")
                else:
                    print("SUCCESSFULLY MOVED A DIR")
            else:
                print("DIR %s DOESN'T EXIST" % dla_czy_istnieje) 
     
    elif Cmd.startswith("python "):
        File_Name = Cmd.replace('python ', '', 1)
        File_Dir = Default_Dir + "\\" + File_Name
        try:
            print(" ")
            os.system(File_Dir)
        except OSError:
            print("PLAYING FILE FAILED")
    

    elif Cmd == "LD" or Cmd == "Ld" or Cmd == "ld": 
        dir_list = os.listdir(Default_Dir)
        for dir_list in dir_list:
            print(dir_list)
            
    elif Cmd.startswith("mkfile "):
        File_Name = Cmd.replace("mkfile ", "", 1)
        Path = Default_Dir + "\\" + File_Name
        
        try:
            with open(Path, 'w', encoding='utf-8') as f:
                line1 = input("1:  ")
                line2 = input("2:  ")
                line3 = input("3:  ")
                line4 = input("4:  ")
                line5 = input("5:  ")
                line6 = input("6:  ")
                line7 = input("7:  ")
                line8 = input("8:  ")
                line9 = input("9:  ")
                line10 = input("10: ")
                line11 = input("11: ")
                line12 = input("12: ")
                line13 = input("13: ")
                line14 = input("14: ")
                line15 = input("15: ")
                line16 = input("16: ")
                line17 = input("17: ")
                line18 = input("18: ")
                line19 = input("19: ")
                line20 = input("20: ")
                line21 = input("21: ")
                line22 = input("22: ")
                line23 = input("23: ")
                line24 = input("24: ")
                line25 = input("25: ")
                f.write(line1)
                f.write("\n")
                f.write(line2)
                f.write("\n")
                f.write(line3)
                f.write("\n")
                f.write(line4)
                f.write("\n")
                f.write(line5)
                f.write("\n")
                f.write(line6)
                f.write("\n")
                f.write(line7)
                f.write("\n")
                f.write(line8)
                f.write("\n")
                f.write(line9)
                f.write("\n")
                f.write(line10)
                f.write("\n")
                f.write(line11)
                f.write("\n")
                f.write(line12)
                f.write("\n")
                f.write(line13)
                f.write("\n")
                f.write(line14)
                f.write("\n")
                f.write(line15)
                f.write("\n")
                f.write(line16)
                f.write("\n")
                f.write(line17)
                f.write("\n")
                f.write(line18)
                f.write("\n")
                f.write(line19)
                f.write("\n")
                f.write(line20)
                f.write("\n")
                f.write(line21)
                f.write("\n")
                f.write(line22)
                f.write("\n")
                f.write(line23)
                f.write("\n")
                f.write(line24)
                f.write("\n")
                f.write(line25)

        except FileNotFoundError:
            print ("CREATION OF THE DIRECTORY %s FAILED" % Command)
        else:
            print(" ")
            
    elif Cmd == "EXIT" or Cmd == "Exit" or Cmd == "exit":
        exit()
            
    elif Cmd == 'Math' or Cmd == 'MATH' or Cmd == 'math':
        print(eval(input()))
       
    elif Cmd.startswith('delfile '):
        File_Name = Cmd.replace("delfile ", "", 1)
        Del_Path = Default_Dir + "\\" + File_Name
        try:
            os.remove(Del_Path)
        except OSError:
            print ("DELETION OF THE FILE %s FAILED" % File_Name)
        else:
            print("SUCCESSFULLY DELETE THE FILE %s" % File_Name)

    elif Cmd.startswith('deldir '):
        Dir_Name = Cmd.replace("deldir ", "", 1)
        Del_Path = Default_Dir + "\\" + Dir_Name
        try:
            shutil.rmtree(Del_Path)
        except OSError:
            print ("DELETION OF THE DIRECTORY %s FAILED" % Del_Path)
        else:
            print("SUCCESSFULLY DELETE THE DIRECTORY %s" % Del_Path)
        
        
    elif Cmd.startswith("mkdir "):
        Dir_Name = Cmd.replace("mkdir ", "", 1)
        Path = Default_Dir + "\\" + Dir_Name
        try:
            os.makedirs(Path)
        except OSError:
            print ("CREATION OF THE DIRECTORY %s FAILED" % Path)
        else:
            print ("SUCCESSFULLY CREATED THE DIRECTORY %s" % Path)

    elif Cmd.startswith("cls"):
        os.system('cls')

    elif Cmd.startswith("ddtufs"):
        drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":\\") ]
        for drives in drives:
            total, used, free = shutil.disk_usage(drives)
            print(drives + "\\    Total: " + str((total // (2**30))) + " GiB    Used: " + str((used // (2**30))) + " GiB    Free: " + str((free // (2**30))) + " GiB")

    elif Cmd.startswith("print"):
        what_to_print = Cmd.replace("print ", "", 1)
        userandsysenv = os.environ
        uase = ["$" + userandsysenv for userandsysenv in userandsysenv]
        what_print = what_to_print.replace("$", "", 1)
        if what_print.startswith('str<'):
            printfs = what_print.replace('str<', '', 1)
            printf_len = len(printfs)
            print(printfs)
        else:
            what = os.getenv(what_print)
            print(what)
                                  
    else:
        print("THERE IS NO SUCH COMMAND LIKE",'"'+Cmd+'"')          
