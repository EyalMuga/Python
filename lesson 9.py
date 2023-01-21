import pprint
import json


class EBook:

    def __init__(self, book_path: str, words_num: int):
        self.book_path = book_path
        self.words_num = words_num
        self.pages: dict[int:str] = {}

        with open(book_path, 'r') as f:
            content = f.read()

        all_words: list[str] = content.split()
        number_page = 1
        for i in range(0, len(all_words), words_num):
            page_words = all_words[i: i + words_num]
            self.pages[number_page] = " ".join(page_words)
            number_page += 1

    def get_total_pages(self):
        return len(self.pages)

    def get_page_content(self, page_number) -> str:
        if page_number not in self.pages:
            return None
        else:
            return self.pages[page_number]


new_book = EBook('/Users/MUGA/PycharmProjects/EDULABS/edulabs excercises/Classes practise/eyal', 47)
print(new_book.get_total_pages())
print(new_book.get_page_content(1))
# pprint.pprint(new_book.pages)
pprint.pprint(new_book.__dict__)

