# A1: Importul pentru definirea structurii de date
from dataclasses import dataclass

# A4: Module pentru citirea JSON și rezolvarea căii fișierului
import json
import os

# A2: Directoarele suspecte verificate în calea procesului
CALI_SUSPECTE = ("temp", "roaming")

# A3: ID-urile de eveniment Windows considerate suspecte
SUSPECTE_ID = {4625, 1102, 7045}


# A1: Definirea procesului ca dataclass
@dataclass
class Proces:
    pid: int
    nume: str
    user: str
    cale: str

    # A2: Metoda care verifică dacă procesul rulează dintr-o cale suspectă
    def e_suspect(self) -> bool:
        cale_lower = self.cale.lower()
        return any(c in cale_lower for c in CALI_SUSPECTE)


# A3: Definirea evenimentului din jurnalul Windows ca dataclass
@dataclass
class Eveniment:
    id: int
    nivel: str
    sursa: str
    cont: str
    mesaj: str

    # A3: Verifică dacă evenimentul are un ID suspect sau nivel critic
    def e_suspect(self) -> bool:
        return self.id in SUSPECTE_ID or self.nivel.lower() == "critical"


# A4: Citește procese.json și întoarce o listă de obiecte Proces
def incarca_procese(nume_fisier: str = "procese.json") -> list[Proces]:
    dir_curent = os.path.dirname(os.path.abspath(__file__))
    cale_fisier = os.path.join(dir_curent, nume_fisier)

    if not os.path.exists(cale_fisier):
        cale_start = os.path.join(dir_curent, "start", os.path.basename(nume_fisier))
        if os.path.exists(cale_start):
            cale_fisier = cale_start

    with open(cale_fisier, "r", encoding="utf-8") as f:
        date = json.load(f)

    return [Proces(**d) for d in date]


# B3: Încarcă evenimentele dintr-un fișier JSON și le transformă în obiecte Eveniment
def evenimente_din_json(cale: str) -> list[Eveniment]:
    if not os.path.isabs(cale) and not os.path.exists(cale):
        dir_curent = os.path.dirname(os.path.abspath(__file__))
        for candidat in (
            os.path.join(dir_curent, os.path.basename(cale)),
            os.path.join(dir_curent, "start", os.path.basename(cale)),
        ):
            if os.path.exists(candidat):
                cale = candidat
                break

    if not os.path.exists(cale):
        return []

    with open(cale, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Eveniment(**d) for d in data]


# B1: Clasa-container care grupează lista de procese
@dataclass
class Inventar:
    procese: list[Proces]

    # B1: Constructor alternativ care încarcă procesele dintr-un fișier JSON
    @classmethod
    def din_json(cls, cale: str):
        if not os.path.isabs(cale) and not os.path.exists(cale):
            dir_curent = os.path.dirname(os.path.abspath(__file__))
            for candidat in (
                os.path.join(dir_curent, os.path.basename(cale)),
                os.path.join(dir_curent, "start", os.path.basename(cale)),
            ):
                if os.path.exists(candidat):
                    cale = candidat
                    break

        with open(cale, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls([Proces(**d) for d in data])

    # B1: Returnează numărul total de procese din inventar
    def __len__(self) -> int:
        return len(self.procese)

    # B2: Returnează lista proceselor marcate ca suspecte
    def suspecte(self) -> list[Proces]:
        return [p for p in self.procese if p.e_suspect()]

    # B2: Grupează numele proceselor pe utilizator folosind setdefault
    def pe_user(self) -> dict[str, list[str]]:
        rezultat: dict[str, list[str]] = {}
        for p in self.procese:
            rezultat.setdefault(p.user, []).append(p.nume)
        return rezultat


if __name__ == "__main__":
    # B3: Afișează rezumatul proceselor suspecte și al evenimentelor în alarmă
    inv = Inventar.din_json("procese.json")
    susp = inv.suspecte()
    print(f"Procese: {len(inv)} | suspecte: {len(susp)}")
    for p in susp:
        print(f"  [{p.pid}] {p.nume}  ({p.user})  {p.cale}")

    evenimente = evenimente_din_json("evenimente.json")
    alarma = [e for e in evenimente if e.e_suspect()]
    print(f"Evenimente: {len(evenimente)} | alarma: {len(alarma)}")
    for e in alarma:
        print(f"  {e.id} [{e.nivel}] {e.cont}: {e.mesaj}")
 # B4: Adaugă folderul curent în sys.path și importă clasele și funcțiile din inventar
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from inventar import Eveniment, Inventar, Proces, evenimente_din_json


# B4: Testul 1 — verifică procesele suspecte, Inventar și gruparea pe utilizator
def test_procese_suspecte_si_grupari():
    p_suspect = Proces(
        pid=3120,
        nume="update.exe",
        user="ana",
        cale="C:\\Users\\ana\\AppData\\Local\\Temp\\update.exe",
    )
    p_curat = Proces(
        pid=100,
        nume="System",
        user="SYSTEM",
        cale="C:\\Windows\\System32\\ntoskrnl.exe",
    )

    assert p_suspect.e_suspect() is True
    assert p_curat.e_suspect() is False

    inv = Inventar(procese=[p_suspect, p_curat])
    assert len(inv) == 2
    assert inv.suspecte() == [p_suspect]
    assert inv.pe_user() == {"ana": ["update.exe"], "SYSTEM": ["System"]}


# B4: Testul 2 — verifică evenimentele suspecte și încărcarea din JSON
def test_evenimente_suspecte():
    ev_id = Eveniment(
        id=4625,
        nivel="warning",
        sursa="Security",
        cont="administrator",
        mesaj="An account failed to log on",
    )
    ev_crit = Eveniment(
        id=1102,
        nivel="critical",
        sursa="Security",
        cont="administrator",
        mesaj="The audit log was cleared",
    )
    ev_normal = Eveniment(
        id=1000,
        nivel="Information",
        sursa="Application",
        cont="ana",
        mesaj="Normal execution",
    )

    assert ev_id.e_suspect() is True
    assert ev_crit.e_suspect() is True
    assert ev_normal.e_suspect() is False
    assert evenimente_din_json("fisier_inexistent_xyz.json") == []