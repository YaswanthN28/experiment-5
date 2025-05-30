class book:
    def __init__(self,title):
        self.title=title
def create_book_list():
    return[book("python 101"),book("ai basics"),book("data science")]
book=create_book_list()
for b in book:
    print("book title",b.title)
        
