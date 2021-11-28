def str_sort(str):
    
    str = str.lower()
    str = str.split(' ')
    str = sorted(str, key=len)
    str = " ".join(str)
    str = str.capitalize()

    return str

if __name___=='__main__':
    str = "Keep calm and carry on"
    print(str_sort(str))
