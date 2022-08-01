import os
from os.path import exists
from datetime import datetime
import re
import sys
import fileinput

publishers = os.listdir('C:/Users/MikkelAndersen/Desktop/Repos/adnami-publishers/src/publishers')
cert_log_defined = "Certified format;Date modified;Updated by"
publisher_to_replace = "publisher: ['Mediaforce 1XL']"
publisher_defined = "publisher: ['Mediaforce']"
publisher_to_replace_spot = "}"
default_publisher = "  publisher: ['Unknown'] // Added default publisher \n }"
publisher_information_defined = "publisher_information;"
publisher_info_existing = False


for publisher in publishers:
    fileToSearch  = 'C:/Users/MikkelAndersen/Desktop/Repos/adnami-publishers/src/publishers/' + publisher + '/config.js'
    update_cert_log = "C:/Users/MikkelAndersen/Desktop/Repos/adnami-publishers/src/publishers/" + publisher + "/cert_log.csv"
    try:
        if exists(fileToSearch):
            with open(fileToSearch) as x:
                 if publisher_defined in x.read():
                    #Found publisher in config, let's replace it
                    x.close()
                    f = open(fileToSearch,'r')
                    filedata = f.read()
                    f.close()

                    newdata = filedata.replace(publisher_defined,publisher_to_replace)

                    f = open(fileToSearch,'w')
                    f.write(newdata)
                    f.close()
                    update_log(update_cert_log)
                 else:
                    pass
                    # All the files that did NOT find any publishers in the config file
                    # f = open(fileToSearch,'r')
                    # filedata = f.read()
                    # f.close()

                    # defaultPublisher = filedata.replace(publisher_to_replace_spot, default_publisher)
                    # f = open(fileToSearch,'w')
                    # f.write(defaultPublisher)
                    # f.close()
        else:
            # Could not find config.js in the given PATH
            print(f"Config on {publisher} does not exist")

        def update_log(update_cert_log):
            date_today = datetime.today().strftime('%Y-%m-%d')
            new_log_line = "Certified format;Date modified;Updated by\npublisher_information;" + date_today + ";mka\n"
            if exists(update_cert_log):
                # Get top line of cert document for replacement
                with open(update_cert_log,"r") as log:
                    for line in log:
                        pattern = ";(.*?);"
                        substring = re.search(pattern, line).group(1)
                        if substring == '05-04-2022' or substring == '06-04-2022':
                            f = open(update_cert_log, 'r')
                            file_data = f.read()
                            f.close()

                            updated_cert_log = file_data.replace(substring, date_today)

                            f = open(update_cert_log, 'w')
                            f.write(updated_cert_log)
                            f.close()
                        
                        if publisher_information_defined in line:
                            publisher_info_existing = True
                            old_log_line = line
                            
                        elif cert_log_defined in line:
                            publisher_info_existing = False
                            old_log_line = line
                
                if publisher_info_existing:
                    f = open(update_cert_log, 'r')
                    file_data = f.read()
                    f.close()

                    updated_cert_log = file_data.replace(old_log_line, "publisher_information;" + date_today + ";mka\n")

                    f = open(update_cert_log, 'w')
                    f.write(updated_cert_log)
                    f.close()
                else:
                    f = open(update_cert_log, 'r')
                    file_data = f.read()
                    f.close()

                    updated_cert_log = file_data.replace(old_log_line, new_log_line)

                    f = open(update_cert_log, 'w')
                    f.write(updated_cert_log)
                    f.close()
            else:
                # This gets hit if it couldn't find the cert_log file => create one and insert the dataj
                f = open(update_cert_log, 'w')
                f.write(new_log_line)
                f.close()
    except:
        print(f"Error on {publisher}")




