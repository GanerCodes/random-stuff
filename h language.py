abcs = "#abcdefghijklmnopqrstuvwxyz "

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def encode(msg):
	return 'h' * int(''.join([bin(abcs.index(i))[2:].rjust(5, '0') for i in msg]), 2)

def decode(msg):
	t = ''.join(list(chunks(bin(len(msg))[2:], 5)))
	return ''.join([abcs[int(i, 2)] for i in chunks('0' * (5 - len(t) % 5) + t, 5)])

print((encode("hey")))