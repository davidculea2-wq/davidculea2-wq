# Importă clasele și funcția din modulul principal al lucrării
from arsenal.windows.inventar import Eveniment, Inventar, Proces, evenimente_din_json


# Verifică detecția proceselor suspecte, lungimea inventarului, filtrarea și gruparea pe utilizator
def test_procese_si_inventar():
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


# Verifică detecția evenimentelor suspecte și comportamentul la fișier lipsă
def test_evenimente():
    ev_brute_force = Eveniment(
        id=4625,
        nivel="warning",
        sursa="Security",
        cont="administrator",
        mesaj="An account failed to log on",
    )
    ev_critic = Eveniment(
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

    assert ev_brute_force.e_suspect() is True
    assert ev_critic.e_suspect() is True
    assert ev_normal.e_suspect() is False
    assert evenimente_din_json("fisier_inexistent_xyz.json") == []