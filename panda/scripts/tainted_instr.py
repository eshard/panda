#!/usr/bin/python2.7

import sys
import os
import zlib
import struct
from google.protobuf.json_format import MessageToJson
from os.path import dirname, join, realpath

panda_dir = dirname(dirname(dirname(realpath(__file__))))

def try_path(*args):
    args = list(args) + ['i386-softmmu']
    build_dir = join(*args)
    if os.path.isdir(build_dir):
        sys.path.append(build_dir)
try_path(panda_dir, 'build')
try_path(panda_dir)
try_path(dirname(panda_dir), 'opt-panda')
try_path(dirname(panda_dir), 'debug-panda')
import plog_pb2

def plogiter(fn):
    f = open(fn)

    version, _, dir_pos, _, chunk_size = struct.unpack('<IIQII', f.read(24))

    f.seek(dir_pos)
    num_chunks = struct.unpack('<I', f.read(4))[0]

    if num_chunks == 0:
        sys.exit(0)

    entries = []
    for i in range(num_chunks):
        buf = f.read(24)
        entries.append(struct.unpack('<QQQ', buf))

    if entries[-1][1] != dir_pos:
        entries.append((0, dir_pos, 0))

    for entry, next_entry in zip(entries, entries[1:]):
        start_instr, start_pos, num_entries = entry
        next_pos = next_entry[1]
        f.seek(start_pos)
        zsize = next_pos - start_pos

        zdata = f.read(zsize)
        data = zlib.decompress(zdata, 15, chunk_size)

        i = 0
        while i < len(data):
            yieldstr = ""
            if i != 0: yieldstr += ","
            entry_size = struct.unpack('<I', data[i:i+4])[0]
            i += 4
            entry_data = data[i:i+entry_size]
            message = plog_pb2.LogEntry()
            message.ParseFromString(entry_data)
            yield message
            i += entry_size


if __name__ == "__main__":
    current_asid = -1
    tainted_pcs = {}
    for ple in plogiter(sys.argv[1]):
        # see ~/work/panda/i386-softmmu/plog.proto

        if ple.HasField('asid'):
            current_asid = ple.asid
            print("asid =", current_asid)

        # TODO
