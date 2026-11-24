from pathlib import Path

from arsenal.forensics.amprente import amprenta_fisier, scaneaza, tip

PROBE = Path(__file__).resolve().parent / "probe"


def test_tip_din_magic():
    assert tip(b"\x89PNG\r\n") == "PNG"
    assert tip(b"%PDF-1.4") == "PDF"
    assert tip(b"PK\x03\x04") == "ZIP"
    assert tip(b"altceva") == "necunoscut"


def test_amprenta_png():
    rez = amprenta_fisier(str(PROBE / "imagine.png"))
    assert rez["nume"] == "imagine.png"
    assert rez["tip"] == "PNG"
    assert rez["sha256"] == "ea3a9848da7e6c1d"


def test_scaneaza_toate():
    rez = scaneaza(str(PROBE))
    assert len(rez) == 4
    assert [r["nume"] for r in rez] == [
        "arhiva.zip",
        "imagine.png",
        "note.txt",
        "raport.pdf",
    ]
