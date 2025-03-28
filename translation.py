from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    """
    Translates text from one language to another using Google Translator API.
    :param text: The text to be translated (string)
    :param source_lang: Source language code (e.g., 'en' for English, 'sw' for Swahili)
    :param target_lang: Target language code (e.g., 'sw' for Swahili, 'en' for English)
    :return: Translated text (string)
    """
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)

# Test the function with examples
examples = [
    ("Hello, how are you?", "en", "sw"),
    ("Ninapenda kujifunza programu", "sw", "en"),
    ("The weather is beautiful today.", "en", "sw"),
    ("Elimu ni ufunguo wa maisha.", "sw", "en")
]

# Run examples to show that it indeed works
for text, src, tgt in examples:
    translated_text = translate_text(text, src, tgt)
    print(f"Original ({src}): {text}")
    print(f"Translated ({tgt}): {translated_text}\n")
