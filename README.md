# BPConvert

This is an implenmentation of the simple First-Come-First-Served algorithm to convert RNA secondary structure from BPSEQ format to dot-bracket format described in this paper (https://doi.org/10.1093/bioinformatics/btx783).

This package supports converting RNA secondary structure with up to 8 sets of brackets (order-7 pseudoknot).

<br>

## Usage
To read secondary structure from BPSEQ file:

```
from BPConvert import Converter

converter = Converter()
converter.parse("./example/example1.bpseq")
```

Converter class possesses three attributes.

* `.id` holds the name of target RNA. It is provided by the line starting with #.
* `.sequence` holds the sequence of target RNA.
* `.Regions` is the list of Region instances, which store base pair information as Python tuple.

<br>

To convert BPSEQ to dot-bracket:

```
converter.convert()
```

convert() method returns a tuple where the first element is RNA ID and the second element is the dot-bracket sequence. 

If a path parameter is given, convert() will write the dot-bracket sequence to the designated path. The file name is given by `.id` attribute.

```
converter.convert(path="./example/results/")
```
