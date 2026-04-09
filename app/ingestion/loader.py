import os 

def save_file(file_name):

    path = f"/home/lap-49/Documents/ai-proj-capstone/doc/{file_name}"

    with open(path, 'wb') as f: 
        f.write(file_name.read())
    
    return path 
