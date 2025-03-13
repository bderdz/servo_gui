import time

from serial import Serial
import serial.tools.list_ports as list_ports
import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL
from tkinter.ttk import Label

SERIAL_PORT = "/dev/cu.usbmodem11201"
BAUD_RATE = 9600
WIDTH = 500
HEIGHT = 500

slider_label: Label | None = None
arduino: Serial | None = None


def update_slider(angle) -> None:
    global arduino
    angle = int(float(angle))

    arduino.write(bytes([angle]))
    slider_label.config(text=f"Angle: {angle}")


# def get_all_ports() -> List[str]:

def main() -> None:
    global slider_label, arduino

    arduino = Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("servo gui")

    label = ttk.Label(root, text="Arduino Servo GUI")
    label.pack(pady=20)

    # Servo Rotation Slider
    slider_label = ttk.Label(root, text="Angle: 0")
    slider_label.pack()

    slider = ttk.Scale(root, orient=HORIZONTAL, length=WIDTH // 2, from_=0, to=180, command=update_slider)
    slider.pack()

    root.mainloop()

    # available_ports = list_ports.comports()
    # available_ports = [port.device for port in available_ports]
    #
    # print(available_ports)


if __name__ == '__main__':
    main()
