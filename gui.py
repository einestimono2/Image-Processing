import tkinter as tk
from tkinter import FALSE, TRUE, messagebox
from tkinter import simpledialog
from tkinter.filedialog import askopenfilenames
import cv2
from PIL import Image, ImageTk

from index import *

image1 = ''
image2 = ''


def set_image(filepath, lbl):
    if not filepath:
        return

    img = Image.open(filepath)
    img = img.convert("L")
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)

    if lbl == lbl1:
        global image1
        image1 = cv2.imread(filepath, 0)
        txt1.grid(row=0, column=1, sticky="nsew", padx=(20, 20), pady=(30, 1))
    else:
        global image2
        image2 = cv2.imread(filepath, 0)
        txt2.grid(row=0, column=2, sticky="nsew", padx=(20, 20), pady=(30, 1))

    lbl.configure(image=img)
    lbl.image = img


def open_image():
    """Open a file for editing."""
    filepaths = askopenfilenames(
        initialdir='./images/',
        title="SelectImage File",
        filetypes=[("All Files", "*.*"), ("PNG Files", "*.png"),
                   ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")]
    )

    if len(filepaths) == 1:
        set_image(filepaths[0], lbl1)
        lbl2.configure(image=None)
        lbl2.image = None
        txt2.grid_remove()

        global image2
        image2 = ''
    elif len(filepaths) == 2:
        set_image(filepaths[0], lbl1)
        set_image(filepaths[1], lbl2)


def check_opened_file():
    if type(image1) == str:
        messagebox.showerror("Error", "No file selected!")
        return FALSE
    return TRUE


def check_ksize():
    try:
        size_int = int(ksize.get())
        if size_int % 2 == 0:
            messagebox.showerror("Error", "Size must be an odd number!")
            return FALSE
        return TRUE
    except ValueError:
        messagebox.showerror("Error", "Size must be an integer!")
        return False


def gaussian():
    if not check_opened_file():
        return

    if not check_ksize():
        return

    sigma = simpledialog.askinteger(
        title="Sigma", prompt="Enter sigma: ", initialvalue=0)

    result_path = gaussian_filter(
        image1, int(ksize.get()), sigma)
    set_image(result_path, lbl2)


def median():
    if not check_opened_file():
        return

    if not check_ksize():
        return

    result_path = median_filter(image1, int(ksize.get()))
    set_image(result_path, lbl2)


def fft():
    if not check_opened_file():
        return
    show_io_fft(image1, image2)

# def test_f():
#     if not check_opened_file():
#         return

#     fourier_transform(image1)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Image Processing")

    global ksize
    ksize = tk.StringVar(value='5')

    window.rowconfigure(0, minsize=350, weight=1)
    window.columnconfigure(1, minsize=350, weight=1)

    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_imgs = tk.Frame(window, bd=2)

    lbl1 = tk.Label(frm_imgs)
    global txt1
    txt1 = tk.Label(frm_imgs, text="Original", fg="white", bg="grey")
    lbl2 = tk.Label(frm_imgs)
    global txt2
    txt2 = tk.Label(frm_imgs, text="Result", fg="white", bg="green")

    btn_open = tk.Button(frm_buttons, text="Choose file",
                         command=open_image, bg="blue", fg="white")
    lbl_size = tk.Label(frm_buttons, text="Size", fg="white", bg="green")
    size_entry = tk.Entry(frm_buttons, textvariable=ksize,
                          justify='center', width=5)
    lbl_filter = tk.Label(frm_buttons, text="Filter", fg="white", bg="green")
    btn_gf = tk.Button(frm_buttons, text="Gaussian Filter", command=gaussian)
    btn_mf = tk.Button(frm_buttons, text="Median Filter", command=median)
    lbl_fft = tk.Label(frm_buttons, text="Fourier", fg="white", bg="green")
    btn_fft = tk.Button(frm_buttons, text="FFT", command=fft)
    # btn_test = tk.Button(frm_buttons, text="Test", command=test_f)

    frm_buttons.grid(row=0, column=0, sticky="nsew")
    frm_imgs.grid(row=0, column=1, sticky="nsew")

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=(10, 5))
    lbl_size.grid(row=1, column=0, sticky="ew", padx=5, pady=(20, 2))
    size_entry.grid(row=2, column=0, sticky="ew", padx=5, pady=(2, 5))
    lbl_filter.grid(row=3, column=0, sticky="ew", padx=5, pady=(20, 5))
    btn_gf.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    btn_mf.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
    lbl_fft.grid(row=6, column=0, sticky="ew", padx=5, pady=(20, 5))
    btn_fft.grid(row=7, column=0, sticky="ew", padx=5, pady=(5, 20))
    # btn_test.grid(row=6, column=0, sticky="ew", padx=5, pady=(30, 5))

    lbl1.grid(row=1, column=1, sticky="nsew", padx=(20, 20), pady=(1, 30))
    txt1.grid(row=0, column=1, sticky="nsew", padx=(20, 20), pady=(30, 1))
    lbl2.grid(row=1, column=2, sticky="nsew", padx=(20, 20), pady=(1, 30))
    txt2.grid(row=0, column=2, sticky="nsew", padx=(20, 20), pady=(30, 1))

    txt1.grid_remove()
    txt2.grid_remove()

    window.mainloop()
