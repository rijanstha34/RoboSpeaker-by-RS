from gtts import gTTS
import pygame
import tkinter as tk
from tkinter import messagebox
import os
import time

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Function to convert text to speech
def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Text", "Please enter something to speak.")
        return

    try:
        import tempfile
        fd, filename = tempfile.mkstemp(suffix=".mp3")
        os.close(fd)  # close the file so gTTS can write to it
        tts = gTTS(text=text, lang='en')
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            root.update()
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Exit safely
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Create GUI window
root = tk.Tk()
root.title("Code By RS")
root.geometry("400x300")
root.resizable(False, False)

# Style
root.configure(bg="#e6f2ff")
tk.Label(root, text="Welcome", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=10)

# Text input box
text_input = tk.Text(root, height=6, width=40, font=("Arial", 12))
text_input.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#e6f2ff")
btn_frame.pack(pady=10)

speak_btn = tk.Button(btn_frame, text="Speak", font=("Arial", 12), command=speak_text, width=10, bg="#66ccff")
speak_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", font=("Arial", 12), command=exit_app, width=10, bg="#ff6666")
exit_btn.grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()
