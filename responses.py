import random
import requests

def get_response(message: str) -> str:
    p_message = message.lower()
   
    #array of words that will trigger certain responses
    
    lols = ['oi no lols fancy boy','oi no lols butt man','oi dont be lollin','Oi no lols allowed','one more lol outta you and ban','reported','all reported']
    lol_in = ['lol','ha ha','haha','lel','lolz','lelz','lulz','hehe','keke','he he','heha']
    mike_man = ['mike','mick','michael']
    rob = ['sweetbotboy,','reported','oi']
    xmas = ['merry','happy new year','xmas']
    
    for word in xmas:
        if word in p_message:
            return 'Merry Xmas noob, Love Sweety xoxo'

    for word in rob:
        if word in p_message:
            return 'Oh hi rob :)'
    
    if message == '!roll':
        return str(random.randint(000, 999))


    for word in lol_in:
        if word in p_message:
            return random.choice(lols)

    def get_help_message():
        message = "`Welcome to the SweetyBot help menu!`\n"
        message += "`Here are the available commands:`\n"
        message += "`!play song title: Search youtube for a song and plays in the voice channel you are in. (bit shitty)`\n"
        message += "`!stop, !pause and !resume also work`\n"
        message += "`!roll: Generates a random number between 0001 and 999.`\n"
        message += "`!image top text | bottom text: Creates a shitty meme with the specified top and bottom text.(thats a Pipe sign inbetween the text.)`\n"
        message += "`!worth top text: Creates a shittier meme with the specified top text.`\n"
        message += "`!pres any text: Creates a shittier meme with the specified text.`\n"
        message += "`!change any text: Creates an even shittier meme with the specified text.`\n"
        message += "`!yt search query: Returns a youtube video from your search string.`\n"
        message += "`? prefixed to your message will return command/message privately.`\n"
        message += "`\n`"
        message += "`\n`"
        message += "`Cheers Cobbs.`\n"
        
        return message

    if p_message == '!help':
        return get_help_message()



    

