import pandas as pd
var=pd.DataFrame({"A":[2,3,4,5],"B":[2,7,4,9]})
var.insert(0,"Python",[11,12,13,14])
print(var)
int(input("Press Enter to continue..."))