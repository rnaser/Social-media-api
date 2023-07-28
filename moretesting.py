from csv import writer
f = open('C:/Users/rami/Desktop/test/test.txt', 'a')
writer_object = writer(f)
f = open('C:/Users/rami/Desktop/test/test.txt', 'r')
ExportedTxt = f.readlines()
p =0
#for p in ExportedTxt:
 #   if int(ExportedTxt[p].len) < 2:
  #      ExportedTxt.remove[p]
x=int(len(ExportedTxt[p]))
print(x)