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
graph_file = 'example_graphs/ortuzar10.1.txt' # the graph of the traffic network (the file format is specified by the algorithm's help)
origin = 'A'                                  # the origin node
destination = 'L'                             # the destionation node
K = 4                                         # the number of paths to find

# run the algorithm (return the K routes and associated costs of the given origin-destination pair)
routes = KSP.getKRoutes(graph_file, origin, destination, K)

# print routes
for i in routes:
	
	# the route as a list of strings, where each element corresponds to a link's name
	route = i[0]
	
	# the cost of the route (a float value)
	cost = i[1]
	
	print '%s has cost %.2f' % (route, cost)
