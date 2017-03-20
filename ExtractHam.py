import os
files = os.listdir(r"easy_ham")
with open("dataham.csv","w") as out:
    n = 0
    for fname in files:
	path = os.path.join(os.path.expanduser('~'), 'easy_ham',fname)
        with open(path) as f:
            data = f.readlines()
            for line in  data:
                if line.startswith("Subject:"):
		    line=line.replace(",", "")
		    print(line)
                    n +=1
                    out.write("{0},nospam\n".format(line[8:-1]))
		if n >= 550:
	            break
            print(fname)
