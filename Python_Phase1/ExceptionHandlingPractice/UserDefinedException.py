class Error(Exception):
    pass
class ValueTooSmall(Error):
    pass
class valueTooLarge(Error):
    pass

num=int(input("Enter the value : "))
try:
    if num<10:
        raise ValueTooSmall
    elif num>20:
        raise valueTooLarge
    else:
        raise Error
except ValueTooSmall as e:
    print("Value too small  ",e)
except valueTooLarge as e:
    print("Value too large  ",e)
except Error as e:
    print("Not a correct value  ",e)
finally:
    print("Compiled")