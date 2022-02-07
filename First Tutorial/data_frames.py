from traceback import print_tb
import numpy as np
import pandas as pd


def main():
    rows = ['X','Y','Z']
    cols = ['A', 'B', 'C', 'D', 'E']
    data = np.round(np.random.randn(3,5),2)
    my_data_frame = pd.DataFrame(data,rows,cols)
    print(my_data_frame)
    print("")
    print("Getting data")
    print(my_data_frame["E"])
    print(my_data_frame[['A','E']])
    print(my_data_frame["A"]["Y"])
    print("")
    print("Creating and removing columns")
    my_data_frame['A + B'] = my_data_frame['A'] + my_data_frame['B']
    print(my_data_frame)
    #dele columns
    #my_data_frame = my_data_frame.drop("A + B",axis=1)
    #automatically overwrites
    #my_data_frame.drop("A+B",axis=1,inplace=True)
    my_data_frame = my_data_frame.drop("Z")
    print(my_data_frame)
    #select a specific column
    print(my_data_frame.loc['X'])
    #rows with index
    print(my_data_frame.iloc[0])
    #Determine number of rows and columns
    print(f"Rows and columns: {my_data_frame.shape}")


if __name__ == "__main__":
    main()