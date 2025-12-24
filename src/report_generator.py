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
parser.add_argument("--presentation", type=str)
parser.add_argument("--placeholders", type=str)

args = parser.parse_args()

current_report_content = ""

def start_generation():
    global current_report_content
    current_report_content = ""

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

    if args.presentation is not None:
        placeholders = args.placeholders.split(",") if args.placeholders else []

        for placeholder in placeholders:
            p = placeholder.split(":")
            args.presentation = args.presentation.replace(p[0], p[1])

        args.presentation += f'\n\n{PAGE_BREAK}\n'

        current_report_content = args.presentation + current_report_content

    if args.toc is not None:
        generate_toc()

    try:
       with open(args.output, "w", encoding='utf-8') as file:
            file.write(preprocess_file(current_report_content))
    except:
        print("Could not save the report")

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
    
    global current_report_content

    content = preprocess_file(content)
    content += f'\n\n{PAGE_BREAK}\n\n'

    current_report_content += content

def generate_toc():
    global current_report_content
    
    lines = current_report_content.splitlines()
    headers = []

    for line in lines:
        if re.match(r'^#+ ', line):
            headers.append(line)

    toc = f"# Table of Contents\n"

    for header in headers:
        level = header.count("#")
        label = re.sub(r'^#+ ', '', header)

        toc += f"{'  ' * level}- [{label}](#{label.lower().replace(' ', '-')})\n"
    toc += f"\n{PAGE_BREAK}"

    pages = [m.start() for m in re.finditer(PAGE_BREAK, current_report_content)]
    
    if args.toc < 0 or len(pages) < args.toc or len(pages) == 0 or args.toc == 0:
        toc_index = 0
    else:
        toc_index = pages[args.toc - 1] + len(PAGE_BREAK)

    if toc_index > 0:
        toc = "\n\n" + toc

    current_report_content = current_report_content[:toc_index] + toc + current_report_content[toc_index:]

if __name__ == "__main__":
    start_generation()