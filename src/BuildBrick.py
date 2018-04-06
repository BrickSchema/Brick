# !pip install rdflib
# !pip install pydot2
# !pip install pydotplus


import rdflib
from rdflib.namespace import RDFS
from rdflib import URIRef, BNode, Literal
import re
from collections import defaultdict
import numpy as np
import pandas as pd
import json
import itertools

# Configuration

createEquipmentTagSets = True
setEquivalent = True
usedMeasOnly = True
writeUsedByPoint = False
writeTagUsedBy = True
removeSynonyms = False
with open('../config.json', 'r') as fp:
    config = json.load(fp)
BRICK_VERSION = config['version']

# Helper Functions

def getIdentifier(url):
    return url.split('#')[-1]

def IndivName(name):
    return re.sub(r'\s', '_', re.sub(r'[^\d\w\s]', '', name))

def get_str(s):
    # if type(s)==str or type(s)==unicode:
    if type(s) == 'str' or type(s) == 'unicode':
        return s
    else:
        return ''

def getLastDim(istr):
    if ">" not in istr:
        return istr
    else:
        sstr = istr.split(">")
        return sstr[-1]

def replace_in_file(old, new, filename):
    """
    with open(filename, "rt") as fin:
        with open(filename + '.new.ttl', "wt") as fout:
            for line in fin:
                fout.write(re.sub(old, new, line))
    """
    with open(filename, 'r') as fp:
        s = fp.read()
    with open(filename, 'w') as fp:
        s = re.sub(old, new, s)
        fp.write(s)

def version_update_infile(version, filename):
    replace_in_file('\d+\.\d+\.\d+', BRICK_VERSION, filename)



# ### Load Tag and TagSets from Definition

# dfTags=pd.read_excel('Schema Engineering.xlsx',"Tags")
dfTags = pd.read_csv('Tags.csv')
schemaTags = set(pd.unique(dfTags.Tag.dropna().ravel()))
len(schemaTags)
dfTags.head()

dfTagSets = pd.read_csv('TagSets.csv')
schemaTagSets = set()
for ts in pd.unique(dfTagSets.TagSet.dropna().ravel()):
    schemaTagSets.add(ts.replace(' ', '_'))
for ts in pd.unique(dfTagSets.hasSynonym.dropna().ravel()):
    for ts2 in ts.split(","):
        schemaTagSets.add(ts2.replace(' ', '_'))
for row in pd.unique(dfTagSets.usesEquipment.dropna().ravel()):
    for ts in row.split(';'):
        schemaTagSets.add(ts.replace(' ', '_'))
for row in pd.unique(dfTagSets.isPartOf.dropna().ravel()):
    for ts in row.split(';'):
        schemaTagSets.add(ts.replace(' ', '_'))
#print(dfTagSets.head())

# In[ ]:

schemaUsedTags = set()
schemaTagSetTags = {}
for ts in schemaTagSets:
    schemaUsedTags.update(ts.split('_'))
    schemaTagSetTags[ts] = set(ts.split('_'))
schemaMissingTags = (schemaUsedTags - schemaTags) - set([''])
if len(schemaMissingTags) > 0:
    print('Missing Tags: {0}'.format(schemaMissingTags))


### Create Brick

# Classify Tags by Type

# init Brick ontology
nsBrickTagSet = ":"  # "ts:"
foBrick = open('../dist/Brick.ttl', 'w')
foBrick.write("""
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

@prefix bf:    <https://brickschema.org/schema/{0}/BrickFrame#> .

@prefix :      <https://brickschema.org/schema/{0}/Brick#> .

<https://brickschema.org/schema/{0}/Brick>  a owl:Ontology ;
    owl:imports <https://brickschema.org/schema/{0}/BrickFrame> ;
    rdfs:comment "Domain TagSet Definition"@en .

""".format(BRICK_VERSION))

# In[ ]:

# init BrickUse ontology
nsTagTag = ":"
nsTagTagSet = "brick:"  # "ts:"
foUse = open('../dist/BrickUse.ttl', 'w')
foUse.write("""
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

@prefix bf:    <https://brickschema.org/schema/{0}/BrickFrame#> .
@prefix brick: <https://brickschema.org/schema/{0}/Brick#> .

@prefix :      <https://brickschema.org/schema/{0}/BrickUse#> .

<https://brickschema.org/schema/{0}/BrickUse>  a owl:Ontology ;
    owl:imports <https://brickschema.org/schema/{0}/Brick> ;
    rdfs:comment "Domain TagSet Use Definition"@en .

""".format(BRICK_VERSION))

