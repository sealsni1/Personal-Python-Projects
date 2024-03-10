from PyPDF2 import PdfReader
from gtts import gTTS

# Insert the name of your PDF
pdf_reader = PdfReader(open('Chapter 14 Notes.pdf', 'rb'), strict=False)

full_text = ""  # Initialize an empty string to store the entire text

# Use len(reader.pages) instead of numPages
for page_num in range(len(pdf_reader.pages)):

    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

    full_text += clean_text + " "  # Append each page's text to the full_text

# Save the text to an MP3 file using gTTS
tts = gTTS(text=full_text, lang='en')
tts.save('story.mp3')
