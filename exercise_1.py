#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#function
def product_or_sum(first_given_number, second_given_number):
    product = first_given_number * second_given_number
    if product <= 1000:
        return product
    else:
        return (first_given_number + second_given_number)

#Given 1
given1_number1 = 20
given1_number2 = 30

#Given 2
given2_number1 = 40
given2_number2 = 30

