""" \\ AGENDA : A Farewell Day Greet to my cast and crew \\"""

from datetime import date
import emoji

### Variables - My Memory Space

Json_data = {
    "MOVIE_NAME": "No Again",
    "PRODUCERS": [
        "R, Rajaram (RR)",
        "Muthuswamy, Rajesh",
        "Jyothi Gadikal Krishnamurthy",
    ],
    "THE_DIRECTOR": "Subash, Ebenezer Joyson",
    "HERO_TEAM": "APP Migration Factory Unix Team Members",
    "EXECUTIVE_PRODUCER": "Schofield, Steve",
    "VILLAN_TEAM": ["Scrum Leads", "MMs", "MPMs", "Command Center"],
    "ART_DIRECTORS": (
        "Application Team",
        "Oracle Team",
        "Tiger Team",
        "Network/Firewall Team",
        "CTB Team",
        "RTB Team",
        "Patching Team",
    ),
    "PRODUCTION_YEARS": 5.2,
    "SCENE1_TAKE1_DATE": date(2017, 1, 11),
    "FINALSCENE_FINALTAKE_DATE": date(2022, 4, 22),
}

Film_Credits = """
It's been an honour to work with this entire cast and crew and made the movie
=============================================================================

\t\t\t\t\t\t\t   ============
\t\t\t\t\t\t\t   | {} |
\t\t\t\t\t\t\t   ============

\t\t\t\t\t\t\t {} a BlockBuster 

 From the day 1 till date the makeover of the film is an awestruck process.

\t\t\t\t I would like to splash my special thanks to 

\t\t\t\t\t\t\t  {}
""".format(
    Json_data["MOVIE_NAME"], emoji.emojize(":grinning_face_with_big_eyes:"),
    "\n".join(Json_data["PRODUCERS"])
)

print(Film_Credits)
