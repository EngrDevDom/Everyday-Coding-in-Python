layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"
print(layout.format("x*y", "I", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
print("----------------------------------------------------")
for i in range(0, 11):
    print(layout.format(i, 'I', i*0, i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10 ))

