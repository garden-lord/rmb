import os
import hashlib

barks = os.listdir('barks')

out = "const barks = [\n"

for b in barks:
    m = hashlib.sha256()
    the_bytes = open(f"barks/{b}", "rb").read()
    m.update(the_bytes)
    hash = m.hexdigest()[0:3].upper()

    out += f"\t[\"{hash}\", \"{b}\"],\n"

out += "];\n"

open("barks.js", "w").write(out)

# hi
