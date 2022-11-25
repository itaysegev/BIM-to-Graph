# BIM-to-Graph
The BIM to GNN  will establish the feasibility of using Graph Neural Networks (GNN) on data derived from Building Information Models (BIM). BIM models are a state-of-the-art method of producing and storing Architectural and Engineering information. However, their complicated data format prevents them from being used as a basis for Machine Learning. This project will establish a workflow which will be able to translate BIM derived data into property graphs such as Neo4J and enrich the graph with geometrical information derived from the 3D BIM model. Later, the property graph will be used as a basis for a GNN node classification task such as recognizing the wall type. The developed method will demonstrate the strengths of using GNN in the architectural domain and pave the way to changing the way BIM is stored and represented.

Research stages:
1.       Establishment of a BIM dataset –In progress, headed by Prof. Yasha Grobman
2.       Definition of the required properties and relations – In progress, headed By Dr. Tanya Bloch
3.       Extraction of BIM data into a textual, machine and human readable format – In Progress , Headed by Dr. Austern, based on research from PhD candidate Zijian Wang
4.       Enrichment of the textual data with Geometric information and translation to a property graph format. Headed by Dr. Austern
5.       Training a GNN to classify wall types Headed by Dr. Austern
