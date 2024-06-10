#! /usr/bin/env python3
''' Multiply large integers or polynomials using NTT

Perform fast multiplication of polynomials using the Number Theoretic Transform,
with fewer reductions modulo N using the method described by David Harvey in
http://dx.doi.org/10.1016/j.jsc.2013.09.002 '''

import argparse


def main():
    '''Run NTT and produce test vectors for the given inputs'''

    parser = argparse.ArgumentParser(
        prog='fast_ntt',
        description='Run Harvey\'s Fast NTT and produce test vectors'
    )
    parser.add_argument(
        '--xlen', '-x',
        default=32,
        type=int,
        help='machine word size (i.e. 32 for 32-bit)'
    )
    parser.add_argument(
        '--transform-len', '-L',
        required=True,
        type=int,
        help='NTT length. must be some power of 2 such that p = 1 (mod L) is a large prime'
    )


    # beta = machine word size
    beta = 2^args.xlen
    
    

if __name__ == "__main__":
    main()
