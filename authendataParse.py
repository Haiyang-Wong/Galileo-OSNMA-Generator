import hmac
import hashlib
from bitstring import BitArray

def binary_to_hex_and_count(binary_str):
    # fill in 0
    remainder = len(binary_str) % 4
    if remainder != 0:
        binary_str = binary_str + '0' * (4 - remainder)

    # bin-hex
    hex_str = ''
    for i in range(0, len(binary_str), 4):
        binary_segment = binary_str[i:i + 4]
        hex_digit = hex(int(binary_segment, 2))[2:]  # remove '0x'
        hex_str += hex_digit

    hex_length = len(hex_str)

    return hex_str, hex_length

#Tag,mac函数
def _hmac256(key: BitArray, message: BitArray):
    #  SHA-256
    mac = hmac.new(key=key.tobytes(), msg=message.tobytes(), digestmod=hashlib.sha256)
    # HMAC - BitArray
    return BitArray(mac.digest())

#TOW = 277200
binary_authdata = "00000010010011100011010000111010111011100000000101000100110001000111111000100110001110111000011000011010000000000000011111000001101110011110101010000001001101011101101101000100110011001101100110001010100100001001001001110111010100101001101110101110110100110010101110000110010011110100101010000100110011111111110000011010001000100111101011001111110101111110000010001110111000011111110011011111110100000001011010110001001100000010111111111110111111111111111011000100011111100000000000000111010100111010011010000000000000100110010000000100101111000001000101000010100110100001011111111001111111000000000"
binary_navdata = "000100110001000111111000100110001110111000011000011010000000000000011111000001101110011110101010000001001101011101101101000100110011001101100110001010100100001001001001110111010100101001101110101110110100110010101110000110010011110100101010000100110011111111110000011010001000100111101011001111110101111110000010001110111000011111110011011111110100000001011010110001001100000010111111111110111111111111111011000100011111100000000000000111010100111010011010000000000000100110010000000100101111000001000101000010100110100001011111111001111111000000000"
hex_value, hex_length =binary_to_hex_and_count(binary_authdata)

#TOW = 277260
key_hex="aca75fbc1c6e40a397ca7ee7ee908870"
key = BitArray(hex=key_hex)
message = BitArray(hex=hex_value)
tag = _hmac256(key, message)
print(tag)