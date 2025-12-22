import re
import argparse
from os import listdir
from os.path import isfile, join, basename
from preprocessor import preprocess_file

PAGE_BREAK = "<div style=\"page-break-after: always;\"></div>"

parser = argparse.ArgumentParser()

parser.add_argument("--docs", type=str)
parser.add_argument("--output", type=str)
parser.add_argument("--blacklist", type=str)
parser.add_argument("--toc", type=int)

args = parser.parse_args()

report_resetted = False

def start_generation():
    if not args.docs:
        raise Exception("Docs path not provided.")

    if not args.output:
        raise Exception("Output path not provided.")

    if args.blacklist:
        args.blacklist = args.blacklist.split(",")
    else:
        args.blacklist = []

    args.blacklist.append(basename(args.output))
    
    print("Starting report generation")
    append_to_report(args.docs, None)

    if args.toc is not None:
        generate_toc()

    print(f"Report completed at {args.output}.")

def append_to_report(path, element):
    full_path = join(path, element) if element is not None else path

    if isfile(full_path):
        if not element.endswith(".md"):
            return
        
        append_file(full_path)
    else:
        sub_elements = [e for e in sorted(listdir(full_path)) if not e in args.blacklist]
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
            file.write(f'\n\n{PAGE_BREAK}\n\n')
        
    except IOError as e:
        print(f"Could not update the report: {e}")

def generate_toc():
    try:
        with open(args.output, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.splitlines()
        headers = []

        for line in lines:
            if re.match(r'^#+ ', line):
                headers.append(line)

        toc = f"# Table of Contents\n"

        for header in headers:
            level = header.count("#")
            label = re.sub(r'^#+ ', '', header)

            toc += f"{"  " * level}- [{label}](#{label.lower().replace(' ', '-')})\n"
        toc += f"\n\n{PAGE_BREAK}\n\n"

        pages = [m.start() for m in re.finditer(PAGE_BREAK, content)]
        
        if args.toc < 0 or len(pages) < args.toc or len(pages) == 0 or args.toc == 0:
            toc_index = 0
        else:
            toc_index = pages[args.toc] - 1

        if toc_index < 0:
            toc_index = 0
        elif toc_index > 0:
            toc = f"\n\n{PAGE_BREAK}\n\n" + toc

        content = content[:toc_index] + toc + content[toc_index:]

        with open(args.output, 'w', encoding='utf-8') as file:
            content = file.write(content)

    except IOError as e:
        print(f"Could read the report: {e}")

if __name__ == "__main__":
    start_generation()