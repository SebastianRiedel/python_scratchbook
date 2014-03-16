import numpy as np
from scipy.spatial import cKDTree
from transformation import transformation as tf

"""
from http://www.nandnor.net/?p=86
"""
def loadOBJ(filename):
  numVerts = 0
  verts = []
  norms = []
  vertsOut = []
  normsOut = []
  for line in open(filename, "r"):
    vals = line.split()
    if vals[0] == "v":
      v = map(float, vals[1:4])
      verts.append(v)
    if vals[0] == "vn":
      n = map(float, vals[1:4])
      norms.append(n)
    if vals[0] == "f":
      for f in vals[1:]:
        w = f.split("/")
        # OBJ Files are 1-indexed so we must subtract 1 below
        vertsOut.append(list(verts[int(w[0])-1]))
        normsOut.append(list(norms[int(w[2])-1]))
        numVerts += 1
  return vertsOut, normsOut

"""
creates an orthogonal basis with the first axis pointing in vec direction
"""
def make_orthonormal_basis(vec):
  v1 = vec / np.linalg.norm(vec)

  t = np.random.rand(3)

  v2 = np.cross(v1,t)
  v3 = np.cross(v1,v2)

  v2 = v2 / np.linalg.norm(v2)
  v3 = v3 / np.linalg.norm(v3)

  np.testing.assert_allclose(np.dot(v1,v2), 0)
  np.testing.assert_allclose(np.dot(v1,v3), 0)
  np.testing.assert_allclose(np.dot(v2,v3), 0)

  return v1, v2, v3

"""
converts a pose tuple to a transformation matrix

Input: a tuple with the first element the translation vector and
        the second element a rotation quaternion in [w x y z] format
"""
def pose_tuple_to_transformation(pose_tuple):
  angles = tf.euler_from_quaternion(pose_tuple[1])
  return np.matrix(tf.compose_matrix(angles=angles, translate=pose_tuple[0]))



def kdtree_example():
  x, y, z = np.mgrid[0:1:100j, 0:1:100j, 0:1:100j]
  
  tree_points = np.asarray(zip(x.ravel(), y.ravel(), z.ravel()))
  tree = cKDTree(tree_points)
  
  xq, yq, zq = np.mgrid[0:1:5j, 0:1:5j, 0:1:5j]
  query_points = np.asarray(zip(xq.ravel(), yq.ravel(), zq.ravel()))
  query_tree = cKDTree(query_points)

  dist = 0.015
  nn = query_tree.query_ball_tree(tree, dist, 2.0, 0.0)


  print 'Example:'
  print 'query', query_points[19,:]
  print 'nn'
  tree_points[nn[19]]

def main():
  kdtree_example()




if __name__ == '__main__':
  main()