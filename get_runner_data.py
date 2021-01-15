# argv[1] is the folder for the genre

import sys
import os
current_dir = os.getcwd()
first_only = True
genre_name = sys.argv[1]
genre_dic = {}
current_dir_name = current_dir.split("/")[-1]
print(genre_name+"_bundle_dic" + " = {")
for (dirpath, dirnames, filenames) in os.walk(genre_name):
    if first_only:
        dirs = dirnames
        first_only = None
        
    dir_name = dirpath.split("/")[-1]
    for filename in filenames:
        if (filename.endswith(".py") and dir_name in dirs and (not dir_name.startswith("-"))):
            path = dirpath.split("/headspin")[-1]
            file_path = path+"/"+filename
            path = os.path.join(dirpath)
            path1 = path+"/" + filename
            app_name_set = True
            package_set = True
            with open(path1, 'r') as f:
                for line in f:
                    line = line.rstrip()
                    if "app_name" in line and "=" in line and "\"" in line and app_name_set:
                        app_name = line.split("=")[-1]
                        app_name_set = None
                    if "package" in line and "=" in line and "\"" in line and package_set:
                        package = line.split("=")[-1]
                        package_set = None
            print("\t"+package+" : "+"{\n\t\t"+"'path' : path_to_parent_folder + '"+file_path+"',\n\t\t'name' : "+app_name+"\n\t},")
print("}")
