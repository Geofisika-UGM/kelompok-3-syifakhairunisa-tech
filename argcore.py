import argparse
import sys
from fungs import ramp_prob

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=float, default=1.0,
                        help='Massa benda')
    parser.add_argument('--g', type=float, default=1.0,
                        help='Gravitasi')
    parser.add_argument('--agl', type=float, default=1.0,
                        help='Sudut')
    parser.add_argument('--kg', type=float, default=1.0,
                        help='Koefisien Gesek')
    parser.add_argument('--t', type=float, default=1.0,
                        help='Waktu')                    
    parser.add_argument('--op', type=str, default='ok',
                        help='Operator')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.op == 'ok':
        m=args.m
        g=args.g
        sudut=args.agl
        μs=args.kg
        t=args.t
        ramp_prob(m,g,sudut,μs,t)

if __name__ == '__main__':
    main()