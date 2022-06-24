import csv
# not being used import os
from os.path import exists
# not being used import sys
# not being used import fileinput
from datetime import datetime
import re

country_defined = "country:"
publisher_defined = "publisher:"
cert_log_defined = "Certified format;Date modified;Updated by"

with open("Domain_to_publisher-Sheet1_v2.csv", 'r') as file:
    reader = csv.DictReader(file, skipinitialspace=True)
   
    for l in reader:
        site = (l["publisher"], l["Creative site"], l["country"])

        # Tuple unpack til at gemme publishers og site navn til 2 variabler
        publisher,cs,country = site

        # Sæt path til det site som står i CSV
        update_creative_site = "C:/Users/Mikke/OneDrive/Desktop/Projekter/new-adnami-publishers/adnami-publishers/src/publishers/" + cs + "/config.js"
        update_cert_log = "C:/Users/Mikke/OneDrive/Desktop/Projekter/new-adnami-publishers/adnami-publishers/src/publishers/" + cs + "/cert_log.csv"

        publisher_search = "  publisher: ['" + str(publisher) + "'],\n"
        publisher_to_replace = "}"
        try:
            if exists(update_creative_site) and publisher !=  '':
                with open(update_creative_site) as x:
                    if publisher_defined in x.read():
                        x.close()
                        with open(update_creative_site,"r") as fi:
                            for line in fi:
                                if publisher_defined in line:
                                    publisher_to_replace = line

                        f = open(update_creative_site,'r')
                        filedata = f.read()
                        f.close()

                        newdata = filedata.replace(publisher_to_replace,publisher_search)

                        f = open(update_creative_site,'w')
                        f.write(newdata)
                        f.close()

                        # Run cert_log and country update
                        update_log(update_cert_log)
                        update_countries(update_creative_site)

                    else:
                        publisher_search = "  publisher: ['" + str(publisher) + "'],\n }"
                        f = open(update_creative_site,'r')
                        filedata = f.read()
                        f.close()

                        newdata = filedata.replace(publisher_to_replace,publisher_search)

                        f = open(update_creative_site,'w')
                        f.write(newdata)
                        f.close()

                        # Run cert_log and country update
                        update_countries(update_creative_site)
                        update_log(update_cert_log)
                
            else:
                pass
                # print("Site does not exist")

                    # Check if cert_log exist
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

                            if cert_log_defined in line:
                                old_log_line = line

                    f = open(update_cert_log, 'r')
                    file_data = f.read()
                    f.close()

                    updated_cert_log = file_data.replace(old_log_line, new_log_line)

                    f = open(update_cert_log, 'w')
                    f.write(updated_cert_log)
                    f.close()
                else:
                    # This gets hit if it couldn't find the cert_log file => create one and insert the data

                    f = open(update_cert_log, 'w')
                    f.write(new_log_line)
                    f.close()


            def update_countries(path_to_countries):
                if exists(path_to_countries):
                   with open(path_to_countries) as x:
                       # Find country already defined in config
                        if country_defined in x.read():
                           new_countries_line = "  country: ['" + str(country) + "'],\n"
                           x.close()
                           with open(path_to_countries,"r") as config:
                                for line in config:
                                    if country_defined in line:
                                        old_country_array = line

                                        f = open(path_to_countries, 'r')
                                        file_data = f.read()
                                        f.close()

                                        updated_country_array = file_data.replace(old_country_array, new_countries_line)

                                        f = open(path_to_countries, 'w')
                                        f.write(updated_country_array)
                                        f.close()

                                        # print(f'changed: {old_country_array} to {new_countries_line} on {cs}')

                        else:
                            # Country is not defined in config
                            new_countries_line = " country: ['" + str(country) + "'],\n }"
                            end_of_config = "}"
                            f = open(path_to_countries, 'r')
                            file_data = f.read()
                            f.close()

                            updated_country_array = file_data.replace(end_of_config, new_countries_line)

                            f = open(path_to_countries, 'w')
                            f.write(updated_country_array)
                            f.close()
                            # print(f'did not find existing country but added: {new_countries_line} to {cs}')
                else:
                    # Path to config wasn't found
                    pass

        except:
            pass

      
