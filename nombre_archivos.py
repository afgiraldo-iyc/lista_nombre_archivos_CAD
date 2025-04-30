#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: nombre_archivos.py
Descripción: Lista todos los archivos de una carpeta seleccionada
             y genera un Excel con sus nombres.
Requisitos: pip install pandas openpyxl
"""

import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def select_and_list_folder():
    # Abrir diálogo para seleccionar carpeta
    folder_path = filedialog.askdirectory(title="Seleccionar carpeta")
    if not folder_path:
        return

    # Listar solo archivos (no subcarpetas)
    file_names = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    count = len(file_names)

    if count == 0:
        messagebox.showinfo("Sin archivos", "La carpeta seleccionada no contiene archivos.")
        return

    # Crear DataFrame y exportar a Excel
    df = pd.DataFrame({'Name': file_names})
    output_path = os.path.join(folder_path, 'file_list.xlsx')

    try:
        df.to_excel(output_path, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el archivo de Excel:\n{e}")
        return

    # Guardar ruta generada y habilitar botón
    root.generated_file = output_path
    btn_open.config(state=tk.NORMAL)

    # Mensaje de éxito
    messagebox.showinfo(
        "Listado completado",
        f"Se leyeron {count} archivos en:\n{folder_path}\n\n"
        f"Archivo Excel generado:\n{output_path}"
    )

def open_excel():
    path = getattr(root, 'generated_file', None)
    if not path or not os.path.exists(path):
        messagebox.showwarning("Atención", "No hay un archivo de Excel válido para abrir.")
        return

    try:
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', path))
        elif os.name == 'nt':
            os.startfile(path)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', path))
    except Exception as e:
        messagebox.showerror("Error al abrir", f"No se pudo abrir el archivo:\n{e}")

if __name__ == "__main__":
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Listar archivos en carpeta")
    root.geometry("350x180")
    root.resizable(False, False)

    # Botón para seleccionar carpeta
    btn_select = tk.Button(root, text="Seleccionar carpeta", command=select_and_list_folder)
    btn_select.pack(pady=(20, 5))

    # Botón para abrir Excel (inicialmente deshabilitado)
    btn_open = tk.Button(root, text="Abrir Excel", command=open_excel, state=tk.DISABLED)
    btn_open.pack(pady=5)

    # Leyenda del desarrollador
    legend = tk.Label(
        root,
        text="Desarrollador por Nuevas Tecnologías División TI",
        font=("Arial", 8)
    )
    legend.pack(side=tk.BOTTOM, pady=5)

    # Iniciar la GUI
    root.mainloop()
