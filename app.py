import cv2

# Carregar os classificadores pré-treinados do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Iniciar a captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    # Ler o frame da câmera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Converter para escala de cinza (melhor para detecção)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Área do rosto em escala de cinza
        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

        # Detectar sorriso dentro do rosto
        smiles = smile_cascade.detectMultiScale(face_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            # Desenhar um retângulo ao redor do sorriso
            cv2.rectangle(face_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
            cv2.putText(frame, "Sorrindo!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Mostrar o frame
    cv2.imshow("Detecção de Sorriso", frame)

    # Pressione "q" para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
