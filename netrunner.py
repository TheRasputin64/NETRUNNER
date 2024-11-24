# ═══════════════════════════════════════════════════════════════════════════════════════════════════
# ████████╗██╗  ██╗███████╗    ███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
# ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
#    ██║   ███████║█████╗      ██╔██╗ ██║█████╗     ██║   ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
#    ██║   ██╔══██║██╔══╝      ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
#    ██║   ██║  ██║███████╗    ██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║
#    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
# ═══════════════════════════════════════════════════════════════════════════════════════════════════
# CORE ENCRYPTION/DECRYPTION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════════════════════════

class NetrunnerCipher:
    def __init__(self):
        self.CYBER_MASK = 0xF0  # Binary: 11110000
        
    def layer1_encrypt(self, text: str) -> list:
        """
        ICE_BREAKER Layer: Dual ASCII manipulation
        Step 1: Dynamic shift based on text length
        Step 2: Position-based ASCII scramble
        """
        text_len = len(text)
        shift = text_len % 26  # Dynamic shift based on text length
        
        encrypted = []
        for i, char in enumerate(text):
            # Step 1: Dynamic ASCII shift
            shifted = (ord(char) + shift) % 255
            # Step 2: Position-based scramble using simpler math
            scrambled = (shifted + (i * shift)) % 255
            encrypted.append(scrambled)
        return encrypted
    
    def layer2_encrypt(self, values: list) -> list:
        """
        GHOST_RUNNER Layer: Hex value transformations
        Step 1: Reverse bits in hex representation
        Step 2: Circular shift based on position
        """
        encrypted = []
        for i, val in enumerate(values):
            # Step 1: Reverse bits in hex representation
            reversed_bits = int(f"{val:08b}"[::-1], 2)
            # Step 2: Simple position-based shift
            shifted = (reversed_bits + i) % 255
            encrypted.append(shifted)
        return encrypted

    def layer3_encrypt(self, values: list) -> bytes:
        """
        MATRIX_DIVE Layer: Binary operations and final transformation
        Step 1: XOR with dynamic mask
        Step 2: Byte substitution with position influence
        """
        final = []
        for i, val in enumerate(values):
            # Step 1: XOR with dynamic mask
            dynamic_mask = (self.CYBER_MASK + i) % 256
            xored = val ^ dynamic_mask
            # Step 2: Simple substitution
            substituted = (xored + i) % 256
            final.append(substituted)
        return bytes(final)

    def layer1_decrypt(self, values: list) -> list:
        """Reverse ICE_BREAKER transformation"""
        text_len = len(values)
        shift = text_len % 26
        
        decrypted = []
        for i, val in enumerate(values):
            # Ensure input is in correct range
            val = val % 255
            # Reverse Step 2: Unscramble
            unscrambled = (val - (i * shift)) % 255
            # Reverse Step 1: Reverse shift
            unshifted = (unscrambled - shift) % 255
            decrypted.append(unshifted)
        return decrypted

    def layer2_decrypt(self, values: list) -> list:
        """Reverse GHOST_RUNNER transformation"""
        decrypted = []
        for i, val in enumerate(values):
            # Ensure input is in correct range
            val = val % 255
            # Reverse Step 2: Reverse position-based shift
            unshifted = (val - i) % 255
            # Reverse Step 1: Reverse bits (maintaining 8 bits)
            unreversed = int(f"{unshifted:08b}"[::-1], 2) % 255
            decrypted.append(unreversed)
        return decrypted

    def layer3_decrypt(self, data: bytes) -> list:
        """Reverse MATRIX_DIVE transformation"""
        decrypted = []
        for i, byte in enumerate(data):
            # Reverse Step 2: Reverse substitution
            unsubstituted = (byte - i) % 256
            # Reverse Step 1: XOR with same dynamic mask
            dynamic_mask = (self.CYBER_MASK + i) % 256
            unxored = unsubstituted ^ dynamic_mask
            decrypted.append(unxored % 255)  # Ensure output is in mod 255 range
        return decrypted

    def encrypt(self, text: str) -> dict:
        """Full NETRUNNER encryption sequence with detailed tracking"""
        try:
            # Store original ASCII values
            ascii_values = [ord(c) for c in text]
            
            # Layer 1: ICE_BREAKER
            ice_breaker = self.layer1_encrypt(text)
            
            # Layer 2: GHOST_RUNNER
            ghost_runner = self.layer2_encrypt(ice_breaker)
            
            # Layer 3: MATRIX_DIVE
            matrix_dive = self.layer3_encrypt(ghost_runner)
            
            return {
                'input': text,
                'ascii': ascii_values,
                'ice_breaker': ice_breaker,
                'ghost_runner': ghost_runner,
                'matrix_dive': matrix_dive.hex(),
                'signal_strength': len(text),
                'entropy_level': sum(ice_breaker) % 100,
                'transforms': [
                    f"ASCII [{' '.join(f'{x:03d}' for x in ascii_values)}] ─→",
                    f"ICE_BREAKER [{' '.join(f'{x:03d}' for x in ice_breaker)}] ─→",
                    f"GHOST_RUNNER [{' '.join(f'{x:03d}' for x in ghost_runner)}] ─→",
                    f"MATRIX_DIVE [{matrix_dive.hex()}]"
                ]
            }
        except Exception as e:
            return {'error': f"NETRUNNER_ENCRYPTION_FAILED: {str(e)}"}

    def decrypt(self, hex_data: str) -> str:
        """Full NETRUNNER decryption sequence"""
        try:
            data = bytes.fromhex(hex_data)
            matrix_exit = self.layer3_decrypt(data)
            ghost_exit = self.layer2_decrypt(matrix_exit)
            ice_exit = self.layer1_decrypt(ghost_exit)
            # Ensure all values are valid ASCII before converting
            return ''.join(chr(x % 128) for x in ice_exit)
        except Exception as e:
            return f"[NETRUNNER_DECRYPT_FAILED] {str(e)}"

