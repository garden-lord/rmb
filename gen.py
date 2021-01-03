import os

barks = os.listdir('barks')

out = "const barks = [\n"

for b in barks:
    out += f"\t\"{b}\",\n"

out += "];\n"

open("barks.js", "w").write(out)

# hi
