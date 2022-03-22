class Document(object):
    def __init__(self, id_document: int, title: str = "title", number_page: str = "number", category: str = "category",
                 author: str = "author"):
        self.author = author
        self.category = category
        self.number_page = number_page
        self.title = title
        self.id_document = id_document

    @property
    def id_document(self) -> int:
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        self._id_document = id_document

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def number_page(self) -> str:
        return self._number_page

    @number_page.setter
    def number_page(self, number_page: str):
        self._number_page = number_page

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str):
        self._author = author

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_document, self.title, self.number_page, self.category, self.author)


if __name__ == '__main__':
    edwin = Document(id_document=123, title="undo", number_page="23", author="carlos")
    print(edwin)