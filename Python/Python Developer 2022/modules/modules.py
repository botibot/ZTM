import utility #! import from a module
import shopping.shopping_cart #! import from a package
import random

print(utility)
print(utility.multiply(1,2))
print(shopping.shopping_cart.buy("apple"))

print(__name__)

if __name__ == '__main__':
    print('please run this')

print(random)