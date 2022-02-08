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
    print("")
    #Slicing Data frames
    print(my_data_frame[["A","B"]].loc[["X","Y"]])
    print("")
    #Items bigger than element
    print(my_data_frame > 4)
    print("")
    #If the values not bigger than number then NaN will it be the value
    print(my_data_frame[my_data_frame > 0.5])
    print("")
    #The same thing for columns
    print(my_data_frame["C"]<1)
    print("")
    #The same thing for rows
    print(my_data_frame[my_data_frame["C"]<1])
    print("")
    #We can use both at the same time
    print(my_data_frame[(my_data_frame['C'] > 0) & (my_data_frame['A']> 0)])
    print("")
    
    #Modify index
    print(my_data_frame.reset_index())
    print("")
    print(my_data_frame.set_index("A"))

    #Rename Columns
    print(my_data_frame.columns)
    my_data_frame.columns = [1, 2, 3, 4, 5, 6]
    print(my_data_frame)


if __name__ == "__main__":
    main()