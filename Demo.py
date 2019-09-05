import pandas as pd
import matplotlib.pyplot as plt

def demo_hubble():
    data = pd.read_csv("hubble_data.csv")
    # print(data.head(), '\n')

    headers = ["dist", "rec_vel"]
    data_no_headers = pd.read_csv("hubble_data_no_headers.csv", names=headers)
    # print(data_no_headers.head(), '\n')

    # print(data_no_headers["dist"])

    data.set_index("distance", inplace= True)   # OR:P1 was: distance chg to recession_velocity
    print(data.head(), '\n')

    data = pd.read_csv("hubble_data.csv")
    data.set_index("recession_velocity", inplace= True)
    print(data.head(), '\n')

    print(data.axes, '\n')
    print(data.columns, '\n')
    print(data.index, '\n')
    print(data.values, '\n')

    # data.plot()
    # plt.show()

def demo_xacs():
    data = pd.read_csv('transaction_list.csv')
    print(data)
    print(data.head())
    print (data['Time']) #  [4])

def main():
    # demo_hubble()
    demo_xacs()

if __name__ == '__main__':
    main()