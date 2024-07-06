import pandas as pd
var=pd.DataFrame({"A":[2,3,4,5],"B":[2,7,4,9]})
var.pop("B")
print(var)