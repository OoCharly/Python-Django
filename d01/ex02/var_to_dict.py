def var_to_dict():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925')
    ]

    for dict in d:
        print(dict[1]+" : "+dict[0])

if __name__ == '__main__':
    var_to_dict()