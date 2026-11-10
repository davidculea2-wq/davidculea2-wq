#Partea B
s = "Salut"
b = s.encode()  # b'Salut'
print("Bytes:", b)
# TODO: sparete b.hex() si refa bytes din hex
b_hex = b.hex()
b_from_hex = bytes.fromhex(b_hex)
print("Hex:", b_hex)
print("Din hex înapoi:", b_from_hex) 
import re

# B2. strings: textul citibil dintr-un binar
def extrage_strings(cale):
    with open(cale, "rb") as f:
        data = f.read()
    
    print(f"--- Secvențe text găsite în {cale} ---")
    # Caută secvențe de cel puțin 4 caractere imprimabile (între spațiu ' ' și tildă '~')
    for m in re.findall(b'[ -~]{4,}', data):
        print(m.decode('ascii', errors='ignore'))

# B3. Metadate EXIF și GPS din poză
from PIL import Image
from PIL.ExifTags import TAGS


def citeste_exif(cale):
  img = Image.open(cale)
  exif = img.getexif() or {}
  for id_tag, val in exif.items():
    tag = TAGS.get(id_tag, id_tag)
    print(f"{tag}: {val}")


citeste_exif("probe/foto.jpg")
# B4. File carving: scoți fișierul ascuns
def file_carving(cale):
  with open(cale, "rb") as f:
    data = f.read()
  i = data.find(b"PK\x03\x04")
  if i != -1:
    with open("probe/gasit.zip", "wb") as out:
      out.write(data[i:])
    print("Arhivă extrasă cu succes în probe/gasit.zip")


file_carving("probe/ascuns.png")
# B5. Ascunzi un mesaj prin LSB
from PIL import Image


def ascunde_lsb(cale_poza, mesaj):
  img = Image.open(cale_poza).convert("RGB")
  px = list(img.getdata())
  bina = "".join(format(ord(c), "08b") for c in mesaj) + "00000000"

  nou_px = []
  idx = 0
  for p in px:
    r, g, b = p
    if idx < len(bina):
      r = (r & ~1) | int(bina[idx])
      idx += 1
    nou_px.append((r, g, b))

  img_noua = Image.new(img.mode, img.size)
  img_noua.putdata(nou_px)
  img_noua.save("stego.png")
  print("Mesaj ascuns în stego.png")


ascunde_lsb("probe/foto.jpg", "MesajSecret")
# B6. Dezvălui mesajul înapoi
from PIL import Image


def dezvalui_lsb(cale_stego):
  img = Image.open(cale_stego).convert("RGB")
  px = list(img.getdata())
  biti = ""
  for r, g, b in px:
    biti += str(r & 1)

  octeti = [int(biti[i : i + 8], 2) for i in range(0, len(biti), 8)]
  rezultat = ""
  for o in octeti:
    if o == 0:
      break
    rezultat += chr(o)
  print("Mesaj dezvăluit:", rezultat)
  return rezultat


dezvalui_lsb("stego.png")