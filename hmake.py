from dearpygui.dearpygui import *
import os
import sys
from datetime import date

today = date.today()
header = ["/*###########################################","","Written by hmake", "", "###########################################*/"]
hheader = ["#ifndef ","#define ", "#endif"]

platform = sys.platform

def pasteHeaders(cFile,hFile, filename):
    file = open(cFile, "w")
    tempheader = header
    tempheader[1] = "Filename: " + filename
    tempheader[3] = "Generated on date: " + today
    file.writelines(tempheader)
    file.writelines(includes)
    file.writelines(customIncludes)
    file.close()

    file = open(hFile, "w")
    tempheader = header
    tempheader[1] = "Filename: " + filename
    tempheader[3] = "Generated on date: " + today
    file.writelines(tempheader)
    tempdefs = hheader
    tempdefs[0].append(filename.upper() +"_H_")
    tempdefs[2].append(filename.upper() +"_H_")
    tempdefs[3].append("//" + filename.upper() +"_H_")
    file.writelines(tempdefs)
    file.close()

def getFiles():
    filename = input("Enter filename to generate: ")
    includes = input("Enter standard headers to include: ").split()
    dependencies = input("Enter custom headers to include: ").split()
    generateDeps = input("Generate custom headers?[y/N]")
    if(generateDeps == "y" && dependencies):
        makedependencies = True
    else
        makedependencies = False
    directory = input("type in directory path where files are to be created: ")
    if(not directory):
        directory = "~/"
    generateFiles(includes, dependencies, filename, directory, makedependencies)


def rungui():


def generateFiles(includes, dependencies, filename, directory, makedependencies):

    ## generating the includes as well as the empty headers
    if(not includes)
        includes = []
    else:
        includes = list(map(lambda u: "#include <"+u+">",includes))
    if(not customIncludes):
        customIncludes = []
    else:
        customIncludes = list(map(lambda u: "#include \""+u+"\"",dependencies))

    if (makedependencies == True):
        dependentCpp = list(map(lambda x,y: x+'/'+y+'.cpp',[directory]*len(dependencies), dependencies))
        dependentH = list(map(lambda x,y: x+'/'+y+'.cpp',[directory]*len(dependencies), dependencies))

    cFile = directory + '/' + filename+'.cpp'
    hFile = directory + '/' + filename+'.h'

    #generate the command to make the files:
    if(platform == 'linux'):
        command = "touch" + cFile +"\ntouch" + hFile + "\n"
        if(makedependencies == True):
            itr = 0
            while itr < len(dependentCpp):
                command += "touch" + dependentCpp[itr] + "\ntouch" + dependentH[itr] + "\n"
                itr += 1
    else:
        command = "type nul >" + cFile + "\r\ntype nul > " + hFile + "\r\n"
        if(makedependencies == True):
            itr = 0
            while itr < len(dependentCpp):
                command += "type nul >" + dependentCpp[itr] + "\r\ntype nul >" + dependentH[itr] + "\r\n"
                itr += 1

    #time to make files in one go
    os.system(command)

    pasteHeaders(cFile,hFile,filename)
    if(makedependencies == True):
        while itr < len(dependentCpp):
            pasteHeaders(dependentCpp[itr], dependentH[itr], dependencies[itr])
            itr += 1



def main(gui):
    if (platform == "darwin"):
        print("Mac OS not supported")
        return
    if(gui == False):
        getFiles()
    else
        rungui()



if __name__ == '__main__':
    main(False)
