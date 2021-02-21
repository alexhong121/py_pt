fout=open('oops.txt','wt')
print('oops, i created a file',file=fout)
fout.close()


fin=open('oops.txt','rt')
po=fin.read()
fin.close()
print(po)