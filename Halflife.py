caffeine = float(input("How many milligrams of caffeine is in your drink? "))

def halflife(caffeine):
  return caffeine / 2


print("After 6 hours, the caffeine level is ", float(halflife(caffeine)), "mg")
caffeine = halflife(caffeine)

print("After 12 hours, the caffeine level is ", float(halflife(caffeine)), "mg")
caffeine = halflife(caffeine)

print("After 18 hours, the caffeine level is ", float(halflife(caffeine)), "mg")
caffeine = halflife(caffeine)
