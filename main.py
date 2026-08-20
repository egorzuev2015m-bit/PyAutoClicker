import customtkinter as ctk
import keyboard
import mouse
import time
import threading

isClicking = False
clicking_thread = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x370")
root.resizable(False, False)
root.title("AUTO CLICKER")
root.iconbitmap("icon.ico")

def start_clicking():
    global isClicking, clicking_thread
    if isClicking:
        return
    isClicking = True
    status_label.configure(text="ACTIVE", text_color="#FF4444")
    start_btn.configure(text="STOP", fg_color="#D35B58", hover_color="#C0504D")
    clicking_thread = threading.Thread(target=click_loop, daemon=True)
    clicking_thread.start()

def stop_clicking():
    global isClicking
    isClicking = False
    status_label.configure(text="STOPPED", text_color="#00FF00")
    start_btn.configure(text="START", fg_color="#1F6AA5", hover_color="#144870")

def toggle_clicking():
    if isClicking:
        stop_clicking()
    else:
        start_clicking()

def click_loop():
    while isClicking:
        mouse.double_click(button="left")
        time.sleep(0.01)

def hotkey_handler():
    root.after(0, toggle_clicking)

keyboard.add_hotkey("Alt + P", hotkey_handler)

frame = ctk.CTkFrame(root)
frame.pack(expand=True, fill="both", padx=30, pady=30)

title = ctk.CTkLabel(frame, text="AUTO CLICKER", font=("Arial", 28, "bold"))
title.pack(pady=(20, 10))

status_label = ctk.CTkLabel(frame, text="STOPPED", font=("Arial", 20, "bold"), text_color="#00FF00")
status_label.pack(pady=10)

start_btn = ctk.CTkButton(frame, text="START", command=toggle_clicking, width=250, height=60, font=("Arial", 18, "bold"), corner_radius=15, fg_color="#1F6AA5", hover_color="#144870")
start_btn.pack(pady=20)

hotkey_label = ctk.CTkLabel(frame, text="Hotkey: Alt + P", font=("Arial", 14))
hotkey_label.pack(pady=(10, 5))

info_label = ctk.CTkLabel(frame, text="Press button or Alt+P to start/stop", font=("Arial", 12), text_color="gray")
info_label.pack(pady=5)

def on_close():
    global isClicking
    isClicking = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()