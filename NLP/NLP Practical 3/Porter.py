import re

def porter_stemmer(word):
   
    step1a_patterns = [
        (r"sses$", "ss"),
        (r"ies$", "i"),
        (r"ss$", "ss"),
        (r"s$", ""),
    ]

    for pattern, replacement in step1a_patterns:
        word = re.sub(pattern, replacement, word)

    m = re.search(r"eed$", word)
    if m:
        if len(word[:m.start()]) > 0:
            word = word[:-1]

    elif re.search(r"ed$|ing$", word):
        m = re.search(r"ed$|ing$", word)
        stem = word[:m.start()]

        if re.search(r"at|bl|iz$", stem):
            word = stem + "e"
        elif re.search(r"(bb|dd|ff|gg|mm|nn|pp|rr|tt)$", stem):
            word = stem[:-1]
        elif re.search(r"([^aeiou])\1$", stem):
            word = stem[:-1]
        elif len(stem) == 1 and re.search(r"[aeiou][^aeiou][aeiou]$", word):
            word += "e"

    m = re.search(r"y$", word)
    if m:
        stem = word[:m.start()]
        if re.search(r"[aeiou]", stem):
            word = stem + "i"

 
    step2_patterns = [
        (r"ational$", "ate"),
        (r"tional$", "tion"),
        (r"enci$", "ence"),
        (r"anci$", "ance"),
        (r"izer$", "ize"),
        (r"abli$", "able"),
        (r"alli$", "al"),
        (r"entli$", "ent"),
        (r"eli$", "e"),
        (r"ousli$", "ous"),
        (r"ization$", "ize"),
        (r"ation$", "ate"),
        (r"ator$", "ate"),
        (r"alism$", "al"),
        (r"iveness$", "ive"),
        (r"fulness$", "ful"),
        (r"ousness$", "ous"),
        (r"aliti$", "al"),
        (r"iviti$", "ive"),
        (r"biliti$", "ble"),
    ]

    for pattern, replacement in step2_patterns:
        m = re.search(pattern, word)
        if m:
            stem = word[:m.start()] + replacement
            if len(stem) >= 2:
                word = stem

 
    step3_patterns = [
        (r"icate$", "ic"),
        (r"ative$", ""),
        (r"alize$", "al"),
        (r"iciti$", "ic"),
        (r"ical$", "ic"),
        (r"ful$", ""),
        (r"ness$", ""),
    ]

    for pattern, replacement in step3_patterns:
        m = re.search(pattern, word)
        if m:
            stem = word[:m.start()] + replacement
            if len(stem) >= 2:
                word = stem

  
    m = re.search(r"log$", word)
    if m:
        stem = word[:m.start()]
        if len(stem) >= 2:
            word = stem

    m = re.search(r"ness$", word)
    if m:
        stem = word[:m.start()]
        if len(stem) >= 2:
            word = stem

    m = re.search(r"^(m|s|t)(?:[^aeiou])+$", word)
    if m:
        word = word[:-1]

    m = re.search(r"^(.+?)eed$", word)
    if m:
        if len(m.group(1)) >= 2:
            word = m.group(1)

    m = re.search(r"^[^aeiou](.+?)(ed|ing)$", word)
    if m:
        stem = m.group(1)
        if re.search(r"[aeiou]", stem):
            word = stem

  
    m = re.search(r"i$", word)
    if m:
        stem = word[:m.start()]
        if re.search(r"[^aeiou]", stem):
            word = stem

 
    if len(word) >= 2 and word[-1] == "y":
        stem = word[:-1]
        if re.search(r"[^aeiou]", stem):
            word = stem

    return word

words = ["running", "flies", "happily", "agreed", "owned", "jumps", "stemming", "stemmer"]
for word in words:
    print(f"{word} -> {porter_stemmer(word)}")
