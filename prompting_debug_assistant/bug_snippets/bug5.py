def manage_books(book_list, action):
    if action == "add":
        new_book = "Clean Code"
        book_list.append(new_book)
    
    # Səhv 1: Siyahıdan silmə zamanı olmayan elementi silməyə çalışmaq (ValueError)
    elif action == "remove":
        book_list.remove("Refactoring")
    
    # Səhv 2: Dövr daxilində siyahının ölçüsünü dəyişmək (Məntiqi xəta)
    for book in book_list:
        if len(book) > 5:
            book_list.pop(0)

    # Səhv 3: 'status' dəyişəni hər iki halda təyin edilməyib
    print("Sistem vəziyyəti: " + status)
    return book_list

library = ["Python 101", "Algorithms"]
manage_books(library, "add")
