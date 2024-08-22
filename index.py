import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

# Configurações
input_path = 'input'
output_path = 'out'
image_quality = 75
max_workers = os.cpu_count()


def process_image(file):
    if file.endswith('.jpg') or file.endswith('.png'):
        try:
            # Abre a imagem
            image = Image.open(os.path.join(input_path, file))
            # Salva a imagem em webp
            image.save(os.path.join(output_path, f'{file.rsplit(".", 1)[0]}.webp'), 'webp', quality=image_quality)
            print(f'{file} convertido com sucesso')
        except Exception as e:
            print(f'Erro ao converter {file}: {e}')

def execute_conversion():
    print(f'Diretório de trabalho atual: {os.getcwd()}')  # Verificação do diretório de trabalho atual
    if not os.path.exists(input_path):
        return f'Pasta de entrada "{input_path}" não encontrada.'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    files = os.listdir(input_path)
    if not files:
        return f'Pasta de entrada "{input_path}" está vazia.'
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(process_image, files)
    return 'Conversão finalizada'

def clear_folders():
    for folder in [input_path, output_path]:
        if not os.path.exists(folder):
            continue
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    return 'Pastas de entrada e saída limpas'

def display_message(message):
    print(message)
    input("Pressione Enter para continuar...")

def menu():
    menu_items = ['Executar Código', 'Limpar Pastas', 'Sair']
    
    while True:
        print("\nMenu:")
        for idx, item in enumerate(menu_items):
            print(f"{idx + 1}. {item}")
        
        choice = input("Escolha uma opção: ")
        
        if choice.isdigit():
            current_row = int(choice) - 1
            if current_row == 0:
                message = execute_conversion()
                display_message(message)
            elif current_row == 1:
                message = clear_folders()
                display_message(message)
            elif current_row == 2:
                break
        else:
            print("Opção inválida. Por favor, escolha um número válido.")

if __name__ == '__main__':
    menu()