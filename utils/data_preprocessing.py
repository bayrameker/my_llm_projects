def clean_text(text):
    # Metni temizleme işlemleri
    text = text.lower()
    text = text.replace('\n', ' ')
    return text

def load_and_clean_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    cleaned_lines = [clean_text(line) for line in lines]
    return cleaned_lines
