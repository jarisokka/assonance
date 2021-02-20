import geonamescache

def get_locations():
    gc = geonamescache.GeonamesCache()
    locations = list(gc.get_countries().values())
    converted_locations= []
    for country in locations:
        converted_locations.append((country["name"].lower(), country["name"]))

    return converted_locations

def get_genres():
    genres = ["Blues","Classic Rock","Country","Dance","Disco","Funk","Grunge",
    "Hip-Hop","Jazz","Metal","New Age","Oldies","Other","Pop","R&B",
    "Rap","Reggae","Rock","Techno","Industrial","Alternative","Ska",
    "Death Metal","Pranks","Soundtrack","Euro-Techno","Ambient",
    "Trip-Hop","Vocal","Jazz+Funk","Fusion","Trance","Classical",
    "Instrumental","Acid","House","Game","Sound Clip","Gospel",
    "Noise","AlternRock","Bass","Soul","Punk","Space","Meditative",
    "Instrumental Pop","Instrumental Rock","Ethnic","Gothic",
    "Darkwave","Techno-Industrial","Electronic","Pop-Folk",
    "Eurodance","Dream","Southern Rock","Comedy","Cult","Gangsta",
    "Top 40","Christian Rap","Pop/Funk","Jungle","Native American",
    "Cabaret","New Wave","Psychadelic","Rave","Showtunes","Trailer",
    "Lo-Fi","Tribal","Acid Punk","Acid Jazz","Polka","Retro",
    "Musical","Rock & Roll","Hard Rock","Folk","Folk-Rock",
    "National Folk","Swing","Fast Fusion","Bebob","Latin","Revival",
    "Celtic","Bluegrass","Avantgarde","Gothic Rock","Progressive Rock",
    "Psychedelic Rock","Symphonic Rock","Slow Rock","Big Band",
    "Chorus","Easy Listening","Acoustic","Humour","Speech","Chanson",
    "Opera","Chamber Music","Sonata","Symphony","Booty Bass","Primus",
    "Porn Groove","Satire","Slow Jam","Club","Tango","Samba",
    "Folklore","Ballad","Power Ballad","Rhythmic Soul","Freestyle",
    "Duet","Punk Rock","Drum Solo","Acapella","Euro-House","Dance Hall"]
    converted_genres = [] 
    for genre in genres: 
        converted_genres.append((genre.lower(), genre))

    return converted_genres

def get_instruments():
    instruments = [
        "accordian",
        "air horn",
        "baby grand piano",
        "bagpipe",
        "banjo",
        "bass guitar",
        "bassoon",
        "bugle",
        "calliope",
        "cello",
        "clarinet",
        "clavichord",
        "concertina",
        "didgeridoo",
        "dobro",
        "dulcimer",
        "fiddle",
        "fife",
        "flugelhorn",
        "flute",
        "French horn",
        "glockenspiel",
        "grand piano",
        "guitar",
        "harmonica",
        "harp",
        "harpsichord",
        "hurdy-gurdy",
        "kazoo",
        "kick drum",
        "lute",
        "lyre",
        "mandolin",
        "marimba",
        "mellotran",
        "melodica",
        "oboe",
        "pan flute",
        "piano",
        "piccolo",
        "pipe organ",
        "saxaphone",
        "sitar",
        "sousaphone",
        "tambourine",
        "theremin",
        "trombone",
        "tuba",
        "ukulele",
        "viola",
        "violin",
        "vuvuzela",
        "washtub bass",
        "xylophone",
        "zither"]
    converted_instruments = [] 
    for instrument in instruments: 
        converted_instruments.append((instrument.lower(), instrument.capitalize()))
    return converted_instruments