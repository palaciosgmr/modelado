import pandas as pd
with open("v4test.csv", 'r') as csvfile:
    df = pd.read_csv(csvfile)
    print(df)



