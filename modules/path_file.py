import os, pygame
#Путь к файлу
def path_to_file(name_file):
    path_to_file = __file__
    path_to_file = path_to_file.split('\\')
    del path_to_file[-1]
    del path_to_file[-1]
    path_to_file_n = "\\".join(path_to_file)
    path_to_file_n = os.path.join(path_to_file_n, name_file)
    try:
        # print("path file mode is Windows")
        # first_letter_in_file_format = str(name_file[-3]) == "p"
        # print(f"Path is to image: {first_letter_in_file_format}, path: {path_to_file_n}, \nonly path to file: {name_file}")
        if str(name_file[-3]) == "p":
            a=pygame.image.load(path_to_file_n)
        else:
            a=pygame.font.Font(path_to_file_n, 10)
    except:
        # print("path file mode switched to MacOS")
        path_to_file_n = "/".join(path_to_file)
        name_file = name_file.split("\\")
        name_file = "/".join(name_file)
        path_to_file_n = os.path.join(path_to_file_n, name_file)
    return path_to_file_n 
