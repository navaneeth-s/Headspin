# argv[1] is the folder for the genre
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import sys
import os
current_dir = os.getcwd()

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
first_only = True
try:
    genre_name = sys.argv[1]
except:
    genre_name = "social_entertainment"
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
            test_name_set = True
            pre_set = True
            post_set = True
            with open(path1, 'r') as f:
                for line in f:
                    line = line.rstrip()
                    if "test_name" in line and "=" in line and "\"" in line and test_name_set:
                        test_name = line.split("=")[-1].split("\"")[1]
                        tabs = line.split("test_name")[0]
                        new_test_name = tabs+"test_name = \""+test_name+" automated\""
                        replace(path1, line, new_test_name)
                    
                    if "self.app_size_info_pre_launch" in line and "=" in line and "self.device_info.get_app_size_info" in line and pre_set:
                        pre_set = None
                    if "self.app_size_info_post_launch" in line and "=" in line and "self.device_info.get_app_size_info" in line and post_set:
                        post_set = None

            if pre_set or post_set:
                pre_set = True
                post_set = True
                with open(path1, 'r') as f:
                    for line in f:
                        line = line.rstrip()
                        if "self.first_launch_time()" in line and pre_set:
                            tabs = line.split("self.first_launch_time()")[0]
                            pre_mem = tabs+"self.app_size_info_pre_launch = self.device_info.get_app_size_info(self.driver, self.app_name)\n"+tabs+"self.first_launch_time()"
                            replace(path1, line, pre_mem)
                            pre_set = None

                        if "if self.use_capture" in line and post_set:
                            tabs = line.split("if self.use_capture:")[0]
                            post_mem = tabs+"self.app_size_info_post_launch = self.device_info.get_app_size_info(self.driver, self.app_name)\n"+tabs+"if self.use_capture:"
                            replace(path1, line, post_mem)
                            post_set = None

                        if "self.app_size_info = self.device_info.get_app_size_info(self.driver, self.app_name)" in line:
                            replace(path1,line, "")
                        if "#self.app_size_info" in line:
                            replace(path1,line, "")
