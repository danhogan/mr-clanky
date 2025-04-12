import discord

TOKEN = ''

times = [
    "12:00am-12:30pm",
    "12:30pm-1:00pm",
    "1:00pm-1:30pm",
    "1:30pm-2:00pm",
    "2:00pm-2:30pm",
    "2:30pm-3:00pm",
    "3:00pm-3:30pm",
    "3:30pm-4:00pm",
    "4:00pm-4:30pm",
    "4:30pm-5:00pm",
    "5:00pm-5:30pm",
    "5:30pm-6:00pm",
    "6:00pm-6:30pm",
    "6:30pm-7:00pm",
    "7:00pm-7:30pm",
    "7:30pm-8:00pm",
    "8:00pm-8:30pm",
    "8:30pm-9:00pm",
    "9:00pm-9:30pm",
    "9:30pm-10:00pm"
]

discord_id_map = {
    "team_1": "175276474817970177",  # Replace with actual Discord ID
    "team_2": "174239847192847392",  # Replace with actual Discord ID
    "team_3": "182736547198374981",  # Replace with actual Discord ID
    # Add as many as you need
}

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    full_message = "All times are in EST.\n\n"
    
    for idx, time in enumerate(times):
        # Map team names and Discord IDs dynamically based on index or any other logic
        team_key = f"team_{idx + 1}"  # Adjust logic as needed
        if team_key in discord_id_map:
            discord_id = discord_id_map[team_key]
            full_message += f"{time} — <@{discord_id}>\n"
        else:
            full_message += f"{time} — [No team assigned]\n"

    full_message += "10:00pm-24 hours past your pick — MAKE UP PICKS"

    channel = client.get_channel(1359982556275019958)
    await channel.send(full_message)

client.run(TOKEN)