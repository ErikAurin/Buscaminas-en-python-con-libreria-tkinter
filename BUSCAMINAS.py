import tkinter as tk
from tkinter import messagebox
import random

class Buscaminas:
    def __init__(self, root, num_filas, num_columnas, num_minas):
        # Constructor de la clase Buscaminas
        # root: La ventana principal de Tkinter donde se mostrará el juego0
        # num_filas: Número de filas en el tablero del jueo
        # num_columnas: Número de columnas en el tablero del ju1ego
        # num_minas: Número de minas que se colocarán en el tablero
        self.root = root  # 1Asigna la ventana principal de Tkinter a la instancia
        self.num_filas = num_filas  # 2Asigna el número de filas a la instancia
        self.num_columnas = num_columnas  # 3Asigna el número de columnas a la instancia
        self.num_minas = num_minas  # 4Asigna el número de minas a la instancia
        self.tiempo_transcurrido = 0#5 Inicializa el tiempo transcurrido en el juego
        self.tablero = [[None] * num_columnas for _ in range(num_filas)]  # 6Crea una matriz para representar el tablero
        self.minas = set()  # 1nicializa un conjunto para almacenar las posiciones de las minas
        self.casillas_marcadas = set()  # 18Inicializa un conjunto para almacenar las casillas marcadas como minas
        self.casillas_marcadas_counter = 0  # 0Inicializa el contador de casillas marcadas como minas

        self.iniciar_juego()  # Llama al método iniciar_juego() para comenzar el juego

    def generar_tablero(self):
    # Método para generar y mostrar el tablero del juego

    # Recorre todas las filas del tablero
        for fila in range(self.num_filas):
        # Recorre todas las columnas del tablero
            for columna in range(self.num_columnas):
            # Para cada casilla en el tablero, se crea un botón de Tkinter
                 boton = tk.Button(self.root, text="", height=2, width=5)
            # Se configura el botón con un tamaño adecuado y sin texto inicialmente
                 boton.grid(row=fila, column=columna)
            # Se coloca el botón en la ventana de Tkinter en la posición correspondiente (fila, columna)
                 boton.bind("<Button-1>", lambda event, f=fila, c=columna: self.abrir_casilla(event, f, c))
# Se asigna al botón el evento de clic izquierdo (Button-1).
# Se utiliza una función lambda para capturar el evento y las coordenadas de la casilla (fila, columna).
# Cuando se produce un clic izquierdo, se llama al método abrir_casilla() con el evento y las coordenadas de la casilla como argumentos.

                 boton.bind("<Button-3>", lambda event, f=fila, c=columna: self.marcar_casilla(f, c))
          
# Se asigna al botón el evento de clic derecho (Button-3).
# Se utiliza una función lambda para capturar el evento y las coordenadas de la casilla (fila, columna).
# Cuando se produce un clic derecho, se llama al método marcar_casilla() con las coordenadas de la casilla como argumentos.

                 self.tablero[fila][columna] = boton
