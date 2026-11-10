from arsenal.forensics.decode import desfaci


def test_base64():
  strat, _ = desfaci('U2FsdGVkXQ==')
  assert strat == b'Base64'


def test_salut():
  strat, _ = desfaci('Salut')
  assert strat == b'Salut'