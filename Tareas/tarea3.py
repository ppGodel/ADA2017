#heurisitca grasp para sat 
import files.heuristicaksat
import generadorksat
generadorksat.generarkSat(100, 300, True)
print(files.heuristicaksat.heuristicgrasp('files/cnft.txt', 30, 0.1))
