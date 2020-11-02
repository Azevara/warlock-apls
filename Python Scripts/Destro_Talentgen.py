t15 = ["NaN", "Flo", "Erd", "SFr"]
t25 = ["NaN", "RvE", "InC", "Sbr"]
t35 = ["NaN", "Inf", "FnB", "Cat"]
t45 = ["NaN", "RoB", "RoC", "GrS"]
t50 = ["NaN", "SoC", "CDf", "DSI"]

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            for l in range(1,4):
                for m in range(1,4):
                    print(f"profileset.{t15[i]}_{t25[j]}_{t35[k]}_{t45[l]}_{t50[m]}=talents={i}{j}0{k}0{l}{m}")
