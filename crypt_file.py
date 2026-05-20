text = input("✍️ Shifrlamoqchi bo'lgan maxfiy gapni yozing: ")
shifr = "".join(chr(ord(c) + 5) for c in text)  # Oddiy shifrlash algoritmi
print(f"🔒 Shifrlangan holati: {shifr}")

ochish = "".join(chr(ord(c) - 5) for c in shifr)
print(f"🔓 Qayta ochilgan holati: {ochish}")