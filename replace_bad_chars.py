import argparse

def replace_badchars(sequence):
	sequence = [x for x in sequence]
	for i in range(len(sequence)):
		if sequence[i] not in 'ACGTacgt-':
			sequence[i] = 'N'
	return "".join(sequence)

parser = argparse.ArgumentParser(description = 'Replaces invalid bases with N \n Usage : remove_bad_chars.py -i input_maf_file -o output_maf_file')
parser.add_argument('-i', '--input', type=str)
parser.add_argument('-o', '--output', type=str)

args = parser.parse_args()

if args.input is None or args.output is None:
	print("No input or output specified")
	exit()

f = open(args.input, 'r')

of = open(args.output, 'w')

for line in f.readlines():
	segments = line.split()
	if len(segments) != 7:
		of.write(line)
	else:
		segments[-1] = replace_badchars(segments[-1])
		of.write(" ".join(segments)+'\n')
