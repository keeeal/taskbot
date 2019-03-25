noun = {
    "cheese[| and tomato] toasty": 1,
    "dog": 0.2,
    "circular thing": 1,
    "kitchen appliance": 1,
    "[|instant ]coffee": 0.5,
    "pinger": 1,
    "potato lum": 1,
    "[Magna|V8]": 1,
    "stringer": 1,
    "[pen|wowstick]": 1,
    "koofka": 1,
    "[danga|weeb]": 0.5,
    "cheezel": 1,
    "pickle": 1,
    "beer": 1,
    "fast food wrapper": 1,
    "piece of paper": 1,
    "[|RGB ]keyboard": 1,
    "mouse": 1,
    "fidget spinner": 1,
    "Nickleback album": 1,
    "pizza": 1,
    "[coles|weed] cookie": 1,
    "croissant": 1,
}

nouns = {
    "cheese[| and tomato] toasties": 1,
    "dogs": 1,
    "circular things": 1,
    "kitchen appliances": 1,
    "[|instant ]coffees": 0.5,
    "[|monster rehab ]pingers": 1,
    "potato lums": 1,
    "[Magnas|V8's]": 1,
    "stringers": 1,
    "[pens|wowsticks]": 1,
    "koofka fries": 1,
    "[dangas|weebs]": 1,
    "cheezels": 1,
    "pickles": 1,
    "beers": 1,
    "fast food wrappers": 1,
    "pieces of paper": 1,
    "[|RGB ]keyboards": 1,
    "mice": 1,
    "fidget spinners": 1,
    "socks that belong to [Perky|{person}]": 1,
    "Nickleback albums": 1,
    "slices of pizza": 1,
    "[coles|weed] cookies": 1,
    "croissants": 1,
}

concept = {
    "mystery skin": 1,
    "discord": 1,
    "[|bad |discord |beats|quoth]bot": 1,
    "Give Priv": 1,
    "[spotify|netflix] debt": 1,
    "[nut-2-butt|butt-2-nut]": 1,
    "reeeeeeeeee": 1,
    "green dot": 1,
    "pikagirl": 1,
    "chicken dinner": 1,
    "un-epic may-mays": 1,
    "CentreLink": 1,
    "food vids": 1,
    "r/[watchpeopledie|cringe]": 1,
    "[Destiny|Density][| debate]": 1,
    "Mr 100k": 1,
    "homework": 1,
    "sammasambuddhassa namo tasso bhagavato arahato": 1,
    "[hydroponic lettuce|'basil']": 1,
}

verb = {
    "[find|locate]": 1,
    "touch": 1,
    "diddle": 1,
    "hide": 1,
    "make a sculpture of": 1,
    "[make|create]": 1,
}

adj = {
    "nearby": 1,
    "weird": 1,
    "salty": 0.2,
    "funny looking": 1,
    "old": 1,
    "upside down": 1,
    "strange": 1,
    "tiny": 1,
}

time = {
    "one week": 1,
    "one day": 1,
    "one hour": 1,
    "ten minutes": 1,
    "one minute": 1,
    "thirty seconds": 1,
}

event = {
    "you next breathe out": 1,
    "the clock strikes midnight": 1,
    "Hexix next joins the chat": 1,
    "Logan next loses a game": 1,
    "Nano next talks about V8's": 1,
    "James H-Bean next drinks a beer": 1,
}

extreme = {
    "biggest": 1,
    "smallest": 1,
    "coolest": 1,
    "best": 3,
    "worst": 1,
    "most unexpected": 1,
    "weirdest looking": 2,
    "nearest": 1,
    "most circular": 1,
    "saltiest": 1,
    "nearest": 1,
    "most flamboyant": 1,
    "heaviest": 1,
    "first": 2,
    "most impressive": 3,
}

person = {
    "You, the reader": 0.2,
    "Perky": 1,
    "Jarrad": 1,
    "Travis": 1,
    "Keal": 1,
    "Logan": 1,
    "Nano": 1,
    "Chris": 1,
    "Beans": 0.5,
    "James H-Bean": 1,
    "Kyle": 1,
    "a stranger": 0.5,
    "not one of the boiss": 0.5,
}

