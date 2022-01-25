opml2json is a simple python module that convert opml to json 

## installation
---

#### Using pip
        pip install opml2json
    
#### from sources
        * git clone https://github.com/vishnu012/opml2json && cd opml2json

        * python3 setup.py install
---
## usage

#### for help
    python3 -m opml2json -h

#### import on another python file
    from opml2json.dump import write_json

    write_json("input.opml","output.json")

#### directly use on terminal / cmd
    python3 -m opml2json -f filename.opml

    python3 -m opml2json -f ./dir/filename.opml -o ./dir/output_filename.json

