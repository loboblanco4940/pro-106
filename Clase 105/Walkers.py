import cv2


# Crear nuestro clasificador de cuerpos


# Inicializar la captura de video para nuestro archivo de video
cap = cv2.VideoCapture('walking.avi')

# Comenzar el bucle una vez que el video esté cargado exitosamente
while True:
    
    # Leer el primer cuadro
    ret, frame = cap.read()

    # Convertir cada cuadro a escala de grises
    
    # Pasar el cuadro a nuestro clasificador de cuerpos
    
    
    # Extraer las cajas envolventes para cualquier cuerpo identificado
    

    if cv2.waitKey(1) == 32: #32 es la barra espaciadora
        break

cap.release()
cv2.destroyAllWindows()
