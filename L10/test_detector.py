import pytest
from collections import Counter
from parse_auth import esec
from detector import suspecți

def test_esec_valid():
    linie = "Failed password for root from 203.0.113.9 port 51230 ssh2"
    assert esec(linie) == ("root", "203.0.113.9")

def test_suspecti_valid():
    c = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
    rezultat = suspecți(c, prag=10)
    assert rezultat == [("203.0.113.9", 13)]