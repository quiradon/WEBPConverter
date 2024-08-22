# Pegue todas as imagens na pasta input e salve na out como webp crie variaveis de configuração para o tamanho da imagem e a qualidade da imagem

import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

# Configurações
input_path = 'input'
output_path = 'out'
image_quality = 75
max_workers = 16  # Número de threads

def process_image(file):
    if file.endswith('.jpg') or file.endswith('.png'):
        try:
            # Abre a imagem
            image = Image.open(f'{input_path}/{file}')
            # Salva a imagem em webp
            image.save(f'{output_path}/{file.rsplit(".", 1)[0]}.webp', 'webp', quality=image_quality)
            print(f'{file} convertido com sucesso')
        except Exception as e:
            print(f'Erro ao converter {file}: {e}')

def main():
    files = os.listdir(input_path)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(process_image, files)

if __name__ == '__main__':
    main()
    print('Conversão finalizada')

