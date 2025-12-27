def sum_numbers_from_strings(strings):
    try:
        #розділ.за комами
        parts = s.split(',')
        #перетвор. кожен єл. у число
        numbers = [int(p) for p in parts]
        return sum(numbers)
    except:
        return 0

    #масив зі строками
    data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

    #обробка масиву
    for item in data:
        print(sum_numbers_from_strings(item))
        