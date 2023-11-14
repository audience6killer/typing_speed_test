import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from showtext import *

# Constants
FONT = ("Ubuntu", 16)
FONT_MEDIUM = ("Ubuntu", 13)
FONT_BIG = ("Ubuntu", 24)
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

        self.start_timer = False
        self.timer_count = 60
        self.points = 0
        #self.text_grid = None

        # Frames of the window
        self.information_frame = tk.Frame(self, width=600, height=100, bg=LABELS)
        self.information_frame.grid(row=0, column=0, padx=5, pady=5)

        self.test_display = tk.Frame(self, width=600, height=150, bg=LABELS)
        self.test_display.grid(row=1, column=0, padx=5, pady=5)

        self.text_grid = DisplayTextHandler(self.test_display, text='Nothing yet',
                                            bg='white', width=20, font=FONT_BIG,
                                            row=1, column=0)
        # Contents of the Frames
        # Information frame
        welcome_label = tk.Label(self.information_frame, text="Welcome",
                                 font=('Ubuntu', 18, 'bold'),
                                 bg=LABELS)
        welcome_label.grid(row=0, column=0, padx=5, pady=5, ipadx=10, columnspan=2)

        instructions_label = tk.Label(self.information_frame,
                                      text="To start the test please press the 'Start' button, "
                                           "to stop before the time is up just press 'Stop'.\n"
                                           "Each time you press 'Space' the word will be checked, "
                                           "and a new word will appear",
                                      bg=LABELS)
        instructions_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.start_button = tk.Button(self.information_frame, text='Start',
                                      background=BUTTONS, width=15, command=self.start_test)
        self.start_button.grid(row=2, column=0, padx=3, pady=3)

        self.stop_button = tk.Button(self.information_frame, text='Stop',
                                     background=BUTTONS, width=15,
                                     state=tk.DISABLED, command=self.stop_test)
        self.stop_button.grid(row=2, column=1, padx=3, pady=3)

        # Display Frame
        text_display_label = tk.Label(self.test_display,
                                      text="Text to write",
                                      bg=LABELS)
        text_display_label.grid(row=0, column=0, padx=3, pady=3)

        time_display_label = tk.Label(self.test_display,
                                      text='Time Remaining',
                                      bg=LABELS)
        time_display_label.grid(row=0, column=1, padx=3, pady=3)

        words_label = tk.Label(self.test_display,
                               text='Words',
                               bg=LABELS)
        words_label.grid(row=0, column=2, padx=3, pady=3)

        self.time_remaining = tk.Label(self.test_display, text='00',
                                       bg='white', width=8, font=FONT_BIG)
        self.time_remaining.grid(row=1, column=1, padx=3, pady=3)

        self.score_label = tk.Label(self.test_display, text='0',
                                    bg='white', width=8, font=FONT_BIG)
        self.score_label.grid(row=1, column=2, padx=3, pady=3)

        user_input_label = tk.Label(self.test_display, text='User Entry', bg=LABELS)
        user_input_label.grid(row=2, column=0, padx=3, pady=3, columnspan=3)

        self.word_written = tk.StringVar()
        self.user_input = ttk.Entry(self.test_display, font=FONT_BIG,
                                    textvariable=self.word_written, state=tk.DISABLED,
                                    justify='center')
        self.user_input.grid(row=3, column=0, padx=3, pady=5, columnspan=3, sticky='w' + 'e' + 'n' + 's')

    def start_test(self):
        self.start_button['state'] = tk.DISABLED
        self.stop_button['state'] = tk.NORMAL
        self.user_input['state'] = tk.NORMAL
        if not self.start_timer:
            self.start_timer = True
            self.decrease_timer()

        self.text_grid.change_word()
        self.user_input.focus()

        # We bind the space bar to check everytime a word is written
        self.bind("<space>", func=self.check_word)

    def decrease_timer(self):
        if self.timer_count > 0 and self.start_timer:
            self.time_remaining.config(text=self.timer_count)
            self.timer_count -= 1
            self.after(1000, self.decrease_timer)
        else:
            self.stop_test()

    # TODO: Change word color depending on the result
    def check_word(self, event):
        if self.text_grid.get_word() == self.word_written.get()[:-1]:
            self.points += 1
            self.score_label.config(text=self.points)

        self.user_input.delete(0, 'end')
        self.text_grid.change_word()

    def stop_test(self):
        self.start_timer = False
        self.timer_count = 60
        tkinter.messagebox.showinfo(title='Test Completed',
                                    message=f'You achieved {self.points} per minute')

        self.start_button['state'] = tk.NORMAL
        self.stop_button['state'] = tk.DISABLED

        self.text_grid.clear_text()
        self.time_remaining.config(text='00')
        self.score_label.config(text='0')
        self.user_input.delete(0, 'end')
        self.user_input['state'] = tk.DISABLED
        self.unbind("<space>")

        self.start_button.focus()







