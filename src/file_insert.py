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