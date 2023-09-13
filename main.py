from tkinter import *

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
}



def text_to_morse():
    text_input = text_entry.get().upper().split(" ")
    text = ""
    for word in text_input:
        text_word = ""
        for letter in word:
            text_word = text_word + f"  {morse_code_dict[f'{letter}']}"
        text = text + f"{text_word}      "
    morse_code.delete(1.0, END)
    morse_code.insert(1.0, f"{text}")

window = Tk()
window.title("Text To Morse Code Converter")
window.config(padx=50, pady=50)

label = Label(text="Enter Your Text:")
label.grid(row=0, column=0)

text_entry = Entry()
text_entry.grid(row=1, column=0)
text_entry.config(width=35)

submit_button = Button(text="Convert to Morse Code", command=text_to_morse)
submit_button.grid(row=2, column=0)

morse_code = Text(height=10, borderwidth=10)
morse_code.grid(row=3, column=0)

window.mainloop()
