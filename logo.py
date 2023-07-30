def logo():
    f = open('logo.txt', 'r')
    show_logo = f.read()
    print(show_logo)
    f.close()