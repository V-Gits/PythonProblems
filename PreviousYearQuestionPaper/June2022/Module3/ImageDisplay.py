import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Display Image")
image = Image.open(".\\PyProbs-Updated\\PreviousYearQuestionPaper\\June2022\\Module3\\bird.gif")
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()

root.mainloop()