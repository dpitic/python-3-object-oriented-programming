# Demonstration of writing to a file.

contents = "Some file contents"
file = open("filename", "w")        # truncate if already exists
file.write(contents)
file.close()
