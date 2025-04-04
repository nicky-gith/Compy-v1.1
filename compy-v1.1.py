import shutil
import os as compy

currentdir = compy.getcwd()
print()
print("░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░██╗")
print("██╔══██╗██╔══██╗████╗░████║██╔══██╗╚██╗░██╔╝")
print("██║░░╚═╝██║░░██║██╔████╔██║██████╔╝░╚████╔╝░")
print("██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░░░╚██╔╝░░")
print("╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░░░░██║░░░")
print("░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░ v1.1")
print("It's Linux but with some changes and twists!")
print()
print("Welcome to Compy v1.1! Type 'help' for information.")
print("by Carlos Eduardo Laborda (Charlie)")
print()
print("Type 'readme' for the history of Compy.")

def lang():
    currentlang = str(input("Pick a language (type 'help' for information): "))
    currentlang
    if currentlang == "help":
        print("Here are all available languages: ")
        print()
        print("eng - English (US)")
        print("esp - Spanish (Castellano)")
        print()
        lang()
    elif currentlang == "eng" or currentlang == "esp":
        pass
    else:
        print("Not an available language.")
        print()
        lang()
    return currentlang

def cp_command(src, dest):
    try:
        if not compy.path.exists(src):
            print(f"ERROR: Source file/directory '{src}' does not exist.")
            return
        if compy.path.isdir(src):
            if compy.path.isdir(dest):
                dest = compy.path.join(dest, compy.path.basename(src))
            shutil.copytree(src, dest)
            print(f"Copied directory '{src}' to '{dest}'.")
        else:
            if compy.path.isdir(dest):
                dest = compy.path.join(dest, compy.path.basename(src))
            shutil.copy(src, dest)
            print(f"Copied file '{src}' to '{dest}'.")
    except Exception as e:
        print(f"ERROR: {e}")

print()
currentlang = lang()

