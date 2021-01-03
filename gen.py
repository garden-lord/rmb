import os
import hashlib
import re

barks = os.listdir('barks')

dogs = os.listdir('images')
dogs = [x for x in dogs if re.search("dog[0-9]+\.png", x)]
print(dogs)

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
    dog = dogs[hash % len(dogs)]
    highlight = dog.replace(".png", "-highlight.png")

    left = hash % 2 == 0

    out += f"""
    {{
        img: "images/{dog}",
        highlight: "images/{highlight}",
        name: "{adjective} {noun}",
        file: "{b}",
        left: {'true' if left else 'false'},
    }},"""

out += "];\n"

open("barks.js", "w").write(out)

# hi
