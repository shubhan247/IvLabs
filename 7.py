text = "X-DSPAM-Confidence:    0.8475";
i=text.find(':')
str=text[i+2:]
value=float(str)
print(value)
