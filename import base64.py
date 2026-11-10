# Partea A
s = "Salut"
b = s.encode()  # b'Salut'
b_hex = b.hex()
b_from_hex = bytes.fromhex(b_hex)

print("Text original:", s)
print("Octeți (bytes):", b)
print("În format Hex:", b_hex)
print("Înapoi din Hex în bytes:", b_from_hex)
# Salvează ca test_a2.py
import re


def ghici_strat(s):
  if re.search(r'%[0-9a-fA-F]{2}', s):
    return 'url'
  if re.match(r'^[0-9a-fA-F]+$', s) and len(s) % 2 == 0:
    return 'hex'
  if re.match(r'^[A-Za-z0-9+/=]+$', s) and len(s) % 4 == 0:
    return 'base64'
  return 'necunoscut'


print(ghici_strat('48656c6c6f'))  # Ar trebui să afișeze hex
print(ghici_strat('U2FsdGVkXQ=='))  # Ar trebui să afișeze base64
# Salvează ca test_a3.py
import base64
from urllib.parse import unquote


def ghici_strat(s):
  if re.search(r'%[0-9a-fA-F]{2}', s):
    return 'url'
  if re.match(r'^[0-9a-fA-F]+$', s) and len(s) % 2 == 0:
    return 'hex'
  if re.match(r'^[A-Za-z0-9+/=]+$', s):
    return 'base64'
  return 'necunoscut'


def desfaci(strat):
  st = ghici_strat(strat)
  if st == 'base64':
    return base64.b64decode(strat), 'base64'
  elif st == 'hex':
    return bytes.fromhex(strat), 'hex'
  elif st == 'url':
    return unquote(strat).encode(), 'url'
  return strat.encode(), 'necunoscut'


rezultat, tip = desfaci('QmFzZTY0')
print('Rezultat decodat:', rezultat)
print('Tip detectat:', tip)
# Salvează ca test_a4.py


def citibil(b):
  # True dacă toți octeții sunt caractere imprimabile (între 32 și 126)
  return all(32 <= c < 127 for c in b)


# Exemplu de test pentru funcția citibil
text_probă = b'Salut, David!'
print("Este textul citibil?", citibil(text_probă))
# Salvează ca test_a5.py


def citibil(b):
  # Verifică dacă toți octeții sunt caractere ASCII imprimabile
  return all(32 <= c < 127 for c in b)


try:
  with open('probe/xor.bin', 'rb') as f:
    data = f.read()

  gasit = False
  for k in range(256):
    # Aplică operația XOR pe fiecare octet cu cheia 'k'
    clar = bytes(b ^ k for b in data)
    if citibil(clar):
      print(f'[+] Cheie XOR găsită: {k}')
      print(f'[+] Text decodat: {clar.decode("latin1", errors="ignore")}')
      gasit = True
      break

  if not gasit:
    print('Nu s-a găsit nicio cheie validă.')

except FileNotFoundError:
  print(
      "Eroare: Fișierul 'probe/xor.bin' lipsește. Asigură-te că ai generat"
      ' fișierele de probă!'
  )