import tkinter as tk
from tkinter import ttk, messagebox

# Diccionario de conversiones
conversiones = {
    "Temperatura": {
        "Celsius": lambda x: {"Fahrenheit": x * 9/5 + 32, "Kelvin": x + 273.15},
        "Fahrenheit": lambda x: {"Celsius": (x - 32) * 5/9, "Kelvin": (x - 32) * 5/9 + 273.15},
        "Kelvin": lambda x: {"Celsius": x - 273.15, "Fahrenheit": (x - 273.15) * 9/5 + 32}
    },
    "Longitud": {
        "Metros": lambda x: {"Kilómetros": x / 1000, "Millas": x / 1609.34, "Pies": x * 3.28084},
        "Kilómetros": lambda x: {"Metros": x * 1000, "Millas": x / 1.60934, "Pies": x * 3280.84},
        "Millas": lambda x: {"Metros": x * 1609.34, "Kilómetros": x * 1.60934, "Pies": x * 5280},
        "Pies": lambda x: {"Metros": x / 3.28084, "Kilómetros": x / 3280.84, "Millas": x / 5280}
    },
    "Peso": {
        "Gramos": lambda x: {"Kilogramos": x / 1000, "Libras": x / 453.592, "Onzas": x / 28.3495},
        "Kilogramos": lambda x: {"Gramos": x * 1000, "Libras": x * 2.20462, "Onzas": x * 35.274},
        "Libras": lambda x: {"Gramos": x * 453.592, "Kilogramos": x / 2.20462, "Onzas": x * 16},
        "Onzas": lambda x: {"Gramos": x * 28.3495, "Kilogramos": x / 35.274, "Libras": x / 16}
    }
}

# Función de conversión
def convertir():
    categoria = combo_categoria.get()
    unidad_origen = combo_origen.get()
    valor = entrada_valor.get()

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return

    resultados = conversiones[categoria][unidad_origen](valor)
    salida_texto = f"\n🔁 {valor} {unidad_origen} equivale a:\n"
    for unidad_destino, resultado in resultados.items():
        salida_texto += f"→ {resultado:.2f} {unidad_destino}\n"

    etiqueta_resultado.config(text=salida_texto)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("🧮 Conversor de Unidades")
ventana.geometry("400x500")
ventana.resizable(False, False)

tk.Label(ventana, text="Conversor de Unidades", font=("Arial", 16)).pack(pady=10)

# Categoría
tk.Label(ventana, text="Selecciona categoría:", font=("Arial", 12)).pack()
combo_categoria = ttk.Combobox(ventana, state="readonly", font=("Arial", 11))
combo_categoria["values"] = list(conversiones.keys())
combo_categoria.pack(pady=5)

# Unidad origen
tk.Label(ventana, text="Unidad de origen:", font=("Arial", 12)).pack()
combo_origen = ttk.Combobox(ventana, state="readonly", font=("Arial", 11))
combo_origen.pack(pady=5)

# Actualizar unidades según categoría
def actualizar_unidades(event):
    categoria = combo_categoria.get()
    unidades = list(conversiones[categoria].keys())
    combo_origen["values"] = unidades
    combo_origen.set("")

combo_categoria.bind("<<ComboboxSelected>>", actualizar_unidades)

# Valor
tk.Label(ventana, text="Valor a convertir:", font=("Arial", 12)).pack()
entrada_valor = tk.Entry(ventana, font=("Arial", 11))
entrada_valor.pack(pady=5)

# Botón
tk.Button(ventana, text="Convertir", command=convertir, font=("Arial", 12)).pack(pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 11), justify="left")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
