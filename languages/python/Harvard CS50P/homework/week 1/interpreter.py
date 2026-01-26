x, y, z = input("Expression: ").split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        ans = float(x + z)
    case "-":
        ans = float(x - z)
    case "*":
        ans = float(x * z)
    case "/":
        ans = float(x / z)
print(f"{ans:.1f}")