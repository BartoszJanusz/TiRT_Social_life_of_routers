def walrus_output(graph, spanning_tree):
    gf = open("pythonWalrus.graph", mode='w')

    gf.write("Graph\n")
    gf.write("{\n")
    gf.write("\t### metadata ###\n")
    gf.write("\t@name=;\n")
    gf.write("\t@description=;\n")
    gf.write("\t@numNodes=" + str(graph.num_vertices(ignore_filter=True)) + ";\n")
    gf.write("\t@numLinks=" + str(graph.num_edges(ignore_filter=True)) + ";\n")
    gf.write("\t@numPaths=0;\n")
    gf.write("\t@numPathLinks=0;\n")
    gf.write("\n")
    gf.write("\t### structural data ###\n")
    gf.write("\t@links=[\n")

    edges = graph.get_edges()

    for e in edges[:-1]:
        gf.write("\t\t{ @source=" + str(e[0]) + "; @destination=" + str(e[1]) + "; },\n")
    gf.write("\t\t{ @source=" + str(edges[-1][0]) + "; @destination=" + str(edges[-1][1]) + "; }\n")

    gf.write("\t];\n")
    gf.write("\t@paths=;\n")
    gf.write("\n")
    gf.write("\t### attribute data ###\n")
    gf.write("\t@enumerations=;\n")

    gf.write("\t@attributeDefinitions=[\n")
    gf.write("\t\t{\n")
    gf.write("\t\t\t@name=$root;\n")
    gf.write("\t\t\t@type=bool;\n")
    gf.write("\t\t\t@default=|| false ||;\n")
    gf.write("\t\t\t@nodeValues=[ { @id=0; @value=T; } ];\n")
    gf.write("\t\t\t@linkValues=;\n")
    gf.write("\t\t\t@pathValues=;\n")
    gf.write("\t\t},\n")
    gf.write("\t\t{\n")
    gf.write("\t\t\t@name=$tree_link;\n")
    gf.write("\t\t\t@type=bool;\n")
    gf.write("\t\t\t@default=|| false ||;\n")
    gf.write("\t\t\t@nodeValues=;\n")
    gf.write("\t\t\t@linkValues=[\n")

    edges = spanning_tree
    edges_ids = []
    for i, edge in enumerate(edges):
        if edge:
            edges_ids.append(int(i))

    for e_id in edges_ids[:-1]:
        gf.write("\t\t\t\t{ @id=" + str(e_id) + "; @value=T; },\n")

    gf.write("\t\t\t\t{ @id=" + str(edges_ids[-1]) + "; @value=T; }\n")

    gf.write("\t\t\t];\n")
    gf.write("\t\t\t@pathValues=;\n")
    gf.write("\t\t}\n")
    gf.write("\t];\n")
    gf.write("\t@qualifiers=[\n")
    gf.write("\t\t{\n")
    gf.write("\t\t\t@type=$spanning_tree;\n")
    gf.write("\t\t\t@name=$sample_spanning_tree;\n")
    gf.write("\t\t\t@description=;\n")
    gf.write("\t\t\t@attributes=[\n")
    gf.write("\t\t\t\t{ @attribute=0; @alias=$root; },\n")
    gf.write("\t\t\t\t{ @attribute=1; @alias=$tree_link; }\n")
    gf.write("\t\t\t];\n")
    gf.write("\t\t}\n")
    gf.write("\t];\n")
    gf.write("\n")
    gf.write("\t### visualization hints ###\n")
    gf.write("\t@filters=;\n")
    gf.write("\t@selectors=;\n")
    gf.write("\t@displays=;\n")
    gf.write("\t@presentations=;\n")
    gf.write("\n")
    gf.write("\t### interface hints ###\n")
    gf.write("\t@presentationMenus=;\n")
    gf.write("\t@displayMenus=;\n")
    gf.write("\t@selectorMenus=;\n")
    gf.write("\t@filterMenus=;\n")
    gf.write("\t@attributeMenus=;\n")
    gf.write("}\n")

    return
