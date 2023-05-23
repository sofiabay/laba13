import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    key = '28aa4e2daa08ffdf9d4fd431dc578b2d'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    return weather

def get_weather_info(city):
    data = get_weather(city)
    if data:
        main = data["main"]
        temperature = main["temp"]
        weather_desc = data["weather"][0]["description"]
        return (temperature, weather_desc)
    else:
        return None

def get_weather_report(city):
    weather_info = get_weather_info(city)
    if weather_info:
        tk.messagebox.showinfo(
            "Прогноз погоды",
            f"""Температура: {weather_info[0]}""",
        )
    else:
        tk.messagebox.showerror("Ошибка", "Город не найден")

def main():
    root = tk.Tk()
    root.geometry("300x150")
    root.title("Weather App")

    city_label = tk.Label(root, text="Введите город:")
    city_label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    get_weather_button = tk.Button(
        root, text="Узнать погоду", command=lambda: get_weather_report(city_entry.get())
    )
    get_weather_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()