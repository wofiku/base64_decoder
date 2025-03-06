"""
Base64 decoder
Version: 0.1

Author: wofiku
https://github.com/wofiku
"""

# IMPORTS
from base64 import b64decode  # base64 byte decoder
from pathlib import Path


# VARS
current_path = Path('./.')  # Hi! You're here!
spl_user_ask_base64: dict = {'en': 'Write Base64 text down there:\n', 'ru': 'Введите Base64 текст ниже:\n'}


# FUNCTIONS
# Fool check. Creating current path where script is running, if it somehow doesn't exist yet (deleted, corrupted, etc.)
if not current_path.exists():
    current_path.mkdir(parents=True, exist_ok=True)  # You're here! Again


# Forcefully set variable to expected type
def type_force(var: any, should_be: type) -> vars:
    if not isinstance(var, should_be):
        if should_be == str:
            var = str(var)
        elif should_be == bytes:
            var = str(var).encode('utf-8')

    return var


def write_file(filename: str, file_insides: bytes, folder: str | None = None) -> None:
    # VARS
    # Making sure files_insides is really bytes, if no then making it bytes
    file_insides: bytes = type_force(file_insides, bytes)
    folder_to_save = Path(str(folder)) if folder else Path("decoded base64")

    # MAIN
    # Creating path for decoded files
    if not folder_to_save.exists():
        folder_to_save.mkdir(parents=True, exist_ok=True)

    # Creating file
    print(folder_to_save.resolve() / str(filename))
    with open(folder_to_save.resolve() / str(filename), 'wb') as pdf_file:
        pdf_file.write(bytes(file_insides))

    return None  # That's all, folks! No more fool checks here


def base64_to_file(base64_encoded: bytes, filename: str, extension: str = 'pdf', folder: str | None = None) -> None:
    # VARS
    base64_encoded: bytes = type_force(base64_encoded, bytes)
    filename: str = type_force(filename, str)
    extension = type_force(extension, str).replace('.', '', 1)  # Replace (".") in file extension

    # MAIN
    base64_decoded = b64decode(base64_encoded)
    write_file(filename=f"{filename}.{extension}", file_insides=base64_decoded, folder=folder)


# MAIN
if __name__ == '__main__' or __name__ != '__main__':  # I don't care, JUST START ALREADY
    # USER INPUT
    input_user = str(input(spl_user_ask_base64['ru']))
    input_base64: bytes = input_user.encode('utf-8')

    # VARS
    output_filename = f"{input_user[:8]}...{input_user[-7:]}"

    # FUNCTIONS
    base64_to_file(base64_encoded=input_base64, filename=output_filename, extension='pdf')
