################################################################################
# Representation Conversion Utility Functions
################################################################################


def int2lehex(value, width):
    """
    Convert an unsigned integer to a little endian ASCII hex string.
    Args:
        value (int): value
        width (int): byte width
    Returns:
        string: ASCII hex string
    """

    return value.to_bytes(width, byteorder='little').hex()


def int2varinthex(value):
    """
    Convert an unsigned integer to little endian varint ASCII hex string.
    Args:
        value (int): value
    Returns:
        string: ASCII hex string
    """

    if value < 0xfd:
        return int2lehex(value, 1)
    elif value <= 0xffff:
        return f"fd{int2lehex(value, 2)}"
    elif value <= 0xffffffff:
        return f"fe{int2lehex(value, 4)}"
    else:
        return f"ff{int2lehex(value, 8)}"


def bitcoinaddress2hash160(addr):
    """
    Convert a Base58 Bitcoin address to its Hash-160 ASCII hex string.
    Args:
        addr (string): Base58 Bitcoin address
    Returns:
        string: Hash-160 ASCII hex string
    """

    table = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    addr = addr[::-1]
    hash160 = sum((58 ** i) * table.find(c) for i, c in enumerate(addr))
    # Convert number to 50-byte ASCII Hex string
    hash160 = "{:050x}".format(hash160)

    # Discard 1-byte network byte at beginning and 4-byte checksum at the end
    return hash160[2:50 - 8]

