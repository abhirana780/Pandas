import pandas as pd
var=pd.DataFrame({"A":[2,3,4,5],"B":[2,3,4,5]})
var["A*B"]=var["A"]*var["B"]
var["A+B"]=var["A"]+var["B"]
print(var)
