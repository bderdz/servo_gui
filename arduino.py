import time
import serial
from serial import Serial


class Arduino:
    """
    A class representing an Arduino connection over a serial port.

    This class allows establishing a connection to an Arduino board via a serial port,
    sending commands (servo angle adjustments), and disconnecting from the board.
    """

    def __init__(self, __port: str, baud_rate: int) -> None:
        self.__port: str = __port
        self.__baud_rate = baud_rate
        self.__board: Serial | None = None
        self.status: bool = False

    def connect(self) -> str:
        try:
            self.__board = Serial(self.__port, self.__baud_rate, timeout=1)
            time.sleep(2)
            self.status = True
            return "Connected"
        except serial.SerialException as e:
            self.status = False
            return str(e.__context__)

    def disconnect(self) -> None:
        if self.__board:
            self.__board.close()
        self.status = False

    def set_port(self, __port: str) -> None:
        self.__port = __port

    def serial_write(self, value: int):
        if self.status:
            self.__board.write(bytes([value]))
