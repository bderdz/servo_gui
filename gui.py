import serial.tools.list_ports as list_ports
import tkinter as tk
from tkinter.ttk import Label, Combobox, Button, Scale, Frame
from tkinter.constants import HORIZONTAL
from arduino import Arduino

BAUD_RATE = 9600


class ServoApp:
    """
    A GUI application for controlling a servo motor via Arduino.

    This class provides an interface for selecting a serial port, connecting to the Arduino,
    and controlling the servo motor angle via a slider.
    """

    WIDTH = 500
    HEIGHT = 400

    def __init__(self, root: tk.Tk) -> None:
        self.root: tk.Tk = root
        self.__ports: list[str] = []
        self.__arduino = Arduino("", BAUD_RATE)

        # GUI WIDGETS
        self.ports_menu: Combobox | None = None
        self.slider_label: Label | None = None
        self.port_status: Label | None = None

    def refresh_ports(self) -> None:
        available_ports = list_ports.comports()
        self.__ports = [f"{port.description} - {port.device}" for port in available_ports]
        self.ports_menu["values"] = self.__ports

    def select_port(self, event):
        selected_port: str = self.ports_menu.get().split(" - ")[1]
        self.__arduino.set_port(selected_port)

    def update_slider(self, angle: str) -> None:
        angle = int(float(angle))
        self.slider_label.config(text=f"Angle: {angle}")

        self.__arduino.serial_write(angle)

    def connect_port(self) -> None:
        if self.__arduino.status:
            self.__arduino.disconnect()

        output = self.__arduino.connect()
        self.port_status["text"] = output

    def run(self) -> None:
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.title("ServoGUI Controller")

        # Servo Rotation Slider
        servo_frame = Frame(self.root)
        servo_frame.pack(pady=50)
        self.slider_label = Label(servo_frame, text="Angle: 0")
        self.slider_label.grid(row=0, column=0, pady=5)

        slider = Scale(servo_frame,
                       orient=HORIZONTAL,
                       length=self.WIDTH // 1.8,
                       from_=0,
                       to=180,
                       command=self.update_slider)
        slider.grid(row=1, column=0)

        # Port connection
        port_frame = Frame(self.root)
        port_frame.pack(pady=20)

        # List of available ports
        self.ports_menu = Combobox(port_frame,
                                   values=self.__ports,
                                   state="readonly", width=30)
        self.ports_menu.set("Choose port")
        self.ports_menu.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.ports_menu.bind("<<ComboboxSelected>>", self.select_port)

        self.port_status = Label(port_frame, text="Not Connected")
        self.port_status.grid(row=1, column=0, columnspan=3, pady=10)
        # Serial port
        reload_button = Button(port_frame, text="RELOAD", command=self.refresh_ports)
        reload_button.grid(row=0, column=2)
        # Connect to port
        connect_button = Button(port_frame, text="CONNECT", command=self.connect_port)
        connect_button.grid(row=2, column=0, columnspan=3)

        self.root.mainloop()
