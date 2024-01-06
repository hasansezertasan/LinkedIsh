from typing import Any, Callable


class NavbarLink:
    def __init__(
        self,
        name: str,
        endpoint: str,
        url_for: Callable = None,
    ):
        self.name: str = name
        """The name of the link."""
        self.endpoint: str = endpoint
        """The endpoint to resolve."""
        self.url_for: Callable = url_for
        """The url_for function to resolve the endpoint."""

    def is_active(self, request: Any):
        return request.endpoint == self.endpoint

    def get_attrs(self, request: Any):
        attrs = {}
        attrs["class"] = "nav-link"
        attrs["href"] = self.url_for(self.endpoint)
        if self.is_active(request):
            attrs["aria-current"] = "page"
            attrs["class"] = "nav-link active"
        attrs = " ".join([f'{k}="{v}"' for k, v in attrs.items()])
        return attrs

    def get_link(self, request: Any):
        return f'<li class="nav-item"><a {self.get_attrs(request)}>{self.name}</a></li>'


class Navbar:
    def __init__(
        self,
        url_for: Callable = None,
    ):
        self.links: list[NavbarLink] = []
        """The links to show in the navbar."""
        self.right_buttons: list[NavbarLink] = []
        """The buttons to show in the right side of the navbar."""
        self.url_for: Callable = url_for
        """The url_for function to resolve the endpoint."""

    def add_link(self, link: NavbarLink):
        """Adds a link to the navbar."""
        link.url_for = self.url_for
        self.links.append(link)

    def add_right_button(self, button: NavbarLink):
        """Adds a button to the right side of the navbar."""
        self.right_buttons.append(button)

    def get_links(self, request: Any):
        """Gets the HTML element of the navbar."""
        links = "".join([link.get_link(request) for link in self.links])
        return f'<ul class="navbar-nav me-auto mb-2 mb-md-0">{links}</ul>'

    def inject_navbar(self):
        """Injects the navbar into the context."""
        return dict(navbar=self)

    def init_app(self, app: Any):
        """Initializes the navbar for the given app."""
        app.context_processor(self.inject_navbar)
