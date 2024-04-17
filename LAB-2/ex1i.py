length =int(input("Enter length: "))
width =int(input("Enter width: "))
depth =int(input("Enter depth: "))
Vol = length*depth*width
print(Vol)
if Vol>=1 and Vol<=10:
    label = "Extra Small"
elif Vol>=11 and Vol<=25:
    label = "Small"
elif Vol>=26 and Vol<=75:
    label = "Medium"
elif Vol>=76 and Vol<=100:
    label = "Large"
elif Vol>=101 and Vol<=250:
    label = "Extra Large"
else:
    label = "Extra-Extra Large"

print(label)
