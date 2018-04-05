# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:26:44 2018

@author: pbecza
"""

import sys

cnt_args = len(sys.argv)
if cnt_args < 4:
    print('Too few arguments, check if you have these arguments <length> <threshold> <input_file>')
elif cnt_args > 4:
    print('Too much arguments, check if you have these arguments <length> <threshold> <input_file>')
else:
    length = float(sys.argv[1])
    threshold = float(sys.argv[2]) 
    input_file = sys.argv[3]
#    print('minimum length: {}'.format(length))
#    print('threshold of identity: {}'.format(threshold))
#    print('input_file: {}'.format(input_file))
    output_file = 'selfal{}_{}.psl'.format(int(length), int(threshold))
#    print('output_file: {}'.format(output_file))
    threshold = threshold / 100.0
    
    with open(input_file, 'r') as fin:
        with open(output_file, 'w') as fout:
            cnt = 0
            cnt_lines = 0
            for line in fin:
                cnt += 1
                C = line.split()
                if len(C) != 21:
                    print('Error line number: {}'.format(cnt))
                    continue
                matches = float(C[0])
                tmp_sum = (matches + float(C[1]) + float(C[2]) + float(C[3]) + float(C[5]) + float(C[7]))
                A = ((C[9] == C[13]) and (float(C[10]) == float(C[12])) and ((float(C[11]) == 0)))
                B = ((float(C[12])-float(C[11])) < float(length))
                C = ((float(C[16])-float(C[15])) < float(length))
                D = (matches < (threshold * tmp_sum))
                if (A or B or C or D):
                    continue
                cnt_lines += 1
                fout.write(line)
print('Done. Result have: {}. You fill find it in file with name: {}'.format(cnt_lines, output_file))