# ═══════════════════════════════════════════════════════════════════════════════════════════════════
# ██╗   ██╗██╗███████╗██╗   ██╗ █████╗ ██╗         ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗ █████╗  ██████╗███████╗
# ██║   ██║██║██╔════╝██║   ██║██╔══██╗██║         ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝
# ██║   ██║██║███████╗██║   ██║███████║██║         ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝█████╗  ███████║██║     █████╗  
# ╚██╗ ██╔╝██║╚════██║██║   ██║██╔══██║██║         ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██║     ██╔══╝  
#  ╚████╔╝ ██║███████║╚██████╔╝██║  ██║███████╗    ██║██║ ╚████║   ██║   ███████╗██║  ██║██║     ██║  ██║╚██████╗███████╗
#   ╚═══╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
# ═══════════════════════════════════════════════════════════════════════════════════════════════════

def generate_cyber_art(length: int) -> str:
    """Generate dynamic cyberpunk ASCII art"""
    symbols = ['╔', '═', '╗', '║', '╝', '╚', '╬', '╣', '╠', '╩', '╦']
    art = [''.join(symbols[((i * j) + length) % len(symbols)] for i in range(20)) for j in range(3)]
    return '\n'.join(art)

def display_matrix(data: dict):
    """Display NETRUNNER matrix with transformation stages"""
    cyber_art = generate_cyber_art(data['signal_strength'])
    
    print(f"""
{cyber_art}
╔══════════[ NETRUNNER MATRIX SEQUENCE ]═══════╗
║                                               ║
║  TARGET_SIGNAL: {data['input']:<30} ║
║  SIGNAL_STRENGTH: {data['signal_strength']:<26} ║
║  ENTROPY_LEVEL: {data['entropy_level']}%{' ' * 27}║
║                                               ║
║  TRANSFORMATION_SEQUENCE                      ║
║  {''.join('═' for _ in range(45))}║
║  {data['transforms'][0]:<44} ║
║  {data['transforms'][1]:<44} ║
║  {data['transforms'][2]:<44} ║
║  {data['transforms'][3]:<44} ║
║  {''.join('═' for _ in range(45))}║
║                                               ║
║  ENCRYPTED_SIGNAL                            ║
║  {data['matrix_dive']:<44} ║
{cyber_art}
""")

def main():
    netrunner = NetrunnerCipher()
    
    while True:
        print("""
╔════[ NETRUNNER SYSTEM ]════╗
║                            ║
║  [1] RUN ENCRYPTION        ║
║  [2] RUN DECRYPTION        ║
║  [3] EXIT MATRIX           ║
║                            ║
╚════════════════════════════╝
""")
        cmd = input("NETRUNNER_CMD >> ")
        
        if cmd == '1':
            text = input("\nTARGET_DATA >> ")
            print("\nINITIATING_NETRUNNER_SEQUENCE...")
            display_matrix(netrunner.encrypt(text))
        
        elif cmd == '2':
            hex_data = input("\nENCRYPTED_SIGNAL >> ")
            result = netrunner.decrypt(hex_data)
            print(f"\nDECRYPTED_DATA >> {result}\n")
        
        elif cmd == '3':
            print("""
╔════[ MATRIX_EXIT ]════╗
║    CONNECTION_LOST    ║
║    RUNNER_OFFLINE     ║
║    SYSTEM_SECURE      ║
╚═══════════════════════╝
""")
            break

if __name__ == "__main__":
    main()
