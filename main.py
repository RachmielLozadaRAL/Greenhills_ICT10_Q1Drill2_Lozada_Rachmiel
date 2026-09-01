# Arithmetic Operations
from pyscript import display, document

def adding_numbers(event):
    document.getElementById('1').innerHTML = '' # clear the output
    num1 = float(document.getElementById('num1').value)
    num2 = float(document.getElementById('num2').value)
    total = num1 + num2
    display(f'The sum is: {total}', target='1')

def subtracting_numbers(event):
    document.getElementById('1').innerHTML = '' # clear the output
    num1 = float(document.getElementById('num1').value)
    num2 = float(document.getElementById('num2').value)
    total = num1 - num2
    display(f'The difference is: {total}', target='1')

def multiplying_numbers(event):
    document.getElementById('1').innerHTML = '' # clear the output
    num1 = float(document.getElementById('num1').value)
    num2 = float(document.getElementById('num2').value)
    total = num1 * num2
    display(f'The product is: {total}', target='1')

def dividing_numbers(event):
    document.getElementById('1').innerHTML = '' # clear the output
    num1 = float(document.getElementById('num1').value)
    num2 = float(document.getElementById('num2').value)
    total = num1 / num2
    display(f'The quotient is: {total}', target='1')