# In[ ]:

# init BrickTag ontology
nsTagTag = ":"
nsTagTagSet = "brick:"  # "ts:"
foTag = open('../dist/BrickTag.ttl', 'w')
foTag.write("""
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .

@prefix bf:    <https://brickschema.org/schema/{0}/BrickFrame#> .
@prefix brick: <https://brickschema.org/schema/{0}/Brick#> .

@prefix :      <https://brickschema.org/schema/{0}/BrickTag#> .

<https://brickschema.org/schema/{0}/BrickTag>  a owl:Ontology ;
    owl:imports <https://brickschema.org/schema/{0}/Brick> ;
    rdfs:comment "Domain Tag Definition"@en .

""".format(BRICK_VERSION))

dfTagSets.MainDimension = dfTagSets.Dimension.str.split(">", 1, True)[0]
dfDimensions = list(dfTagSets.MainDimension.unique())

# synonyms
synonyms = {}
for r in dfTagSets.index:
    if str(dfTagSets.hasSynonym[r]) != "nan":
        syn = dfTagSets.hasSynonym[r].split(";")
        for s in syn:
            synonyms[s] = dfTagSets.TagSet[r]
dfTagSets["Measurement2"] = dfTagSets.TagSet
dfMM = dfTagSets.Measurement2.ravel()
for r in range(len(dfMM)):
    dfM = " " + str(dfMM[r]) + " "
    if str(dfTagSets.usesLocation[r]) != "nan":
        for loc in str(dfTagSets.usesLocation[r]).split(";"):
            dfM = dfM.replace(" " + loc.strip() + " ", " ")
    if str(dfTagSets.usesEquipment[r]) != "nan":
        for eq in str(dfTagSets.usesEquipment[r]).split(";"):
            dfM = dfM.replace(" " + eq.strip() + " ", " ")
            if removeSynonyms and eq.strip() in synonyms:
                for s in synonyms[eq.strip()].split(' '):
                    dfM = dfM.replace(" " + s + " ", " ")
    if str(dfTagSets.usesPoint[r]) != "nan":
        dfM = dfM.replace(" " + str(dfTagSets.usesPoint[r]) + " ", " ")
    dfMM[r] = dfM.strip()
dfTagSets["Measurement2"] = dfMM
dfTagSets['Parent'] = dfTagSets.Dimension.apply(getLastDim)
dfTagSets['MainDimension'] = dfTagSets.Dimension.str.split(">", 1, True)[0]

# Missing tags
for dim in dfDimensions:
    usedTags = set([t for i in dfTagSets.loc[dfTagSets.Dimension.str.startswith(dim)].TagSet.str.split(' ') for t in i])
    defTags = set(dfTags.loc[dfTags.Dimension.str.startswith(dim)].Tag)
    # print("Missing Tags for "+dim+"\n"+str(usedTags-defTags)+"\n")

# Classify TagSets
dfTagSetsEqLoc = dfTagSets.loc[dfTagSets.Dimension.str.startswith("Equipment") |
                               dfTagSets.Dimension.str.startswith("Location")]
dfTagSetsPoints = dfTagSets.loc[dfTagSets.Dimension.str.startswith("Point")]
dfTagSetsMeas = dfTagSets.loc[dfTagSets.Dimension.str.startswith("MeasurementProperty")]

