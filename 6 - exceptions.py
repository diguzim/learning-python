try:
  resultado = 10 / 0
except ZeroDivisionError:
  print("You can't divide by zero!")
except Exception as e:
  print(f"Unknown error: {e}")
else:
  print("Everything went OK!")
finally:
  print("I always run no matter what!")

class MyCustomError(Exception):
  pass

try:
  raise MyCustomError("Something went wrong")
except MyCustomError as e:
  print(f"My custom error: {e}")