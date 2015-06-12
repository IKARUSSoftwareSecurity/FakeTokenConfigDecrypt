__author__ = 'bachmann.s & elias.t'

import base64
from Crypto.Cipher import Blowfish
import zipfile
import sys
from os.path import isdir
from os.path import exists
from os.path import join
from os.path import split
from os import listdir
from argparse import ArgumentParser

blfs = 'res/raw/blfs.key'
config = 'res/raw/config.cfg'
iv = "12345678"

def decrypt_config(file_path):
    '''
    This is an APK reader that reads out config and blfs.key.
    Prints the APK name along with the decrypted config data.

    :param file_path: APK file to read and decrypt its config.cfg
    :return: nothing
    '''
    try:
        arch = zipfile.ZipFile(file_path, 'r')
        key = "".join(list(map(lambda x: x[2:], map(hex, map(ord, (arch.open(blfs,'r').read()).decode("utf-8"))))))[:50]
        ciphertext = base64.b64decode(arch.read('res/raw/config.cfg'))
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        print("\n" + ''.join(split(file_path)[-1:]) + ":")
        print(cipher.decrypt(ciphertext).decode("UTF-8"))
    except zipfile.BadZipfile:
        print(file_path + r" is not a ZIP file!")
        return
    except KeyError:
        print(file_path + r" is either not the Trojan-Banker APK/n"
                          r"or the filename(s) are not the same anymore.")
        print("Unexpected error: " + sys.exc_info())
        raise

def process_folder(folder_path):
    '''
    Runs decrypt_config() on all APKs
    in the directory where folder_path
    points to

    :param folder_path: folder to analyze
    :return: nothing
    '''
    folder_entries = listdir(folder_path)
    # check if the folder is empty
    if len(folder_entries) != 0:
        for entry in folder_entries:
            absolute_path = join(folder_path, entry)
            if isdir(absolute_path):
                process_folder(absolute_path)
            elif exists(path):
                decrypt_config(absolute_path)

if __name__ == "__main__":
    '''
    Tested on Windows 8.1 and Ubuntu 14.04
    '''
    parser = ArgumentParser(description="Decrypts the config.cfg file of Trojan-Banker.")
    parser.add_argument('-i', '--input', nargs='+',
                        help='Input APK file for analysis.', required=True)

    # if the path is a folder or a file
    args = parser.parse_args()

    if args.input:
        print("Analyzing APK(s)...")
        for path in args.input:
            # if it is a folder then process all files that are APK files
            if isdir(path):
                process_folder(path)
            # otherwise process the single file
            elif exists(path):
                decrypt_config(path)
    pass