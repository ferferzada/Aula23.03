x = [
    {"x": 10, "y": 2, "z":1},
    {"x": 6, "y": 30, "z":15},
    {"x": 5, "y": 20, "z":-1},
    {"x": 5, "y": 3, "z":5},
    {"x": 3, "y": 13, "z":8}
    ]

for i in range(len(x)):
    if x[i]["x"] > x[i]["y"] ** 2 or x[i]["z"] < 0:
        print(f"{x[i]}',A'")
    elif x[i]["z"] !=  x[i]["y"] and x[i]["x"] % 2 == 0:
        print(f"{x[i]} ,'B'")
    elif x[i]["z"] > x[i]["x"] and x[i]["y"] // x[i]["x"] > 3:
        print(f"{x[i]} ,'C'")
    else:
        print(f"{x[i]} ,'D'")


