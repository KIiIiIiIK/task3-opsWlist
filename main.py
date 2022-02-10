src1 = [23, "23", 12, 'src', 2*2, 2.2, "null", 10, '10', 'perform']

separateListFrom = src1[1:5]  # making separate list from src1
print(separateListFrom)

src2 = ['2.1', 1*10, 77, "empty", "33"]

src1.extend(src2[2:4])  # adding items from src2 to src1
print(src1)

print(src1+src2)  # merging src1 & src2

print((src1+src2)*5)  # duplicating merged list

print()
# ------------------------------------------------------tuples------------------------------------------------------

src1 = (23, "23", 12, 'src', 2*2, 2.2, "null", 10, '10', 'perform')

separateListFrom = src1[1:5]
print(separateListFrom)

src2 = ('2.1', 1*10, 77, "empty", "33")

# src1.extend(src2[2:4]) doesn't work with tuples

print(src1+src2)

print((src1+src2)*5)

