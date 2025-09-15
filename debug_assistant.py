import os
import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

genai.configure(api_key="AIzaSyBq3mRz46QKDFXpShE3sIqzyYnEacQu-yU")

model = genai.GenerativeModel("gemini-1.5-flash")

def send_message():
    user_text = user_input.get().strip()
    if not user_text:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_text + "\n", "user")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

    user_input.set("")

    try:
        response = model.generate_content(user_text)
        bot_text = response.text.strip()
    except Exception as e:
        bot_text = "Error: " + str(e)

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Bot: " + bot_text + "\n\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

root = tk.Tk()
root.title("Gemini Chatbot")
root.geometry("500x600")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.X)

user_input = tk.StringVar()
entry = tk.Entry(frame, textvariable=user_input)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry.bind("<Return>", lambda event: send_message())

send_btn = tk.Button(frame, text="Send", command=send_message)
send_btn.pack(side=tk.RIGHT)

root.mainloop()

