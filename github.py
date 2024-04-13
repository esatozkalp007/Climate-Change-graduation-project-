import discord

intents = discord.Intents.default()
intents.messages = True  
intents.reactions = True 
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!İklim değişikliğini nasıl önleriz?'):
        await message.channel.send("İklim değişikliğini önlemek için fosil yakıtları azaltın, yenilenebilir enerjiye yatırım yapın, enerji verimliliğini artırın, ormanları koruyun, sürdürülebilir tarım ve sanayi uygulamalarını teşvik edin, uluslararası işbirliği sağlayın, toplumu eğitin.")
    elif message.content.startswith('!help'):
        await message.channel.send("Bana sorabileceğiniz bazı sorular;\n"
                                   "!İklim değişikliği neden olur?\n"
                                   "!İklim değişikliğini engellemek için evde ne gibi değişikliklere gidebiliriz?\n"
                                   "!İklim değişikliğini nasıl önleriz?\n" 
                                   "!Elektrikli araçlar iklim değişikliğine ne gibi fayda sağlar?\n"
                                   "!İklim değişikliğinin dünyaya etkileri nelerdir?\n"
                                   "!Hangi doğal afetler iklim değişikliği ile ilişkilendirilir?\n"
                                   "!İklim değişikliği neden tehlikelidir?\n"
                                   "!Ormanların korunması ve ağaçlandırma iklim değişikliğiyle nasıl ilişkilendirilir?")
                                    

                                   
                                
    elif message.content.startswith('!İklim değişikliği neden olur?'):
        await message.channel.send("İklim değişikliği, insan faaliyetleri ve doğal süreçlerin bir sonucudur. Fosil yakıtların yanması, endüstriyel süreçler, orman kesimi ve tarım gibi etmenler sera gazı emisyonlarını artırarak atmosferdeki sera etkisini güçlendirir. Bu da dünya yüzeyinin ısınmasına yol açar.")
    elif message.content.startswith("!İklim değişikliğini engellemek için evde ne gibi değişikliklere gidebiliriz?"):
        await message.channel.send("Evde iklim değişikliğini azaltmak için enerjiyi verimli kullanın, yenilenebilir enerjiye geçin, tercih edin, geri dönüşüm yapın, sürdürülebilir ürünleri tercih edin, su tasarrufu yapın.")
    elif message.content.startswith("!Elektrikli araçlar iklim değişikliğine ne gibi fayda sağlar?"):
        await message.channel.send("Elektrikli araçlar, düşük veya hiçbir egzoz emisyonu üreterek hava kirliliğini azaltır ve yenilenebilir enerjiyle çalıştığında sera gazı emisyonlarını azaltarak iklim değişikliğiyle mücadeleye katkıda bulunur. Ayrıca, daha verimli teknolojilerle donatılmış olmaları, enerji tüketimini azaltarak çevresel etkileri azaltır ve fosil yakıt kullanımını azaltır. Bu nedenlerle, elektrikli araçlar, iklim değişikliğiyle mücadelede önemli bir rol oynarlar.")
    elif message.content.startswith("!İklim değişikliğinin dünyaya etkileri nelerdir?"):
        await message.channel.send("İklim değişikliği, artan sıcaklık, aşırı hava olayları, deniz seviyesinin yükselmesi, ekosistem bozulması, tarım ve gıda güvencesinde azalma, su kaynaklarında azalma ve sağlık sorunları gibi bir dizi olumsuz etkiye neden olur. Bu etkiler, insan yaşamını, ekonomiyi, doğal sistemleri ve sosyal dengeleri ciddi şekilde tehdit eder.")
    elif message.content.startswith("!Hangi doğal afetler iklim değişikliği ile ilişkilendirilir?"):
        await message.channel.send("İklim değişikliği, aşırı sıcaklık, şiddetli fırtınalar, aşırı yağışlar, kuraklık ve sel gibi doğal afetlerin sıklığını ve şiddetini artırabilir. Bu afetler, iklim değişikliğinin etkilerinden sadece birkaçıdır.")
    elif message.content.startswith("!İklim değişikliği neden tehlikelidir?"):
        await message.channel.send("İklim değişikliği, doğal afetlerin artması, deniz seviyesinin yükselmesi, su ve gıda güvenliğinin tehlikeye girmesi gibi ciddi riskleri beraberinde getirir.")
    elif message.content.startswith("!Ormanların korunması ve ağaçlandırma iklim değişikliğiyle nasıl ilişkilendirilir?"):
        await message.channel.send("Ormanların korunması ve ağaçlandırma, atmosferden karbon emilimini artırarak sera gazı miktarını azaltır ve erozyonu önleyerek toprakları korur. Bu, iklim değişikliğiyle mücadelede etkili bir stratejidir.")
    else:
        await message.channel.send("Dediğinizi tam anlayamadım komutlar için !help")

client.run("token")
