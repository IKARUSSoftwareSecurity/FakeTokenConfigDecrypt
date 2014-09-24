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

* Copy blfs.key and config.cfg from /res/raw folder in APK
* run `decrypt_config.py blfs.key config.cfg`

Samples
=======

List of APK MD5s

* da1a9a13503993729cacfa854a90e56f
* b9f793e01a255f4116dc5b96da6ce54e
* 84e2e9e8430792b583d02d3cc1bf8535 