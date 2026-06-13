import base64

# Nhập thông điệp đã mã hoá Base64
base64_message = input("Nhập thông điệp đã mã hoá Base64: ")

# Giải mã thông điệp từ Base64
base64_bytes = base64_message.encode('utf-8')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('utf-8')

# In thông điệp đã giải mã
print("Thông điệp đã mã hoá Base64:", base64_message)
print("Thông điệp đã giải mã:", message)
