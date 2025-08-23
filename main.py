from pyzkolari import LogManager
from pypyrus import TranslationManager
import logging

def main():
    print("Running [add your description here...]")

    # Initialize the log manager
    LOGGER = LogManager(default_log_level=logging.INFO)
    LOGGER.info("LogManager initialized successfully.")
    LOGGER.set_console_level(logging.WARNING) 
    
    # Prepare and enable file logging
    try:
        LOGGER.info("Setting up file logging...")
        LOGGER.prepare_logfile(brieffilename="logfile", logfolder="./logs", force_create_folder=True)
        LOGGER.enable_file_logging()
        LOGGER.set_file_level(logging.NOTSET) 
        LOGGER.info("File logging setup successfully.")
    except Exception as e_file_logging:
        LOGGER.error(f"Exception during file logging setup: {e_file_logging}")

    # Loading texts and translations
    LOGGER.info("Loading translations...")
    try:
        SAMPLE_TEXTS = TranslationManager( 
            translations_path="assets/text_resources/sample", #the path where the translations are stored
            translations_file=None, # [optional] the name of the translations file (without the .json extension), but I advise to use the default one** 
            active_lang="en" # [optional] the language to be used by default. If not specified, it will use english (en) as default.
            )
    except Exception as e_translation_manager:
        LOGGER.error(f"Error loading translations: {e_translation_manager}")   

    # Now you can use the translation manager to get the texts and translations.
    print(SAMPLE_TEXTS.translate("GREETINGS"))




if __name__ == "__main__":
    main()