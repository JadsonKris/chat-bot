import aiml

bot = aiml.Kernel()
bot.learn('dialogue.xml')

print(bot.respond("INICIO"))
while True:
    r = input("Cliente->")
    r = bot.respond(r).split("/n")
    print("BOT ->>")
    for i in r:
        print(i)
    print()