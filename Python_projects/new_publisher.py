import os
from os.path import exists
import sys
import fileinput

publishers = os.listdir('C:/Users/Mikke/OneDrive/Desktop/Projekter/new-adnami-publishers/adnami-publishers/src/publishers')

publisher_search = "publisher: ['manmn']"
publisher_to_replace = "publisher: ['Unknown']"

publisher_defined = "publisher:"

publisher_to_replace_spot = "}"
default_publisher = "  publisher: ['Unknown'] // Added default publisher \n }"



for publisher in publishers:
    fileToSearch  = 'C:/Users/Mikke/OneDrive/Desktop/Projekter/new-adnami-publishers/adnami-publishers/src/publishers/' + publisher + '/config.js'
    try:
        if exists(fileToSearch):
            with open(fileToSearch) as x:
                 if publisher_defined in x.read():
                    #Found publisher in config, let's replace it
                    x.close()
                    f = open(fileToSearch,'r')
                    filedata = f.read()
                    f.close()

                    newdata = filedata.replace(publisher_search,publisher_to_replace)

                    f = open(fileToSearch,'w')
                    f.write(newdata)
                    f.close()
                 else:
                    # All the files that did NOT find any publishers in the config file
                    f = open(fileToSearch,'r')
                    filedata = f.read()
                    f.close()

                    defaultPublisher = filedata.replace(publisher_to_replace_spot, default_publisher)
                    f = open(fileToSearch,'w')
                    f.write(defaultPublisher)
                    f.close()
        else:
            # Could not find config.js in the given PATH
            print("Config does not exist")
    except:
        print("Error")




