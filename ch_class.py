#number = (1,2,3,4,5)
#odd= (1,3,5,7,9)
#def test_pytest_case():
  #  print()
   # assert # 2 in number

    #assert #0  in numbers
    #assert number[2] in odd
  

#list =  (('Apple', 'Banana', 'Pork'))
#assert list is orderd

numbers = (1,2,3,4,5)
odd = (1,3,5,7,9)

def test_number_in_list_case():
    print()
    assert 2 in numbers # 1 Number is in a list

def test_zero_flase_case():
    assert False == 0

def test_number_is_odd_case():
    num = 12
    assert (num % 2) == 0

def test_list_is_ordered_case():
    assert all(numbers[i] <= numbers[i+1] for i in range(len(numbers)- 1))

def test_list_is_set_case():
    assert len(odd) == len(set(odd))

def truefunction(num1, num2):
    return num1 > num2

def test_true_function_case():
    assert truefunction(23,12)





