import os
import urllib.request
import fasttext

LANGUAGE_MODEL_PATH = "models/lid.176.bin"  # the model used for language detection
URL = "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

if not os.path.exists(LANGUAGE_MODEL_PATH):
    print("Downloading language detection model...")
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(URL, LANGUAGE_MODEL_PATH)
    print("Download complete!")

model = fasttext.load_model(LANGUAGE_MODEL_PATH)


def isSwedishText(text):
    """Returns true if the inputted text is in swedish otherwise false (likely english language)"""
    text = text.replace("\n", " ").strip()     # Remove newlines
    lang = model.predict(text)[0][0].replace("__label__", "")
    return lang == "sv"
