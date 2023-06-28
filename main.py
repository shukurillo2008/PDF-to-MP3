from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] original file:  {Path(file_path).name}')
        print(f"[+] bajarilmoqda......")

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        
        text = ''.join(pages)
        text = text.replace('\n', '')

        my = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my.save(f'{file_name}.mp3')

        return f"[+] {file_name}.mp3 muvofiqiyatli saqlandi"
    else:
        return 'file tipi hato'
    
def main():
    tprint('PDF>>>TO>>>MP3', font='bulbhead')
    file_path = input("\n Fayl joylashuvini kirhizing :  ")
    language = input("tilni tanlang misol uchun : 'ru' yoki 'en' :  ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main() 