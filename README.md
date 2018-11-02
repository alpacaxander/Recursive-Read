# Recursive-Read
Very basic function read json like object from file and search with given keys.

## Example
data.json  
`{"a" : [{"" : 1, "b" : 2, "c" : 3}, {}], "d":[{},{}]}`  

`>>>python read.py data.json -k a 1 ''`  
`>>>1`
