import open3d as o3d
import numpy as np

def load_point_cloud_from_csv(filename):
    points = np.loadtxt(filename, delimiter=',')
    pcd = o3d.geometry.PointCloud() # point cloud object
    pcd.points = o3d.utility.Vector3dVector(points) # NumPy Array to Open3D format to obj attribute
    return pcd

def visualize_point_cloud(pcd):
    o3d.visualization.draw_geometries([pcd])

filename = "rats_nest_xy_0.csv"  
pcd = load_point_cloud_from_csv(filename)
visualize_point_cloud(pcd)