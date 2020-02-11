# RealEstateCore / Brick Alignment

Aligns concepts in Brick v1.1 with concepts in RealEstateCore v3.1 (https://doc.realestatecore.io/3.1/full.html)

Use the alignment file `Brick-REC-alignment.ttl`; import this into your RDF graph in order to realize the mappings between concepts in RealEstateCore and Brick.

`Brick-REC-nodevice.rdf` represents the intermediate alignment output, without the device type mappings. `generate.py` accepts the `BRICk-REC-nodevice.rdf` file as input and generates the final alignment file.
