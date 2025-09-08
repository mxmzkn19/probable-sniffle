import tkinter as tk
from tkinter import messagebox
import webbrowser

# Данные конференций
meetings = [
    {
        "subject": "Web-програмування",
        "teacher": "Ярослав Кривий",
        "link": "https://meet.google.com/ztn-hzje-arf",
        "id": None,
        "passcode": None
    },
    {
        "subject": "Аналіз вимог до програмного забезпечення",
        "teacher": "Мильцев Олександр",
        "link": "https://us04web.zoom.us/j/6124502314?pwd=T0hvdTgyL0lCTlFrOUFSZnpYYUpSQT09",
        "id": "612 450 2314",
        "passcode": "12345"
    },
    {
        "subject": "Інженерія даних",
        "teacher": "Кудін Олексій",
        "link": "https://us04web.zoom.us/j/9971262369?pwd=KbnZh7gVBfvt9ukRYJuiYTeohyuLVj.1",
        "id": "997 126 2369",
        "passcode": "KdNF4T"
    },
    {
        "subject": "Нереляційні бази даних",
        "teacher": "Лимаренко Юлія",
        "link": "https://us02web.zoom.us/j/7422143985?pwd=UVNLMVNLK1lac2xjVzdOaEJFa2Nwdz09",
        "id": "742 214 3985",
        "passcode": "379"
    }
]

# Открыть ссылку в браузере
def open_link(url):
    webbrowser.open(url)

# Показать информацию о конференции
def show_info(meeting):
    info = f"Предмет: {meeting['subject']}\n"
    info += f"Викладач: {meeting['teacher']}\n"
    if meeting["id"]:
        info += f"Meeting ID: {meeting['id']}\n"
    if meeting["passcode"]:
        info += f"Пароль: {meeting['passcode']}\n"
    messagebox.showinfo("Інформація", info)

# UI
root = tk.Tk()
root.title("Мої конференції")

for m in meetings:
    frame = tk.Frame(root, pady=5)
    frame.pack(fill="x")

    lbl = tk.Label(frame, text=f"{m['subject']} ({m['teacher']})", anchor="w")
    lbl.pack(side="left", padx=5)

    btn_open = tk.Button(frame, text="Відкрити", command=lambda url=m["link"]: open_link(url))
    btn_open.pack(side="right", padx=5)

    btn_info = tk.Button(frame, text="Інфо", command=lambda meeting=m: show_info(meeting))
    btn_info.pack(side="right")

root.mainloop()
