import marshal
import zlib
import lzma
import base64

print("Enter 1 to encode short string")
print("Enter 2 to encode content a file")
print("Enter 0 to exit")

choice = input("Your choice: ")

if choice == '1':
    string = input("Enter your string: ")
    
    # Marshal encode
    string = marshal.dumps(string.encode())  
    
    # Zlib encode
    string = zlib.compress(string)

    # LZMA encode
    string = lzma.compress(string)
    
    # Base64 encode
    string = base64.b64encode(string) 
    
    print("Your result:", string)

elif choice == '2':
    filename = input("Enter your file name: ")
    with open(filename, 'rb') as f:
        content = f.read()
        
    # Marshal encode
    content = marshal.dumps(content) 
    
    # Zlib encode
    content = zlib.compress(content)

    # LZMA encode
    content = lzma.compress(content)
    
    # Base64 encode
    content = base64.b64encode(content)

    with open('output.txt', 'wb') as f:
        f.write(content)
        
    print("Result written to output.txt")
    
elif choice == '0':
    exit()