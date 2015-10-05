Language used:Python
To run the code
  you might need to "chmod +x navigator" to give execution permissions
  for command line argument the library argparse is used, do you might need to "pip install argparse"
  (if pip is not installed then "apt-get install pip")

  ./navigator runs the code for A-star for path 1,20 to 20,1 and uses default graph file as ATM.graph.txt in the present directory
  ./navigator -h displays help as follows
usage: navigator [-h] [-f GRAPH_FILE] [--debug] [--no-debug] [-s SEARCH_TYPE]
                 [--print] [--no-print]
                 [points [points ...]]

positional arguments:
  points

optional arguments:
  -h, --help            show this help message and exit
  -f GRAPH_FILE, --file GRAPH_FILE
                        input graph file
  --debug               set debug flag True
  --no-debug            set debug flag False, default is False
  -s SEARCH_TYPE, --search SEARCH_TYPE
                        can have values: astar, gbfs, bfs, dfs. Default is
                        a_star
  --print               display so as to get output for graphical display on
                        webpage
  --no-print            Default display as mentioned in the HW handout


A sample execution would be:
./navigator 1 20 20 1 -s bfs
runs BFS for 1,20 to 20,1
./navigator 13 6 7 6 -s astar --debug
runs ASTAR for 13,6 to 7,6 and also displays debug messages
./navigator 1 1 20 20 -f ATM.graph.txt -s dfs
runs DFS for 1,1 to 20,20 with ATM.graph.txt as graph file

options:
-s bfs/dfs/gbfs/astar
--debug for debug messages
--print displays solution so that it can be pasted into webpage for graphical display
-f <FILENAME> path to input graph file
-h help menu
