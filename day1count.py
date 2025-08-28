def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = input("Enter a string: ")
print("Character Frequency:")
for char, count in char_frequency(s).items():
    print(f"{char}: {count}")