while True:
    command = input(f"nickylinux@compy {currentdir} $ ")
    
    if command.lower() == "exit":
        if currentlang == "eng":
            print("See you next time. Bye! :D")
        else:
            print("Nos vemos la próxima. ¡Chau! :D")
        print()
        break
    
    elif command.lower() == "help":
        if currentlang == "eng":
            print("Here are the valid commands:")
            print()
            print("list - Lists files/directories. Here are its variants:")
            print("    list.di - Lists files/directories with detailed information.")
            print("    list.ih - Lists all files/directories, including hidden ones.")
            print("    list.hr - Lists files/directories in a way humans can read.")
            print()
            print("exit - Just exits the terminal, nothing more ._.")
            print()
            print("help - I think you can guess what this one does.")
            print()
            print("l - Clears the screen.")
            print()
            print("chdir - Changes your directory.")
            print()
            print("whereami - Shows in which directory you are.")
            print()
            print("mkdir - Makes a directory.")
            print()
            print("rmv - Removes a file. Here are its variants:")
            print("    rmv.di - Removes a directory with its content.")
            print("    rmv.fo - Removes a file without warning.")
            print()
            print("copy - Copies a file. Here is its variant:")
            print("    copy.di - Copies a directory.")
            print()
            print("mvornm - Moves or renames a file.")
            print()
            print("mkfil - Makes a file.")
            print()
            print("rdfil - Reads a file.")
            print()
            print("ping - Pings a website.")
            print()
            print("edfil - Edits a file.")
            print()
            print("readme - Reads the file 'readme.txt'.")
            print()
            print("timedate - Shows the current time and date.")
        else:
            print("Estos son los comandos válidos:")
            print()
            print("list - Lista archivos/directorios. Estas son sus variantes:")
            print("    list.di - Lista archivos/directorios con información detallada.")
            print("    list.ih - Lista todos los archivos/directorios, incluyendo los ocultos.")
            print("    list.hr - ista archivos/directorios de manera que los humanos puedan leer.")
            print()
            print("exit - Solo sale de la terminal, nada más ._.")
            print()
            print("help - Creo que puedes adivinar lo que esto hace.")
            print()
            print("l - Limpia la pantalla.")
            print()
            print("chdir - Cambia su directorio.")
            print()
            print("whereami - Muestra en cual directorio estás.")
            print()
            print("mkdir - Hace un directorio.")
            print()
            print("rmv - Elimina un archivo. Estas son sus variantes:")
            print("    rmv.di - Elimina un directorio con su contenido.")
            print("    rmv.fo - Elimina un archivo sin advertencias.")
            print()
            print("copy - Copia un archivo. Esta es su variante:")
            print("    copy.di - Copia un directorio.")
            print()
            print("mvornm - Move o renombra un archivo.")
            print()
            print("mkfil - Hace un archivo.")
            print()
            print("rdfil - Lee un archivo.")
            print()
            print("ping - Hace un ping a un website.")
            print()
            print("edfil - Edita un archivo.")
            print()
            print("readme - Lee el archivo 'readme.txt'.")
            print()
            print("timedate - Muestra que hora y fecha es.")
    elif command.lower() == "l":
        if compy.name == "nt":
            compy.system("cls")
        else:
            compy.system("clear")
    elif command.lower().startswith("list"):
        if ".di" in command:
            if compy.name == "nt":
                compy.system("dir /q")
            else:
                compy.system("ls -l")
        elif ".ih" in command:
            if compy.name == "nt":
                compy.system("dir /a")
            else:
                compy.system("ls -a")
        elif ".hr" in command:
            if compy.name == "nt":
                compy.system("dir /s")
            else:
                compy.system("ls -h")
        else:
            if compy.name == "nt":
                compy.system("dir")
            else:
                compy.system("ls")
    elif command.lower().startswith("chdir "):
        path = command[6:].strip()
        if path:
            try:
                compy.chdir(path)
                currentdir = compy.getcwd()
            except FileNotFoundError:
                if currentlang == "eng":
                    print(f"ERROR: Directory '{path}' does not exist.")
                else:
                    print(f"ERROR: Directorio '{path}' no existe.")
            except PermissionError:
                if currentlang == "eng":
                    print(f"ERROR: Access to directory '{path}' denied.")
                else:
                    print(f"ERROR: Acceso al directorio '{path}' denegado.")
        else:
            if currentlang == "eng":   
                print("ERROR: Path not specified.")
            else:
                print("ERROR: Ruta no especificada.")
    elif command.lower() == "whereami":
        print(currentdir)
    elif command.lower().startswith("mkdir "):
        newdir = command[6:].strip()
        if newdir:
            if compy.name == "nt":
                compy.system(f"md {newdir}")
            else:
                compy.system(f"mkdir {newdir}")
            if currentlang == "eng":   
                print(f"Made directory '{newdir}'.")
            else:
                print(f"Directorio '{newdir}' hecho.")
        else:
            if currentlang == "eng":   
                print("ERROR: Directory name not specified.")
            else:
                print("ERROR: Nombre de directorio no especificado.")
    elif command.lower().startswith("rmv"):
        if ".di " in command:
            targetdir = command[7:].strip()
            if targetdir:
                if currentdir == "eng":
                    want = str(input(f"The removal of directory '{targetdir}' may be irreversible. Are you sure you want to remove directory '{targetdir}'?[y/n]"))
                else:
                    want = str(input(f"La eliminación del directorio '{targetdir}' puede ser irreversible. ¿Estás seguro que quieres eliminar el directorio '{targetdir}'?[y/n]"))
                if want == 'y':
                    if compy.name == "nt":
                        compy.system(f"rmdir /s {targetdir}")
                    else:
                        compy.system(f"rm -r {targetdir}")
                    if currentlang == "eng":
                        print(f"Removed directory '{targetdir}'.")
                    else:
                        print(f"Directorio '{targetdir}' eliminado.")
                else:
                    if currentlang == "eng":
                        print(f"Cancelled removal of directory '{targetdir}'.")
                    else:
                        print(f"Eliminación del directorio '{targetdir}' cancelada.")
            else:
                if currentlang == "eng":
                    print("ERROR: Directory name not specified.")
                else:
                    print("ERROR: Nombre de directorio no especificado.")
        elif ".fo " in command:
            targetfil = command[7:].strip()
            if targetfil:
                if compy.name == "nt":
                    compy.system(f"del /f {targetfil}")
                else:
                    compy.system(f"rm -f {targetfil}")
                if currentlang == "eng":
                    print(f"Removed file '{targetfil}'.")
                else:
                    print(f"Archivo '{targetfil}' eliminado.")
            else:
                if currentlang == "eng":
                    print("ERROR: Filename not specified.")
                else:
                    print("ERROR: Nombre de archivo no especificado.")
        else:
            targetfil = command[4:].strip()
            if targetfil:
                if currentdir == "eng":
                    want = str(input(f"The removal of file '{targetfil}' may be irreversible. Are you sure you want to remove file '{targetfil}'?[y/n]"))
                else:
                    want = str(input(f"La eliminación del archivo'{targetfil}' puede ser irreversible. ¿Estás seguro que quieres eliminar el archivo '{targetfil}'?[y/n]"))
                if want == 'y':
                    if compy.name == "nt":
                        compy.system(f"del {targetfil}")
                    else:
                        compy.system(f"rm {targetfil}")
                    if currentlang == "eng":
                        print(f"Removed file '{targetfil}'.")
                    else:
                        print(f"Archivo '{targetfil}' eliminado.")
                else:
                    if currentlang == "eng":
                        print(f"Cancelled removal of file '{targetfil}'.")
                    else:
                        print(f"Eliminación del archivo '{targetfil}' cancelada.")
            else:
                if currentlang == "eng":
                    print("ERROR: Filename not specified.")
                else:
                    print("ERROR: Nombre de archivo no especificado.")
    elif command.lower().startswith("copy.di"):
        parts = command[8:].strip().split(" ", 1)
        if len(parts) == 2:
            source_dir, destination = parts
            cp_command(source_dir, destination)
        else:
            if currentlang == "eng":
                print("ERROR: Invalid syntax")
            else:
                print("ERROR: Sintaxis no válida.")
    elif command.lower().startswith("copy"):
        parts = command[5:].strip().split(" ", 1)
        if len(parts) == 2:
            source, destination = parts
            cp_command(source, destination)
        else:
            if currentlang == "eng":
                print("ERROR: Invalid syntax")
            else:
                print("ERROR: Sintaxis no válida.")
    elif command.lower().startswith("mvornm"):
        parts = command[7:].strip().split(" ", 1)
        if len(parts) == 2:
            file, name = parts
            if compy.name == "nt":
                compy.system(f"move {file} {name}")
            else:
                compy.system(f"mv {file} {name}")
            if currentlang == "eng":
                print(f"Moved/renamed file '{file}' to '{name}'.")
            else:
                print(f"Archivo movido/renombrado de '{file}' a '{name}'.")
        else:
            if currentlang == "eng":
                print("ERROR: Invalid syntax")
            else:
                print("ERROR: Sintaxis no válida.")
    elif command.lower().startswith("mkfil "):
        file = command[6:].strip()
        if file:
            if compy.name == "nt":
                compy.system(f"copy NUL {file}")
            else:
                compy.system(f"touch {file}")
            if currentlang == "eng":
                print(f"Made file '{file}'.")
            else:
                print(f"Archivo '{file}' hecho.")
        else:
            if currentlang == "eng":
                print("ERROR: Filename not specified.")
            else:
                print("ERROR: Nombre de archivo no especificado.")
    elif command.lower().startswith("rdfil "):
        file = command[6:].strip()
        if file:
            print()
            if compy.name == "nt":
                compy.system(f"type {file}")
            else:
                compy.system(f"cat {file}")
            print()
        else:
            if currentlang == "eng":
                print("ERROR: Filename not specified.")
            else:
                print("ERROR: Nombre de archivo no especificado.")
    elif command.lower().startswith("ping "):
        web = command[5:].strip()
        if web:
            compy.system(f"ping {web}")
        else:
            if currentlang == "eng":
                print("ERROR: Website not specified.")
            else:
                print("ERROR: Website no especificado.")
    elif command.lower().startswith("edfil "):
        file = command[6:].strip()
        if file:
            if compy.name == "nt":
                compy.system(f"notepad {file}")
            else:
                compy.system(f"vi {file}")
    elif command.lower() == "readme":
        if compy.name == "nt":
            compy.system("cls")
            compy.system("type readme.txt")
        else:
            compy.system("clear")
            compy.system("cat readme.txt")
    elif command.lower() == "timedate":
        if compy.name == "nt":
            compy.system("time")
            compy.system("date")
        else:
            compy.system("date")
    else:   
        if currentlang == "eng":
            print("ERROR: Command not valid. Type 'help' for information.")
        else:
            print("ERROR: Comando no válido. Teclea 'help' para ver información.")