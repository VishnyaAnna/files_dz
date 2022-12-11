import zipfile, os

# добавление zip файла
path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'files_dz/resources'))
file_dir = os.listdir(path)

with zipfile.ZipFile('resources/test.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(path, file)
        zf.write(add_file)
        os.system('file test.zip')

#добавление файлов в zip csv pdf xlsx
with zipfile.ZipFile("resources/test.zip", "a") as myzip:
     myzip.write("resources/file_csv.csv")
     myzip.write("resources/file_pdf.pdf")
     myzip.write("resources/file_xlsx.xlsx")
