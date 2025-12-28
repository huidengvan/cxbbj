import re
import os

def procfile(filepath):
    # read file line by line
    file = open(filepath, "r", encoding='UTF-8')
    lines = file.readlines()
    file.close()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            text += ' ' + line.rstrip('\n')
        text = text.lstrip()
    # print(text)

    f = open(filepath + ".md", "w", encoding='UTF-8')
    f.write(text)
    f.close()

def procdir():
    with os.scandir('.') as it:
        for entry in it:
            if entry.name.endswith(".srt") and entry.is_file():
                print(entry.name, entry.path)
                procfile(entry.path)


    # directory = os.fsencode('.')
        
    # for file in os.listdir(directory):
    #     filename = os.fsdecode(file)
    #     if filename.endswith(".srt"): # or filename.endswith(".py"): 
    #         print(os.path.join(directory, filename))
    #         procfile(os.path.join(directory, filename))
    #         continue
    #     else:
    #         continue

procdir()