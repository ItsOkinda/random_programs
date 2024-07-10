import qrcode

def generate_qr_code(link):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the link to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save("qr_code.png")
    print("QR code generated and saved as 'qr_code.png'.")

# Example usage
link = ""
generate_qr_code(link)
