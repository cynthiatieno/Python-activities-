from datetime import datetime

# calculating the fine
def calculate_fine(bookID, dueDate, returnDate):

    due_date = datetime.strptime(dueDate, "%Y-%m-%d")
    return_date = datetime.strptime(returnDate, "%Y-%m-%d")
    
    # Calculating the number of days overdue
    days_overdue = (return_date - due_date).days
    
    
    if days_overdue <= 0:
        fine_rate = 0
        fine_amount = 0
    else:
    
        if days_overdue <= 7:
            fine_rate = 20
        elif days_overdue <= 14:
            fine_rate = 50
        else:
            fine_rate = 100
        
        # Calculating total fine 
        fine_amount = fine_rate * days_overdue
    
    
    print(f"Book ID: {bookID}")
    print(f"Due Date: {dueDate}")
    print(f"Return Date: {returnDate}")
    print(f"Days Overdue: {days_overdue}")
    print(f"Fine Rate: Ksh. {fine_rate}")
    print(f"Total Fine Amount: Ksh. {fine_amount}")


def main():
    #  inputs from the user
    bookID = input("Enter Book ID: ")
    dueDate = input("Enter Due Date (YYYY-MM-DD): ")
    returnDate = input("Enter Return Date (YYYY-MM-DD): ")
    
    # displaying the fine details
    calculate_fine(bookID, dueDate, returnDate)


if __name__ == "__main__":
    main()
