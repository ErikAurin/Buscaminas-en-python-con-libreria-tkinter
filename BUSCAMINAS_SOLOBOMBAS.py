import tkinter as tk
import random

class Busca:
    def __init__(self, root, numero_filas, numero_columnas, numero_minas):
        self.root = root
        self.numero_filas = numero_filas
        self.numero_columnas = numero_columnas
        self.numero_minas = numero_minas
        self.tablero = [[None] * numero_columnas for _ in range(numero_filas)]
        self.minas = set()

        self.generar_tablero()

    def generar_tablero(self):
        for fila in range(self.numero_filas):
            for columna in range(self.numero_columnas):
                boton = tk.Button(self.root, text="", height=2, width=5)
                boton.grid(row=fila, column=columna)
                self.tablero[fila][columna] = boton

        minas_colocadas = 0
        while minas_colocadas < self.numero_minas:
            fila = random.randint(0, self.numero_filas - 1)
            columna = random.randint(0, self.numero_columnas - 1)
            if (fila, columna) not in self.minas:
                self.minas.add((fila, columna))
                minas_colocadas += 1

        for fila in range(self.numero_filas):
            for columna in range(self.numero_columnas):
                if (fila, columna) in self.minas:
                    self.tablero[fila][columna]["text"] = "X"
                    self.tablero[fila][columna]["bg"] = "red"

                else:
                    numero_minas_adyacentes = self.contar_minas_adyacentes(fila, columna)
                    self.tablero[fila][columna]["text"] = str(numero_minas_adyacentes)

    def contar_minas_adyacentes(self, fila, columna):
        count = 0
        for i in range(max(0, fila - 1), min(self.numero_filas, fila + 2)):
            for j in range(max(0, columna - 1), min(self.numero_columnas, columna + 2)):
                if (i, j) in self.minas:
                    count += 1
        return count

if __name__ == '__main__':
    numero_filas = 10
    numero_columnas = 10
    numero_minas = 10

    root = tk.Tk()
    busca = Busca(root, numero_filas, numero_columnas, numero_minas)
    root.mainloop()
