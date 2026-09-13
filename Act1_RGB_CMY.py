"""
Cuadro de colores RGB y CMY con barras deslizadoras
-----------------------------------------------------

Cuadro izquierdo: 3 sliders R, G, B controlan directamente el color
                  (modelo aditivo: 0,0,0 = negro, 255,255,255 = blanco)
 
Cuadro derecho:   3 sliders C, M, Y controlan cuanta tinta se "resta"
                  a la luz blanca (modelo sustractivo: 0,0,0 = blanco,
                  255,255,255 = negro)

"""
 
import tkinter as tk
 
 
def rgb_a_hex(r, g, b):
    """Convierte 3 valores 0-255 al formato hexadecimal que usa Tkinter."""
    # Nos aseguramos de que el valor quede dentro del rango válido
    r = max(0, min(255, int(r)))
    g = max(0, min(255, int(g)))
    b = max(0, min(255, int(b)))
    return f"#{r:02x}{g:02x}{b:02x}"
 
 
def actualizar_rgb(_=None):
    """Lee los 3 sliders RGB y pinta el cuadro con esa mezcla de luz."""
    r = slider_r.get()
    g = slider_g.get()
    b = slider_b.get()
    cuadro_rgb.config(bg=rgb_a_hex(r, g, b))
    etiqueta_rgb.config(text=f"R={r}  G={g}  B={b}")
 
 
def actualizar_cmy(_=None):
    """
    Lee los 3 sliders CMY (cuanta tinta hay de cada uno, 0-255) y
    calcula el RGB resultante restando cada tinta de la luz blanca (255).
 
    Formula clasica de conversion CMY -> RGB:
        R = 255 - C
        G = 255 - M
        B = 255 - Y
    """
    c = slider_c.get()
    m = slider_m.get()
    y = slider_y.get()
 
    r = 255 - c
    g = 255 - m
    b = 255 - y
 
    cuadro_cmy.config(bg=rgb_a_hex(r, g, b))
    etiqueta_cmy.config(text=f"C={c}  M={m}  Y={y}")
 
 
# Construccion de la ventana 
 
ventana = tk.Tk()
ventana.title("Cuadros de color RGB vs CMY")
ventana.geometry("560x420")
 
marco = tk.Frame(ventana)
marco.pack(expand=True, fill="both", padx=20, pady=20)
 
# ============== COLUMNA RGB ==============
columna_rgb = tk.Frame(marco)
columna_rgb.pack(side="left", expand=True, fill="both", padx=15)
 
tk.Label(columna_rgb, text="Modelo RGB", font=("Arial", 12, "bold")).pack(pady=5)
 
cuadro_rgb = tk.Label(columna_rgb, bg="#000000", width=14, height=6, relief="ridge")
cuadro_rgb.pack(pady=8)
 
etiqueta_rgb = tk.Label(columna_rgb, text="R=0  G=0  B=0")
etiqueta_rgb.pack(pady=(0, 10))
 
# Un slider por canal. "command=actualizar_rgb" hace que se llame la
# funcion automaticamente cada vez que mueves la barra.
tk.Label(columna_rgb, text="Rojo", fg="red").pack()
slider_r = tk.Scale(columna_rgb, from_=0, to=255, orient="horizontal", command=actualizar_rgb)
slider_r.pack(fill="x")
 
tk.Label(columna_rgb, text="Verde", fg="green").pack()
slider_g = tk.Scale(columna_rgb, from_=0, to=255, orient="horizontal", command=actualizar_rgb)
slider_g.pack(fill="x")
 
tk.Label(columna_rgb, text="Azul", fg="blue").pack()
slider_b = tk.Scale(columna_rgb, from_=0, to=255, orient="horizontal", command=actualizar_rgb)
slider_b.pack(fill="x")
 
# ============== COLUMNA CMY ==============
columna_cmy = tk.Frame(marco)
columna_cmy.pack(side="right", expand=True, fill="both", padx=15)
 
tk.Label(columna_cmy, text="Modelo CMY", font=("Arial", 12, "bold")).pack(pady=5)
 
cuadro_cmy = tk.Label(columna_cmy, bg="#ffffff", width=14, height=6, relief="ridge")
cuadro_cmy.pack(pady=8)
 
etiqueta_cmy = tk.Label(columna_cmy, text="C=0  M=0  Y=0")
etiqueta_cmy.pack(pady=(0, 10))
 
tk.Label(columna_cmy, text="Cian", fg="#00b7b7").pack()
slider_c = tk.Scale(columna_cmy, from_=0, to=255, orient="horizontal", command=actualizar_cmy)
slider_c.pack(fill="x")
 
tk.Label(columna_cmy, text="Magenta", fg="#b700b7").pack()
slider_m = tk.Scale(columna_cmy, from_=0, to=255, orient="horizontal", command=actualizar_cmy)
slider_m.pack(fill="x")
 
tk.Label(columna_cmy, text="Amarillo", fg="#b7b700").pack()
slider_y = tk.Scale(columna_cmy, from_=0, to=255, orient="horizontal", command=actualizar_cmy)
slider_y.pack(fill="x")
 
actualizar_rgb()
actualizar_cmy()
 
ventana.mainloop()