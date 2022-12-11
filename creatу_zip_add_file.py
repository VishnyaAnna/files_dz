import zipfile, os
from os.path import basename

#путь к папкам
path_inputfiles = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
path_outputfiles = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')


files_dir = os.listdir(path_inputfiles)  # список имен фалов в папке "files"
path_zip = os.path.join(path_outputfiles, "test.zip")  # путь к архиву

# добавление zip файла
with zipfile.ZipFile(path_zip, mode='w',
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in files_dir:
        add_file = os.path.join(path_inputfiles, file)
        zf.write(add_file, basename(add_file))

# Проверка содержимого xlsx
with zipfile.ZipFile(path_zip, mode='r') as zip_file:
        text = str(zip_file.read('file_xlsx.xlsx'))
        assert text.__contains__("February")

# Проверка содержимого pdf
with zipfile.ZipFile(path_zip, mode='r') as zip_file:
    text = str(zip_file.read('file_pdf.pdf'))
    assert text.__contains__('PDF')

# Проверка содержимого csv
with zipfile.ZipFile(path_zip, mode='r') as zip_file:
    text = str(zip_file.read('file_csv.csv'))
    assert text.__contains__('Anna,Pavel,Peter')

