def dsss_simulation():
    data = input("Enter binary data (2, 3 or 4 digits): ")
    barker_code = "10110111000"
    
    print(f"\nBarker code (11 chips): {barker_code}")
    print(f"Input data            : {data}")
    
    # ----- TRANSMITTER -----
    print("\n----- TRANSMITTER -----")
    transmitted_chips = []
    
    for idx, bit in enumerate(data):
        print(f"Digit {idx + 1} = {bit}")
        print(f"  Barker   : {barker_code}")
        
        repeated_bit = bit * 11
        print(f"  Data bit : {repeated_bit}  (bit {bit} repeated 11 times)")
        
        # XOR Operation
        xor_result = "".join([str(int(a) ^ int(b)) for a, b in zip(repeated_bit, barker_code)])
        transmitted_chips.append(xor_result)
        print(f"  XOR      : {xor_result}  <- transmitted chip")
        
    # ----- CHANNEL -----
    print("\n----- CHANNEL -----")
    received_chips = []
    for idx, chip in enumerate(transmitted_chips):
        print(f"Chip {idx + 1}:")
        print(f"  Initial transmitted : {chip}")
        # Simulating an ideal channel for exact recovery, though a real simulation could inject bit flips here
        received_chips.append(chip)
        print(f"  Received            : {chip}")
        
    # ----- RECEIVER -----
    print("\n----- RECEIVER -----")
    recovered_data = ""
    
    for idx, r_chip in enumerate(received_chips):
        print(f"Chip {idx + 1}:")
        print(f"  Received chip  : {r_chip}")
        print(f"  Barker         : {barker_code}")
        
        # XOR Despread
        despread_xor = "".join([str(int(a) ^ int(b)) for a, b in zip(r_chip, barker_code)])
        print(f"  XOR (despread) : {despread_xor}")
        
        # Summation
        summation = sum([int(b) for b in despread_xor])
        print(f"  Summation      : {summation}")
        
        # Decision Logic
        if summation < 4:
            rec_bit = '0'
            condition = f"sum {summation} < 4 -> bit = 0"
        elif summation > 7:
            rec_bit = '1'
            condition = f"sum {summation} > 7 -> bit = 1"
        else:
            rec_bit = '?'
            condition = f"sum {summation} ambiguous -> bit = ?"
            
        print(f"  Condition      : {condition}")
        print(f"  Recovered bit  : {rec_bit}")
        recovered_data += rec_bit

    # ----- SUMMATION -----
    print("\n----- SUMMATION -----")
    print(f"Original Input  : {data}")
    print(f"Recovered Output: {recovered_data}")
    
    all_match = True
    for idx in range(len(data)):
        match_str = "match" if data[idx] == recovered_data[idx] else "MISMATCH"
        print(f"  Digit {idx + 1}: sent {data[idx]}, recovered {recovered_data[idx]} -> {match_str}")
        if data[idx] != recovered_data[idx]:
            all_match = False
            
    if all_match:
        print("Comment: Initial input matches output -> CORRECT")
    else:
        print("Comment: Initial input does not match output -> ERROR")

if __name__ == "__main__":
    dsss_simulation()
