import flet as ft
from UI.view import View
from database.DAO import DAO
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view: View = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year = None
        self.dizionario = {}

    def populateMinDur(self):
        listDur = DAO.getDurata()
        minDur = float(listDur[0][0])
        return minDur

    def populateMaxDur(self):
        listDur = DAO.getDurata()
        maxDur = float(listDur[0][1])
        return maxDur

    def handle_graph(self, e):
        anno = self._view.dd_anno.value
        minDurata = self.populateMinDur()
        maxDurata = self.populateMaxDur()
        minDur = float(self._view.txt_durata_min.value)
        maxDur = float(self._view.txt_durata_max.value)
        if anno is None:
            self._view.create_alert("Shape non inserita")
            return
        elif minDur is None or minDur < minDurata:
            self._view.create_alert("Durata minima non valida")
            return
        elif maxDur is None or maxDur > maxDurata:
            self._view.create_alert("Durata massima non valida")
            return

        self._model.buildGraph(anno, minDur, maxDur)
        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))

        self.durate = self._model.conta(anno, minDur, maxDur)
        for durata in self.durate:
            self._view.txt_result1.controls.append(ft.Text(f" {durata[1]} nodi con durata {durata[0]} "))

        media = self._model.media(anno, minDur, maxDur)
        self._view.txt_result1.controls.append(ft.Text(f"La durata media degli avvistamenti nel grafo è: {media[0]}"))


        self._view.update_page()

    def handle_path(self, e):
        pass

    def fill_dd_anno(self):
        self._listYears = self._model.getYears() # shape = nodi

        for c in self._listYears:
            self._view.dd_anno.options.append(ft.dropdown.Option(c))
        self._view.update_page()

    def read_year(self, e):
        if e.control.value is None:
            self._year = None
        else:
            self._year = e.control.value


