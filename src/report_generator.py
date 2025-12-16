import argparse
from os import listdir
from os.path import isfile, join
from preprocessor import preprocess_file

parser = argparse.ArgumentParser()

parser.add_argument("--docs", type=str)
parser.add_argument("--output", type=str)
parser.add_argument("--blacklist", type=str)

args = parser.parse_args()

report_resetted = False

def start_generation():
    if not args.docs:
        raise Exception("Docs path not provided.")

    if not args.output:
        raise Exception("Output path not provided.")

    if args.blacklist:
        args.blacklist = args.blacklist.split(",")

    print("Starting report generation")
    append_to_report(args.docs, None)

    print(f"Report completed at {args.output}.")

def append_to_report(path, element):
    full_path = join(path, element) if element is not None else path

    if isfile(full_path):
        if not element.endswith(".md"):
            return
        
        append_file(full_path)
    else:
        sub_elements = [e for e in listdir(full_path) if not e in args.blacklist]
        print(f"\nLooking at {len(sub_elements)} elements to append to the report.")

        for e in sub_elements:
            append_to_report(full_path, e)

def append_file(path):
    print(f"Processing file {path}")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
    except Exception as e:
        print(f"Could not process file: {e}")
        return
    
    fileMode = "a"

    global report_resetted
    if not report_resetted:
        report_resetted = True
        fileMode = "w"

    try:
        with open(args.output, fileMode, encoding='utf-8') as file:
            file.write(preprocess_file(content))
            file.write('\n\n<div style="page-break-after: always;"></div>\n\n')
        
    except IOError as e:
        print(f"Could not update the report: {e}")

if __name__ == "__main__":
    start_generation()