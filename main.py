import dearpygui.dearpygui as dpg
import json

peliculas = {
    "P001": {
        "titulo": "Avengers: Endgame",
        "horarios": ["14:00", "18:30", "22:00"],
        "precio": 8.50
    },
    "P002": {
        "titulo": "Spider-Man: No way home",
        "horarios": ["15:15", "17:30", "19:00"],
        "precio": 9.00
    },
    "P003": {
        "titulo": "Star wars: Nuevo imperio",
        "horarios": ["11:00", "15:30", "23:00"],
        "precio": 7.20
    },
    "P004": {
        "titulo": "Venom: Last Dance",
        "horarios": ["9:00", "13:00", "19:00"],
        "precio": 9.50
    },
    "P005": {
        "titulo": "Saw 7",
        "horarios": ["8:00", "10:30", "12:00"],
        "precio": 6.50
    }
}

def actualizar_horarios(sender, app_data):
    """Actualiza dinámicamente los horarios según el código ingresado"""
    codigo = dpg.get_value("codigo_input").strip().upper()
    if codigo in peliculas:
        horarios = peliculas[codigo]["horarios"]
        dpg.configure_item("horario_input", items=horarios)
        dpg.configure_item("codigo_input", default_value=codigo)  
    else:
        dpg.configure_item("horario_input", items=[])
        dpg.configure_item("resultado", default_value="")

def guardar_reserva(codigo_pelicula, horario, cantidad, total):
    reserva = {
        "pelicula": peliculas[codigo_pelicula]["titulo"],
        "horario": horario,
        "cantidad": cantidad,
        "total": total
    }

    try:
        with open("reservas.json", "r") as file:
            reservas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        reservas = []

    reservas.append(reserva)

    with open("reservas.json", "w") as file:
        json.dump(reservas, file, indent=4)

def procesar_reserva(sender, app_data):
    codigo = dpg.get_value("codigo_input").strip().upper()
    horario = dpg.get_value("horario_input")
    cantidad = dpg.get_value("cantidad_input")

    
    if not codigo or codigo not in peliculas:
        dpg.set_value("resultado", "Código inválido!")
        return
    
    if not horario or horario not in peliculas[codigo]["horarios"]:
        dpg.set_value("resultado", "Seleccione un horario válido!")
        return
    
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError
    except:
        dpg.set_value("resultado", "Cantidad inválida!")
        return
    
    precio_total = peliculas[codigo]["precio"] * cantidad
    guardar_reserva(codigo, horario, cantidad, precio_total)

    dpg.set_value("resultado",
        f"Reserva exitosa!\n"
        f"Película: {peliculas[codigo]['titulo']}\n"
        f"Horario: {horario}\n"
        f"Cantidad: {cantidad}\n"
        f"Total: ${precio_total:.2f}"
    )

def mostrar_historial(sender, app_data):
    try:
        with open("reservas.json", "r") as file:
            reservas = json.load(file)
    except:
        reservas = []

    with dpg.window(label="Historial de reservas", width=600, height=400):
        if reservas:
            with dpg.table(header_row=True, policy=dpg.mvTable_SizingStretchProp):
                dpg.add_table_column(label="Película", width_stretch=True)
                dpg.add_table_column(label="Horario", width_fixed=True)
                dpg.add_table_column(label="Cantidad", width_fixed=True)
                dpg.add_table_column(label="Total", width_fixed=True)

                for reserva in reservas:
                    with dpg.table_row():
                        dpg.add_text(reserva["pelicula"])
                        dpg.add_text(reserva["horario"])
                        dpg.add_text(str(reserva["cantidad"]))
                        dpg.add_text(f"${reserva['total']:.2f}")
        else:
            dpg.add_text("No hay reservas registradas", color=[200, 200, 200])

dpg.create_context()


with dpg.window(label="Cine Ticket System", width=800, height=500):
    
    with dpg.child_window(autosize_x=True, height=200):
        dpg.add_text("Películas Disponibles:", color=[255, 215, 0])
        with dpg.table(header_row=True, borders_innerH=True, borders_outerH=True):
            dpg.add_table_column(label="Código", width_fixed=True)
            dpg.add_table_column(label="Título", width_stretch=True)
            dpg.add_table_column(label="Horarios", width_stretch=True)
            dpg.add_table_column(label="Precio", width_fixed=True)

            for codigo, info in peliculas.items():
                with dpg.table_row():
                    dpg.add_text(codigo, color=[0, 255, 255])
                    dpg.add_text(info["titulo"])
                    dpg.add_text(", ".join(info["horarios"]))
                    dpg.add_text(f"${info['precio']:.2f}")

    dpg.add_separator()

    
    with dpg.group(horizontal=True):
        with dpg.child_window(width=300):
            dpg.add_text("Nueva Reserva", color=[50, 205, 50])
            
            
            dpg.add_input_text(
                label="Código Película",
                tag="codigo_input",
                callback=actualizar_horarios,
                uppercase=True,
                width=100
            )
            
            
            dpg.add_combo(
                label="Horario",
                tag="horario_input",
                items=[],
                width=100
            )
            
            
            dpg.add_input_int(
                label="Cantidad",
                tag="cantidad_input",
                min_value=1,
                max_value=10,
                width=100
            )
            
            
            with dpg.group(horizontal=True):
                dpg.add_button(
                    label="Reservar",
                    callback=procesar_reserva,
                    width=120,
                    height=30
                )
                dpg.add_button(
                    label="Ver Historial",
                    callback=mostrar_historial,
                    width=120,
                    height=30
                )
            
            
            dpg.add_text("", tag="resultado", color=[50, 205, 50])


with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255, 50))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (30, 144, 255, 150))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5, 5)

dpg.bind_theme(global_theme)


dpg.create_viewport(
    title="Sistema de Cine",
    width=820,
    height=600,
    min_width=800,
    min_height=500
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()