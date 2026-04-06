import hashlib

hash = "f338e1ff264d8c6d745caf27dd30a2f4eab4a138de1c32e9162a340ac8880fb9"

for i in range(10_000_000_000):
    s = f"{i:010d}"  
    h = hashlib.sha256(s.encode()).hexdigest()

    if h == hash:
        print("Secuencia de entrada:", s)
        break
