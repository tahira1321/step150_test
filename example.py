print("hello world")

def  greet(str):
  print(str)
greet("こんにちは")

def print_name(name):
  print(f"私の名前は{name}です")
print_name("takuya")

def get_greet(greet):
  return greet
aisatu = get_greet("おはようございます")
print(aisatu)

def add(a, b):
  return a + b
sum = add(4, 6)
print(sum)