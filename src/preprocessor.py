from os import listdir
from os.path import isfile
from file_insert_strategy import *

def preprocess_file(content):
    content = find_subcollections(content)

    # Format lists.
    
    return content

def find_subcollections(content):
    include_index = content.find("<!-- include:files")
    while include_index != -1:
        include_block = content[include_index:content.find("-->", include_index) + 3]
        
        if "\n" in include_block:
            break

        path_index = include_block.find("path=\"")
        if path_index != -1:
            path = include_block[path_index + 6:include_block.find("\"", path_index + 6)]
            
            strat_index = include_block.find("insert=\"")
            if strat_index != -1:
                strat = include_block[strat_index + 8:include_block.find("\"", strat_index + 8)]
            else:
                strat = ""

            match strat:
                case "h-table":
                    insert_strategy = HorizontalTableStrategy()
                case "table":
                    insert_strategy = TableStrategy()
                    pass
                case _:
                    insert_strategy = RawStrategy()
            
            content = read_subcollection(content, path, insert_strategy)

        include_index = content.find("<!-- include:files", include_index + 1)

    return content

def read_subcollection(content, path: str, insert_strategy: FileInsertStrategy):
    files = [e for e in listdir(path) if isfile(e) and e.endswith(".md")]
    print(f"Found {len(files)} files in collection {path}")

    return content