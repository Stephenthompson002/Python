import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io

API_KEY = "7da33ccc2f2b859e6723e043191675f8"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        icon_code = data["weather"][0]["icon"]

        # Load and display icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        image_data = icon_response.content
        image = Image.open(io.BytesIO(image_data)).resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        icon_label.config(image=photo)
        icon_label.image = photo  # Prevent garbage collection

        # Update result text
        result_label.config(
            text=(f"{city.capitalize()}\n\n"
                  f"🌡 Temperature: {temp}°C\n"
                  f"🌥 Condition: {condition}\n"
                  f"💧 Humidity: {humidity}%\n"
                  f"💨 Wind Speed: {wind_speed} m/s")
        )
    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve weather data.\n{e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#e3f2fd")

tk.Label(root, text="Enter City", font=("Helvetica", 14), bg="#e3f2fd").pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather, bg="#42a5f5", fg="white").pack(pady=10)

icon_label = tk.Label(root, bg="#e3f2fd")
icon_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#e3f2fd", justify='center')
result_label.pack(pady=20)

root.mainloop()
