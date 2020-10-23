from requests_html import HTMLSession
        
# Add streamers you want to check if online to this array
# i.e. 'streamers = ["channel1", "channel2"]' as needed
streamers = []

session = HTMLSession()
def check_online(streamer):
    url = "https://twitch.tv/" + str(streamer)
    p = session.get(url)
    p.html.render(timeout=20)
    elems = p.html.find("p.tw-strong")
    for elem in elems:
        if elem.text == "LIVE":
            return "✅"
    return "❌"

for streamer in streamers:
    print("{}: {}".format(streamer, check_online(streamer)))