import pdfplumber

def is_header_or_footer(y, page_height):
    """
    Funcao para determinar se o texto e um cabeçalho ou rodape baseado na posicao Y.
    """
    margin = input ("Por favor, insira a margem de topo e fundo desejada (px): ") 
    if y < margin or y > page_height - margin:
        return True
    return False

def extrair_txt(pdf_path, txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        body_text = ""
        for page in pdf.pages:
            page_height = page.height
            page_width = page.width
            page_text = ""
            for element in page.extract_words():
                # Filtra cabecalhos e rodapes
                if not is_header_or_footer(element['top'], page_height):
                    page_text += element['text'] + ' '
            body_text += page_text + '\n\n'

    # Escrever o conteudo extraido em um arquivo de texto
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(body_text)
    
    print(f'Arquivo de texto criado neste caminho {txt_path}')

# Solicita ao usuário que insira o caminho do arquivo PDF
pdf_path = input("Por favor, insira o caminho do arquivo PDF: ")

# Solicita ao usuário que insira o caminho do arquivo de texto
txt_path = input("Por favor, insira o caminho do arquivo de texto onde o texto será gravado: ")

# Chama a função com os caminhos fornecidos
extrair_txt(pdf_path, txt_path)
