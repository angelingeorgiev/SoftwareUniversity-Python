filepath = input().split("\\")
# Retrieves the last element of the list, which is assumed to be the filename and extension.
filename_and_extension = filepath[-1]
filename, extension = filename_and_extension.split(".")

print(f"File name: {filename}\nFile extension: {extension}")
