import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    """
    Generate a QR code and save it to a file.

    Parameters:
        data (str): The data to encode in the QR code.
        filename (str): The filename to save the QR code image. Default is "qrcode.png".
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
data_to_encode = "Hello, this is a QR code!"
generate_qr_code(data_to_encode)
