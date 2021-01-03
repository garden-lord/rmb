import os
import hashlib

barks = os.listdir('barks')

out = "const barks = [\n"

adjectives = open("english-adjectives.txt", "r").readlines()
nouns = open("english-nouns.txt", "r").readlines()


for b in barks:
    m = hashlib.sha256()
    the_bytes = open(f"barks/{b}", "rb").read()
    m.update(the_bytes)
    hash = int.from_bytes(m.digest(), 'big', signed=False)
    adjective = adjectives[hash % len(adjectives)].strip()
    noun = nouns[hash % len(nouns)].strip()
    print(adjective, noun)

    out += f"\t[\"{adjective} {noun}\", \"{b}\"],\n"

out += "];\n"

open("barks.js", "w").write(out)

# hi
