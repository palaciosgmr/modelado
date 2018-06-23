import pandas as pd
import numpy as np



def main():
    with open('../resources/v4test.csv') as csvfile:

        df = pd.read_csv(csvfile)


if __name__ == "__main__":
    main()
