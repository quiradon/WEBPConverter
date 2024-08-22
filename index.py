# Pegue todas as imagens na pasta input e salve na out como webp crie variaveis de configuração para o tamanho da imagem e a qualidade da imagem

import os
from PIL import Image

# Configurações
input_path = 'input'
output_path = 'out'
image_quality = 75

for file in os.listdir(input_path):
    if file.endswith('.jpg') or file.endswith('.png'):
        # Abre a imagem
        image = Image.open(f'{input_path}/{file}')
        # Salva a imagem em webp
        image.save(f'{output_path}/{file.rsplit(".", 1)[0]}.webp', 'webp', quality=image_quality)
        print(f'{file} convertido com sucesso')

print('Conversão finalizada')