tagsetsPoints = {}
for r in dfTagSetsPoints.index:
    if createEquipmentTagSets and dfTagSetsPoints.usesEquipment[r] != '' and str(
            dfTagSetsPoints.usesEquipment[r]) != "nan":
        equip = [s.strip() for s in dfTagSetsPoints.usesEquipment[r].split(';')]
        equip.append("")
    else:
        equip = [""]
    tagsets = set([dfTagSetsPoints.TagSet[r]]) | set(str(dfTagSetsPoints.hasSynonym[r]).split(",")) - set(['', 'nan'])
    for tagset in tagsets:
        for eq in equip:
            if eq != "" and eq not in tagset:
                ts = eq.replace(" ", "_") + " " + tagset
            else:
                ts = tagset
            if ts not in tagsetsPoints:
                tagsetsPoints[ts] = {
                    'TagSet': ts,
                    'Tags': set(ts.split(' ')),
                    'usesPoint': dfTagSetsPoints.usesPoint[r],
                    'usesLocation': dfTagSetsPoints.usesLocation[r],
                    'usesEquipment': dfTagSetsPoints.usesEquipment[r],
                    'usesMeasurement': dfTagSetsPoints.usesMeasurement[r],
                    'description': dfTagSetsPoints.Definition[r],
                    'dimension': dfTagSetsPoints.Dimension[r],
                    'maindimension': dfTagSetsPoints.MainDimension[r],
                    'synonyms': tagsets - set([ts]),
                    'parent': dfTagSetsPoints.Parent[r],
                    'parents': set([dfTagSetsPoints.Parent[r].replace('_', ' ')]),
                    'allparents': set([dfTagSetsPoints.Parent[r].replace('_', ' ')]),
                    # 'measurement':dfTagSetsPoints.Measurement[r],
                    # 'measurement2':dfTagSetsPoints.Measurement2[r]
                }
                if createEquipmentTagSets:
                    tagsetsPoints[ts]['usesEquipment'] = eq
                if eq != "" and len(tagsets - set([ts])) > 0:
                    tagsetsPoints[ts]['synonyms'] = [(eq.replace(" ", "_") + " " + ts2) for ts2 in (tagsets - set([ts]))
                                                     if eq not in ts2]
                dfM = " " + tagset + " "
                if str(dfTagSets.usesLocation[r]) != "nan":
                    for loc in str(dfTagSets.usesLocation[r]).split(";"):
                        dfM = dfM.replace(" " + loc.strip() + " ", " ")
                if str(dfTagSets.usesEquipment[r]) != "nan":
                    for eq in str(dfTagSets.usesEquipment[r]).split(";"):
                        dfM = dfM.replace(" " + eq.strip() + " ", " ")
                        dfM = dfM.replace(" " + eq.replace(" ", "_").strip() + " ", " ")
                        if removeSynonyms and eq.strip() in synonyms:
                            for s in synonyms[eq.strip()].split(' '):
                                dfM = dfM.replace(" " + s + " ", " ")
                if str(dfTagSets.usesPoint[r]) != "nan":
                    dfM = dfM.replace(" " + str(dfTagSets.usesPoint[r]) + " ", " ")
                tagsetsPoints[ts]['measurement2'] = dfM.strip()
if '' in tagsetsPoints: del tagsetsPoints['']

# determine parent concepts
for tsA in tagsetsPoints:
    for tsB in tagsetsPoints:
        if tagsetsPoints[tsA]['maindimension'] == tagsetsPoints[tsB]['maindimension']:
            if tagsetsPoints[tsB]['Tags'] < tagsetsPoints[tsA]['Tags']:
                tagsetsPoints[tsA]['allparents'].add(tsB)
                tagsetsPoints[tsA]['parents'].add(tsB)

# minimize parent concepts
for tsA in tagsetsPoints:
    rmOldParent = set()
    for tsB in tagsetsPoints[tsA]['parents']:
        for tsC in tagsetsPoints[tsA]['parents']:
            if set(tsB.split(' ')) > set(tsC.split(' ')):  # if direct parent
                rmOldParent.add(tsC)
    for tsC in rmOldParent:
        tagsetsPoints[tsA]['parents'].remove(tsC)

tagsetsMeas = {}
if not usedMeasOnly:
    for r in dfTagSetsMeas.index:
        tagsetsMeas[dfTagSetsMeas.TagSet[r]] = {
            'TagSet': dfTagSetsMeas.TagSet[r],
            'Tags': set(dfTagSetsMeas.TagSet[r].split(' ')),
            'dimension': dfTagSetsMeas.Dimension[r],
            'maindimension': dfTagSetsMeas.MainDimension[r],
            'description': dfTagSetsMeas.Definition[r],
            'reference': dfTagSetsMeas.Reference[r],
            'parent': dfTagSetsMeas.usesMeasurement[r],
            'parents': set(['MeasurementProperty']),
            'allparents': set(['MeasurementProperty'])
        }

# add missing
meas = set([tagsetsPoints[ts]['measurement2'] for ts in tagsetsPoints])
# remove default tags
meas -= set(['Setpoint', 'Sensor', 'Status', 'Command', 'Alarm', 'Meter', ''])
# remove dimension tagsets
meas -= set(itertools.chain.from_iterable(dfTagSets.Dimension.dropna().str.split('>').tolist()))
for ts in list(meas):
    if ts not in tagsetsMeas:
        tagsetsMeas[ts] = {
            'TagSet': ts,
            'Tags': set(ts.split(' ')),
            'dimension': 'MeasurementProperty',
            'maindimension': 'MeasurementProperty',
            'measdim': 'MeasurementProperty',
            'description': '',
            'parent': '',
            'parents': set(['UndefinedMeasurement']),
            'allparents': set(['UndefinedMeasurement'])
        }
