class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Переход на страницу с группами
        self.open_group_page()
        wd.find_element_by_name("new").click()
        # Заполнение формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Сохранение данных формы
        wd.find_element_by_name("submit").click()
        # Возврат на страницу со списком групп
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()