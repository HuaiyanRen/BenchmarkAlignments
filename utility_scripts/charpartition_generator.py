# a little script to generate charpartitions from files of charsets
filename = r"C:\Users\u7151703\Desktop\sets.nex"

charsets = open(filename, 'r').readlines()

names = [s.split("=")[0].split("charset")[1].strip() for s in charsets]

parts = []
for i, n in enumerate(names):
    print(i, n)
    part = ''.join([str(i+1), ":", n, ","])
    parts.append(part)

charpartition = ' '.join(parts)
charpartition = charpartition.rstrip(",")

charpartition = ''.join([charpartition, ";"])

print(charpartition)