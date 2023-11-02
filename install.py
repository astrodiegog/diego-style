import matplotlib as mpl
import os
import shutil


mpl_configdir = mpl.get_configdir()
lib_path = os.path.join(mpl_configdir, 'stylelib')

style_fname = 'dstyle.mplstyle'

if (not os.path.isdir(lib_path)):
    _ = os.mkdir(lib_path)
    print("Could not find mpl_configdir/stylelib. Created in ", path)

curr_dir = os.getcwd()
style_path = os.path.join(curr_dir, style_fname)

_ = shutil.copy(style_path, lib_path)
print("dstyle placed in", style_path)
