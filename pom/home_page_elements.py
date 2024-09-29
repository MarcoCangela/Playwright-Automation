class HomePage:
    def __init__(self,page):
        self.welcome = page.get_by_role("heading", name="Welcome!")
        self.contacto = page.get_by_role("link", name="Contact")
