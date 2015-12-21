'''
Example of KSP call from external applications

This code presents an example on how to call the KSP algorithm by external
applications in Python. Here we show:
 - what parameters are needed
 - how to call the KSP algorithm
 - how to handle the algorithm's output

Created on June 5, 2014 by Gabriel de Oliveira Ramos <goramos@inf.ufrgs.br>
'''

#import the KSP source
import KSP

# parameters to be passed to the KSP algorithm
graph_file = 'example_graphs/OW.txt'                # the graph of the traffic network (the file format is specified by the algorithm's help)
ODpairs = [['A','L'],['A','M'],['B','L'],['B','M']] # the list of origins and destinations
K = 4                                               # the number of paths to find

# generate the list of vertices and edges from the network file
V, E = KSP.generateGraph(graph_file)

# for each OD pair
for od in ODpairs:

	print 'Pair %s|%s' % (od[0], od[1])
	
	# run the algorithm (return the K routes and associated costs of the given origin-destination pair)
	routes = KSP.getKRoutes(V, E, od[0], od[1], K)
	
	# print the routes
	for i in routes:
		
		# the route as a list of strings, where each element corresponds to a link's name
		route = i[0]
		
		# the cost of the route (a float value)
		cost = i[1]
		
		print '%s has cost %.2f' % (route, cost)
