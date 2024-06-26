from PIL import Image

def apply_operation(pixel, operation, key):
    if operation == 'swap':
        return tuple(component ^ key for component in pixel)
    elif operation == 'multiply':
        return tuple((component * key) % 256 for component in pixel)

def process_image(image, operation, key):
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            pixels[x, y] = apply_operation(pixels[x, y], operation, key)

def encrypt_image(image_path, operation, key):
    image = Image.open(image_path)
    process_image(image, operation, key)
    encrypted_image_path = image_path.replace('.', '_encrypted.')
    image.save(encrypted_image_path)
    print("Image encrypted successfully:", encrypted_image_path)

def decrypt_image(image_path, operation, key):
    image = Image.open(image_path)
    process_image(image, operation, key)
    decrypted_image_path = image_path.replace('_encrypted', '_decrypted')
    image.save(decrypted_image_path)
    print("Image decrypted successfully:", decrypted_image_path)

def main():
    image_path = input("Enter the path to the image: ")
    operation = input("Enter the operation (swap or multiply): ")
    key = int(input("Enter the key (integer): "))

    if operation not in ['swap', 'multiply']:
        print("Invalid operation. Choose between 'swap' and 'multiply'.")
        return

    encrypt_image(image_path, operation, key)
    decrypt_image(image_path.replace('.', '_encrypted.'), operation, key)

if __name__ == "__main__":
    main()
