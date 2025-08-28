def count_vowels_consonants(s):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    for ch in s.lower():
        if ch.isalpha():  # consider only letters
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count


s = "Hello World"
v, c = count_vowels_consonants(s)

print("String:", s)
print("Vowels:", v)
print("Consonants:", c)
