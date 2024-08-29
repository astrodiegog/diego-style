# diego-style

Develop my own Matplotlib Plotting Style

To install, just need to run `python3 install.py`. Requires Nimbus Sans, which can be installed using [mplfonts](https://pypi.org/project/mplfonts/). 

To check system has Nimbus Sans font, run the following to find the font names loaded:

```
import matplotlib.font_manager as fm
print(sorted(fm.get_font_names()))
```

Clearing the matplotlib cache directory can help as well: ``rm ~/.cache/matplotlib -rf``.

Adapted from Ryan Hausen's [Robertson Rules](https://github.com/ryanhausen/robertsons-rules).
