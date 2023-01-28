
import argparse
import sys
  

def cli(argv=sys.argv):
    parser = argparse.ArgumentParser(description='Enter string')
    parser.add_argument('string', type=str, help='Enter word or words',
                        nargs='*')

    cli_args = parser.parse_args(argv[1:])

    cli_args = str(cli_args).replace('Namespace(string=[', '')[:-2]
    cli_args = cli_args.split(',')

    for (n, i) in enumerate(cli_args):
        cli_args[n] = i.strip()[1:-1]


    class args:
      string = " ".join(cli_args)
      array = cli_args
