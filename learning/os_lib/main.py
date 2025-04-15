import os

directory_path = '/Users/chassie/Desktop'
directory_content = os.listdir(directory_path)
n = 0
for filename in directory_content:
    n+=1
    if filename.startswith('1'):
        os.remove(os.path.join(directory_path, filename)) # объединяем пути до файлов
    else:
        print(filename)
print(f'Всего файлов на рабочем столе:{n}')