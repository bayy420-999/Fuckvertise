import argparse
from Fuckvertise import Fuckvertise

def main():
    parser = argparse.ArgumentParser(
        description = 'Fuckvertise CLI program'
    )

    parser.add_argument(
        'urls',
        nargs = '*',
        help = 'List of url')
    parser.add_argument(
        '-b',
        '--batch',
        help = 'Provide `.txt` file that contains list of url')
    parser.add_argument(
        '-o',
        '--output-file',
        default = 'result.txt',
        help = 'Provide output file')
    parser.add_argument(
        '-v',
        '--verbose',
        action = 'store_true',
        help = 'For verbosity reason')

    args = parser.parse_args()
    urls = args.urls
    filename = args.batch
    output_file = args.output_file
    verbose = args.verbose

    fv = Fuckvertise(verbose)

    if urls:
        fv.get_direct_link(urls)
    if filename:
        fv.get_direct_link(fv.load_from_txt(filename))

    fv.save_result(output_file)

if __name__ == '__main__':
    main()
