import tkinter as tk

class EndGame:
    def __init__(self):
        """ Initialize view of the game """
        # Constants
        self.CONTROL_FRAME_HEIGHT = 700

        # Create window
        self.window = tk.Tk()
        self.window.title("Battleship")

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = self.CONTROL_FRAME_HEIGHT, 
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 1, column = 2, padx=40, pady=40)
        (self.repeat_button, self.quit_button, self.who_won) = self.add_control()

    def add_control(self):
        """ 
        Create control buttons and welcome message, and add them to the control frame 
        """
        welcome = tk.Label(self.control_frame, text="Game has ended", font=("Helvetica", 20))
        welcome.grid(row=1, column = 1)

        who_won = tk.Label(self.control_frame, text="", font=("Helvetica", 20))
        who_won.grid(row=2, column = 1)

        repeat_button = tk.Button(self.control_frame, text="Repeat Game?", font=("Helvetica", 10))
        repeat_button.grid(row=3, column=1)

        quit_button = tk.Button(self.control_frame, text="Quit", font=("Helvetica", 10))
        quit_button.grid(row=4, column=1)

        return (repeat_button, quit_button, who_won)

    def set_repeat_handler(self, handler):
        """ set handler for clicking on start button to the function handler """
        self.repeat_button.configure(command = handler)

    def set_quit_handler(self, handler):
        """ set handler for clicking on pause button to the function handler """
        self.quit_button.configure(command = handler)