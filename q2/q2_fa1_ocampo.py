class Publication:
    
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def set_title(self, title):
        self._title = title
    def get_title(self):
        return f"Title: {self._title}"
    
    def set_author(self, author):
        self._author = author
    def get_author(self):
        return f"Author: {self._author}"
    
    def display_info(self):
        print(self.get_title())
        print(self.get_author())

class Book(Publication):
    number_pages = 0
    def __init__(self, title, author, number_pages):
        self._title = title
        self._author = author
        self._number_pages = number_pages
    
    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self._number_pages = number_pages
        else:
            print("Number of pages must be positive.")
            return
    def get_number_of_pages(self):
        return f"Number of pages: {self._number_pages}"

class Magazine(Publication):
    issue_number = 0
    def __init__(self, title, author, issue_number):
        self._title = title
        self._author = author
        self._issue_number = issue_number
    
    def set_issue_number(self, issue_number):
        self._issue_number = issue_number
    def get_issue_number(self):
        return f"Issue number: {self._issue_number}"




pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. and Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors",202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
