t15 = ["NaN", "Nfl", "InD", "DrS"]
t25 = ["NaN", "WiA", "AbC", "SiL"]
t35 = ["NaN", "StS", "PhS", "ViT"]
t45 = ["NaN", "DkC", "Hnt", "GrS"]
t50 = ["NaN", "SoC", "CrD", "DSM"]

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            for l in range(1,4):
                for m in range(1,4):
                    print(f"profileset.{t15[i]}_{t25[j]}_{t35[k]}_{t45[l]}_{t50[m]}=talents={i}0{j}{k}0{l}{m}")
