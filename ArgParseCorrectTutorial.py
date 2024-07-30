import argparse
import pprint
from typing import Sequence
from typing import Optional

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    #Positional
    #parser.add_argument('filename', help='configuration filename %(prog)s')
    # Optional
    # - short vs long opts
    # - aliases
    # - defaults
    #parser.add_argument('-c', '--config', '--jsonfile',
    #                    default='config.json')

    #Types
    #parser.add_argument('--days',type=int)

    #Custom Types

    args = parser.parse_args(argv)
    pprint.pprint(vars(args))
    return 0


if __name__ == "__main__":
    exit(main())