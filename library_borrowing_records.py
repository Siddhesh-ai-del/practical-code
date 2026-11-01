# Python Program: Library Book Borrowing Records


def average_borrowings(borrow_counts):
    total = 0

    for count in borrow_counts:
        total = total + count

    average = total / len(borrow_counts)

    return average


def highest_borrowing(borrow_counts):
    highest = borrow_counts[0]

    for count in borrow_counts:
        if count > highest:
            highest = count

    return highest


def lowest_borrowing(borrow_counts):
    lowest = borrow_counts[0]

    for count in borrow_counts:
        if count < lowest:
            lowest = count

    return lowest


def count_zero_borrowings(borrow_counts):
    count_zero = 0

    for count in borrow_counts:
        if count == 0:
            count_zero = count_zero + 1

    return count_zero


def mode_borrowing(borrow_counts):
    mode = borrow_counts[0]
    highest_frequency = 0

    for i in range(len(borrow_counts)):
        frequency = 0

        for j in range(len(borrow_counts)):
            if borrow_counts[i] == borrow_counts[j]:
                frequency = frequency + 1

        if frequency > highest_frequency:
            highest_frequency = frequency
            mode = borrow_counts[i]

    return mode


def main():
    borrow_counts = list(
        map(int, input("Enter borrowing counts: ").replace(",", " ").split())
    )

    print("\n--- Library Borrowing Records ---")

    print("Average number of books borrowed:", average_borrowings(borrow_counts))
    print("Highest number of borrowings:", highest_borrowing(borrow_counts))
    print("Lowest number of borrowings:", lowest_borrowing(borrow_counts))
    print("Members who borrowed 0 books:", count_zero_borrowings(borrow_counts))
    print("Most frequently borrowed count:", mode_borrowing(borrow_counts))


if __name__ == "__main__":
    main()
