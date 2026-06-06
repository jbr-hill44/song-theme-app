from dash import Dash, dcc, html, page_container
import dash_bootstrap_components as dbc


app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div("Song Theme App", className="app-eyebrow"),
                        html.H1("Collect song picks for your weekly theme.", className="app-title"),
                        html.P(
                            "Invite people to search Spotify, submit a track, and let you approve the final playlist.",
                            className="app-subtitle",
                        ),
                    ],
                    className="hero-copy",
                ),
                html.Div(
                    [
                        dcc.Link("Submit a song", href="/", className="nav-link"),
                        dcc.Link("Admin", href="/admin", className="nav-link"),
                    ],
                    className="hero-nav",
                ),
            ],
            className="hero-shell",
        ),
        html.Main(page_container, className="page-shell"),
    ],
    className="app-shell",
)


if __name__ == "__main__":
    app.run(debug=True)
