import tkinter as tk
from tkinter import ttk, messagebox
from tkhtmlview import HTMLLabel
from main import main


def show_weather_data():
    """Display weather data analysis in a new window."""
    try:
        weather_data = main()
        weather_html_window = tk.Toplevel()
        weather_html_window.title("Weather Data Analysis")
        weather_html_label = HTMLLabel(weather_html_window, html=weather_data)
        weather_html_label.pack(expand=True, fill="both")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def main_window():
    """Create the main window for the StormSense application."""
    root = tk.Tk()
    root.title("StormSense: Weather Data Analysis")
    root.geometry("400x250")
    root.configure(bg="#333333")

    custom_font = ("Arial", 12)
    root.option_add("*Font", custom_font)

    style = ttk.Style()

    style.configure("TLabel", background="#333333", foreground="white")

    style.configure("TButton", font=custom_font, background="#002040", foreground="white")

    label = ttk.Label(root, text="Click the button to view weather data analysis:", font=custom_font,
                      background="#333333", foreground="white")
    label.pack(pady=(30, 10))

    subtitle_label = ttk.Label(root, text="Takes a few seconds to load", font=("Arial", 8), background="#333333",
                               foreground="#999999")
    subtitle_label.pack()

    button = ttk.Button(root, text="Run Weather Analysis", command=show_weather_data, style="TButton")
    button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main_window()
