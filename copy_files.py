import shutil

def copy_files_from_requirements(requirement_file_location, source, destination):
    req_file = open(requirement_file_location, "r")
    for file_name in req_file.readlines():
        file_path = None
        if source[-1] == "/" or source[-1] == "\\":
            file_path = source+file_name
        else:
            file_path = source+"/"+file_name
        shutil.copyfile(file_path, destination)
