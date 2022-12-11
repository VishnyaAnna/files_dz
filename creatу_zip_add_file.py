import zipfile, os

#путь к папкам
path_inputfiles = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
path_outputfiles = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')


files_dir = os.listdir(path_inputfiles)  # список имен фалов в папке "files"
path_zip = os.path.join(path_outputfiles, "test.zip")  # путь к архиву

# добавление zip файла
with zipfile.ZipFile(path_zip, mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in files_dir:
        add_file = os.path.join(path_outputfiles, file)
        zf.write(add_file)
      #  os.system('file test.zip')

# добавление файлов в zip csv pdf xlsx
with zipfile.ZipFile('test.zip', "a") as myzip:
    myzip.write(files_dir)