for ts in set(['UndefinedMeasurement']):
    if ts not in tagsetsMeas:
        tagsetsMeas[ts] = {
            'TagSet': ts,
            'Tags': set([ts]),
            'dimension': 'MeasurementProperty',
            'maindimension': 'MeasurementProperty',
            'measdim': 'MeasurementProperty',
            'description': '',
            'parent': '',
            'parents': set(['MeasurementProperty']),
            'allparents': set(['MeasurementProperty'])
        }

if '' in tagsetsMeas: del tagsetsMeas['']

# determine parent concepts
for tsA in tagsetsMeas:
    for tsB in tagsetsMeas:
        if tagsetsMeas[tsA]['maindimension'] == tagsetsMeas[tsB]['maindimension']:
            if tagsetsMeas[tsB]['Tags'] < tagsetsMeas[tsA]['Tags']:
                tagsetsMeas[tsA]['allparents'].add(tsB)
                tagsetsMeas[tsA]['parents'].add(tsB)

# minimize parent concepts
for tsA in tagsetsMeas:
    while True:
        rmOldParent = set()
        for tsB in tagsetsMeas[tsA]['parents']:
            for tsC in tagsetsMeas[tsA]['parents']:
                # if tagsetsMeas[tsB]['Tags'] > tagsetsMeas[tsC]['Tags']: # if direct parent
                if set(tsB.split(' ')) > set(tsC.split(' ')):  # if direct parent
                    rmOldParent.add(tsC)
        if len(tagsetsMeas[tsA]['parents']) > 1 and 'UndefinedMeasurement' in tagsetsMeas[tsA]['parents']:
            rmOldParent.add('UndefinedMeasurement')
        for tsC in rmOldParent:
            tagsetsMeas[tsA]['parents'].remove(tsC)
        if len(rmOldParent) == 0:
            break;

brickTagSets = {}
for hir in pd.unique(dfTagSets.Dimension.dropna().ravel()):
    tags = hir.split('>')
    atags = ""
    for i in range(len(tags)):
        tag = tags[i]
        otags = atags
        atags = tag.strip('_')
        if atags not in brickTagSets:
            indivLocName = nsBrickTagSet + IndivName(atags)
            if i > 0:
                foBrick.write("\n " + indivLocName + "  rdfs:subClassOf   " + brickTagSets[otags] + ";")
            else:
                foBrick.write("\n " + indivLocName + "  rdfs:subClassOf   bf:TagSet;")
            foBrick.write('\n\t\t\t rdf:type   owl:Class ;')
            foBrick.write('\n\t\t\t rdfs:label "' + tag + '"@en .\n')
            brickTagSets[atags] = indivLocName;
            if i > 1:
                # check for tag consistency
                missingTags = set(otags.split(' ')) - set(atags.split(' '))
                if missingTags:
                    print('Warning! Tags: ' + str(missingTags) + " missing in " + atags)

# Add TagSets leaves

# create location individuals
for idx in dfTagSetsEqLoc.index:
    tagsets = set([str(dfTagSetsEqLoc.loc[idx, "TagSet"])]) | (
                set(str(dfTagSetsEqLoc.loc[idx, "hasSynonym"]).split(",")) - set(['', 'nan']))
    ots = None
    for tagset in tagsets:
        if tagset != "nan":
            parent = brickTagSets[str(dfTagSetsEqLoc.loc[idx, "Dimension"]).split('>')[-1]]
            indivLocName = nsBrickTagSet + IndivName(tagset)
            foBrick.write("\n " + indivLocName + "  rdfs:subClassOf   " + parent + ";")
            foBrick.write('\n\t\t\t rdf:type   owl:Class ;')
            if ots:
                if setEquivalent:
                    foBrick.write('\n\t\t\t owl:equivalentClass ' + ots + ';')
                else:
                    foBrick.write('\n\t\t\t bf:equivalentTagSet ' + ots + ';')
            foBrick.write('\n\t\t\t rdfs:label "' + str(dfTagSetsEqLoc.loc[idx, "TagSet"]) + '"@en.\n')
            for tag in tagset.split():  # write to BrickTag
                foTag.write('\n ' + nsTagTagSet + IndivName(tagset) + '  bf:usesTag :' + tag + '.')
                if writeTagUsedBy:
                    foTag.write('\n :' + tag + '  bf:usedBy ' + nsTagTagSet + IndivName(tagset) + '.')
            brickTagSets[tagset] = indivLocName;
            ots = indivLocName;

