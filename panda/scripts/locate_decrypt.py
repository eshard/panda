#!/usr/bin/env python2

from collections import Counter
import numpy as np
import unigram_hist
import sys

def ent(arr):
    norm = arr.astype('float32')
    row_sums = norm.sum(axis=1)
    norm = norm / row_sums[:, np.newaxis]
    ma = np.ma.log2(norm) * norm
    return -np.array(ma.sum(axis=1))

def chisq(arr):
    work = arr.astype('float')
    expect = ((1/256.)*work.sum(axis=1))[:,np.newaxis]
    work -= expect
    work *= work
    work /= expect
    return work.sum(axis=1)

reads = unigram_hist.load_hist(open(sys.argv[1]))
reads = reads[reads['hist'].sum(axis=1) > 100000]
reads = reads[reads['cr3'] != 0]
writes = unigram_hist.load_hist(open(sys.argv[2]))
writes = writes[writes['hist'].sum(axis=1) > 100000]
writes = writes[writes['cr3'] != 0]

print reads
print writes
# TODO
