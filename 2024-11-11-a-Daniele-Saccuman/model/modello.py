
from database.DAO import DAO
import networkx as nx




class Model:
    def __init__(self):
        self._listYears = []
        self._nodi = []
        self._idMap = {}
        self._grafo = nx.DiGraph()

    def getYears(self):
        self._listYears = DAO.getAllYears()
        return self._listYears

    def buildGraph(self, anno, minDur, maxDur):
        self._grafo.clear()
        self._nodi = DAO.get_all_sightings(anno, minDur, maxDur)
        for s in self._nodi:
            self._idMap[s.id] = s

        self._grafo.add_nodes_from(self._nodi)
        self._archi = DAO.getAllEdges(anno, minDur, maxDur)
        self.dizio = {}
        for e in self._archi:
            if e[1] < e[3]:
                self._grafo.add_edge(self._idMap[e[0]], self._idMap[e[2]])
            elif e[1] > e[3]:
                self._grafo.add_edge(self._idMap[e[2]], self._idMap[e[0]])
            elif e[1] == e[3]:
                self._grafo.add_edge(self._idMap[e[0]], self._idMap[e[2]])
                self._grafo.add_edge(self._idMap[e[2]], self._idMap[e[0]])


    def conta(self, anno, minDur, maxDur):
        self.listaDurate = DAO.getAllDurate(anno, minDur, maxDur)
        return self.listaDurate

    def media(self, anno, minDur, maxDur):
        media = DAO.getMedia(anno, minDur, maxDur)
        return media

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)
