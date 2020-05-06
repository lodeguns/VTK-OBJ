# VTK-OBJ Converter
After careful online research, there seems to be too much confusion about how to transform a 3D Mesh object in VTK format into an OBJ wavefront format using Python. For this reason, in this repository I present a simple solution based on the well-known [pyvista package](https://docs.pyvista.org/).

In detail, I took the model of a reconstructed liver kindly provided by [Suwelack et al.](https://opencas.webarchiv.kit.edu/?q=node/14) and I converted their VTK files in OBJ wavefront meshes.

Here's what you get:

![Liver with an external marker](https://github.com/lodeguns/VTK-OBJ/blob/master/lvertake.gif)

Basic usage:

```
 python3 vtk_to_obj_converter.py '/your_dir/toconvert_vtks_folder/' -o '/your_dir/converted_objs_folder/'
```
