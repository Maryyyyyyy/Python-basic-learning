# System already have defined invoice(). It takes the invoice number as argument and outputs it. 
# Add a decorator for the invoice() that will print the invoice in specific format

def decor(func):
    def star(num):
        print("***")
        func(num)
        """the func must have argument input, or the later main function cannot detect argument """
        print("***")
        print("END OF PAGE")
    return star

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(str(input("What is the invoice number?")))

# When decorate a function, note that if the main function has argument input, the decorate have to have argument as well
