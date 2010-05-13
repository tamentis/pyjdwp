"""Parsers and packers for JDWP formats and types."""

import os
import sys
import struct

# Default object sizes (will be changed by set_sizes)
field_id_size = 4
method_id_size = 4
object_id_size = 4
reference_id_size = 4
frame_id_size = 4

def unpack_string( data):
    """Extra a JDWP string.

    Find the length of a string in the first 4 bytes and extract from the
    UTF-8 encoded data that follows.
    """
    length = unpack_int(data) + 4
    return str(data[4:length], "UTF-8"), length

def unpack_int(data):
    """Extract an int from 4 bytes, big endian."""
    return struct.unpack(">i", data[:4])[0]

def unpack_ubyte(data):
    """Extract an unsigned int from a byte."""
    return data[0]

def unpack_boolean(data):
    if unpack_ubyte(data) == 0:
        return False
    else:
        return True

def unpack_address(data, id_size):
    """Extract a memory pointer."""
    if id_size == 8:
        return struct.unpack(">Q", data[:8])[0]
    else:
        return struct.unpack(">L", data[:4])[0]

def unpack(data, format, add_offset=False):
    """Unpack a Java/JDWP string."""
    offset = 0
    unpacked_objects = [ ]
    for fchar in format:
        # String (pascal-style with a uint32 for the size)
        if fchar == "s":
            obj, length = unpack_string(data[offset:])
            offset += length
        # Integers (4 bytes big endian)
        elif fchar == "i":
            obj = unpack_int(data[offset:])
            offset += 4
        # Byte
        elif fchar == "b":
            obj = unpack_ubyte(data[offset:])
            offset += 1
        # ReferenceID
        elif fchar in ("r", "o"):
            obj = unpack_address(data[offset:], reference_id_size)
            offset += reference_id_size
        # Bool
        elif fchar == "?":
            obj = unpack_boolean(data[offset:])
            offset += 1
        else:
            raise ValueError("Unknown format character: " + fchar)
        unpacked_objects.append(obj)
    if add_offset:
        unpacked_objects.append(offset)
    return unpacked_objects

def pack_byte(b):
    """Pack one integer byte in a byte array."""
    return bytes([b])

def pack_int(i):
    """Pack an int into 4 bytes big endian."""
    return struct.pack(">i", i)

def pack_string(s):
    """Pack a string into a 4byte int (len) + its UTF-8 equivalent."""
    b = bytes(s, "UTF-8")
    packed_length = pack_int(len(b))
    return packed_length + b

def set_sizes(sizes):
    global field_id_size
    global method_id_size
    global objet_id_size
    global reference_id_size
    global frame_id_size
    (field_id_size, method_id_size, objet_id_size, reference_id_size,
        frame_id_size) = sizes

