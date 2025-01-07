import tkinter as tk
from tkinter import messagebox
import requests

# Define the API key and base URL
API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}randompassword"

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    # API request URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    try:
        # Make the request
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check if the city was found
        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"].capitalize())
            return

        # Extract data
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display the data
        result_label.config(text=f"Weather in {city_name}, {country}:\n"
                                 f"Temperature: {temperature}°C\n"
                                 f"Condition: {weather.capitalize()}\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Wind Speed: {wind_speed} m/s")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Weather Data Fetcher")
root.geometry("400x300")

# City input
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=5)

# Fetch button
fetch_button = tk.Button(root, text="Get Weather", command=get_weather)
fetch_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
