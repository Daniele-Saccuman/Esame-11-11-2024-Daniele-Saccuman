import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP 2024 - Esame del 11/11/2024 - A"
        self._page.horizontal_alignment = 'CENTER'
        self._page.window_width = 950
        self._page.window_height = 800
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # title
        self._title = None
        # first row
        self.txt_durata_min: ft.TextField = None
        self.txt_durata_max: ft.TextField = None
        self.dd_anno: ft.Dropdown = None

        self.btn_graph = None
        self.btn_path = None
        # second row
        self.txt_result1 = None  # Qui scrivere gli outputs del punto 1
        self.txt_result2 = None  # Qui scrivere gli outputs del punto 2

    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Esame del 16-09-2024 - A", color="blue", size=24)
        self._page.controls.append(self._title)

        # First row with some controls
        self.txt_durata_min = ft.TextField(label="Durata minima degli avvistamenti", hint_text="inserire una durata")
        self.txt_durata_max = ft.TextField(label="Durata massima degli avvistamenti", hint_text="inserire una durata")
        self.dd_anno = ft.Dropdown(label="Anno",
                                   hint_text="Anno da considerare per gli avvistamenti.")
        self._controller.fill_dd_anno()

        row1 = ft.Row([self.txt_durata_min, self.txt_durata_max, self.dd_anno],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        self._page.controls.append(row1)

        # Second row with some controls
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo",
                                           tooltip="Crea il grafo del punto 1",
                                           on_click=self._controller.handle_graph)
        self.btn_path = ft.ElevatedButton(text="Calcola percorso",
                                          tooltip="Risolvi il punto 2",
                                          on_click=self._controller.handle_path)
        self.btn_path.disabled = True

        row2 = ft.Row([self.btn_graph, self.btn_path],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        self._page.controls.append(row2)


        # List View where the reply is printed
        self.txt_result1 = ft.ListView(width=400, expand=1, spacing=10, padding=20, auto_scroll=False)
        self.txt_result2 = ft.ListView(width=400, expand=1, spacing=10, padding=20, auto_scroll=False)
        self.txt_result1.controls.append(ft.Text("Risultati punto1"))
        self.txt_result2.controls.append(ft.Text("Risultati punto2"))

        container1 = ft.Container(
            content=self.txt_result1,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREY_200,
            width=450,
            height=550,
            border_radius=10,
        )
        container2 = ft.Container(
            content=self.txt_result2,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREY_200,
            width=450,
            height=550,
            border_radius=10,
        )

        row3 = ft.Row([container1, container2],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                      spacing=50)
        self._page.controls.append(row3)
        self._page.update()

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()