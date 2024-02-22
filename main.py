import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser

def show_info():
    ip = entry.get()
    messagebox.showinfo("Information", f"You entered: {ip}")

def search():
    ip = entry.get()
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        ip_details = response.json()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"IP: {ip}\n", "purple")
        output_text.insert(tk.END, f"Hostname: {ip_details.get('hostname', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"City: {ip_details.get('city', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Region: {ip_details.get('region', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Country: {ip_details.get('country', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Location: {ip_details.get('loc', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Organization: {ip_details.get('org', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Postal Code: {ip_details.get('postal', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Timezone: {ip_details.get('timezone', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"ASN: {ip_details.get('asn', 'N/A')}\n", "purple")
        output_text.insert(tk.END, f"Carrier: {ip_details.get('carrier', 'N/A')}\n", "purple")
    else:
        messagebox.showerror("Error", f"Failed to fetch details for IP: {ip}")

def hide_window():
    root.withdraw()

def close_window():
    root.destroy()

def on_drag(event):
    x = root.winfo_pointerx() - root._offsetx
    y = root.winfo_pointery() - root._offsety
    root.geometry(f"+{x}+{y}")

def on_drag_start(event):
    root._offsetx = event.x
    root._offsety = event.y

def toggle_fullscreen():
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def open_website_1():
    webbrowser.open("https://epieos.com/)

def open_website_2():
    webbrowser.open("https://www.numlookup.com/")

root = tk.Tk()
root.title("Devil IP OSINT (made by Lucifer)")
root.configure(bg="black")
root.attributes("-topmost", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600
window_height = 400
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.overrideredirect(True)

top_panel = tk.Frame(root, bg="black", bd=2, relief="solid", highlightbackground="purple", highlightthickness=2)
top_panel.pack(fill=tk.X)

title_label = tk.Label(top_panel, text="Devil IP OSINT", bg="black", fg="purple", padx=10)
title_label.pack(side=tk.LEFT)

hide_button = tk.Button(top_panel, text="Hide", command=hide_window, bg="black", fg="purple")
hide_button.pack(side=tk.RIGHT, padx=5)

exit_button = tk.Button(top_panel, text="Exit", command=close_window, bg="black", fg="purple")
exit_button.pack(side=tk.RIGHT, padx=5)

top_panel.bind("<ButtonPress-1>", on_drag_start)
top_panel.bind("<B1-Motion>", on_drag)

label = tk.Label(root, text="Enter IP Address:", bg="black", fg="purple")
label.pack()

entry = tk.Entry(root, bg="black", fg="purple")
entry.pack()

search_button = tk.Button(root, text="Search", command=search, bg="black", fg="purple")
search_button.pack()

output_frame = tk.Frame(root, bg="black")
output_frame.pack()

output_text = tk.Text(output_frame, height=10, width=40, bg="black", fg="purple", bd=2, relief="solid")
output_text.pack()

output_text.tag_configure("purple", foreground="purple")

website_button_2 = tk.Button(root, text="Number OSINT (WEBSITE)", command=open_website_2, bg="black", fg="purple")
website_button_2.pack(side=tk.LEFT)

website_button_1 = tk.Button(root, text="Email OSINT (WEBSITE)", command=open_website_1, bg="black", fg="purple")
website_button_1.pack(side=tk.LEFT)

root.mainloop()
