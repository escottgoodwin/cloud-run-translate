import os
import urllib
from urllib.request import urlretrieve
from config import *

model = f'opus-mt-{SOURCE_LANG}-{TARGET_LANG}'

def download_language_model():
    print(f">>>Downloading data for {SOURCE_LANG} to {TARGET_LANG} model...")
    os.makedirs(os.path.join("data", model))
    for f in FILENAMES:
        try:
            print(os.path.join(HUGGINGFACE_S3_BASE_URL, model, f))
            urlretrieve(
                "/".join([HUGGINGFACE_S3_BASE_URL, model, f]),
                os.path.join(MODEL_PATH, model, f),
            )
            print("Download complete!")
        except urllib.error.HTTPError:
            print("Error retrieving model from url. Please confirm model exists.")
            os.rmdir(os.path.join("data", model))
            break


if __name__ == "__main__":
    download_language_model()
