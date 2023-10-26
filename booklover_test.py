import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in book_list.
        human = BookLover("Mohammad", "mbf4ay@virginia.edu", "fiction")
        testBookName = "Good Book"
        testRating = 5
        human.add_book(testBookName, testRating)
        self.assertTrue(human.has_read(testBookName))

    def test_2_add_book(self):
        # add the same book twice. Test it's in book_list only once.
        human = BookLover("Mohammad", "mbf4ay@virginia.edu", "fiction")
        testBookName = "Good Book"
        testRating = 5
        human.add_book(testBookName, testRating)
        human.add_book(testBookName, testRating)
        expected = 1
        actual = len(human.book_list[human.book_list.book_name == testBookName])
        self.assertEqual(expected, actual)
        
    def test_3_has_read(self): 
        # pass a book in the list and test the answer is True.   
        human = BookLover("Mohammad", "mbf4ay@virginia.edu", "fiction")
        testBookName = "Good Book"
        testRating = 5
        human.add_book(testBookName, testRating)
        self.assertTrue(human.has_read(testBookName))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use assert False to test if the answer is True.
        human = BookLover("Mohammad", "mbf4ay@virginia.edu", "fiction")
        testBookName = "Bad Book"
        self.assertFalse(human.has_read(testBookName))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        human = BookLover("Mohammad", "mbf4ay@virginia.edu", "fiction")
        testBooks = [("Good Book", 5), ("Mid Book", 3), ("Bad Book", 1)]
        for book in testBooks:
            human.add_book(*book)

        expected = len(testBooks)
        actual = human.num_books_read() 
        self.assertEqual(expected, actual)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # your test should check that the returned books have rating > 3.
        human = BookLover("Mohammad", "mbf4ay@virginia.edu", "fiction")
        testBooks = [("Good Book", 5), ("Mid Book", 3), ("Bad Book", 1)]
        for book in testBooks:
            human.add_book(*book)

        expected = len([x for x , y in testBooks if y > 3])
        actual = len(human.fav_books())
        self.assertEqual(actual, expected)
              
if __name__ == '__main__':
    
    unittest.main(verbosity=3)