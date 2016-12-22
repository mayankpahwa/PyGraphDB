g = Graph()

Saturn = Node('Saturn')
Jupiter = Node('Jupiter')
Hercules = Node('Hercules')
Neptune = Node('Neptune')
Alcemene = Node('Alcemene')
Pluto = Node('Pluto')
Nemean = Node('Nemean')
Hydra = Node('Hydra')
Cerebrus = Node('Cerebrus')
Tartarus = Node('Tartarus')
Sky = Node('Sky')
Sea = Node('Sea')

E1 = Edge('father')
E2 = Edge('father')
E3 = Edge('mother')
E4 = Edge('pet')
E5 = Edge('battled')
E6 = Edge('battled')
E7 = Edge('battled')
E8 = Edge('lives')
E9 = Edge('lives')
E10 = Edge('lives')
E11 = Edge('lives')

Saturn.add_properties({'age':10000,'type':'titan'})
Sky.add_properties({'type':'location'})
Sea.add_properties({'type':'location'})
Jupiter.add_properties({'age':5000,'type':'god'})
Neptune.add_properties({'age':4500,'type':'god'})
Hercules.add_properties({'age':30, 'type':'demigod'})
Alcemene.add_properties({'age':45,'type':'human'})
Pluto.add_properties({'age':4000,'type':'god'})
Nemean.add_properties({'type':'monster'})
Hydra.add_properties({'type':'monster'})
Cerebrus.add_properties({'type':'monster'})
Tartarus.add_properties({'type':'location'})

E5.add_properties({'time':1,'place':[38.1,23.7]})
E6.add_properties({'time':2,'place':[37.7,23.9]})
E7.add_properties({'time':12,'place':[39,22]})
E9.add_properties({'reason':'no fear of death'})
E10.add_properties({'reason':'loves fresh breezes'})
E11.add_properties({'reason':'loves waves'})

g.add_node(Saturn,Sky,Sea,Jupiter,Neptune,Hercules,Alcemene,Pluto,Nemean,Hydra,Cerebrus,Tartarus)
g.add_edge(E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11)

g.render_edge_by_nodes(E1,Jupiter,Saturn)
g.render_edge_by_nodes(E2,Hercules,Jupiter)
g.render_edge_by_nodes(E3,Hercules,Alcemene)
g.render_edge_by_nodes(E4,Pluto,Cerebrus)
g.render_edge_by_nodes(E5,Hercules,Nemean)
g.render_edge_by_nodes(E6,Hercules,Hydra)
g.render_edge_by_nodes(E7,Hercules,Cerebrus)
g.render_edge_by_nodes(E8,Cerebrus,Tartarus)
g.render_edge_by_nodes(E9,Pluto,Tartarus)
g.render_edge_by_nodes(E10,Jupiter,Sky)
g.render_edge_by_nodes(E11,Neptune,Sea)

g.V('Jupiter').both_query().values('name')