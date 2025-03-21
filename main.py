import tkinter as tk
from gui import ServoApp


def main() -> None:
    root = tk.Tk()
    app = ServoApp(root)
    
    app.run()


if __name__ == '__main__':
    main()
