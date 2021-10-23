
## Basic ML with DVC

### Usefull Error:

```
ERROR: failed to reproduce 'dvc.yaml':  output 'artifacts\raw_local_dir\data.csv' is already tracked by SCM (e.g. Git).
    You can remove it from Git, then add to DVC.
        To stop tracking from Git:
            git rm -r --cached 'artifacts\raw_local_dir\data.csv'
            git commit -m "stop tracking artifacts\raw_local_dir\data.csv"

```

Note: If get `fatal: pathspec [data.csv or filepath] did not match any files` error.
Sometimes it's happens when you are not tracking your file add your file with `git add untracked file name`, after this simply do `git rm -r file name`

then run the file creation pyhton file again, then run `dvc repro`.
all is you need to restart the process.