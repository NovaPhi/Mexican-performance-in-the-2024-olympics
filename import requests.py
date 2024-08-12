"""
Este programa usa la informacion encontrada en la pagina de wikipedia sobre mexico en las olimpiadas y la extrae a una tabla en una ventana nueva con un intervalo diario para ver si tiene algun cambio del dia anterior
Autor:SuperNova
fecha:Agosto-12-2024
"""

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime

def medalsMex():
    url = "https://en.wikipedia.org/wiki/Mexico_at_the_2024_Summer_Olympics"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # encuentra todas las tablas en la pagina
        tables = soup.find_all('table', {'class': 'wikitable'})

        # debugging para asegurarse de que haya 2 atletas
        if len(tables) < 2:
            print("Not enough tables found on the page.")
            return {"error": "Not enough tables found on the page."}

        # Extrae los atletas de la tabla
        first_table = tables[0]
        first_rows = first_table.find_all('tr')

        # Crea diccionario para asimilar atletas al deporte
        athlete_sport_mapping = {}
        for row in first_rows[1:]:  # Salto de encabezaod
            cols = row.find_all('td')
            if len(cols) >= 5:
                medal = cols[0].text.strip()      # Extrae el tipo de medalla
                athlete = cols[1].text.strip()    # Extrae los atletas
                sport = cols[2].text.strip()      # Extrae el deporte
                # Guarda los atletas en un diccionario
                if sport in athlete_sport_mapping:
                    athlete_sport_mapping[sport].append(athlete)
                else:
                    athlete_sport_mapping[sport] = [athlete]

        # Extrae las medallas de la pagina HTML
        second_table = tables[1]
        second_rows = second_table.find_all('tr')

        sports_data = []
        for row in second_rows[1:]:  # esto es para saltarse la linea de encabezado
            cols = row.find_all('td')
            if len(cols) >= 4:
                sport_name = cols[0].text.strip()  # Extrae el nombre del deporte
                medals = {
                    "Gold": cols[1].text.strip(),   # Extrae las medallas de oro
                    "Silver": cols[2].text.strip(), # Extrae las medallas de plate
                    "Bronze": cols[3].text.strip(), # Extrae las medallas de bronze
                }
                
                # encuentra los atletas por deporte
                athletes = athlete_sport_mapping.get(sport_name, ["Unknown"])
                
                # añade los datos a la lista
                sports_data.append({
                    "Sport": sport_name,
                    "Medals": medals,
                    "Athletes": athletes
                })

        return sports_data
    else:
        print("Failed to retrieve the webpage")
        return {"error": "Failed to retrieve the webpage"}

def create_window(sports_data):
    root = tk.Tk()
    root.title("Olympic Medals Report")

    # genera una tabla con treeview para ver la informacion
    tree = ttk.Treeview(root, columns=("Sport", "Gold", "Silver", "Bronze", "Athletes"), show="headings")
    tree.heading("Sport", text="Sport")
    tree.heading("Gold", text="Gold")
    tree.heading("Silver", text="Silver")
    tree.heading("Bronze", text="Bronze")
    tree.heading("Athletes", text="Athletes")

    # La forma visual default de treeview
    tree.pack(fill=tk.BOTH, expand=True)

    # Inserta la informacion a treeview
    for data in sports_data:
        tree.insert("", tk.END, values=(
            data["Sport"],
            data["Medals"]["Gold"],
            data["Medals"]["Silver"],
            data["Medals"]["Bronze"],
            ', '.join(data["Athletes"])
        ))

    # Loop principal de Tktinker
    root.mainloop()

def test_run():
    # Simula la funcion al tiempo actual
    sports_data = medalsMex()
    if "error" not in sports_data:
        create_window(sports_data)
    else:
        print("Error fetching sports data.")

def run_daily_test():
    test_run()  # Corre la funcion una vez

# Corre la funcion de testing
run_daily_test()
