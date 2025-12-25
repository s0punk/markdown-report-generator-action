import re
import textwrap
from os import listdir
from os.path import isfile, join

class CollectionInsertStrategy:
    def insert(self, content: str, collection_path: str, insert_index: int) -> str:
        pass

class HorizontalTableStrategy(CollectionInsertStrategy):
    def insert(self, content: str, collection_path: str, insert_index: int) -> str:
        files = read_collection(collection_path)
        if len(files) == 0:
            return content

        new_content = ""

        headers = parse_headers(files[0])
        
        for file in files:
            table = "<table style=\"page-break-inside: avoid; break-inside: avoid;\">"

            for header in headers:
                value = parse_value(file, f"## {header}")
                table += f"\n<tr><th>{header}</th><td>{format_lists(value)}</td></tr>"

            table += "\n</table>"
            new_content += f"\n{table}<br />"

        content = content[:insert_index] + new_content + content[insert_index:]
        return content

class TableStrategy(CollectionInsertStrategy):
    def insert(self, content: str, collection_path: str, insert_index: int) -> str:
        files = read_collection(collection_path)
        if len(files) == 0:
            return content

        new_content = ""
        sep = ""

        headers = parse_headers(files[0])

        for header in headers:
            new_content += f"| {header} "
            sep += f"| {"-" * len(header)} "
        new_content += f"|\n{sep}|"
        
        for file in files:
            new_content += "\n"

            for header in headers:
                value = parse_value(file, f"## {header}")
                new_content += f"| {format_lists(value).replace("\n", "<br/>")} "

            new_content += "|"

        content = content[:insert_index] + new_content + content[insert_index:]
        return content

class RawStrategy(CollectionInsertStrategy):
    def insert(self, content: str, collection_path: str, insert_index: int) -> str:
        files = read_collection(collection_path)
        if len(files) == 0:
            return content

        new_content = ""

        for file in files:
            new_content += f"{file}\n"

        content = content[:insert_index] + new_content + content[insert_index:]
        return content

def read_collection(path):
    files = [e for e in sorted(listdir(path)) if isfile(join(path, e)) and e.endswith(".md")]
    print(f"Found {len(files)} files in collection {path}")

    contents = []

    for f in files:
        try:
            with open(join(path, f), 'r', encoding='utf-8') as file:
                contents.append(file.read())
        except:
            print(f"Could not read file {f}")

    return contents

def parse_headers(content):
    headers = []

    for line in content.split("\n"):
        if "## " in line:
            headers.append(line.replace("## ", ""))
    
    return headers

def parse_value(content, header):
    start = content.find(header)
    if start == -1:
        return ""
    
    end = content.find("## ", start + 1)
    if end == -1:
        end = len(content)
    
    value = content[start + len(header):end]
    
    while value.startswith("\n") or value.endswith("\n"):
        value = value.removeprefix("\n").removesuffix("\n")

    return value

def format_lists(text: str) -> str:
    lines = text.splitlines()
    out = []

    state = ""

    def check_state(pattern: str, state_id: str, line: str) -> bool:
        nonlocal state
        nonlocal out
        
        if re.match(pattern, line):
            if state != state_id:
                close_state()

                state = state_id
                out.append(f"<{state}>")

            out.append(f"<li>{re.sub(pattern, '', line)}</li>")

            return True
    
        return False
    
    def close_state():
        nonlocal state
        nonlocal out

        if state != "":
            out.append(f"</{state}>")

    i = 0
    while i < len(lines):
        if check_state(r'^[0-9]+[.)]\s+', "ol", lines[i]):
            i += 1
            continue

        if check_state(r'^-\s+', "ul", lines[i]):
            i += 1
            continue

        if re.match(r'^\s+(?:[0-9]+[.)]|-)\s+', lines[i]):
            for j in range(i, len(lines)):
                match = re.match(r'^\s+(?:[0-9]+[.)]|-)\s+', lines[j])
                if j == len(lines) - 1 or not match:
                    sublines = textwrap.dedent("\n".join(lines[i:j + 1 if j == len(lines) - 1 and match else j]))
                    out.append(format_lists(sublines))
                    i = j + 1 if j == len(lines) - 1 and match else j - 1
                    break
            i += 1
            continue

        out.append(lines[i])
        i += 1

    close_state()

    return "\n".join(out)