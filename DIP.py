# class Book():
#     def read(self):
#         print("чтение интересной истории")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()
from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение интересной книги")
class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересной книги вслух")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source
    def tell_story(self):
        self.story_source.get_story()

book = Book()
audiobook = AudioBook()
readerBook = StoryReader(book)
readerAudioBook = StoryReader(audiobook)
readerBook.tell_story()
readerAudioBook.tell_story()