# write measurement tagsets
for tsA in tagsetsMeas:
    ts = tagsetsMeas[tsA]
    indivLocName = nsBrickTagSet + IndivName(ts['TagSet'])
    supClass = ""
    for par in ts['parents']:
        supClass = supClass + ", " + nsBrickTagSet + IndivName(par)
    foBrick.write("\n " + indivLocName + "  rdfs:subClassOf   " + supClass.strip(',').strip() + ";")
    foBrick.write('\n\t\t\t rdf:type   owl:Class ;')
    if ts['description'] != '' and str(ts['description']) != "nan":
        # foBrick.write('\n\t\t\t rdfs:description "'+ts['description']+'"@en;')
        foBrick.write('\n\t\t\t skos:definition "' + ts['description'] + '"@en ;\n')
    foBrick.write('\n\t\t\t rdfs:label "' + ts['TagSet'] + '"@en .\n')
    for tag in ts['Tags']:  # write to BrickTag
        foTag.write('\n ' + nsTagTagSet + IndivName(ts['TagSet']) + '  bf:usesTag :' + tag + '.')
        if writeTagUsedBy:
            foTag.write('\n :' + tag + '  bf:usedBy ' + nsTagTagSet + IndivName(ts['TagSet']) + '.')

# Write point tagsets
for tsA in tagsetsPoints:
    ts = tagsetsPoints[tsA]
    if not ts['parents']:
        print(ts)
        continue;
    # tagsets=set([ts['TagSet']])#  | set(str(ts["synonyms"]).split(",")) - set(['', 'nan'])
    tagsets = set([ts['TagSet']])
    if ts["synonyms"]:
        tagsets |= set(ts["synonyms"])
        tagsets -= set(['', 'nan'])
    ots = None
    for tagset in tagsets:
        tagset = tagset.strip()
        indivLocName = nsBrickTagSet + IndivName(tagset)
        brickTagSets[tagset] = indivLocName;
        supClass = ""  # "bf:TagSet, "
        for par in ts['parents']:
            supClass = supClass + ", " + nsBrickTagSet + IndivName(par)
        foBrick.write("\n " + indivLocName + "  rdfs:subClassOf   " + supClass.strip(',').strip() + ";")
        foBrick.write('\n\t\t\t rdf:type   owl:Class ;')
        if ots:
            if setEquivalent:
                foBrick.write('\n\t\t\t owl:equivalentClass ' + ots + ';')
            else:
                foBrick.write('\n\t\t\t bf:equivalentTagSet ' + ots + ';')
        ots = indivLocName;
        if 'description' in ts and str(ts['description']).strip() != '' and str(ts['description']) != "nan":
            # foBrick.write('\n\t\t\t rdfs:description "'+get_str(ts['description'].replace('"',"'"))+'"@en;')
            foBrick.write('\n\t\t\t skos:definition "' + get_str(ts['description'].replace('"', "'")) + '"@en;')
        if 'reference' in ts and ts['reference'] != '' and str(ts['reference']) != "nan":
            foBrick.write('\n\t\t\t rdfs:isDefinedBy "' + get_str(ts['reference'].replace('"', "'")) + '"@en ;\n')
        foBrick.write('\n\t\t\t rdfs:label "' + ts['TagSet'] + '"@en .\n')
        for tag in ts['Tags']:  # write to BrickTag
            foTag.write('\n ' + nsTagTagSet + IndivName(tagset) + '  bf:usesTag :' + tag + '.')
            if writeTagUsedBy:
                foTag.write('\n :' + tag + '  bf:usedBy ' + nsTagTagSet + IndivName(tagset) + '.')
        if ts['usesLocation'] != '' and str(ts['usesLocation']) != "nan":  # write to BrickUses
            for loc in ts['usesLocation'].split(';'):
                foUse.write('\n brick' + indivLocName + ' bf:usesLocation brick:' + IndivName(loc.strip()) + '.')
                if writeUsedByPoint:
                    foUse.write('\n brick:' + IndivName(loc.strip()) + '  bf:usedByPoint brick' + indivLocName + '.')
        if ts['usesEquipment'] != '' and str(ts['usesEquipment']) != "nan":
            for eq in ts['usesEquipment'].split(';'):
                foUse.write('\n brick' + indivLocName + ' bf:usesEquipment brick:' + IndivName(eq.strip()) + '.')
                if writeUsedByPoint:
                    foUse.write('\n brick:' + IndivName(eq.strip()) + '  bf:usedByPoint brick' + indivLocName + '.')
        if ts['usesPoint'] != '' and str(ts['usesPoint']) != "nan":
            foUse.write('\n brick' + indivLocName + ' bf:usesPoint brick:' + IndivName(ts['usesPoint']) + '.')
            if writeUsedByPoint:
                foUse.write('\n brick:' + IndivName(ts['usesPoint']) + '  bf:usedByPoint brick' + indivLocName + '.')
        if ts['measurement2'] != '' and str(ts['measurement2']) != "nan" and tagset != ts['measurement2']:
            foUse.write('\n brick' + indivLocName + ' bf:usesMeasurement brick:' + IndivName(ts['measurement2']) + '.')
            if writeUsedByPoint:
                foUse.write('\n brick:' + IndivName(ts['measurement2']) + '  bf:usedByPoint brick' + indivLocName + '.')

