class FileInsertStrategy:
    def insert(content: str) -> str:
        pass

class HorizontalTableStrategy(FileInsertStrategy):
    def insert(content: str) -> str:
        pass

class TableStrategy(FileInsertStrategy):
    def insert(content: str) -> str:
        pass

class RawStrategy(FileInsertStrategy):
    def insert(content: str) -> str:
        return content
    
def parse_headers(content):
    headers = []

    for line in content.split("\n"):
        if "## " in line:
            headers.append(line.replace("## ", ""))
    
    return headers