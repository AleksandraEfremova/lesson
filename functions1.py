def get_summ(one, two, delimiter='&'):
    one=str(one).upper()
    two=str(two).upper()
    return one+delimiter+two
    
    
print(get_summ('learn', 'pyhton'))