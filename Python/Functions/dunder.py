def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)

def generate_bill(chai=0, samosa=0):
    """
    Docstring for generate_bill
    
    :param chai: Description
    :param samosa: Description
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting chaicode.com"