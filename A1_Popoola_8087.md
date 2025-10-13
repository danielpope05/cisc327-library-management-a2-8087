Name: Ayobami Popoola
ID: 20418087
Group Number: 3

|function name                | implementation status  |         What is missing?    |
-------------------------------------------------------------------------------
| add_book_to_catalog         |      partial    | The isbn does not have a restriction |
| borrow_book_by_patron       |      partial    | They can borrow more than 5 books |
| return_book_by_patron       |      partial    |  Implementation missing     |
| calculate_late_fee_for_book |      partial    |   Implementation missing    |
| search_books_in_catalog     |      partial    |   Implementation missing    |
| get_patron_status_report   |      partial     |  Implementation missing    |


#SUMMARY
#R1
#test_book_valid_input: adds a book to the catalog. Should work because all fields are correctly filled.
#test_isbn_too_short: tests if an isbn shorter than 13 digits fails because it should
#test_invalid_num_copies: tests if a negative number of total copies fails
#test_title_missin: tests if a missing title leads to an error
#test_add_book_invalid_author_missing: tests is a blank author leads to an error
# test_borrow_valid: Tests borrowing a book with a valid input in all fields. Should be true.
# test_invalid_book_id: Tests if i can borrow a book with an invalid book id. Book is non-existent so it should not work.
# test_invalid_patron_id: Tests borrowing a book with an invalid patron id. Patron is non-existent so it should not work.
# test_borrow_invalid_unavailable_book: Tests if i can borrow a book with no copies available.
 # test_book_return_valid: patron tries to return a book borrowed. should return true
 # test_invalid_patron_id: patron id is not 6 digits and cannot return a book. patron could be non-existent
 # test_invalid_book_id: patron tries to return a book but the book id is invalid
 # test_not_borrowed: patron tries retruning a book they did not borrow.
 #test_invalid_patron_id: Tests if fee can be calculated for a patron with invalid id.
 # test_invalid_book: Tests if fee can be calculated for a book with an invalid id.
    #test_status: tests if a valid patron and book id can return the status
    # test_days_overdue: Tests if a valid patron and book can return the number of days overdue
#test_valid_search_book(): Search for a title "1984" 
# test_valid_search_isbn(): Search for a book with a specific ISBN number
# test_invalid_search_input(): searching for criterias that have nothing to do with books and are not included in the catalog
#test_valid_author_partial_search_case_sensitive(): testing te search mechanism by searching for an author with a partial name.
# test_invalid_patron_id: test getting patron status with invalid character in patron id
# test_invalid_late_fees(): test if late fees is an integer and not a negative one showing an error in calculations
# test_no_patron_id(): Tests if a blank patron id is handled
# test_num_current_borrowed(): test if the number of currently borrowed books is existent and an integer

