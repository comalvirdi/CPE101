def main():
	print(func([[90,90,80,90],[90,60,80,90],[90,60,80,90],[90,60,80,90]]))


def func(l1, val =60):
	res = []
	for x in l1:
		p = True
		for y in x:
			if y<val:
				p = False
				break
		res.append(p)
	return res

if __name__ == '__main__':
   main()