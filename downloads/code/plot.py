import matplotlib
matplotlib.use('PDF')  # if I don't use it, the pdf produced is corrupted?
import matplotlib.pyplot as plt
import numpy as np
from activepapers.contents import data, open_documentation

def plot(x, y, fontsize=19, output='plot.pdf'):
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(1,1,1)

    # data
    ax.plot(x, y, '-', linewidth=2.0, label='normal')

    # legend
    ax.set_xlabel('x', fontsize=fontsize)
    ax.set_ylabel('y', fontsize=fontsize)

    # police
    ax.tick_params(labelsize=fontsize)
    # Add and specify different settings for minor grids
    x_max = x.max()
    ax.set_xticks(np.arange(0.0, x_max+1, 10.0), minor = True)
    y_max = y.max()
    ax.set_yticks(np.arange(0.0, y_max+1, 10.0), minor = True)
    ax.grid(which = 'minor', alpha = 0.9)

#    figure = fig.savefig(output) # cannot do it like that - savefig will be
                                  # the last step
#    return figure
    return fig

# Plotting and saving in documentation
x = data['inputs/dataset_1'][:]
y = data['output/sum'][:]
#p = plot(x, y)
#open_documentation(p, 'w') # cannot use it like that - see solution below
fig = plot(x, y)
fig.savefig(open_documentation('plot.pdf', 'w')) #save plot in /documentation/
