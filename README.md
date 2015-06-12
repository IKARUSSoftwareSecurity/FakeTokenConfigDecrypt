FakeTokenConfigDecrypt
======================

Decrypt the config file of "FakeToken" / "FakeTextsecure" Online Banking Trojans.

* The Config is blowfish encrypted
* The Config is a XML file and contains URLs and Phonenumbers of the attacker
* "FakeTextSecure" uses the Textsecure open source app to disguise itself

Prequisites
===========

* Python 3.x
* Pycrypto: https://www.dlitz.net/software/pycrypto/

Usage
=====
* decrypt_config.py:
* Copy blfs.key and config.cfg from /res/raw folder in APK
* run `decrypt_config.py blfs.key config.cfg`

* decrypt_banksersecure.py:
* Specify an APK or a directory of APKs as an argument for -i or --input
* run `python decrypt_bankersecure.py -i <APK_or_Directory>`

Samples
=======

List of APK MD5s

* da1a9a13503993729cacfa854a90e56f
* b9f793e01a255f4116dc5b96da6ce54e
* 84e2e9e8430792b583d02d3cc1bf8535 
* 1663446441d4e448881179b73f74a989 
* 19498c11b8b1dd03eafadd180f5717c3 
* 8f475c632c8d435846ee6f8d8597d675 
* a15b704743f53d3edb9cdd1182ca78d1 
* 56be8ed180f23641c82556de7a4a1942 
* efbc3bef01e376b75c62277b2711caca 
* 52ab4a4d6fcb68573782f7e2196cd328 
* 48c0fe3e0826216dcb3f9398a6513a1c 
* 3c7d282a57770e4aca8ac63ea637ac49 
* ba46f19e54841ef9428e6566dc79d57d 
* 9e339e5a954a0fc215afa4aecbfd7660
* 9820b73b96f396b2a2d276c99c9750ad