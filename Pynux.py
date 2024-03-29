import os
import getpass
import time
import sys
import shutil
import platform
import Dir
from var import xlsfilename, xlsfilenameorg, Current_Dir, Default_Dir
import xlsxwriter
import openpyxl
from googlesearch import search

#----------------------------------------------------------------------------------------
# Co Dodac:
# ~ gry
# = Tord (word w terminalu) / Theet (excel w terminalu) / Toint (Moze power point w terminalu)
# - Script programming lang (Pyx)
# - graphics in terminal for pyx
# - paczki xd
# - przekdladanit stron html xddddddd
# - Mozliwosc wysylania emaily xddddddddddddddddddd
# = Gzip i Tar 
# - hasla (Dla usuwania plikow admina)
# - multiple files operations
#-----------------------------------------------------------------------------------------

os.system('cls')

def Loadnig():
    Loading = '''
   .-..    ___  ___   ___ .-.    ___  ___   ___  ___   
  /    \  (   )(   ) (   )   \  (   )(   ) (   )(   ) 
 ' .-,  ;  | |  | |   |  .-. .   | |  | |   | |  | |  
 | |  . |  | |  | |   | |  | |   | |  | |    \ `' /   
 | |  | |  | '  | |   | |  | |   | |  | |    / ,. \    
 | |  | |  '  `-' |   | |  | |   | |  | |   ' .  ; .   
 | |  ' |   `.__. |   | |  | |   | |  ; '   | |  | |   
 | `-'  '   ___ | |   | |  | |   ' `-'  /   | |  | |   
 | \__.'   (   )' |  (___)(___)   '.__.'   (___)(___)  
 | |        ; `-' '                                                          
(___)        .__.'                                                            '''

    print(Loading)
    print('CREATED BY PACZEK')
    print("COMMAND LIST = HELP")
    
Loadnig()                      

HostName = platform.node()
Username = getpass.getuser()
HostUserName = str(Username) + "~" + str(HostName)
cmd_layout = "windows"
Default_Dir_print = Default_Dir

