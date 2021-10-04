from .antlr_control import *
from antlr4 import *

def generate_puffin_file(file: InputStream, language: str) -> str:
    ### Generates puffin fiel to enter uncertainties
    if language == 'Python3':
        output = antlr_Python3.read(file)
    elif language == 'R':
        output = antlr_R.read(file)
    else:
        raise Exception('Language not known')
    
    return output

def full_compile(file: InputStream ,puffin: InputStream , language: str) -> str:
    ###Takes a input file and a puffin file and compiler the puffin Uncertainties in to the input file

    uncerts,changes,dependencies = antlr_puffin.read(puffin,language)

    if language == 'Python3':
        output = antlr_Python3.write(file,uncerts,changes,dependencies)
    elif language == 'R':
        output = antlr_R.write(file,uncerts,changes,dependencies)
    
    return output


# def get_puffin(file,output,language):
#     # Reads a script and outputs a puffin file
#     if language == 'Python3':
#         antlr_Python3.read(file,output)
#     elif language == 'R':
#         antlr_R.read(file,output)

#     print('Created puffin file')

# def auto_uq_compile(file,output,language):
#     # Fully automatic uncertainty compile

#     puffin = 'temp.pf'
#     puffin2 = 'temp2.pf'


#     if language == 'Python3':
#         antlr_Python3.read(file,puffin)
#         add_in_auto_uq(puffin,puffin2)
#         uncerts,changes,dependencies = antlr_puffin.read(puffin2,language)
#         antlr_Python3.write(file,output,uncerts,changes,dependencies)

#     elif language == 'R':
#         antlr_R.read(file,puffin)
#         add_in_auto_uq(puffin,puffin2)
#         uncerts,changes,dependencies = antlr_puffin.read(puffin2,language)
#         antlr_R.write(file,output,uncerts,changes)

#     # Try to delete temp files
#     try:
#         os.remove(puffin)
#         os.remove(puffin2)

#     except: pass

# def add_in_auto_uq(puffin,output):
#     # Adds automatic uncertainty to puffin file
#     vars = [line for line in open(puffin,'r')]
#     new_vars = ""
#     for var in vars:

#         if var != "":
#             i = var.split('->')[1]
#             try:

#                 mp.mpf(i)
#                 lower,higher = getSigFig(i)
#                 interval = "[%s,%s]" %(lower,higher)

#                 new_vars+=var.replace(i,interval)+'\n'

#             except: new_vars+=var+'\n'
#         else:
#             new_vars+=var+'\n'

#     with open(output,'w') as f:
#         print(new_vars,file = f)

#     print('Automatically calculated uncertainty')

# def output_auto_script(file,output,language):
#     # outputs puffin file with auto uq
#     temp = 'temp.pf'
#     get_puffin(file,temp,language)
#     add_in_auto_uq(temp,output)

#     try:
#         os.remove(temp)
#     except: pass
