"""Restart and execute every notebook code cell with the invoking Python environment."""
import os
import sys
sys.dont_write_bytecode = True
import json
import time
import tempfile
from pathlib import Path
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

def main():
    root=Path(__file__).resolve().parent
    path=root/'Portfolio_Assessment_3_HoangHuuHoan.ipynb'
    nb=nbformat.read(path,as_version=4)
    for cell in nb.cells:
        if cell.cell_type=='code':
            cell.outputs=[]
            cell.execution_count=None
    started=time.perf_counter()
    with tempfile.TemporaryDirectory() as temp:
        kernels=Path(temp)/'kernels'
        spec=kernels/'cos40007-task3'
        spec.mkdir(parents=True)
        (spec/'kernel.json').write_text(json.dumps({
            'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
            'display_name':'Python 3.12 (Portfolio 3)','language':'python',
            'env':{'PYTHONDONTWRITEBYTECODE':'1','PYTHONUTF8':'1','PYTHONIOENCODING':'utf-8','TF_ENABLE_ONEDNN_OPTS':'0',
                   'TF_CPP_MIN_LOG_LEVEL':'2','CUDA_VISIBLE_DEVICES':'-1','OMP_NUM_THREADS':'2'},
        }),encoding='utf-8')
        km=KernelManager(kernel_name='cos40007-task3',kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(kernels)]))
        client=NotebookClient(nb,km=km,timeout=3600,resources={'metadata':{'path':str(root)}})
        with client.setup_kernel(cwd=str(root)):
            for i,cell in enumerate(nb.cells):
                print(f'Executing cell {i+1}/{len(nb.cells)}',flush=True)
                client.execute_cell(cell,i)
                nbformat.write(nb,path)
    code=[c for c in nb.cells if c.cell_type=='code']
    errors=[o for c in code for o in c.outputs if o.output_type=='error']
    assert not errors and all(c.execution_count is not None for c in code)
    outcome={'passed':True,'fresh_kernel':True,'all_code_cells_executed':True,'code_cell_count':len(code),
             'error_outputs':len(errors),'python':sys.version.split()[0],
             'elapsed_seconds':round(time.perf_counter()-started,2),'relative_paths':True}
    (root/'results/notebook_execution_verification.json').write_text(json.dumps(outcome,indent=2),encoding='utf-8')
    print(json.dumps(outcome,indent=2))

if __name__=='__main__':
    main()
