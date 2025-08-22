from pyzkolari import LogManager
from pypyrus import TranslationManager

def main():
    print("Running [add your description here...]")

    try:
        SAMPLE_TEXTS = TranslationManager( 
            translations_path="assets/text_resources/sample", #the path where the translations are stored
            translations_file=None, # [optional] the name of the translations file (without the .json extension), but I advise to use the default one** 
            active_lang="en" # [optional] the language to be used by default. If not specified, it will use english (en) as default.
            )
    except Exception as e_translation_manager:
        print(f"Error loading translations: {e_translation_manager}")   

    # Now you can use the translation manager to get the texts and translations.
    print(SAMPLE_TEXTS.translate("GREETINGS"))


if __name__ == "__main__":
    main()