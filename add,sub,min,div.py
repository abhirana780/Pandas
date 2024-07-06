import pandas as pd
var=pd.DataFrame({"A":[2,3,4,5],"B":[2,7,4,9]})
var["A+B"]=var["A"]+var["B"]
var["B-A"]=var["B"]-var["A"]
var["A*B"]=var["A"]*var["B"]
var["B/A"]=var["B"]/var["A"]
print(var)