import tkinter as tk
from tkinter import ttk, messagebox
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Vehículos")
        self.root.geometry("600x400")

        self.servicio = GarajeServicio()

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.root,
            text="Registro de Vehículos en Garaje",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        frame_formulario = tk.Frame(self.root)
        frame_formulario.pack(pady=10)

        tk.Label(frame_formulario, text="Placa:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_placa = tk.Entry(frame_formulario)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="Marca:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_marca = tk.Entry(frame_formulario)
        self.entry_marca.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="Propietario:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_propietario = tk.Entry(frame_formulario)
        self.entry_propietario.grid(row=2, column=1, padx=5, pady=5)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(
            frame_botones,
            text="Agregar vehículo",
            command=self.agregar_vehiculo
        )
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_campos
        )
        btn_limpiar.grid(row=0, column=1, padx=10)

        self.tabla = ttk.Treeview(
            self.root,
            columns=("Placa", "Marca", "Propietario"),
            show="headings"
        )
        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")

        self.tabla.pack(pady=20, fill="both", expand=True)

    def agregar_vehiculo(self):
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo(placa, marca, propietario)
        self.servicio.agregar_vehiculo(vehiculo)

        self.actualizar_tabla()
        self.limpiar_campos()

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for vehiculo in self.servicio.listar_vehiculos():
            self.tabla.insert("", "end", values=(
                vehiculo.placa,
                vehiculo.marca,
                vehiculo.propietario
            ))

    def limpiar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)