while True:
    Default_List = os.listdir(Default_Dir)
    first = False
    if Default_Dir.startswith( os.path.expanduser( '~' )):
        fds = Default_Dir.replace( os.path.expanduser( '~' ), "~",1)
        DDP = fds.replace("\\","/")
        Default_Dir_print = DDP
    else:
        fds = Default_Dir.split(":\\")
        fds1 = fds[1].replace("\\", "/")
        DDP = "/" + fds[0].lower() + "/" + fds1
        Default_Dir_print = DDP

    Cmd = input(f"\n{HostUserName} {Default_Dir_print} \n# ")        
    if Cmd.startswith("cd"):
        PATH = Cmd.replace("cd ", "", 1) 
        Dir.Dir_Check(PATH)
        czy_istnieje = os.path.exists(PATH)

        if PATH.startswith(".."):
            peth = os.path.normpath(Default_Dir + os.sep + os.pardir)
            puth = os.path.normpath(peth)
            Default_Dir = puth

        elif PATH == "~":
            def_Dir = os.path.expanduser( '~' )
            puth = os.path.normpath(def_Dir)
            Default_Dir = puth

        elif PATH == ".":
            print()
            
        else:
            if first == True and czy_istnieje == True:
                puth = os.path.normpath(PATH)
                Default_Dir = puth
            elif first == False and czy_istnieje == False:
                Full_Path = Default_Dir + "\\" + PATH
                czy_istnieje = os.path.exists(Full_Path)
                if czy_istnieje == True:
                    puth = os.path.normpath(Full_Path)
                    Default_Dir = puth
                else:
                    print("DIR DOESN'T EXIST")
            else:
                print("DIR DOESN'T EXIST")

    elif Cmd.startswith("open"):
        File_Name = Cmd.replace('open ', '', 1)
        Dir.Dir_Check(File_Name)
        czy_istnieje = os.path.exists(File_Name)
        if first == True and czy_istnieje == True:
            try:
                Plik = str(File_Name)
                ilebajtowwazyplik = os.path.getsize(Plik)
                Data_stworzenia1 = os.path.getctime(File_Name)
                Data_stworzenia2 = time.ctime(Data_stworzenia1)
                ilepotrzebaplik = str(ilebajtowwazyplik // 1024)
                printf = f"--{File_Name}----{ilepotrzebaplik}-kb----{Data_stworzenia2}--"
                pritf = printf.replace(" ", "-")
                print(pritf)
                print("")
                f = open(Plik, "r", encoding="utf8")
                print(f.read())
            except OSError:
                print("OPENING FILE %s FAILED" % File_Name)            

        else:
            try:
                Plik = str(Default_Dir) + "\\" + str(File_Name)
                ilebajtowwazyplik = os.path.getsize(Plik)
                Data_stworzenia1 = os.path.getctime(Default_Dir + "\\" + File_Name)
                Data_stworzenia2 = time.ctime(Data_stworzenia1)
                ilepotrzebaplik = str(ilebajtowwazyplik // 1024)
                printlen = len(f"{File_Name} || {ilepotrzebaplik} kb || {Data_stworzenia2}")
                print(f"{printlen}")
                print(f"{Default_Dir}\\{File_Name} || {ilepotrzebaplik} kb || {Data_stworzenia2}")
                f = open(Plik, "r", encoding="utf8")
                print(f.read())
            except OSError:
                print("OPENING FILE %s FAILED" % File_Name)
            
    elif Cmd.startswith("cpfile"):
        FileAndDir = Cmd.replace('cpfile ', '', 1)
        File_and_Dir = FileAndDir.split(", ")
        File = File_and_Dir[0]
        Dir = File_and_Dir[1]
        Dir.Dir_Check(Dir)
        Old_Copy_File_Path = Default_Dir + "\\" + File
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
            
    elif Cmd.startswith('cpdir'):
        DirAndDir = Cmd.replace('cpdir ', '', 1)
        Dir_and_Dir = DirAndDir.split(", ")
        DirToCopy = Dir_and_Dir[0]
        CopyThere = Dir_and_Dir[1]
        Old_Copy_Dir_Path = Default_Dir + "\\" + DirToCopy
        Dir.Dir_Check(CopyThere)            
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
        
    elif Cmd.startswith("rnfile"):
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

    elif Cmd.startswith("rndir"):
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
            
    elif Cmd.startswith("mvfile"):
        FileAndDir = Cmd.replace('mvfile ', '', 1)
        File_and_Dir = FileAndDir.split(", ")
        FileToCopy = File_and_Dir[0]
        WhereCopyFile = File_and_Dir[1]
        Old_File_Path = Default_Dir + "\\" + FileToCopy
        Dir.Dir_Check(WhereCopyFile)            
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
        
    elif Cmd.startswith("mvdir"):
        DirAndDir = Cmd.replace('mvdir ', '', 1)
        Dir_and_Dir = DirAndDir.split(", ")
        DirToMove = Dir_and_Dir[0]
        WhereMoveDir = Dir_and_Dir[1]
        Old_Dir_Path = Default_Dir + "\\" + DirToMove
        Dir.Dir_Check(Old_Dir_Path)            
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
     
    elif Cmd in Default_List:
        print(Cmd)
        os.system(Cmd)
                
    elif Cmd.startswith("micro"):
        VimCommand = Cmd.replace('micro ', '', 1)
        try:
            os.system('cmd /c ' + Current_Dir + "\\micro\\" + "micro.exe " + Default_Dir + "\\" + VimCommand)
        except OSError:
            print("PLAYING FILE FAILED")

    # Trzeba naprawic zeby wszystko dizalalo w tych samych folderach
    # WAZNE
    elif Cmd.startswith("cmd"):
        VimCommand = Cmd.replace('cmd ', '', 1)
        os.system('cmd /c ' + VimCommand)
        
    elif Cmd == "LD" or Cmd == "Ld" or Cmd == "ld": 
        dir_list = os.listdir(Default_Dir)
        print(".")
        print("..")
        for dir_list in dir_list:
            print(dir_list)
            
    elif Cmd.startswith("touch"):
        File_Name = Cmd.replace("touch ", "", 1)
        Path = Default_Dir + "\\" + File_Name
        
        try:
            with open(Path, 'w', encoding='utf-8') as f:
                f.write("\n")

        except FileNotFoundError:
            print ("CREATION OF THE FILE %s FAILED" % Command)
        else:
            print(" ")
            
    elif Cmd == "EXIT" or Cmd == "Exit" or Cmd == "exit":
        exit()
            
    elif Cmd.startswith('math'):
        question = Cmd.replace('math ', '', 1)
        print(eval(question))
       
    elif Cmd.startswith('delfile'):
        File_Name = Cmd.replace("delfile ", "", 1)
        Del_Path = Default_Dir + "\\" + File_Name
        try:
            os.remove(Del_Path)
        except OSError:
            print ("DELETION OF THE FILE %s FAILED" % File_Name)
        else:
            print("SUCCESSFULLY DELETE THE FILE %s" % File_Name)

    elif Cmd.startswith('deldir'):
        Dir_Name = Cmd.replace("deldir ", "", 1)
        Del_Path = Default_Dir + "\\" + Dir_Name
        try:
            shutil.rmtree(Del_Path)
        except OSError:
            print ("DELETION OF THE DIRECTORY %s FAILED" % Del_Path)
        else:
            print("SUCCESSFULLY DELETE THE DIRECTORY %s" % Del_Path)
        
        
    elif Cmd.startswith("mkdir"):
        Dir_Name = Cmd.replace("mkdir ", "", 1)
        Dir_Check(Dir_Name)
        czy_istnieje = os.path.exists(Dir_Name)
        print(Dir_Check(Dir_Name))
        print(czy_istnieje)
        if Dir_Check == None and czy_istnieje == False:
            Path = Default_Dir + "\\" + Dir_Name
            try:
                os.makedirs(Path)
            except OSError:
                print("CREATION OF THE DIRECTORY %s FAILED" % Path)
            else:
                print("SUCCESSFULLY CREATED THE DIRECTORY %s" % Path)
        elif Dir_Check == True and czy_istnieje == False:
            try:
                os.makedirs(Path)
            except OSError:
                print("CREATION OF THE DIRECTORY %s FAILED" % Path)
            else:
                print("SUCCESSFULLY CREATED THE DIRECTORY %s" % Path)

    elif Cmd.startswith("cls"):
        os.system('cls') 
    elif Cmd.startswith("clear"):
        os.system('cls')

    elif Cmd.startswith("dds"):
        drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
        for drives in drives:
            total, used, free = shutil.disk_usage(drives)
            driv = drives + "\\"
            print(drives + "\\    Total: " + str((total // (2**30))) + " GiB    Used: " + str((used // (2**30))) + " GiB    Free: " + str((free // (2**30))) + " GiB")

#Damy Rade
            
    elif Cmd.startswith("search"):
        query = Cmd.replace("search ", "",1)
        print()
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(j)
        
    elif Cmd.startswith("tted"):
        Ttked = Cmd.replace("tted", "", 1)
        Ted = Ttked.replace(" ","",1)
        os.system("python " +  Current_Dir + "\\" + "Tted.py " + Default_Dir + "\\" + Ted)
        os.system('cls')

    # jeszcze tego nie rub, odpocznij tomus  :)
    elif Cmd.startswith("theet"):
        filename = Cmd.replace("theet","",1)
        if filename == "":
            xlsfilename = xlsfilenameorg
            os.system("python " + Current_Dir + "\\" + "theet.py")
        elif filename.startswith(" open "):
            fname = filename.replace(" open ","",1)
            book = openpyxl.load_workbook(Default_Dir + "\\" + fname)
            sheet = book.active
            cells = sheet['A1': 'B6']
            for c1, c2 in cells:
                print(f"{c1.value} {c2.value}")
        else:
            fname = filename.replace(" ","",1)
            xlsfilename = fname
            os.system("python " + Current_Dir + "\\" + "theet.py")
            
            
        
    elif Cmd.startswith("out"):
        what_to_print = Cmd.replace("out ", "", 1)
        userandsysenv = os.environ
        uase = ["$" + userandsysenv for userandsysenv in userandsysenv]
        what_print = what_to_print.replace("$", "", 1)
        if what_print.startswith('str<'):
            printfs = what_print.replace('str<', '', 1)
            printf_len = len(printfs)
            print(printfs)
        elif what_print.startswith('$'):
            what = os.getenv(what_print)
            print(what)
        else:
            print(what_to_print)

    # dokoncz
    #elif Cmd.startswith("zip"):
    #    CmdZip = Cmd.replace("zip ","",1)
    #    if ", " in CmdZip:
    #        ZipAFilesName = CmdZip.split(", ")
    #         ZipAFiles = ZipAFilesName[0].split(" ")
    #        ct = 1
    #        for a in ZipAFilesName:
    #            ZipAFiles.extend(ZipAFilesName[ct])
    #            print(ZipAFiles)
    #            ct += 1
    #        for i in range(len(ZipAFiles)):
    #            print(ZipAFiles[i])
    #            czy_istnieje = os.path.exists(ZipAFiles[i])
    #            Dir.Dir_Check(ZipAFiles[i])
    #            if first == True and czy_istnieje == True:
    #                ZipAFiles[i] = ZipAFiles[i]
    #            elif first == False and czy_istnieje == False:
    #                ZipAFiles[i] = Default_Dir + "\\" + ZipAFiles[i]
    #            print(ZipAFiles)
    
    else:
        print("THERE IS NO SUCH COMMAND LIKE",'"'+Cmd+'"')          
