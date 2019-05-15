sh=input("enter hours:")
sr=input("enter rate:")
fh=float(sh)
fr=float(sr)
if fh>40:
    #print("overtime")
    reg=fr*fh
    otp=(fh-40.0)*(fr*0.5)
    xp=reg+otp
else:
    xp=fr*fh
    #print("regular")

print("Pay:", xp)
