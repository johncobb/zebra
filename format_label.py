f = open("template", "r")

data = f.read()

data = data.replace("{vin}", "WAULF78K59N031106")
data = data.replace("{year}", "2016")
data = data.replace("{make}", "TOYOTA")
data = data.replace("{model}", "RAV 4")
data = data.replace("{color}", "METALLIC SILVER")
data = data.replace("{stock}", "8371AD3A")
data = data.replace("{mileage}", "35,630 MILES")
data = data.replace("{entry_date}", "JAN 05")





print(data)