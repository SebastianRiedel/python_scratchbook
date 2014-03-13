# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from mayavi import mlab
import numpy as np


def gen_random_quaternions(n):
  q = np.random.rand(n,4)
  norm = np.linalg.norm(q, axis=1)
  q_unit = q / norm[:,None]
  return q_unit

def plot_quaternions(q):
  angles = 2 * np.arccos(q[:,0])
  angles =  angles + 0.000001
  axis = q[:,1:4] / np.sin(0.5 * angles)[:,None]

  s = angles / (2 * np.pi)
  mode='sphere'
  if len(s) > 5000:
    mode = '2dcross'

  mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(640, 480))
  mlab.clf()
  glyph = mlab.points3d(axis[:,0], axis[:,1], axis[:,2], s, mode=mode, scale_factor=0.02, scale_mode='none', vmin=0.0, vmax=1.0)
  # glyph = mlab.quiver3d(axis[:,0], axis[:,1], axis[:,2], axis[:,0], axis[:,1], axis[:,2], scalars=s, mode='2dcircle', line_width=3, scale_factor=0.02, scale_mode='none')
  glyph.actor.property.lighting = False

  sphere = make_sphere()
  mlab.mesh(sphere[0], sphere[1], sphere[2], scalars=np.zeros(sphere[0].shape), colormap='jet', opacity=0.1)
  mlab.show(stop=True)

def make_sphere(subdivision=50, radius=1.0):
  # Create a sphere
  r = 1.0
  pi = np.pi
  cos = np.cos
  sin = np.sin
  phi, theta = np.mgrid[0:pi:50j, 0:2 * pi:100j]

  x = r * sin(phi) * cos(theta)
  y = r * sin(phi) * sin(theta)
  z = r * cos(phi)
  return x,y,z

def plot_alpha_sphere():
  x,y,z = make_sphere(50, 1.0)

  mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
  mlab.clf()

  s = np.zeros(x.shape)
  mlab.mesh(x, y, z, scalars=s, colormap='jet', opacity=0.1)
  mlab.show(stop=True)