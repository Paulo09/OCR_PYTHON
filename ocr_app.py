from PIL import Image
import pytesseract

# Configuração do caminho do executável do Tesseract (necessário apenas no Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    # Abre a imagem
    img = Image.open(image_path)

    # Usa o pytesseract para realizar o OCR na imagem
    text = pytesseract.image_to_string(img)

    return text

if __name__ == "__main__":
    # Caminho para a imagem que você quer processar
    image_path = 'caminho/para/sua/imagem.png'
    
    # Realiza o OCR na imagem
    extracted_text = ocr_image(image_path)
    
    # Imprime o texto extraído
    print("Texto extraído da imagem:")
    print(extracted_text)
