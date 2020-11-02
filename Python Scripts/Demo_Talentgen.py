t15 = ["NaN", "Dls", "BBs", "DSt"]
t25 = ["NaN", "DCa", "PSi", "Dom"]
t35 = ["NaN", "FtS", "SSt", "SVF"]
t45 = ["NaN", "SoC", "InD", "GFg"]
t50 = ["NaN", "SaS", "DCn", "NeP"]

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            for l in range(1,4):
                for m in range(1,4):
                    print(f"profileset.{t15[i]}_{t25[j]}_{t35[k]}_{t45[l]}_{t50[m]}=talents={i}{j}0{k}0{l}{m}")
