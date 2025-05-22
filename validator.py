import re


def product_validator(product):
    errors = []
    if not (type(product[0]) == int and product[0]>0):
        errors.append('Product ID must be an integer > 0')

    if not (type(product[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", product[1])):
        errors.append('Product Name is Invalid')


    if not (type(product[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", product[2])):
        errors.append('Product brand is Invalid')

    if not (type(product[3]) == int and product[3]>0):
        errors.append('buy price must be an integer > 0')

    if not (type(product[4]) == int and product[4]>0):
        errors.append('selling price  must be an integer > 0')

    if not (type(product[5]) == int and product[5]>0):
        errors.append('quantity  must be an integer > 0')

    return errors


