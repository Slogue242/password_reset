import qrcode
import reset_code
import get_code

code = get_code.recover_code()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(code)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()

user_input = input("Please Enter Code: ")
if user_input == str(code):
	print("Correct code")
else:
	print("Wrong code. Closing program")