# Se almacena el botón en la matriz que representa el tablero del juego

        # Se colocan las minas en posiciones aleatorias en el tablero
        minas_colocadas = 0 #~Para ello creamos un contador de minas colocadas que mientras se estan
        #generando estas posiciones calcula si esta posicion ya estaba en minas, si no es asi se suma un contador y elñ bucle se repite hasta que el num minas = al num minas colocadas
        while minas_colocadas < self.num_minas:
            fila = random.randint(0, self.num_filas - 1)
            columna = random.randint(0, self.num_columnas - 1)

            if (fila, columna) not in self.minas:
                self.minas.add((fila, columna))
                minas_colocadas += 1

    # Se crean y muestran etiquetas para el contador de casillas marcadas y el tiempo transcurrido
            self.marcadas_label = tk.Label(self.root, text="Marcadas: 0")
    # Se crea una etiqueta para mostrar la cantidad de casillas marcadas como minas
            self.marcadas_label.grid(row=self.num_filas, columnspan=self.num_columnas)
    # Se coloca la etiqueta en la ventana de Tkinter
            self.tiempo_label = tk.Label(self.root, text="Tiempo: 0 s")
    # Se crea una etiqueta para mostrar el tiempo transcurrido en el juego
            self.tiempo_label.grid(row=self.num_filas + 1, columnspan=self.num_columnas)
    # Se coloca la etiqueta en la ventana de Tkinter, justo debajo de la anterior
            self.actualizar_tiempo()
    # Se llama al método actualizar_tiempo() para iniciar el contador de tiempo del juego

    def actualizar_tiempo(self):
    # Método para actualizar el tiempo transcurrido en el juego

    
        

    # Actualiza el texto de la etiqueta de tiempo para reflejar el nuevo tiempo transcurrido
        self.tiempo_label.config(text="Tiempo: {:.0f} s".format(self.tiempo_transcurrido))
        self.tiempo_transcurrido += 0.01
    # Programa una llamada recursiva al mismo método después de 100 tics(1 segundo)
        self.root.after(100, self.actualizar_tiempo)
        

    
    def abrir_casilla(self, event, fila, columna):
    # Método para abrir una casilla en el juego
        if event.num == 1:  # Si se hizo clic con el botón izquierdo del ratón
            self.revelar_casilla(fila, columna)  # Llama al método revelar_casilla() con la posición de la casilla
        elif event.num == 3:  # Si se hizo clic con el botón derecho del ratón
            self.marcar_casilla(fila, columna)  # Llama al método marcar_casilla() con la posición de la casilla


    
    def marcar_casilla(self, fila, columna):
    # Método para marcar una casilla como sospechosa de contener una mina

    # Verifica si la casilla no ha sido marcada previamente
        if (fila, columna) not in self.casillas_marcadas:
        # Verifica si el número de casillas marcadas es menor que el número de minas permitido
            if len(self.casillas_marcadas) < self.num_minas:
            # Verifica si la casilla está vacía para poder marcarla
                if self.tablero[fila][columna]["text"] == "":
                # Marca la casilla con un asterisco para indicar que está marcada como sospechosa de contener una mina
                    self.tablero[fila][columna]["text"] = "*"
                # Agrega la casilla marcada al conjunto de casillas marcadas
                    self.casillas_marcadas.add((fila, columna))
                # Incrementa el contador de casillas marcadas
                    self.casillas_marcadas_counter += 1
            else:
            # Si el número de casillas marcadas alcanza el límite, muestra un mensaje informando al jugador
                messagebox.showinfo("Limite alcanzado", "Ya has marcado el máximo de casillas.")
        else:
        # Si la casilla ya estaba marcada, se desmarca al hacer clic derecho nuevamente
            self.tablero[fila][columna]["text"] = ""
        # Se remueve la casilla del conjunto de casillas marcadas
            self.casillas_marcadas.remove((fila, columna))
        # Se decrementa el contador de casillas marcadas
            self.casillas_marcadas_counter -= 1

    # Actualiza el contador de casillas marcadas
        self.actualizar_contador()
    # Verifica si se ha alcanzado la condición de victoria
        self.verificar_victoria()
    def revelar_casilla(self, fila, columna):
    # Método para revelar el contenido de una casilla

    # Verifica si la casilla no contiene una mina
        if (fila, columna) not in self.minas:
        # Si la casilla está marcada como sospechosa de contener una mina, no se revela su contenido
            if self.tablero[fila][columna]["text"] == "*":
                return

        # Cambia el fondo de la casilla a gris para indicar que ha sido revelada
            self.tablero[fila][columna]["bg"] = "gray"

        # Cuenta el número de minas adyacentes a la casilla actual
            num_minas_adyacentes = self.contar_minas_adyacentes(fila, columna)

        # Si la casilla no tiene minas adyacentes, revela las casillas vacías adyacentes
            if num_minas_adyacentes == 0:
                self.revelar_casillas_vacias(fila, columna)
            else:
            # Si hay minas adyacentes, muestra el número de minas en la casillaa
                self.tablero[fila][columna]["text"] = str(num_minas_adyacentes)
        else:
        # Si la casilla contiene una mina, explota las bombas y finaliza el juego
            self.explotar_bombas()

      
    def contar_minas_adyacentes(self, fila, columna):
    # Método para contar el número de minas adyacentes a una casilla específica en el tablero

    # Inicializa un contador para el número de minas adyacentes
        count = 0

    # Recorre todas las casillas adyacentes a la casilla dada
    
        for i in range(max(0, fila - 1), min(self.num_filas, fila + 2)):
    # Esta línea crea un bucle que itera sobre las filas adyacentes a la fila actual.
    # El rango de valores de 'i' comienza en el máximo entre 0 y (fila - 1).
    # Esto asegura que no tengamos un índice negativo para la primera fila adyacente.
    # Si 'fila' es 0, 'fila - 1' sería -1, pero el máximo entre 0 y -1 es 0, evitando un índice negativo.
    # Luego, el rango de valores de 'i' termina en el mínimo entre el número total de filas en el tablero y (fila + 2).
    # Esto garantiza que no nos salgamos del rango de filas válido para el tablero.
    # Si 'fila' es el último índice de fila, 'fila + 2' sería un índice fuera del rango de filas del tablero,
    # pero el mínimo entre el número total de filas en el tablero y (fila + 2) asegura que no excedamos el rango de filas.
    
            for j in range(max(0, columna - 1), min(self.num_columnas, columna + 2)):
            # Verifica si la casilla adyacente contiene una mina con la logica anterior
                if (i, j) in self.minas:
                # Si la casilla adyacente contiene una mina, incrementa el contador
                    count += 1

    # Retorna el número total de minas adyacentes a la casilla dada
        return count

    
    def revelar_casillas_vacias(self, fila, columna):
    # Método para revelar las casillas vacías adyacentes a una casilla específica en el tablero

    # Recorre todas las casillas adyacentes a la casilla dada
        for i in range(max(0, fila - 1), min(self.num_filas, fila + 2)):
            for j in range(max(0, columna - 1), min(self.num_columnas, columna + 2)):
            # Verifica si la casilla adyacente está vacía
                if self.tablero[i][j]["text"] == "":
                # Si la casilla adyacente está vacía, la revela
                    self.tablero[i][j]["text"] = "0"
                # Cambia el fondo de la casilla a gris para indicar que ha sido revelada
                    self.tablero[i][j]["bg"] = "gray"
                # Llama recursivamente al método revelar_casilla() para continuar revelando casillas vacías adyacentes
                    self.revelar_casilla(i, j)

  

    def explotar_bombas(self):
    # Método para mostrar todas las minas y terminar el juego

    # Itera sobre todas las minas y las muestra en el tablero con una 'X' y color rojo
        for fila, columna in self.minas:
            self.tablero[fila][columna]["text"] = "X"
            self.tablero[fila][columna]["bg"] = "red"

    # Muestra un cuadro de diálogo para preguntar al jugador si desea reiniciar el juego
        respuesta = messagebox.askquestion("Oh, no!", "¡Has perdido en {:.1f} segundos! ¿Quieres reiniciar el juego?".format(self.tiempo_transcurrido))
        if respuesta == 'yes':
        # Si el jugador elige reiniciar, destruye la ventana actual y crea una nueva instancia del juego
            self.root.destroy()
            self.__init__(tk.Tk(), self.num_filas, self.num_columnas, self.num_minas)
        else:
        # Si el jugador elige no reiniciar, simplemente cierra la ventana
            self.root.destroy()

    def verificar_victoria(self):
    # Método para verificar si el jugador ha ganado el juego

    # Comprueba si todas las casillas marcadas coinciden con la ubicación de las minas
        if self.casillas_marcadas == self.minas:
        # Si el jugador ha marcado todas las minas correctamente, muestra un mensaje de victoria
            respuesta = messagebox.askquestion("¡Felicidades!", "¡Has ganado en {:.1f} segundos! ¿Quieres reiniciar el juego?".format(self.tiempo_transcurrido))
            if respuesta == 'yes':
            # Si el jugador elige reiniciar, destruye la ventana actual y crea una nueva instancia del juego
                self.root.destroy()
                self.__init__(tk.Tk(), self.num_filas, self.num_columnas, self.num_minas)
            else:
            # Si el jugador elige no reiniciar, simplemente cierra la ventana
                self.root.destroy()

    def actualizar_contador(self):
    # Método para actualizar el contador de casillas marcadas en la interfaz

    # Actualiza el texto del contador de casillas marcadas
        self.marcadas_label.config(text="Marcadas: {0}".format(self.casillas_marcadas_counter))

    def iniciar_juego(self):
    # Método para iniciar el juego

    # Configura el título de la ventana del juego
        self.root.title("Buscaminas")
    # Genera el tablero del juego
        self.generar_tablero()

# Bloque principal del programa
if __name__ == '__main__':
    # Definición de las dimensiones del tablero y el número de minas
    num_filas = 10
    num_columnas = 10
    num_minas = 10

    # Crea una instancia del juego y comienza el bucle principal de la interfaz gráfica
Buscaminas(tk.Tk(), num_filas, num_columnas, num_minas)
tk.mainloop()
