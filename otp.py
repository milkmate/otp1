import pyotp

# Generate a secret key
secret_key = pyotp.random_base32()

# Create an OTP object
otp = pyotp.TOTP(secret_key)

# Get the OTP value
otp_value = otp.now()

# Print the OTP value
print("Generated OTP:", otp_value)

# Simulate user input
user_input = input("Enter the OTP:")

# Verify the OTP
is_valid = otp.verify(user_input)

# Check if the OTP is valid
if is_valid:
    print("OTP is valid.")
else:
    print("OTP is not valid.")
