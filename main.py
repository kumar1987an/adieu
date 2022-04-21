""" \\ AGENDA : A Farewell Day Greet to my cast and crew \\"""

from datetime import date
import emoji

### Variables - My Memory Space

Json_data = {
    "MOVIE_NAME":
    "Back Home",
    "producers": [
        "R, Rajaram (RR)",
        "Muthuswamy, Rajesh",
        "Jyothi Gadikal Krishnamurthy",
    ],
    "THE_DIRECTOR":
    "Subash, Ebenezer Joyson",
    "HERO_TEAM":
    "Factory Unix",
    "EXECUTIVE_PRODUCER":
    "Schofield, Steve",
    "villain_team": ["Scrum Leads", "MMs", "MPMs", "Command Center"],
    "art_directors": (
        "Application Team",
        "Oracle Team",
        "Tiger Team",
        "Network/Firewall Team",
        "CTB Team",
        "RTB Team",
        "Patching Team",
    ),
    "PRODUCTION_YEARS":
    5.2,
    "SCENE1_TAKE1_DATE":
    date(2017, 1, 11),
    "FINALSCENE_FINALTAKE_DATE":
    date(2022, 4, 22),
}

PRODUCERS = (i for i in Json_data["producers"])
ART_DIRECTORS = (j for j in Json_data["art_directors"])
VILLAIN_TEAM = (k for k in Json_data["villain_team"])

Film_Credits = f"""
                                    ***************
                                    * END CREDITS *
                                    ***************
            
                DISCLAIMER: JUST 4 FUN NO HARD FEELINGS
                ^^^^^^^^^^
        
                SCENE1 TAKE1 DATE: {Json_data['SCENE1_TAKE1_DATE'].strftime("%d-%B-%Y")}
                
                LAST DAY OF SHOOT: {Json_data['FINALSCENE_FINALTAKE_DATE'].strftime("%d-%B-%Y")}


        It's been an honour to work with our entire cast and crew have made this movie

                                    ============
                                    | {Json_data['MOVIE_NAME']} |
                                    ============
                        
                                  {emoji.emojize(':dollar_banknote:')} a BlockBuster 


          From the day 1 till date the makeover of the film is an awestruck process.


          <<< I would like to splash my special thanks to my Fantabulous Producers >>>
                            

                                {emoji.emojize(':partying_face:')} {next(PRODUCERS)}
                        
                                {emoji.emojize(':face_with_monocle:')} {next(PRODUCERS)}
                        
                                {emoji.emojize(':flexed_biceps:')} {next(PRODUCERS)}


               Without a captain there is no ship he is our multi-faceted Director
                            ---<---<---<---<---<---<---<---<---<--

                                {emoji.emojize(':cinema:')} {Json_data["THE_DIRECTOR"]}


                 Special Credits to our Proactive & Stupendous Executive Producer 
                            ---+---+---+---+---+---+---+---+---+--

                                {emoji.emojize(':briefcase:')} {Json_data["EXECUTIVE_PRODUCER"]}


                     Making audience convinced to reality is always complex.
                       Infinite Thanks for my Curated Art Directors Team
                            -+---+---+---+---+---+---+---+---+---+--

                                {emoji.emojize(':woman_technologist:')} {next(ART_DIRECTORS)}
                    
                                {emoji.emojize(':man_technologist:')} {next(ART_DIRECTORS)}
                    
                                {emoji.emojize(':tiger:')} {next(ART_DIRECTORS)}
                    
                                {emoji.emojize(':nut_and_bolt:')} {next(ART_DIRECTORS)}
                    
                                {emoji.emojize(':chains:')} {next(ART_DIRECTORS)}
                    
                                {emoji.emojize(':fire:')} {next(ART_DIRECTORS)}
                    
                                {emoji.emojize(':puzzle_piece:')} {next(ART_DIRECTORS)}


                     Welcome to the World of our Monstrous Villain team, 
                  Thank you guys for keeping us nail biting all action scenes
                        +---+---+---+---+---+---+---+---+---+---+--

                                {emoji.emojize(':skull:')} {next(VILLAIN_TEAM)}
                        
                                {emoji.emojize(':smiling_face_with_horns:')} {next(VILLAIN_TEAM)}
                        
                                {emoji.emojize(':alien_monster:')} {next(VILLAIN_TEAM)}
                        
                                {emoji.emojize(':vampire:')} {next(VILLAIN_TEAM)}


                        Hero Team always Hero to their self & others, 
                                I proudly present my Hero team
                            {emoji.emojize(':party_popper:') * 15}

                                {emoji.emojize(':person_in_tuxedo:')} {Json_data["HERO_TEAM"]}


            The entire journey of carving this action movie we faced lot of hair pin 
            bends. Happiness, Emptiness, Joy of Finishing a day of shoot, 
            Completeness of a stunt sequence, Tiredness of capturing lengthy chasing 
            scenes on a never ending road. 
    
            At the end of the day we all sleep good with cherising feel of counting 
            every day of the movie shoot.
    
            I Believe you all like the movie very much. Please watch in near cinemas 
            around you, no piracy it is a painstaking hardwork of 300+ crew members.
    
            I will meet in my next movie at Cinema hall not as cast & crew members, 
            you all know I used to police something new in my each movies including 
            cast and crew members gives me immense ideas and creativity.
    
            Thank you all for helping me to complete this movie. 
            Time to loosen the curtain.
            See you all in big screen again.
    
            You can reach back me through
            -----------------------------
            Android:   +919884011997
            POP3/IMAP: kmrnr1987@gmail.com
            
            SCROLL UP {emoji.emojize(':index_pointing_up:')}
            """

print(Film_Credits)