foBrick.write('\n')
foBrick.close()

# format
g = rdflib.Graph()
result = g.parse('../dist/Brick.ttl', format='n3')

# rewrite for formating
g.serialize(destination='../dist/Brick.ttl', format='turtle')

qres = g.query("""SELECT DISTINCT ?ts WHERE {  ?ts rdfs:subClassOf+ bf:TagSet . }""")
brickTagSets = set()
brickTagSetTags = {}
for row in qres:
    ts = getIdentifier(row['ts'])
    brickTagSets.add(ts)
    brickTagSetTags[ts] = set(ts.split('_'))
len(brickTagSets)

# ### Write Tags

# Write Tag Hierachy

brickTags = {}
for hir in pd.unique(dfTags.Dimension.dropna().ravel()):
    tags = hir.split('>')
    atags = ""
    for i in range(len(tags)):
        tag = tags[i]
        otags = atags
        atags = (atags + "_" + tag).strip("_")
        if atags not in brickTags:
            indivLocName = nsTagTag + IndivName(atags)
            if i > 0:
                # foTag.write("\n "+indivLocName+"  rdfs:subClassOf   "+brickTags[otags]+";")
                foTag.write("\n " + indivLocName + "  rdfs:subClassOf   bf:Tag;")
            else:
                foTag.write("\n " + indivLocName + "  rdfs:subClassOf   bf:Tag;")
            foTag.write('\n\t\t\t rdf:type   owl:Class ;')
            foTag.write('\n\t\t\t bf:isHierarchical  "";')
            foTag.write('\n\t\t\t skos:definition ""@en ;\n')
            foTag.write('\n\t\t\t rdfs:label "' + tag + '"@en .\n')
            brickTags[atags] = indivLocName;
            parent = tag;

# Add tag leaves

# create location individuals
for idx in dfTags.index:
    # parent=brickTags[str(dfTags.loc[idx, "Dimension"]).split('>')[-1]]
    parent = brickTags[str(dfTags.loc[idx, "Dimension"]).replace('>', '_')]
    indivLocName = nsTagTag + IndivName(str(dfTags.loc[idx, "Tag"]))
    # foTag.write("\n "+indivLocName+"  rdfs:subClassOf   "+parent+";")
    foTag.write("\n " + indivLocName + "  rdfs:subClassOf   bf:Tag;")
    foTag.write('\n\t\t\t rdf:type   owl:Class ;')
    foTag.write('\n\t\t\t skos:definition "' + get_str(dfTags.loc[idx, "Definition"]) + '"@en ;\n')
    foTag.write('\n\t\t\t rdfs:label "' + str(dfTags.loc[idx, "Tag"]) + '"@en .\n')
    brickTags[tag] = indivLocName;

foTag.close()

# format
g = rdflib.Graph()
result = g.parse('../dist/BrickTag.ttl', format='n3')

# rewrite for formating
g.serialize(destination='../dist/BrickTag.ttl', format='turtle')

# ### Finalize Brick Uses

foUse.close()

# format
g = rdflib.Graph()
result = g.parse('../dist/BrickUse.ttl', format='n3')

# rewrite for formating
g.serialize(destination='../dist/BrickUse.ttl', format='turtle')


# update version of BrickFrame
version_update_infile(BRICK_VERSION, '../dist/BrickFrame.ttl')