place = {
    "Adelaide CBD": 1,
    "Flinders Uni": 1,
    "2 Cheviot Avenue": 3,
    "{person}'s bedroom": 2,
    "Denman park": 1,
    "Woolies": 1,
    "somewhere with [grass|water]": 1,
    "the {extreme} place[| you know]": 1,
}

number = {
    "2": 3,
    "3": 5,
    "5": 4,
    "10": 2,
    "20": 1,
}

money = {
    "no money": 2,
    "$[1|{number}][|.50|.69]": 5,
    "$4.20": 0.1,
}

game = {
    "Minecraft": 1,
    "PUBG": 1,
    "[League of Legends|Legal Lettuce]": 1,
    "Apex Legends": 1,
    "Mount Your Friends": 1,
    "Age of Empires": 1,
    "Words with Friends": 1,
    "StarCraft": 1,
    "Rocket League": 1,
    "Dota 2": 1,
    "Fortnite": 1,
    "World of Warcraft": 1,
    "Dungeons and Dragons": 1,
    "Warhammer": 1,
    "Overwatch": 1,
    "table tennis": 1,
    "Don Bradman cricket": 1,
    "Runescape": 2,
}

a_noun = {
    "[a|a {adj}|the {extreme}] {noun}": 1,
    "the closest object on your [left|right]": 0.1,
    "something": 0.2,
}

n_nouns = {
    "[|{number} ][|{adj} ]{nouns}": 1,
}

start = {
    "form two teams, then ": 1,
    "camouflage yourself, then ": 0.1,
    "starting at {place}, ": 1,
    "tie up {person}. He/she must then ": 1,
    "holding your hands behind your back at all times, ": 1,
    "everyone on Discord[| right now] must ": 1,
    "[your task is to|you must] ": 1,
    "without anyone else knowing, ": 1,
}

middle = {
    "{verb} [{a_noun}|{n_nouns}|a {noun}-related item]": 3,
    "get [{a_noun}|{n_nouns}] to [{person}|{place}]": 2,
    "get {a_noun} across a[n| makeshift] obstacle course": 0.5,
    "buy [{a_noun}|{a_noun} for {person}|the {extreme} gift for {person}] with {money}": 1,
    "[play|live stream|win|lose] a game of {game}[| with {person}| vs. {person}]": 1,
    "[say|write down|post in discord] as many types of {noun} as possible": 1,
    "balance [{a_noun}|at least {number} {nouns}|as many {nouns} as possible] on [a {noun}|your head]": 2,
    "draw[| a picture of|, using MS paint,|, using only condiments,] [{a_noun}|a portrait of {person}|what '{concept}' means to you]": 2,
    "make a Discord chat for all things '[{noun}|{concept}]' related": 1,
    "collect the lowest unique number of {nouns}": 1,
    "hold a {noun} and a {noun} in the same hand without the two touching": 1,
    "secretly steal [a {noun}|{money}] from {person}[| then give it back]": 1,
    "get {person}'s attention using [his/her middle name|a {noun}]": 1,
    "describe a trailer for '{concept}: the movie[| 2| 2 - revenge of the {nouns}]'": 0.2,
    "({person}) hide yourself. Everyone else must find you": 1,
}

end = {
    " without speaking any English": 1,
    " as fast as possible": 1,
    ". You have {time}[|. Your time starts when {event}]": 2,
    " before {event}": 1,
    " while blindfolded": 1,
    ". (Bonus points for creativity)": 1,
    ". {person} cannot refuse this challenge": 1,
    ", taking as few steps as possible": 1,
    " in an unexpected way": 1,
    " to the best of your ability": 0.5,
    " without touching the [floor|ground]": 1,
}

task = {
    "[|{start}]{middle}[|{end}].": 1,
}

################################################################

from random import choice, choices
from re import search

def get(key):
    return choices(*zip(*globals()[key].items()))[0]

def parse(string):

    # evaluate forks
    while True:
        match = search('\[(.*?)\]', string)
        if match:
            i, j = match.start(), match.end()
            key = string[i+1:j-1].split('|')
            string = string[:i] + choice(key) + string[j:]
        else:
            break

    # evaluate tokens
    while True:
        match = search('\{(.*?)\}', string)
        if match:
            i, j = match.start(), match.end()
            key = string[i+1:j-1]
            string = string[:i] + parse(get(key)) + string[j:]
        else:
            return string

def get_task():
    t = parse(get('task'))
    return t[0].upper() + t[1:]
