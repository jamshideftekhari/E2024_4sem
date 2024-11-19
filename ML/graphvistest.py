import graphviz

# Opret et simpelt diagram for at teste
dot = graphviz.Digraph()
dot.node('A', 'Start')
dot.node('B', 'Slut')
dot.edge('A', 'B')

# Vis grafen
dot.view()
