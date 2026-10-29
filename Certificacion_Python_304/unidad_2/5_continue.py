for contador in range(1,11):
   #1. contador1 1 % 2 ==0 -->si lo imprime
   #2. contador2 2 % 2 ==0 -->no lo imprime
   #2. contador3 3 % 2 == 0 -->si lo imprime 
   #2. contador4 4 % 4 ==0  -->si lo imprime
    if contador % 2 != 0:
        continue
    print(contador)