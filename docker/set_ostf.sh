#!/bin/bash

git clone http://192.168.250.3/kernel/neunn-ostf.git
cd /neunn-ostf
pip install -r requirements.txt
python setup.py install


