import tkinter as tk
from tkinter import filedialog
import os
import sys


def get_title(file_path):
    title = os.path.splitext(file_path)[0]
    title = title.split('_')[1]
    title = title.replace('-', ' ')
    return title


GALLERY_OPTION = "gallery"
LINK_OPTION = "link"

# read in argument value
if len(sys.argv) == 2:
    OPTION = sys.argv[1]
else:
    OPTION = 0

# Select images from directory
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames()
# file_paths = ('C:/Users/John/projects/johng/static/images/milan/2017-04-05T123000_VIBRA-Team.jpg',
#              'C:/Users/John/projects/johng/static/images/milan/2017-04-06T063907_Gepaeck.jpg')

# get date of oldest image
file_path = file_paths[-1]
date_oldest = os.path.basename(file_path)[:10]

# build header
header = ["+++", 'date = "{}"'.format(date_oldest),
          "draft = true",
          'title = "Titel"',
          'image = ""',
          'categories = ["Milan"]',
          "+++"]

# write draft blog entry
with open('content/post/italy/draft.md', 'w') as output:
    output.write("\n".join(header))

    output.write("\n\n")

    output.write("{{< load-photoswipe >}}\n\n")

    tab = ''

    if OPTION == GALLERY_OPTION:
        output.write("{{< gallery >}}\n\n")
        tab = "\t"

    for file_path in file_paths:
        title = get_title(file_path)
        rel_path = file_path.split("/static")[1]

        if OPTION == LINK_OPTION:
            image_link = "![{}]({})".format(title, rel_path)
        else:
            image_link = tab + '{{{{< figure caption="{}" src="{}" alt="{}" >}}}}'.format(title, rel_path, title)

        output.write(image_link + "\n\n")

    if OPTION == GALLERY_OPTION:
        output.write("{{< /gallery >}}")
