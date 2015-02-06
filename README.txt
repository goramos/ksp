KSP v1.22

DESCRIPTION
Compute the K shortest loopless paths between two nodes of a given graph, using Yen's algorithm [1].

USAGE
python KSP.py [-h] -f FILE -l OD_LIST -k K

	-h, --help	show this help message and exit
	-f FILE		the graph file
	-l OD_LIST	list of OD-pairs, in the format 'O|D;O|D;[and so on]', where O are valid origin nodes, and D are valid destination nodes
	-k K		number of shortest paths to find

GRAPH FILE FORMATTING INSTRUCTIONS
The graph file supports three types of graphs' entities: node, edge, arc. When creating the graph file, provide just one entity per line. 
Usage:
	node NAME		nodes of the graph
	edge N1 N2 W	create an undirected link between N1 and N2 with weight W
	arc N1 N2 W		create a directed link from N1 to N2 with weight W

	Example 1 - an undirected graph:
		node A
		node B
		edge A B 10

	Example 2 - producing Example 1 with a directed graph:
		node A
		node B
		arc A B 10
		arc B A 10

REFERENCES
[1] Yen, J.Y.: Finding the k shortest loopless paths in a network. Management Science 17(11) (1971) 712-716.

AUTHOR
Created in February 10, 2014, by Gabriel de Oliveira Ramos <goramos@inf.ufrgs.br>.
