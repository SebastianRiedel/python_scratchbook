# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from mayavi import mlab

# To access any VTK object, we use 'tvtk', which is a Python wrapping of
# VTK replacing C++ setters and getters by Python properties and
# converting numpy arrays to VTK arrays when setting data.
from tvtk.api import tvtk
import numpy as np

v = mlab.figure()

# Create a first sphere
# The source generates data points
obj = tvtk.OBJReader()
obj.file_name = '/volume/USERSTORE/ried_sa/data/models/mug.obj'

mesh = obj.output

# The mapper converts them into position in, 3D with optionally color (if
# scalar information is available).
mapper = tvtk.PolyDataMapper(input=mesh)
# The Property will give the parameters of the material.
p = tvtk.Property(opacity=0.2, color=(1, 0, 0))
# The actor is the actually object in the scene.
actor = tvtk.Actor(mapper=mapper, property=p)

t = np.eye(4)
t[0,3] = .4
mat = tvtk.Matrix4x4()
mat.from_array(t)
actor.user_matrix = mat

v.scene.add_actor(actor)

axes = tvtk.AxesActor()
axes.axis_labels = 0
axes.total_length = [0.1, 0.1, 0.1]
v.scene.add_actor(axes)

# # Create a second sphere
# sphere2 = tvtk.SphereSource(center=(7, 0, 1), radius=0.2)
# sphere_mapper2 = tvtk.PolyDataMapper(input=sphere2.output)
# p = tvtk.Property(opacity=0.3, color=(1, 0, 0))
# sphere_actor2 = tvtk.Actor(mapper=sphere_mapper2, property=p)
# v.scene.add_actor(sphere_actor2)

# # Create a line between the two spheres
# line = tvtk.LineSource(point1=(0, 0, 0), point2=(7, 0, 1))
# line_mapper = tvtk.PolyDataMapper(input=line.output)
# line_actor = tvtk.Actor(mapper=line_mapper)
# v.scene.add_actor(line_actor)

# # And display text
# vtext = tvtk.VectorText()
# vtext.text = 'Mayavi'
# text_mapper = tvtk.PolyDataMapper(input=vtext.get_output())
# p2 = tvtk.Property(color=(0, 0.3, 0.3))
# text_actor = tvtk.Follower(mapper=text_mapper, property=p2)
# text_actor.position = (0, 0, 0)
# v.scene.add_actor(text_actor)

# Choose a view angle, and display the figure
# mlab.view(85, -17, 15, [3.5, -0.3, -0.8])
mlab.show(stop=True)

###############################################################################
# import vtk
 
# # create a rendering window and renderer
# ren = vtk.vtkRenderer()
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)
 
# # create a renderwindowinteractor
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)
 
# # create source
# source = vtk.vtkSphereSource()
# source.SetCenter(0,0,0)
# source.SetRadius(5.0)
 
# # mapper
# mapper = vtk.vtkPolyDataMapper()
# if vtk.VTK_MAJOR_VERSION <= 5:
#     mapper.SetInput(source.GetOutput())
# else:
#     mapper.SetInputConnection(source.GetOutputPort())
 
# # actor
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
 
# # assign actor to the renderer
# ren.AddActor(actor)
 
# # enable user interface interactor
# iren.Initialize()
# renWin.Render()
# iren.Start()

# print 'blablablabla'


# # create a rendering window and renderer
# ren = vtk.vtkRenderer()
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)
 
# # create a renderwindowinteractor
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)
 
# # create source
# source = vtk.vtkSphereSource()
# source.SetCenter(0,0,0)
# source.SetRadius(5.0)
 
# # mapper
# mapper = vtk.vtkPolyDataMapper()
# if vtk.VTK_MAJOR_VERSION <= 5:
#     mapper.SetInput(source.GetOutput())
# else:
#     mapper.SetInputConnection(source.GetOutputPort())
 
# # actor
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
 
# # assign actor to the renderer
# ren.AddActor(actor)
 
# # enable user interface interactor
# iren.Initialize()
# renWin.Render()
# iren.Start()