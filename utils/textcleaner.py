def correct_spelling(word):
    # Dummy correction for demo
    corrections = {"intersteller": "interstellar", "avengrs": "avengers"}
    return corrections.get(word.lower(), word)
