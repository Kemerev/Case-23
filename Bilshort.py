import time
def Bubble_sorting1(a): 
   # 1 способ оптимизации метода пузырьковой сортировки
    b = True 
    while(b): 
        b = False 
        for i in range(len(a) - 1): 
            if a[i] > a[i+1]: 
                a[i], a[i+1] = a[i+1], a[i] 
                b = True 
    return a 
a = [5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1, 5, 3, 8, 6, 7, 2, 1] 
print("Исходнные значения: ", a) 
start = time.time()
print("Значения после сортировки: ", Bubble_sorting1(a))
end = time.time()
print(end - start)
# 0.0009996891021728516
