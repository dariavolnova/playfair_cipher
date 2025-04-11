# Шифр Плейфера 

## Установка
- Клонировать репозиторий
```bash
git clone https://github.com/dariavolnova/playfair_cipher
cd playfair_cipher
```
- Запустить программу
``` python
from playfair_cipher import PlayfairCipher

cipher = PlayfairCipher("MONARCHY")
encrypted = cipher.encrypt("INSTRUMENTS")
print(encrypted)  # Output: GATLMZCLRQXA

decrypted = cipher.decrypt(encrypted)
print(decrypted)  # Output: INSTRUMENTSX
```
- Запустить тесты
``` python
python -m unittest test_playfair.py
```

