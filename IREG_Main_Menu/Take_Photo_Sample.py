# Importing all the required modules to create the UI
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class Take_Photo_Sample:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x700+0+0")
        self.root.title("Take Photo Sample")