import pdfplumber

def is_header_or_footer(y, page_height):
    """
    Funcao para determinar se o texto e um cabeçalho ou rodape baseado na posicao Y.
    """
    margin = 35  # margem de 50 pixels do topo e do fundo
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
 
    
    print(f'Arquivo texto criado neste caminho {txt_path}')

# Exemplo de uso, substituir com o caminho do arquivo PDF e do txt
pdf_path = 'C:/pdftotxt/pdf1.pdf' # Caminho do arquivo PDF
txt_path = 'C:/pdftotxt/text2.txt' # Caminho do arquivo txt
extrair_txt(pdf_path, txt_path)
