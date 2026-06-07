from dash import dcc, html
import dash
from db.database import SessionLocal
from db.models import Theme
from datetime import date


dash.register_page(__name__, path="/", name="Submit")


def build_result_card(title, artist, album, duration, accent):
    return html.Div(
        [
            html.Div(className="result-art", style={"background": accent}),
            html.Div(
                [
                    html.Div(title, className="result-title"),
                    html.Div(artist, className="result-artist"),
                    html.Div(f"{album} • {duration}", className="result-meta"),
                    html.Button("Submit this song", className="result-button"),
                ],
                className="result-copy",
            ),
        ],
        className="result-card",
    )


def get_current_theme(day):
    db = SessionLocal()
    current_theme = (
        db.query(Theme.title, Theme.description)
        .filter(Theme.start_date <= day, Theme.end_date >= day)
        .order_by(Theme.start_date.desc())
        .first()
    )
    db.close()
    return current_theme

def layout():
    current_theme = get_current_theme(date.today())

    layout = html.Div(
        [
            html.Section(
                [
                    html.Div(
                        [
                            html.Div("Current theme", className="section-label"),
                            html.H2(current_theme[0] if current_theme else "No theme set", className="theme-title"),
                            html.H3(current_theme[1] if current_theme else "Check back later for this week's theme!", className="theme-subtitle"),
                            html.P(
                                "Pick a song that fits the brief. All submissions are reviewed before being added to the playlist.",
                                className="theme-description",
                            ),
                        ],
                        className="theme-copy",
                    ),
                    html.Div(
                        [
                            html.Div("This week's playlist vibe", className="stat-label"),
                            html.Div("Playful, nostalgic, and easy to sing along to", className="stat-value"),
                        ],
                        className="theme-stat",
                    ),
                ],
                className="theme-banner",
            ),
            html.Section(
                [
                    html.Div(
                        [
                            html.Div("Search Spotify", className="section-label"),
                            html.H3("Find the track you want to submit", className="section-title"),
                            html.P(
                                "Search is not wired up yet, but the layout below is ready for the Spotify integration.",
                                className="section-description",
                            ),
                        ],
                        className="section-header",
                    ),
                    html.Div(
                        [
                            dcc.Input(
                                id="spotify-search",
                                type="text",
                                placeholder="Try: 505, 7 rings, One More Time",
                                className="search-input",
                            ),
                            html.Button("Search", className="search-button"),
                        ],
                        className="search-row",
                    ),
                    html.Div(
                        [
                            build_result_card("One More Time", "Daft Punk", "Discovery", "5:20", "linear-gradient(135deg, #f8d66d, #ef8f6b)"),
                            build_result_card("7 rings", "Ariana Grande", "thank u, next", "2:58", "linear-gradient(135deg, #8fd3f4, #84fab0)"),
                            build_result_card("505", "Arctic Monkeys", "Favourite Worst Nightmare", "4:13", "linear-gradient(135deg, #f6a6b2, #fbc2eb)"),
                        ],
                        className="results-grid",
                    ),
                ],
                className="content-card",
            ),
            html.Section(
                [
                    html.Div(
                        [
                            html.Div("Submission details", className="section-label"),
                            html.H3("Tell us who this pick is from", className="section-title"),
                        ],
                        className="section-header",
                    ),
                    html.Div(
                        [
                            html.Label("Your name", htmlFor="submitter-name", className="field-label"),
                            dcc.Input(
                                id="submitter-name",
                                type="text",
                                placeholder="James",
                                className="text-input",
                            ),
                        ],
                        className="field-group",
                    ),
                    html.Div(
                        [
                            html.Label("Optional comment", htmlFor="submitter-comment", className="field-label"),
                            dcc.Textarea(
                                id="submitter-comment",
                                placeholder="Why does this song fit the theme?",
                                className="textarea-input",
                            ),
                        ],
                        className="field-group",
                    ),
                    html.Div(
                        [
                            html.Button("Submit song", className="submit-button"),
                            html.Div("Your song will go into the review queue for approval.", className="form-note"),
                        ],
                        className="submit-row",
                    ),
                ],
                className="content-card",
            ),
        ]
)
    return layout

layout()



