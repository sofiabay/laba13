import tkinter as tk
import requests

def get_bitcoin_rate(target_currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={target_currency.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "bitcoin" in data:
            return data["bitcoin"][target_currency.lower()]
        else:
            return None
    else:
        return None


def show_bitcoin_rate():
    target_currency = target_currency_var.get()
    bitcoin_rate = get_bitcoin_rate(target_currency)

    if bitcoin_rate:
        result_label.config(text=f"1 Bitcoin -:\n{bitcoin_rate} {target_currency.upper()}")
    else:
        result_label.config(text="Биткоины")


def main():
    global target_currency_var, result_label

    # List of currencies
    currencies = ["USD", "EUR", "RUB"]

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Обменник Bitcoin")

    bitcoin_label = tk.Label(root, text="Обменник Bitcoin", font=("Arial", 16))
    bitcoin_label.pack()

    target_currency_label = tk.Label(root, text="Выберите валюту:")
    target_currency_label.pack()
    target_currency_var = tk.StringVar(root)
    target_currency_var.set(currencies[0])
    target_currency_menu = tk.OptionMenu(root, target_currency_var, *currencies)
    target_currency_menu.pack()

    show_rate_button = tk.Button(
        root, text="Показать курс", command=show_bitcoin_rate)
    show_rate_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()