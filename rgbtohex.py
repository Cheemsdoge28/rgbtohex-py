def dectohex(decinput):
	hexchars="0123456789abcdef"
	hexoutput=""
	
	while decinput>0:
		remainder=decinput%16
		hexoutput+=hexchars[remainder]
		decinput//=16
	return hexoutput

while 1:
	r=int(input("R:"))
	g=int(input("G:"))
	b=int(input("B:"))
	if (r or g or b)>255:
		print("Enter valid values below 255!")
		continue
	else :
		rhex=dectohex(r)
		ghex=dectohex(g)
		bhex=dectohex(b)
		finalhex="#"+rhex+ghex+bhex
		print(f"Your RGB value {r},{g},{b}, is {finalhex} in hex")

	