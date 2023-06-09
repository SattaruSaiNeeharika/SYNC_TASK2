import random
def generateOTP():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    OTP = ""
    for i in range(6):
        OTP += chars[random.randint(0, len(chars)-1)]
    return OTP
def sendOTP(email_id, OTP):
    print("OTP sent successfully")
def verifyOTP(OTP, user_input):
    if OTP == user_input:
        print("OTP verified successfully")
    else:
        print("Incorrect OTP, please try again")
def main():
    email_id = input("Enter your email ID: ")
    OTP = generateOTP()
    sendOTP( email_id, OTP)
    user_input = input("Enter the OTP received: ")
    verifyOTP(OTP, user_input)
if __name__ == "__main__":
    main()
