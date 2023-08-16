import base64
import lzma 
import zlib
import marshal
import io
import sys

print("1. Giải mã đoạn mã ngắn")
print("2. Giải mã file")

option = input("Lựa chọn: ")

if option == '1':
  print("Nhập đoạn mã cần giải mã: ")
  content = input()
  content = base64.b64decode(content)
  content = lzma.decompress(content)
  content = zlib.decompress(content)
  content = marshal.loads(content)

  print(content)
  
elif option == '2':

  print("Nhập tên file cần giải mã: ")
  filename = input()

  with open(filename, 'rb') as f:
   content = f.read()

  content = base64.b64decode(content)
  content = lzma.decompress(content)
  content = zlib.decompress(content)
  content = marshal.loads(content)

  with open('deoutput.txt', 'w') as f:
   content = content.decode('utf-8')
   f.write(content)
    
#   exec(open('deoutput.txt').read())
  
else:
  print("Lựa chọn không hợp lệ!")