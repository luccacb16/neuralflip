from features import *

seq = '01000101110010110110010001110100101101010010010100'
seq2 = '00000000000000000000000001111111111111111111111111'

assert F1(seq) == 0
assert F1(seq2) == -1 # qtd(0) == qtd(1)

assert F2(seq) == 27

assert F3(seq) == 23

assert F4(seq) == 3

assert F5(seq) == 3

assert F6(seq) == 32

assert F7(seq) == 27/17

assert F8(seq) == 23/16

assert F9(seq) == 1

assert F10(seq) == 0

assert F12(seq) == 0
assert F12(seq2) == 0

assert F15(seq) == 16

assert round(F16(seq), 4) == 0.9954