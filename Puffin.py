from app import *
from antlr4 import *

import click
import sys
import os

# sys.tracebacklimit = 0
## Define errors
class Errm(Exception):
    pass

# def user_control():

#     if getattr(sys, 'frozen', False):
#         # If the application is run as a bundle, the pyInstaller bootloader
#         # extends the sys module by a flag frozen=True and sets the app
#         # path into variable _MEIPASS'. WHICH STILL DOESNT WORK
#         directory = os.path.dirname(sys.argv[0])
#     else:
#         directory = os.path.dirname(os.path.abspath(__file__))

#     running = True
#     file = None
#     puffin = None
#     language = None
#     outfile = None
#     file_long = None
#     puffin_long = None
#     outfile_long = None

#     infolder = os.listdir(directory)

#     # Change to current folder
#     os.chdir(directory)

#     if sys.platform.startswith('darwin'):
#         os.system('clear')

#     print('Welcome to Puffin\n\n')
#     print('Working directory: '+directory)
#     print('To enter input script:  \"file=filename\"')
#     print('To enter puffin script: \"puffin=filename\"')
#     print('To specify language: \"language=language\" \n')
#     print('Entering \"outfile = name\" define a outfile name')
#     print('To compile puffin script into input script: \"compile\"')
#     print('To compile using automatic uncertainty analysis: \"auto\"')
#     print('To generate puffin script from input script: \"getpf\"\n')
#     print('To get generate puffin script with automatic uncertainty analysis: \"autopf\"')
#     print('\";\" can be used to enter multiple commands at once')
#     print('i.e. \"file=example.py; puffin=uq.pf; outfile=name.py; compile\"\n\n')
#     print('Entering \"info\" will list all defined files and availible options')
#     print('To exit enter \"quit\"\n\n')

#     while running:

#         line = input('> ')

#         commands = line.split(';')

#         for command in commands:

#             command = command.strip()

#             if command == 'quit':
#                 #Stop running
#                 running = False


#             elif command.startswith('file'):
#                 # Find filename
#                 try:

#                     file = command.split('=')[1].strip()
#                     print('Loaded: '+file)
#                     file_long = directory + '/' + file

#                 except:
#                     print('Can\'t detect filename')

#             elif command.startswith('puffin'):
#                 # Find puffin file name
#                 try:

#                     puffin = command.split('=')[1].strip()
#                     print('Loaded: '+puffin)
#                     file_long = directory + '/' + puffin

#                 except:

#                     print('Can\'t detect puffin filename')

#             elif command.startswith('language'):
#                 # Find language
#                 try:

#                     language = command.split('=')[1].strip()

#                 except:

#                     print('Can\'t detect language')

#             elif command.startswith('outfile'):
#                 # Find language
#                 try:

#                     outfile = command.split('=')[1].strip()

#                 except:

#                     print('Can\'t detect outfile name')

#             elif command == 'compile':

#                 if file is None:
#                     # Cannot compile if no input file
#                     print('ERROR: No input file')
#                 elif puffin is None:
#                     # Cannot compile if no puffin file
#                     print('ERROR: No puffin file')
#                 else:

#                     # If no outfile file need to make one
#                     if outfile is None:
#                         outfile = file.replace('.','_pf.')

#                     # If no entered language then need to define one
#                     if language is None:
#                         fileName, fileExt = file.split('.')
#                         fileExt = fileExt.lower()
#                         if fileExt == 'py':
#                             language = 'Python3'
#                         elif fileExt == 'r':
#                             language = 'R'
#                         else:
#                             print('ERROR: I don\'t know the language')

#                     if language is not None:
#                         # Can do compiles
#                         full_compile(file,puffin,outfile,language)
#                         print('Compiled')

#             elif command == 'getpf':

#                 if file is None:
#                     # Cannot compile if no input file
#                     print('ERROR: No input file')

#                 else:
#                     fileName, fileExt = file.split('.')
#                     fileExt = fileExt.lower()
#                     if language == None:
#                         if fileExt == 'py':
#                             language = 'Python3'
#                         elif fileExt == 'r':
#                             language = 'R'
#                         else:
#                             print('ERROR: I don\'t know the language')

#                     if outfile is None:

#                         outfile = fileName +'.pf'

#                     if language is not None:
#                         # Can get puffin file
#                         get_puffin(file,outfile,language)

#                         puffin = outfile
#                         print('Created '+outfile)

#             elif command == 'auto':

#                 if file is not None:

#                     fileName, fileExt = file.split('.')
#                     fileExt = fileExt.lower()

#                     if language is None:

#                         if fileExt == 'py':
#                             language = 'Python3'
#                         elif fileExt == 'r':
#                             language = 'R'
#                         else:
#                             print('ERROR: I don\'t know the language')

#                     if outfile is None:
#                         outfile = file.replace('.','_pf.')

#                     if language is not None:

#                         auto_uq_compile(file,outfile,language)

#                 elif puffin is not None:

#                     if outfile is None:

