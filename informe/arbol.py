# from graphviz import Digraph
# from anytree import Node
# import streamlit as st
# from PIL import Image
# from informe.constantes import Constants
# import os


# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Ruta completa al ejecutable dot
# graphviz_executable = os.path.abspath(os.path.join(script_dir, "..", "Graphviz", "bin", "dot"))


# def arbol():
#     st.image("informe/imagenes/price.png", caption='Precio de 1000 aperturas y 1000 mensajes', use_column_width=True)
#     st.image("informe/imagenes/mensaje.png", caption='Mensaje utilizado para campaña', use_column_width=True)


#     tupla = Constants().main()
#     print(tupla[0])
#     # Crear los nodos del árbol
#     root = Node("Arbol")
#     mensajes_node = Node(f"Mensajes {tupla[0]}", parent=root)
#     responde_node = Node(f"Responde {tupla[1]}", parent=mensajes_node)
#     si_node = Node(f"Si, me encantaría {tupla[2]}", parent=responde_node)
#     si_porcentaje_node = Node(f"Porcentaje de derivación {tupla[7]}", parent=si_node)
#     no_porcentaje_node = Node(f"Porcentaje de no derivación {tupla[8]}", parent=si_node)
#     no_en_otro_momento_node = Node(f"No en otro momento {tupla[5]}", parent=responde_node)
#     no_responde_node = Node(f"No responde {tupla[6]}", parent=mensajes_node)


#     # Crear un objeto Digraph
#     dot = Digraph(format='png', graph_attr={'rankdir': 'TB', 'bgcolor': 'black'}, engine=graphviz_executable)
#     dot.attr('node', style='filled', shape='box', color='#D9E6F5', fontname='Courier', fontsize='10')
#     dot.attr('edge', color='#808080')


#     # Agregar las relaciones entre los nodos
#     for node in root.descendants:
#         if node.parent:
#             dot.edge(node.parent.name, node.name)

#     # Guarda en un archivo temporal
#     graph_filename = "temp_graph"
#     image_path = os.path.abspath(os.path.join(script_dir, "..", "informe", "imagenes", graph_filename))
#     dot.render(image_path, cleanup=True)
#     # Crear la interfaz de streamlit
#     st.title("Arbol de Mensajes")

#     tree_image = Image.open("informe/imagenes/temp_graph.png")
#     st.image(tree_image, caption="Árbol de Mensajes", use_column_width=True, output_format="PNG")

from treelib import Tree, Node
import streamlit as st
from PIL import Image
from informe.constantes import Constants

def arbol():
    st.image("informe/imagenes/price.png", caption='Precio de 1000 aperturas y 1000 mensajes', use_column_width=True)
    st.image("informe/imagenes/mensaje.png", caption='Mensaje utilizado para campaña', use_column_width=True)

    tupla = Constants().main()

    # Crear un objeto Tree
    tree = Tree()

    # Agregar nodos al árbol
    root_node = tree.create_node("Arbol", "Arbol")
    mensajes_node = tree.create_node(f"Mensajes {tupla[0]}", f"Mensajes {tupla[0]}", parent="Arbol")
    responde_node = tree.create_node(f"Responde {tupla[1]}", f"Responde {tupla[1]}", parent=f"Mensajes {tupla[0]}")
    si_node = tree.create_node(f"Si, me encantaría {tupla[2]}", f"Si, me encantaría {tupla[2]}", parent=f"Responde {tupla[1]}")
    si_porcentaje_node = tree.create_node(f"Porcentaje de derivación {tupla[7]}", f"Porcentaje de derivación {tupla[7]}", parent=f"Si, me encantaría {tupla[2]}")
    no_porcentaje_node = tree.create_node(f"Porcentaje de no derivación {tupla[8]}", f"Porcentaje de no derivación {tupla[8]}", parent=f"Si, me encantaría {tupla[2]}")
    no_en_otro_momento_node = tree.create_node(f"No en otro momento {tupla[5]}", f"No en otro momento {tupla[5]}", parent=f"Responde {tupla[1]}")
    no_responde_node = tree.create_node(f"No responde {tupla[6]}", f"No responde {tupla[6]}", parent=f"Mensajes {tupla[0]}")

    # Visualizar el árbol
    st.title("Arbol de Mensajes")
    tree.show()

    # Opcionalmente, exportar el árbol a formato PNG
    image_path = "informe/imagenes/arbol.png"
    tree.to_picture(image_path)
    tree_image = Image.open(image_path)
    st.image(tree_image, caption="Árbol de Mensajes", use_column_width=True, output_format="PNG")
