import pylab as pl
import sys
import os

plot_count = 0
def plot_out(figsize=None, dpi=60, newline=True, print_out=True):
    global plot_count
    filename = "plot_{}_{:03d}.png".format(os.path.basename(sys.argv[0]), plot_count)
    plot_count += 1

    old_size = pl.gcf().get_size_inches()
    if figsize:
        pl.gcf().set_size_inches(*figsize)

    pl.savefig(filename, dpi=dpi)
    if print_out:
        print("<{}>{}".format(filename, '\n' if newline else ''))

    pl.gcf().set_size_inches(old_size)
    pl.clf()

img_count = 0
def image_out(img, newline=True, print_out=True):
    global img_count
    filename = f"image_{os.path.basename(sys.argv[0])}_{img_count:03d}.png"
    img_count += 1

    img.save(filename)
    if print_out:
        print(f"<{filename}>{os.linesep if newline else ''}")

    return filename