#                         outfile = puffin.replace('.','_auto.')

#                     add_in_auto_uq(puffin,outfile)

#                 else: print("I don\'t know what you want me to do")

#             elif command == 'autopf':

#                 if file is not None and puffin is not None:
#                     print('AMBIGUITY WARNING: Will generate auto puffin file from %s not %s' %(file,puffin))
#                     print('                   To get from %s use \"autopf-pf\"' %(puffin))

#                 if file is not None:

#                     fileName, fileExt = file.split('.')
#                     fileExt = fileExt.lower()

#                     if language is None:

#                         if fileExt == 'py':
#                             language = 'Python3'
#                         elif fileExt == 'r':
#                             language = 'R'
#                         else:
#                             print('ERROR: I don\'t know the language')

#                     if outfile is None:
#                         outfile = file.replace('.','_pf.')

#                     if language is not None:

#                         outfile_auto_script(file,outfile,language)

#                 elif puffin is not None:

#                     if outfile is None:

#                         outfile = puffin.replace('.','_auto.')

#                     add_in_auto_uq(puffin,outfile)

#                 else: print("I don\'t know what you want me to do")

#             elif command == 'info':

#                 if directory is not None:
#                     print('Working directory: '+directory)

#                 if file is not None:
#                     print('file = '+file)
#                 else:
#                     print('No input file')

#                 if puffin is not None:
#                     print('puffin = '+puffin)
#                 else:
#                     print('No puffin language')

#                 if language is not None:
#                     print('language = '+language)
#                 else:
#                     print('Language unknown')

#                 if outfile is not None:
#                     print('outfile = '+outfile)
#                 else:
#                     print('No outfile name specified')

#                 print('\nMethods availible:')

#                 if file is not None and puffin is not None:
#                     print('compile')
#                     print('getpf')
#                     print('auto')
#                     print('autopf')
#                 elif puffin is None and file is not None:
#                     print('getpf')
#                     print('auto')
#                     print('autopf')
#                 elif file is None and puffin is not None:
#                     print('auto')
#                     print('autopf')
#                 else:
#                     print('None availible')

#             elif command == 'cd':
#                 directory = ask_dir()

#             else: print('ERROR: Unkown command')

@click.command()
@click.option('--file',default = None,help='Input File')
@click.option('--outfile',default = None, help='outfile file')
@click.option('--auto', flag_value=True,type = bool ,help = 'Automatically create intervals')
@click.option('--puffin', default = None, help = 'Input puffin file')
@click.option('--getpf',flag_value=True,type = bool ,help = 'Create puffin language file from input file')
def puffinComp(file,outfile,puffin,getpf,auto):
    
    # Method 1 -> full_compile
    # Method 2 -> get_puffin
    # Method 3 -> auto_uq_compile
    # Method 4 -> add_in_auto_uq
    # Method 5 -> outfile_auto_script

    # Find what the user is trying to do or raise an error
    if file is None:

        if puffin is None:

            # user_control()
            method = 0

        elif not auto:

            raise Errm("\nI was expecting --auto=True")

        else:
            method = 4

    else:

        if puffin is None and not getpf and not auto:

            raise Errm("\nI don\'t know what you want me to do")

        elif puffin is None and getpf and auto:

            method = 5

        elif puffin is None and getpf and not auto:

            method = 2

        elif puffin is None and auto and not getpf:

            method = 3

        elif puffin is not None and auto:

            raise Errm("\nI wasn\'t expecting --auto=True\nTry without?")

        elif puffin is not None and getpf:

            raise Errm("\nI wasn\'t expecting --getpf=True\nTry without?")

        elif puffin is not None and not getpf and not auto:

            method = 1

        else: raise Errm("I give up")


    if method in (1,2,3,5):

        fileName, fileExt = file.split('.')

        fileExt = fileExt.lower()

        if outfile is None:
            if getpf:
                outfile = fileName +'.pf'
            else:
                outfile = file.replace('.','_pf.')

        if fileExt == 'py':
            language = 'Python3'
        elif fileExt == 'r':
            language = 'R'
        else:
            raise Errm('I don\'t know that language!')

        if method == 1:
            
            with open(file,'r') as fi:
                file_text = InputStream(fi.read())
            with open(puffin,'r') as fp:
                puffin_text = InputStream(fp.read())

            output = full_compile(file_text,puffin_text,language)
            with open(outfile, 'w') as fo:
                print(output,file = fo)
                
        elif method == 2:
            
            with open(file,'r') as f:
                file_text = InputStream(f.read())
                
            out = generate_puffin_file(file_text,language)

            with open(outfile,'w') as fo:
                print(out, file = fo)

        # elif method == 3:

        #     auto_uq_compile(file,outfile,language)

        # elif method == 5:

        #     outfile_auto_script(file,outfile,language)

    # elif method == 4:

    #     if outfile is None:

    #         outfile = puffin.replace('.','_auto.')

    #     add_in_auto_uq(puffin,outfile)



if __name__ == '__main__':

    puffinComp()
