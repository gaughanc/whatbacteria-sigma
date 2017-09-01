import random
from create_lin_list import create_lin_list
from get_lists import get_genera, get_species, get_urease, get_catcount

#create or define all needed lists
lins = create_lin_list()
genera = get_genera()
species = get_species()
urease = get_urease()
count = get_catcount()
nodes = []
edges = []

#define colors
red = "#ec5148"
maroon = "#9b1b1b"
orange = "#ffce96"
grey = "#e0d8d5"
salmon = "#f28f8a"
blue = "#5094ce"
light_blue = "#c7e3f9"
green = "#82eda7"
edge_color = light_blue
def_node_color = blue

#for each genus
for i, genus in enumerate(genera):
    for j, spec in enumerate(species[i]):
        if urease[i][j] == "urease positive":
            color = green
            count[i][0] += 1
        elif urease[i][j] == "urease negative":
            color = red
            count[i][1] += 1
        else:
            color = blue
        #create a node for each of its species
        nodes.append({"id":"sn"+str(i)+str(j), "label":spec, "x":10*i-10+j, "y":random.randint(850,1000), "size":5, "color":color})
        #create an edge from the genus to each of its species
        edges.append({"id":"se"+str(i)+str(j), "source":"gn"+str(i), "target":"sn"+str(i)+str(j),"size":20,"color":edge_color})
    if count[i][1] < count[i][0]:
        color = green
    elif count[i][0] < count[i][1]:
        color = red
    else:
        color = blue
    #create a node for the genus
    nodes.append({"id":"gn"+str(i), "label":genus, "x":10*i, "y":random.randint(600,800), "size":15, "color":color})
    #for each lineadge
    for lin in lins:
        if len(lin) == 6:
            #if the genus appears
            if lin[5] == genus:
                xs = [10*i+10, 10*i, 11*i, 17*i+25, 750]
                ys = [random.randint(400,500), random.randint(200,300), random.randint(90,100), 0, -300]
                sizes = [20, 25, 30, 35, 40]
                for j, n in enumerate([4, 3, 2, 1, 0]):
                    #if one of its taxon levels does not have a node, create one
                    if not any(node["label"] == lin[n] for node in nodes):
                        nodes.append({"id":"tn"+str(n)+str(i), "label":lin[n], "x":xs[j], "y":ys[j], "size":sizes[j], "color":def_node_color})
                #for each node
                for node in nodes:
                    #if its label belongs to the genus' family, connect the node to the genus
                    if node["label"] == lin[4]:
                        edges.append({"id":"fe"+str(i), "source":"gn"+str(i), "target":node["id"],"size":20,"color":edge_color})
                        #mark the family node
                        source = node["id"]
                        #for each node
                        for node in nodes:
                            #if its label belongs to the genus' order, connect the  node to the family
                            if node["label"] == lin[3]:
                                edges.append({"id":"oe"+str(i), "source":source, "target":node["id"],"size":20,"color":edge_color})
                                #mark the order node
                                source = node["id"]
                                #for each node
                                for node in nodes:
                                    #if its label belongs to the genus' class, connect the node to the order
                                    if node["label"] == lin[2]:
                                        edges.append({"id":"ce"+str(i), "source":source, "target":node["id"],"size":20,"color":edge_color})
                                        #mark the class node
                                        source = node["id"]
                                        #for each node
                                        for node in nodes:
                                            #if its label belongs to the genus' phylum, connect the node to the class
                                            if node["label"] == lin[1]:
                                                edges.append({"id":"pe"+str(i), "source":source, "target":node["id"],"size":20,"color":edge_color})
                                                #mark the class node
                                                source = node["id"]
                                                #for each node
                                                for node in nodes:
                                                    #if its label belongs to the genus' domain, connect the node to the phylum
                                                    if node["label"] == lin[0]:
                                                        edges.append({"id":"de"+str(i), "source":source, "target":node["id"],"size":20,"color":edge_color})
                break

scripta = """<!-- START SIGMA IMPORTS -->
<script src="../src/sigma.core.js"></script>
<script src="../src/conrad.js"></script>
<script src="../src/utils/sigma.utils.js"></script>
<script src="../src/utils/sigma.polyfills.js"></script>
<script src="../src/sigma.settings.js"></script>
<script src="../src/classes/sigma.classes.dispatcher.js"></script>
<script src="../src/classes/sigma.classes.configurable.js"></script>
<script src="../src/classes/sigma.classes.graph.js"></script>
<script src="../src/classes/sigma.classes.camera.js"></script>
<script src="../src/classes/sigma.classes.quad.js"></script>
<script src="../src/classes/sigma.classes.edgequad.js"></script>
<script src="../src/captors/sigma.captors.mouse.js"></script>
<script src="../src/captors/sigma.captors.touch.js"></script>
<script src="../src/renderers/sigma.renderers.canvas.js"></script>
<script src="../src/renderers/sigma.renderers.webgl.js"></script
<script src="../src/renderers/sigma.renderers.svg.js"></script>
<script src="../src/renderers/sigma.renderers.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.nodes.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.nodes.fast.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.fast.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.labels.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.hovers.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.nodes.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.curve.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.curvedArrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.curve.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.curvedArrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.extremities.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.utils.js"></script>
<script src="../src/renderers/svg/sigma.svg.nodes.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.edges.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.edges.curve.js"></script>
<script src="../src/renderers/svg/sigma.svg.labels.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.hovers.def.js"></script>
<script src="../src/middlewares/sigma.middlewares.rescale.js"></script>
<script src="../src/middlewares/sigma.middlewares.copy.js"></script>
<script src="../src/misc/sigma.misc.animation.js"></script>
<script src="../src/misc/sigma.misc.bindEvents.js"></script>
<script src="../src/misc/sigma.misc.bindDOMEvents.js"></script>
<script src="../src/misc/sigma.misc.drawHovers.js"></script>
<!-- END SIGMA IMPORTS -->
<div id="container">
  <style>
    #graph-container {
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      position: absolute;
    }
  </style>
  <div id="graph-container"></div>
</div>

<script>
var g = {
      nodes: [],
      edges: []
    };

// Generate a graph:"""
scriptb = "g.nodes.push(" + str(nodes)[1:-1] + ")"

scriptc = ""

scriptd = "g.edges.push(" + str(edges)[1:-1] + ")"

scripte = """
// Instantiate sigma:
s = new sigma({
  graph: g,
  container: 'graph-container',
});
</script>"""

print(scripta, scriptb, scriptc, scriptd, scripte, sep="\n")
