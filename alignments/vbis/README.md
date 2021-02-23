# VBIS / Brick Alignment

Aligns concepts in Brick v1.1 with concepts in VBIS v3 (https://vbis.com.au/classification-and-tags).

Use the alignment file `Brick-VBIS-alignment.ttl`; import this into your RDF graph in order to realize the mappings between concepts in VBIS and Brick.
Specifically, the file encodes which VBIS search tags are relevant for many different Brick equipment classes.
The VBIS search tags are encoded as string literals and are related to Brick classes through the `https://brickschema.org/schema/Brick/alignments/vbis/v3#hasVBISTag` property.
