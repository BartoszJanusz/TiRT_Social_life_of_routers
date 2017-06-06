import matplotlib.pyplot as plt

# data - list of two element tuples - name and data series
# prop - plot properties (color, type)
# labels - title, xlabel, ylabel


def plot(data, prop, labels):
    plt.figure()
    ax = plt.subplot(111)
    plt.title(labels[0])
    plt.xlabel(labels[1])
    plt.ylabel(labels[2])

    for i, d in enumerate(data):
        plt.plot(d[1], prop[i], ms=2.0, label=d[0])

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), markerscale=3)
    plt.show(block=False)
