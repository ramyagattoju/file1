
def get_initials(full_name):
    """given a person's name, return the persons initials(upper case"""
    
    name = full_name.split()
    init = ''
    
    for a_name in name:
        init.upper()
        init = init + a_name[0]
        init = init.upper()
    return init

def main():
    name = input("what is your name")
    print(get_initials(name))
if __name__ == "__main__":
    main()