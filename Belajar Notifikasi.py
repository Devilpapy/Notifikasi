import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time
import threading

def show_notification(title, message, timeout):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )

def schedule_notification():
    title = title_entry.get()
    message = message_entry.get()
    try:
        delay = int(time_entry.get())
        timeout = int(timeout_entry.get())
    except ValueError:
        messagebox.showwarning("Input SALAH!!!", "Masukkan Input waktu yang VALID(angka)!!")
        return

    if not title or not message:
        messagebox.showwarning("Isian KOSONG", "Tolong diisi semua!!")
        return

    def delayed_notification():
        time.sleep(delay)
        show_notification(title, message, timeout)

    threading.Thread(target=delayed_notification).start()
    messagebox.showinfo("Peringatan!!", f"Notifikasi akan muncul dalam {delay} detik.")

root = tk.Tk()
root.title("Notifikasi")
root.geometry("300x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Tittle Notifikasi:")
title_label.pack(pady=5)
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

message_label = tk.Label(root, text="Pesan Notifikasi:")
message_label.pack(pady=5)
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

time_label = tk.Label(root, text="Delay (dalam detik):")
time_label.pack(pady=5)
time_entry = tk.Entry(root, width=10)
time_entry.pack(pady=5)

timeout_label = tk.Label(root, text="Notifikasi Akan Hilang (dalam detik):")
timeout_label.pack(pady=5)
timeout_entry = tk.Entry(root, width=10)
timeout_entry.pack(pady=5)

schedule_button = tk.Button(root, text="Jalankan", command=schedule_notification)
schedule_button.pack(pady=20)

root.mainloop()
