# Converting bytes to text

# Define a byte object using hexadecimal digits
characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))
print()

# Converting text to bytes
characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
try:
    print(characters.encode("ascii"))
except Exception as e:
    print("Unable to encode")
print()

# Mutable byte strings
b = bytearray(b"abcdefgh")
b[4:6] = b"\x15\xa3"
print(b)
print()

b = bytearray(b'abcdef')
b[3] = ord(b'g')
b[4] = 68
print(b)
