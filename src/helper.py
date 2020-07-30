def PlotPointCloud(xyz):
    from mpl_toolkits.mplot3d import Axes3D 
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], c=xyz[:, -1])
    ax.set_xlim3d(0, 10)
    ax.set_ylim3d(0, 10)
    ax.set_zlim3d(0, 10)

    plt.show()

def PointDistance(p1,p2):
    sum = 0
    for i, v in range(0,2):
        sum += (v-p2[i])**2
    return math.sqrt(sum)

