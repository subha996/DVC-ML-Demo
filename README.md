
## Basic ML with DVC

### Usefull Error:

```
ERROR: failed to reproduce 'dvc.yaml':  output 'artifacts\raw_local_dir\data.csv' is already tracked by SCM (e.g. Git).
    You can remove it from Git, then add to DVC.
        To stop tracking from Git:
            git rm -r --cached 'artifacts\raw_local_dir\data.csv'
            git commit -m "stop tracking artifacts\raw_local_dir\data.csv"

```