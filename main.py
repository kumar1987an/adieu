""" \\ AGENDA : A Farewell Day Greet to my cast and crew \\"""

from datetime import date
import emoji

### Variables - My Memory Space

Json_data = {
    "MOVIE_NAME": "No Again",
    "producers": [
        "R, Rajaram (RR)",
        "Muthuswamy, Rajesh",
        "Jyothi Gadikal Krishnamurthy",
    ],
    "THE_DIRECTOR": "Subash, Ebenezer Joyson",
    "HERO_TEAM": "APP Migration Factory Unix Team Members",
    "EXECUTIVE_PRODUCER": "Schofield, Steve",
    "VILLAN_TEAM": ["Scrum Leads", "MMs", "MPMs", "Command Center"],
    "art_directors": (
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

PRODUCERS = (i for i in Json_data["producers"])
ART_DIRECTORS = (j for j in Json_data["art_directors"])

Film_Credits = f"""
It's been an honour to work with this entire cast and crew and made the movie
-----------------------------------------------------------------------------

\t\t\t\t\t\t\t   ============
\t\t\t\t\t\t\t   | {Json_data['MOVIE_NAME']} |
\t\t\t\t\t\t\t   ============

\t\t\t\t\t\t\t {emoji.emojize(':dollar_banknote:')} a BlockBuster 

 From the day 1 till date the makeover of the film is an awestruck process.

\t\t\tI would like to splash my special thanks to Producers
\t\t\t--->--->--->--->--->--->--->--->--->--->--->--->--->-

\t\t\t\t\t\t  {emoji.emojize(':partying_face:')} {next(PRODUCERS)}

\t\t\t\t\t     {emoji.emojize(':face_with_monocle:')} {next(PRODUCERS)}

\t\t\t\t\t   {emoji.emojize(':flexed_biceps:')} {next(PRODUCERS)}


\tWithout a captain there is no ship he is our multi-faceted Director
\t---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---

\t\t\t\t\t\t {emoji.emojize(':cinema:')} {Json_data["THE_DIRECTOR"]}


\t  Special Thanks to our proactive & stupendous Executive Producer 
\t  ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---

\t\t\t\t\t\t\t {emoji.emojize(':briefcase:')} {Json_data["EXECUTIVE_PRODUCER"]}


\t\t Making audience convinced to reality is always complex, 
\t\t   Countless Thanks for my Curated Art Director(s) Team
\t\t {emoji.emojize(':man_mage:')}--+---+---+---+---+---+---+---+---+---+---+---+---+--{emoji.emojize(':woman_mage:')}

\t\t\t\t\t\t   {emoji.emojize(':woman_technologist:')} {next(ART_DIRECTORS)}

\t\t\t\t\t\t   {emoji.emojize(':man_technologist:')} {next(ART_DIRECTORS)}

\t\t\t\t\t\t   {emoji.emojize(':tiger:')} {next(ART_DIRECTORS)}

\t\t\t\t\t\t   {emoji.emojize(':nut_and_bolt:')} {next(ART_DIRECTORS)}

\t\t\t\t\t\t   {emoji.emojize(':chains:')} {next(ART_DIRECTORS)}

\t\t\t\t\t\t   {emoji.emojize(':fire:')} {next(ART_DIRECTORS)}

\t\t\t\t\t\t   {emoji.emojize(':puzzle_piece:')} {next(ART_DIRECTORS)}


"""

print(Film_Credits)
