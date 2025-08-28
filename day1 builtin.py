def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
input_str = "Hello, World!"
print("Original String:", input_str)
print("Reversed String:", reverse_string(input_str))
