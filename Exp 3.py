# GSM A3 / A8 / A5 Algorithm Simulation
def a3_authentication(ki, rand):
    """
    A3 Authentication Algorithm
    Generates SRES using Ki and RAND.
    """
    sres = ki ^ rand
    return sres

def a8_key_generation(ki, rand):
    """
    A8 Key Generation Algorithm
    Generates the session encryption key Kc.
    """
    kc = ki + rand
    return kc

def a5_encrypt(data, kc): 
    """
    A5 Encryption Algorithm
    Encrypts data using Kc.
    """
    encrypted = data ^ kc
    return encrypted

def a5_decrypt(encrypted, kc):
    """
    A5 Decryption
    XOR encryption can be reversed using the same key.
    """
    decrypted = encrypted ^ kc
    return decrypted

def get_number(message):
    """Read a valid integer from the user."""
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value 
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_binary(label, value):
    """Display a value in decimal and binary."""
    print(f"{label:<20} = {value}")
    print(f"{'Binary':<20} = {value:b}")

def main():
    print("\nEnter GSM parameters:")
    ki = get_number("Enter Ki : ")
    rand = get_number("Enter RAND : ")
    data = get_number("Enter data : ")

    # ------------------------------------------------
    # A3 Authentication
    # ------------------------------------------------
    print("\n" + "-" * 50)
    print("A3 AUTHENTICATION")
    print("-" * 50)
    
    # SIM calculates SRES
    sres_sim = a3_authentication(ki, rand) 
    
    # Network independently calculates SRES
    sres_network = a3_authentication(ki, rand)
    
    print(f"SRES from SIM = {sres_sim}")
    print(f"SRES from Network = {sres_network}")
    
    if sres_sim == sres_network:
        authenticated = True
        print("\nUser authenticated successfully!")
    else:
        authenticated = False
        print("\nAuthentication failed!")

    # ------------------------------------------------
    # A8 Key Generation
    # ------------------------------------------------
    print("\n" + "-" * 50)
    print("A8 KEY GENERATION")
    print("-" * 50)
    kc = a8_key_generation(ki, rand)
    print(f"Ki = {ki}")
    print(f"RAND = {rand}")
    print(f"Kc = {kc}")

    # ------------------------------------------------
    # A5 Encryption 
    # ------------------------------------------------
    print("\n" + "-" * 50)
    print("A5 ENCRYPTION")
    print("-" * 50)
    encrypted_data = a5_encrypt(data, kc)
    print(f"Original data = {data}")
    print(f"Encryption key = {kc}")
    print(f"Encrypted data = {encrypted_data}")

    # ------------------------------------------------
    # A5 Decryption
    # ------------------------------------------------
    print("\n" + "-" * 50)
    print("A5 DECRYPTION")
    print("-" * 50)
    decrypted_data = a5_decrypt(encrypted_data, kc)
    print(f"Encrypted data = {encrypted_data}")
    print(f"Decrypted data = {decrypted_data}")

    # ------------------------------------------------
    # Verification
    # ------------------------------------------------
    print("\n" + "=" * 50)
    print("VERIFICATION")
    print("=" * 50)
    if decrypted_data == data:
        print("Encryption/Decryption : SUCCESS")
    else:
        print("Encryption/Decryption : FAILED")
        
    print("\nSimulation completed.")

if __name__ == "__main__":
    main()