import base64

# Nhập thông điệp cần mã hoá
message = input("Nhập thông điệp cần mã hoá Base64: ")

# Mã hoá thông điệp bằng Base64
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')

# In thông điệp đã mã hoá
print("Thông điệp gốc:", message)
print("Thông điệp đã mã hoá Base64:", base64_message)
