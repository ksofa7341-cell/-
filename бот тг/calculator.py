def c(num1,num2,m ): 
     
    if m == '+':
        print('сложение')
        result=num1+num2
    elif  m == '-':
        print('вычитание')
        result=num1-num2
    elif  m == '/':
        print('деление')
        result=num1/num2
    elif  m == '*':
        print('умножение')
        result=num1*num2
    else:
        result=("Неизвестная функция")

    return result  
         