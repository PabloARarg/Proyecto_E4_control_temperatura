# Implementacion para guardar datos entrantes por puerto serial en archivo de texto plano
import serial

# Configura el puerto serial
# Reemplaza 'COM1' con el nombre de tu puerto UART y 9600 con la velocidad de baudios correcta
ser = serial.Serial('COM16', 115200)

# Abre un archivo para escribir los datos
archivo_texto = open('datos_uart.txt', 'w')

try:
    while True:
        # Lee una línea desde el puerto UART
        linea = ser.readline().decode('utf-8').strip()

        # Muestra la línea en la consola (opcional)
        print(linea)

        # Escribe la línea en el archivo
        archivo_texto.write(linea + '\n')

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C) para cerrar el programa de manera segura
    print("Programa interrumpido por el usuario.")
    archivo_texto.close()
    ser.close()

