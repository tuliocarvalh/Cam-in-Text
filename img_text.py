import cv2
import pytesseract




def open_cam():
    #Abrindo Video da Webcam Com Open-Cv
    webcam = cv2.VideoCapture(0) #Especifique sua camera. Caso esteja usando a nativa, apenas deixe o 0.

    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()
            cv2.imshow("MyCam", frame)
            key = cv2.waitKey(5)
            if key == 27: #Aperte o ESC quando o texto estiver nítido.
                break
        cv2.imwrite("img.jpg", frame) 

    webcam.release()
    cv2.destroyAllWindows()


def img_text():
    imagem = cv2.imread("img.jpg") 
    caminho = r"C:\Users\tulio\AppData\Local\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
    texto = pytesseract.image_to_string(imagem)
    return texto

open_cam()
print(img_text())