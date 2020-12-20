# This method returns the length of the string in bytes.

def byte_size(string):
    return(len(string.encode('utf-8')))

print(byte_size('?'))
print(byte_size('Hello World'))

