import argparse
from opml2json.dump import write_json

def main():
    parser = argparse.ArgumentParser(description ="python module that convert opml to json")
    parser.add_argument("-f","--file",required=True,help="location of the file")
    args = parser.parse_args()    
    if args.file:
        write_json(args.file)
    else:
        print("file not found")


if __name__ == "__main__":
   main()