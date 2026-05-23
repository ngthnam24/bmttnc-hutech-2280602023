from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.rail_fence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher


def run_checks() -> None:
    caesar = CaesarCipher()
    vigenere = VigenereCipher()
    rail_fence = RailFenceCipher()
    playfair = PlayfairCipher()
    transposition = TranspositionCipher()

    assert caesar.decrypt(caesar.encrypt("HELLO NAM", 5), 5) == "HELLO NAM"
    assert vigenere.decrypt(vigenere.encrypt("ATTACK AT DAWN", "NAM"), "NAM") == "ATTACK AT DAWN"

    rail_text = "WE ARE SAFE"
    rail_encrypted = rail_fence.encrypt(rail_text, 3)
    assert rail_fence.decrypt(rail_encrypted, 3) == rail_text

    playfair_text = "BAOMAT"
    playfair_encrypted = playfair.encrypt(playfair_text, "THANHNAM")
    assert playfair.decrypt(playfair_encrypted, "THANHNAM").startswith("BAOMAT")

    transposition_text = "SINH VIEN HUTECH"
    transposition_encrypted = transposition.encrypt(transposition_text, 4)
    assert transposition.decrypt(transposition_encrypted, 4) == transposition_text

    print("Lab 2 self-check passed.")


if __name__ == "__main__":
    run_checks()
