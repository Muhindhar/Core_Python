'''try:
    num = int(input("Enter the number : "))
    if(num<0):
        raise ValueError("This is negative number")
except ValueError as e:
    print(e)
    '''
import traceback

try:
    num = int(input("Enter the number : "))

    if num < 0:
        raise ValueError("Negative number is not allowed")

except Exception as e:

    print("Exception Type :", type(e))
    print("Exception Args :", e.args)
    print("Exception Message :", str(e))
    print("Representation :", repr(e))

    print("\nDetailed Traceback:")
    traceback.print_exc()