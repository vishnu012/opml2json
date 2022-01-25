import argparse
from importlib.metadata import requires
from opml2json.dump import write_json

def main():
    parser = argparse.ArgumentParser(description ="python module that convert opml to json")
    parser.add_argument("-f","--file",required=True,help="location of the file")
    parser.add_argument("-o","--output",default='sample.json',required=False,help="json output file")
    args = parser.parse_args()    
    if args.file:
        write_json(args.file,args.output)


if __name__ == "__main__":
   main()