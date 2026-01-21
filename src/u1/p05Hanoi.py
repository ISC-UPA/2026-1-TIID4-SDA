import os


def hanoi(n, f, to, via):
    global contador
    
    if n == 1:
        contador += 1
        print(contador, "Move disk 1 from",f,"to",to)
    else:
        hanoi(n-1, f, via, to)                          # step 1
        contador += 1
        print(contador ,"Move disk",n,"from",f,"to",to) # step 2
        hanoi(n-1, via, to, f)                          # step 3

os.system('cls')
contador = 0
n = 3
f = '1'
to = '2'
via = '3'
hanoi(n, f, to, via)
print("Total movimientos:", contador, "(esperado:", 2**n - 1, ")")

'''
Step 1 − Move n-1 disks from source to aux
Step 2 − Move nth disk from source to dest
Step 3 − Move n-1 disks from aux to dest

Procedure Hanoi(disk, source, dest, aux)

   IF disk == 1, THEN
      move disk from source to dest             
   ELSE
      Hanoi(disk - 1, source, aux, dest)     // Step 1
      move disk from source to dest          // Step 2
      Hanoi(disk - 1, aux, dest, source)     // Step 3
   END IF
   
END Procedure

'''
