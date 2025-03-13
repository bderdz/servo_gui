import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL
from tkinter.ttk import Label

WIDTH = 500
HEIGHT = 500

slider_label: Label | None = None

def update_slider(value) -> None:
    value = int(float(value))

    slider_label.config(text=f"Angle: {value}")

def main() -> None:
    global slider_label

    root = tk.Tk()

    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("servo gui")

    label = ttk.Label(root, text="Arduino Servo GUI")
    label.pack(pady=20)

    # Servo Rotation Slider
    slider_label = ttk.Label(root, text="Angle: 0")
    slider_label.pack()

    slider = ttk.Scale(root, orient=HORIZONTAL, length=WIDTH//2, from_=-90, to=90, command=update_slider)
    slider.pack()

    root.mainloop()

if __name__ == '__main__':
    main()