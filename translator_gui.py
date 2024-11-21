# First, create a .env file in the same directory as your script with:
# OPENAI_API_KEY=your-api-key-here

# Main script (translator.py)
import os
from dotenv import load_dotenv
import openai
import tkinter as tk
from tkinter import ttk

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language):
    messages = [
        {"role": "system", "content": f"You are a helpful translator that translates text to {target_language}."},
        {"role": "user", "content": text}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.3
    )
    
    translated_text = response.choices[0].message.content.strip()
    return translated_text

def translate_and_display():
    text = input_text.get("1.0", tk.END)
    target_lang = target_lang_var.get()
    result = translate_text(text, target_lang)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Translation Tool")
root.geometry("500x500")
root.configure(bg="#f0f0f5")

# Add title label
title_label = tk.Label(root, text="Language Translation Tool", font=("Arial", 16), bg="#f0f0f5", fg="#333333")
title_label.pack(pady=10)

# Input text frame
input_frame = tk.Frame(root, bg="#f0f0f5")
input_frame.pack(pady=10)
input_label = tk.Label(input_frame, text="Enter Text to Translate:", font=("Arial", 12), bg="#f0f0f5")
input_label.pack(anchor="w")
input_text = tk.Text(input_frame, height=8, width=55, font=("Arial", 10))
input_text.pack()

# Language selection
options_frame = tk.Frame(root, bg="#f0f0f5")
options_frame.pack(pady=10)
target_lang_var = tk.StringVar(root)
target_lang_var.set("Spanish")  # default value
target_lang_label = tk.Label(options_frame, text="Select Target Language:", font=("Arial", 12), bg="#f0f0f5")
target_lang_label.pack(side="left")
target_lang_menu = ttk.Combobox(options_frame, textvariable=target_lang_var, values=["Spanish", "French", "German", "Chinese"], font=("Arial", 10), width=15)
target_lang_menu.pack(side="left", padx=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_and_display, font=("Arial", 12), bg="#4CAF50", fg="white", width=15)
translate_button.pack(pady=10)

# Output text frame
output_frame = tk.Frame(root, bg="#f0f0f5")
output_frame.pack(pady=10)
output_label = tk.Label(output_frame, text="Translated Text:", font=("Arial", 12), bg="#f0f0f5")
output_label.pack(anchor="w")
output_text = tk.Text(output_frame, height=8, width=55, font=("Arial", 10))
output_text.pack()

root.mainloop()