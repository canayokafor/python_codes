# Rename group of files in a directory
import os

os.chdir('C:/Users/CHINEDU/Documents/chinedu/jennifer/jenny 4')
the_dir = os.listdir('C:/Users/CHINEDU/Documents/chinedu/jennifer/jenny 4')

for f in the_dir:
    f_name, f_ext = os.path.splitext(f)
    f_title, f_type = f_name.split(' - ')
    f_ti = f_title[15:]
    f_mid = "Jenifa's_diary"

    filename = ('{}{}{}'.format(f_ti, f_mid, f_ext))
    os.rename(f, filename)
