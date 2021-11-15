import matplotlib.pyplot as plt

def two_subplot(x,y,x2,y2):

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    axes[0].plot(x, y)
    axes[1].plot(x2, y2)
# x = x value of dataset 1
# y = y value of dataset 1
# x2 = x value of dataset 2
# y2 = y value of dataset 2
