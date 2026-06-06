import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from db.database import SessionLocal
from db.models import Theme
from datetime import date, timedelta

dash.register_page(__name__, path="/admin", name="Admin")

def build_theme_upload_notification(title, status="success"):
    return dbc.Toast(
        [html.P(f"Theme saved successfully: {title}", className="mb-0")],
        id="theme-status-message",
        header="Theme Upload Status",
        icon=status,
        duration=2000,
        is_open=False,
    )

layout = html.Div(
    [
        html.Div(
            [
                html.Div("Submission 1", className="submission-card"),
                html.Div("Submission 2", className="submission-card"),
                html.Div("Submission 3", className="submission-card"),
            ],
            className="submission-list",
        ),
        html.H1("Admin Page", className="admin-title"),
        html.P(
            "This page is for admins to review song submissions and manage the playlist. It is not accessible to regular users.",
            className="admin-description",
        ),
        dbc.Button("Create Theme", id="open-theme-modal", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create New Theme")),
                dbc.ModalBody(
                    [
                        dbc.Label("Theme title"),
                        dbc.Input(id="theme-title", type="text"),
                        dbc.Label("Theme description"),
                        dbc.Textarea(id="theme-description"),
                    ],
            ),
        dbc.ModalFooter(
            [
                dbc.Button("Cancel", id="close-theme-modal", color="secondary"),
                dbc.Button("Save theme", id="save-theme", color="primary", n_clicks=0),
            ]
        ),
    ],
        id="theme-modal",
        is_open=False,
    ),
    build_theme_upload_notification(""),
    ],
    className="admin-shell",
)

@callback(
    Output("theme-modal", "is_open",
           allow_duplicate=True),
    Input("open-theme-modal", "n_clicks"), 
    Input("close-theme-modal", "n_clicks"),
    State("theme-modal", "is_open"),
    prevent_initial_call=True,
)
def toggle_theme_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open

@callback(
        Output("theme-modal", "is_open",
               allow_duplicate=True),
        Output("theme-status-message", "children"),
        Output("theme-status-message", "is_open"),
        Input("save-theme", "n_clicks"),
        State("theme-title", "value"),
        State("theme-description", "value"),
        prevent_initial_call=True,
)
def save_new_theme(n_clicks, title, description):
    if n_clicks > 0:
        db = SessionLocal()
        try:
            theme = Theme(title=title, description=description, start_date=date.today(), end_date=date.today() + timedelta(days=14))
            db.add(theme)
            db.commit()
            print(f"Saving new theme: {title} - {description}")
            return False, html.P(f"Theme saved successfully: {title}"), True
        except Exception as e:
            print(f"Error saving theme: {e}")
            return True, html.P(f"Error saving theme: {e}"), False
        finally:
            db.close()