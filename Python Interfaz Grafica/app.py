import dearpygui.dearpygui as dpg
import requests
import threading
import time

# Configuración
CRYPTO_PAIRS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
UPDATE_INTERVAL = 5  # segundos
PRICE_HISTORY_LENGTH = 20  # puntos para el gráfico

# Almacenar datos históricos
price_history = {pair: [0] * PRICE_HISTORY_LENGTH for pair in CRYPTO_PAIRS}  # Inicializar con ceros

def fetch_crypto_price(pair):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print(f"Error obteniendo {pair}: {e}")
        return None

def update_single_crypto(pair):
    price = fetch_crypto_price(pair)
    if price is not None:
        price_history[pair].append(price)
        if len(price_history[pair]) > PRICE_HISTORY_LENGTH:
            price_history[pair].pop(0)
        
        dpg.set_value(f"{pair}_text", f"{pair}: ${price:.2f}")
        dpg.set_value(f"{pair}_plot", [list(range(len(price_history[pair]))), price_history[pair]])

def update_all_prices():
    while True:
        for pair in CRYPTO_PAIRS:
            update_single_crypto(pair)
        time.sleep(UPDATE_INTERVAL)

def setup_gui():
    dpg.create_context()
    dpg.create_viewport(title='Monitor de Criptomonedas', width=800, height=600)
    
    with dpg.window(label="Cripto en Tiempo Real", width=790, height=580):
        dpg.add_text("Precios en Tiempo Real", color=(0, 255, 0))
        dpg.add_separator()
        
        for pair in CRYPTO_PAIRS:
            with dpg.group(horizontal=True):
                dpg.add_text(f"{pair}: ${0:.2f}", tag=f"{pair}_text")
                dpg.add_spacer(width=20)
                dpg.add_button(label="Actualizar", tag=f"{pair}_btn", callback=lambda _, p=pair: update_single_crypto(p))
            
            with dpg.plot(label=f"Historial {pair}", height=150, width=750):
                dpg.add_plot_axis(dpg.mvXAxis, label="Tiempo")
                y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Precio (USD)")
                dpg.add_line_series([], [], parent=y_axis, tag=f"{pair}_plot")
    
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    update_thread = threading.Thread(target=update_all_prices, daemon=True)
    update_thread.start()
    setup_gui()