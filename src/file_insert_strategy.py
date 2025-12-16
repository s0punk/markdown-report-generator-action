class FileInsertStrategy:
    def insert(content: str) -> str:
        pass

class HorizontalTableStrategy(FileInsertStrategy):
    def insert(content: str) -> str:
        pass

class TableStrategy(FileInsertStrategy):
    def insert(content: str) -> str:
        pass
    
def parse_headers(content):
    headers = []

    for line in content.split("\n"):
        if "## " in line:
            headers.append(line.replace("## ", ""))
    
    return headers