import unittest
from src.model.classes.encryption import Encryption
from src.model.classes.registro_climatico import RegistroClimatico
from src.model.functions.encrypt_encrypt import encrypt
from src.model.functions.encrypt_decrypt import decrypt

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.encryption = Encryption()
        self.registro = RegistroClimatico("2025-04-23 10:00", 25.5, 60)

    def test_encrypt_decrypt(self):
        encrypted = encrypt(self.encryption, self.registro)
        self.assertIsInstance(encrypted, str)
        decrypted_data = decrypt(self.encryption, encrypted)
        self.assertEqual(decrypted_data['fecha'], self.registro.fecha)
        self.assertEqual(decrypted_data['temperatura'], self.registro.temperatura)
        self.assertEqual(decrypted_data['humedad'], self.registro.humedad)

if __name__ == "__main__":
    unittest.main()

# Pruebas:
# test_encrypt_decrypt: Verifica que un registro se cifre y descifre correctamente, recuperando los datos originales.

# Uso: Asegura que el cifrado AES funcione correctamente.

