from PIL import Image
import os


def text_to_binary(text):
    """Chuyển đổi chuỗi văn bản thành chuỗi nhị phân"""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary


def encode_image(image_path, secret_message, output_path):
    """Giấu thông điệp vào ảnh sử dụng kỹ thuật LSB"""
    # Mở ảnh
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    # Thêm ký tự kết thúc vào thông điệp
    secret_message += "###END###"

    # Chuyển thông điệp thành chuỗi nhị phân
    binary_message = text_to_binary(secret_message)
    message_length = len(binary_message)

    # Kiểm tra xem ảnh có đủ lớn để giấu thông điệp không
    if message_length > len(pixels) * 3:
        raise ValueError("Ảnh quá nhỏ để giấu thông điệp này!")

    # Giấu thông điệp vào các pixel
    new_pixels = []
    message_index = 0

    for pixel in pixels:
        r, g, b = pixel
        # Thay đổi bit cuối cùng (LSB) của mỗi kênh màu
        if message_index < message_length:
            r = (r & 0xFE) | int(binary_message[message_index])
            message_index += 1
        if message_index < message_length:
            g = (g & 0xFE) | int(binary_message[message_index])
            message_index += 1
        if message_index < message_length:
            b = (b & 0xFE) | int(binary_message[message_index])
            message_index += 1

        new_pixels.append((r, g, b))

    # Tạo ảnh mới với các pixel đã thay đổi
    encoded_img = Image.new(img.mode, img.size)
    encoded_img.putdata(new_pixels)
    encoded_img.save(output_path)
    print(f"[+] Thông điệp đã được giấu vào ảnh: {output_path}")


if __name__ == "__main__":
    # Đường dẫn đến ảnh gốc
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "image.jpg")
    output_path = os.path.join(current_dir, "encoded_image.png")

    # Nhập thông điệp cần giấu
    secret_message = input("Nhập thông điệp cần giấu vào ảnh: ")

    # Giấu thông điệp vào ảnh
    encode_image(image_path, secret_message, output_path)
