from operator import index
import numpy as np
import pandas as pd


def main():
    labels = ['a', 'b', 'c']
    my_list = [10, 20, 30]
    arr = np.array([10, 20, 30])
    d = {'a':10, 'b':20, 'c':30}

    print("Basic:")
    pandas_series = pd.Series(my_list,index=labels)
    print(pandas_series)
    print(f"With label: {pandas_series['a']}")
    print(f"With index {pandas_series[0]}")
    print("")
    
    print("With dictionary:")
    pandas_series_dictionary = pd.Series(d)
    print(pandas_series_dictionary)
    print(f"With label: {pandas_series_dictionary['a']}")
    print(f"With index {pandas_series_dictionary[0]}")
    print("")

    print("Pandas series is more flexible:")
    pandas_series_functions = pd.Series([print, sum, len])
    print(f"{pandas_series_functions}")

    

if __name__ == "__main__":
    main()