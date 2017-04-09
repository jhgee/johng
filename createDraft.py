import tkinter as tk
from tkinter import filedialog
import os


def get_title(file_path):
    title = os.path.splitext(file_path)[0]
    title = title.split('_')[1]
    title = title.replace('-', ' ')
    return title


# Select images from directory
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames()
# file_paths = ('C:/Users/John/projects/johng/static/images/milan/2017-04-05T123000_VIBRA-Team.jpg',
#             'C:/Users/John/projects/johng/static/images/milan/2017-04-06T063907_Gepaeck.jpg')

# get date of oldest image
file_path = file_paths[-1]
date_oldest = os.path.basename(file_path)[:10]

# build header
header = ["+++", 'date = "{}"'.format(date_oldest),
          "draft = false",
          'title = "Titel"',
          'image = "2017-image.jpg"',
          'categories = ["Milan"]',
          "+++"]

# write draft blog entry
with open('content/post/italy/draft.md', 'w') as output:
    output.write("\n".join(header))

    output.write("\n\n")
    for file_path in file_paths:
        title = get_title(file_path)
        rel_path = file_path.split("/static")[1]
        image_link = "![{}]({})".format(title, rel_path)
        output.write(image_link + "\n\n")
