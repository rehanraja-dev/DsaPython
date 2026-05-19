def triangle(rows):
    if rows == 1:
        print("* ")
        return 

    triangle(rows-1)
    print("* "* rows)

print("---Enter the number of rows for printing triangle---")
rows = int(input())
triangle(rows)