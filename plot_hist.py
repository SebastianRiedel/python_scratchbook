def plot_hist(X, yerr=None, ylim=None, title='', axes=None, figure=None):  
  """
  yerr, first dimension == len(X), second dimension mins, third maxs
  """

  # create axes of correct type if necessary
  if axes is None:
    print 'axes none'
    if figure is None:
      print 'figure none'
      figure = plt.figure()
    axes = figure.add_subplot(111)
  elif isinstance(axes, Axes3D):
    print 'axes wrong type'
    if axes.figure is None:
      if figure is None:
        print 'figure none'
        figure = plt.figure()
    else:
      figure = axes.figure
    figure.clear()
    axes = figure.add_subplot(111)

  axes.clear()
  axes.set_title(title)

  colors = ['0.90', 'r', 'g', 'b']

  n_hists = len(X)
  N = len(X[0]) # number bars per hist
  width = 0.8 / n_hists

  rects_list = []
  for i, hist in enumerate(X):
    if yerr is not None:
      rects = axes.bar(np.arange(N) + i*width, hist, width, yerr=yerr[i], ecolor='k', color=colors[i%4])
    else:
      rects = axes.bar(np.arange(N) + i*width, hist, width, color=colors[i%4])
    rects_list.append(rects) 

  axes.set_xticks(np.arange(N) + width*n_hists / 2.0)
  axes.set_xticklabels( [str(i) for i in range(N)] )

  if ylim is not None:
    axes.set_ylim(ylim[0], ylim[1])

  def autolabel(rects):
    # attach some text labels
    for rect in rects:
      height = rect.get_height()
      axes.text(rect.get_x()+rect.get_width()/2., 1.05*height, '{0:.2f}'.format(height),fontsize=8, ha='center', va='bottom')

  for rects in rects_list:
    autolabel(rects)

  if axes.figure.canvas is not None:
    axes.figure.canvas.draw()  
  return figure, axes
