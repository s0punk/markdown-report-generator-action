from os import listdir


class CollectionInsertStrategy:
    def insert(content: str, collection_path: str, insert_index: int) -> str:
        pass

class HorizontalTableStrategy(CollectionInsertStrategy):
    def insert(content: str, collection_path: str, insert_index: int) -> str:
        pass

class TableStrategy(CollectionInsertStrategy):
    def insert(content: str, collection_path: str, insert_index: int) -> str:
        pass

class RawStrategy(CollectionInsertStrategy):
    def insert(content: str, collection_path: str, insert_index: int) -> str:
        return content

def read_collection(path):
    files = [e for e in listdir(path) if True or isfile(join(path, e)) and e.endswith(".md")]
    print(f"Found {len(files)} files in collection {path}")

    contents = []

    for f in files:
        try:
            with open(path, 'r', encoding='utf-8') as file:
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