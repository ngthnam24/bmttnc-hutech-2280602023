from PIL import Image
import os


def decode_image(image_path):
    """Giải mã thông điệp ẩn trong ảnh sử dụng kỹ thuật LSB"""
    # Mở ảnh
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    # Trích xuất các bit LSB từ các pixel
    binary_message = ""
    for pixel in pixels:
        r, g, b = pixel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)

    # Chuyển chuỗi nhị phân thành văn bản
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if len(byte) < 8:
            break
        char = chr(int(byte, 2))
        message += char

        # Kiểm tra ký tự kết thúc
        if message.endswith("###END###"):
            message = message[:-9]  # Xóa ký tự kết thúc
            break

    return message


if __name__ == "__main__":
    # Đường dẫn đến ảnh đã giấu tin
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = input("Nhập tên file ảnh cần giải mã (ví dụ: encoded_image.png): ")
    image_path = os.path.join(current_dir, image_path)

    # Giải mã thông điệp
    hidden_message = decode_image(image_path)
    print(f"[+] Thông điệp ẩn trong ảnh: {hidden_message}")
