import tkinter as tk

# Constants
FONT = ("Ubuntu", 12)
FONT_MEDIUM = ("Ubuntu", 13)
BASE_COLOR = "#F1EAFF"
LABELS = "#E5D4FF"
BUTTONS = "#D0A2F7"


# Class dedicated to handle the main window of the Typer Speed Test
class MainGui(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()

        # Initial window configuration
        self.title(title)
        self.maxsize(geometry[0], geometry[1])
        self.config(padx=20, pady=5, bg=BASE_COLOR)
        self.option_add('*FONT', FONT)

        # Frames of the window
        self.information_frame = tk.Frame(self, width=900, height=100, bg=LABELS)
        self.information_frame.grid(row=0, column=0, padx=5, pady=5)

        self.test_display = tk.Frame(self, width=900, height=150, bg=LABELS)
        self.test_display.grid(row=1, column=0, padx=5, pady=5)

        # Contents of the Frames
        # Information frame
        welcome_label = tk.Label(self.information_frame, text="Welcome",
                                 font=('Ubuntu', 18, 'bold'),
                                 bg=LABELS)
        welcome_label.grid(row=0, column=0, padx=5, pady=5, ipadx=10, columnspan=2)

        instructions_label = tk.Label(self.information_frame,
                                      text="To start the test please press the 'Start' button, "
                                           "to stop before the time is up just press 'Stop'",
                                      bg=LABELS)
        instructions_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.start_button = tk.Button(self.information_frame, text='Start',
                                      background=BUTTONS, width=15)
        self.start_button.grid(row=2, column=0, padx=3, pady=3)

        self.stop_button = tk.Button(self.information_frame, text='Stop',
                                     background=BUTTONS, width=15)
        self.stop_button.grid(row=2, column=1, padx=3, pady=3)

        # Display Frame
        text_display_label = tk.Label(self.test_display,
                                      text="Text to write",
                                      bg=LABELS)
        text_display_label.grid(row=0, column=0, padx=3, pady=3, sticky='w'+'e'+'n'+'s')

        time_display_label = tk.Label(self.test_display,
                                      text='Time Remaining',
                                      bg=LABELS)
        time_display_label.grid(row=0, column=1, padx=3, pady=3, sticky='w'+'e'+'n'+'s')

        words_label = tk.Label(self.test_display,
                               text='Words',
                               bg=LABELS)
        words_label.grid(row=0, column=2, padx=3, pady=3, sticky='w'+'e'+'n'+'s')

        self.text_grid = tk.Label(self.test_display, text='Nothing yet',
                                  bg='white', width=50, font=FONT_MEDIUM)
        self.text_grid.grid(row=1, column=0, padx=3, pady=3)

        self.time_remaining = tk.Label(self.test_display, text='00:00',
                                       bg='white', width=20, font=FONT_MEDIUM)
        self.time_remaining.grid(row=1, column=1, padx=3, pady=3)

        self.word_count = tk.Label(self.test_display, text='0',
                                   bg='white', width=20, font=FONT_MEDIUM)
        self.word_count.grid(row=1, column=2, padx=3, pady=3)

        user_input_label = tk.Label(self.test_display, text='User Entry', bg=LABELS)
        user_input_label.grid(row=2, column=0, padx=3, pady=3, columnspan=3)

        self.user_input = tk.Entry(self.test_display, font=FONT_MEDIUM)
        self.user_input.grid(row=3, column=0, padx=3, pady=5, columnspan=3, sticky='w'+'e'+'n'+'s')


