#python file_converter.py -h
#python file_converter.py <path-to-input-dir> -o <path-to-output-dir>
#!/usr/bin/env python
import os
import pyvista as pv
import argparse
from pyvista import examples

def convertFiles(indir, outdir):
    files = os.listdir(indir)
    files = [ os.path.join(indir,f) for f in files if f.endswith('.vtk') ]
    ret = 0
    print("In:", indir)
    print("Out:", outdir)
    for f in files:
        mesh = pv.read(f)
        print(files)
        basename = os.path.basename(f)
        print("Copying file:", basename)
        basename = os.path.splitext(basename)[0]
        print("Fle name:", basename)
        othermesh = examples.load_uniform()
        legend_entries = []
        legend_entries.append(['Liver converted', 'w'])
        legend_entries.append(['External marker', 'k'])
        plotter = pv.Plotter()
        _ = plotter.add_mesh(mesh)
        _ = plotter.add_mesh(othermesh, 'k')
        _ = plotter.add_legend(legend_entries)
        _ = plotter.export_obj(outdir+"conv_"+basename+".obj")
        ret +=1
        plotter.show()

    print("Successfully converted %d out of %d files." % (ret, len(files)))

def run(args):
    convertFiles(args.indir, args.outdir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="VTK to OBJ converter")
    parser.add_argument('indir', help="Path to input directory.")
    parser.add_argument('--outdir', '-o', default='output', help="Path to output directory.")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    ret = args.func(args)