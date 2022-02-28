import pymeshlab
import os
ms = pymeshlab.MeshSet()


importDirectory = 'D:\Documents\Cell_DAEs\MorphrenderFiles\RPC1\RodBCs'
exportDirectory = 'D:\Documents\Cell_DAEs\MeshlabExports\RPC1\RodBCs'
files=[]
 
for filename in os.listdir(importDirectory):
    f = os.path.join(importDirectory, filename)
    if filename.startswith('Morphology') and filename.endswith('.dae'):
        files.append(f)
        
        
for f in files:
    ms.load_new_mesh(f)
    ms.generate_surface_reconstruction_screened_poisson(depth=10, preclean = True)
    ms.save_current_mesh(os.path.join(exportDirectory, os.path.basename(f)))
    if not os.path.isdir(exportDirectory):
        os.mkdir(exportDirectory)