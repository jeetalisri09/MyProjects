import argparse

def main(5,2,"add"):
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help = "first number")
    parser.add_argument("number2", help = "first number")
    parser.add_argument("operation", help = "operation")

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)


    #Initialize numbers
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None

    if args.operation == "add":
        result = n1+n2
    elif args.operation == "sub":
        result = n1 - n2
    elif args.operation == "mul":
        result = n1*n2
    
    print(result)

if __name__ == "__main__":
    main()