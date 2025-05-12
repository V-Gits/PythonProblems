class Example:
    def __init__(self):
        self.public_var = "Iam Public"
        self._protected_var = "Iam Protected"
        self.__private_var = "Iam Private"

    def show_vars(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)
    
def main():
    obj = Example()
    print(obj.public_var)
    print(obj._protected_var)
    #print(obj.__private_var)
    obj.show_vars()

if __name__ == "__main__":
    main()