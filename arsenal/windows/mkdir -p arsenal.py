mkdir -p arsenal/windows && cat << 'EOF' > arsenal/windows/inventar.py
import sys
import json
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Proces:
    pid: int
    nume: str
    user: str
    cale: str

    def e_suspect(self) -> bool:
        cale_lower = self.cale.lower()
        return "appdata\\local\\temp" in cale_lower or "\\temp\\" in cale_lower

@dataclass
class Eveniment:
    id: int
    nivel: str
    sursa: str
    cont: str
    mesaj: str

def incarca_inventar(folder_cale: Path):
    procese = []
    evenimente = []
    
    p_file = folder_cale / "procese.json"
    if p_file.exists():
        with open(p_file, "r", encoding="utf-8") as f:
            procese = [Proces(**item) for item in json.load(f)]
            
    e_file = folder_cale / "evenimente.json"
    if e_file.exists():
        with open(e_file, "r", encoding="utf-8") as f:
            evenimente = [Eveniment(**item) for item in json.load(f)]
            
    return procese, evenimente

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_start = Path(sys.argv[1])
        print(f"Se analizează folderul: {folder_start}")
        
        procese, evenimente = incarca_inventar(folder_start)
        
        print(f"\n--- RAPORT PROCESE ({len(procese)}) ---")
        for p in procese:
            status = "[SUSPECT]" if p.e_suspect() else "[OK]"
            print(f"{status} PID: {p.pid} | {p.nume} | Utilizator: {p.user} | Cale: {p.cale}")
            
        print(f"\n--- RAPORT EVENIMENTE SECURITATE ({len(evenimente)}) ---")
        for e in evenimente:
            print(f"[{e.nivel.upper()}] ID: {e.id} | Sursă: {e.sursa} | Cont: {e.cont} | Mesaj: {e.mesaj}")
    else:
        print("Utilizare: python -m arsenal.windows.inventar <cale_folder_start>")
EOF