import discord
import random

intents = discord.Intents.default()
intents.messages = True  
intents.reactions = True 
intents.message_content = True
client = discord.Client(intents=intents)


videolar_Tr= {
    1: "https://www.youtube.com/watch?v=aGYjEyHBUTA",
    2: "https://www.youtube.com/watch?v=sgIi3E7MzqA",
    3: "https://www.youtube.com/watch?v=fBS6xkTC9bQ",
    4: "https://www.youtube.com/watch?v=HStCv8ixyWg",
    5: "https://www.youtube.com/watch?v=4Prknhl3Vjk",
    6: "https://www.youtube.com/watch?v=Qyq_WDAoI_Q",
    7: "https://www.youtube.com/watch?v=PR2ALqsvbYQ",
    8: "https://www.youtube.com/watch?v=HbkswWNE3zE",}


videolar_İng= {
    1: "https://www.youtube.com/watch?v=G4H1N_yXBiA",
    2: "https://www.youtube.com/watch?v=dcBXmj1nMTQ",
    3: "https://www.youtube.com/watch?v=eHMLszamZ9w",
    4: "https://www.youtube.com/watch?v=2njn71TqkjA",
    5: "https://www.youtube.com/watch?v=QlQ-MEZgRGY",
    6: "https://www.youtube.com/watch?v=g9p5VKd8VkE",
    7: "https://www.youtube.com/watch?v=Y1mPWVzaGQY",
    8: "https://www.youtube.com/watch?v=myZAvqqp9Jc",}



resimler = {
    1: "images.jpeg",
    2: "images1.jpeg",
    3: "images2.jpeg",
    4: "images3.jpg",
    5: "images4.jpg",
    6: "images5.jpg",
    7: "images6.jpg",
    8: "images7.jpg",
    9: "images8.jpg",
    10: "images9.jpg",
    11: "images10.jpg",
    12: "images11.jpg",
    13: "images12.jpg",
    14: "images13.jpg",
    15: "images14.jpg",
    16: "images15.jpg",
    17: "images16.jpg",
    18: "images17.jpg",
    19: "images18.jpg",
    20: "images19.jpg",
    21: "images20.jpg",
    22: "images21.jpg",
    23: "images22.jpg",
    24: "images23.jpg",
    25: "images24.jpg",
    26: "images25.jpg",
    27: "images26.jpg",
    28: "images27.jpg",
    29: "images28.jpg",
    30: "images29.jpg",
}

@client.event
async def on_ready():
    print(f'{client.user} Bot sunucuya giriş yaptı.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Komut soru-cevap kısmı
    if message.channel.name == 'sohbet':
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
                                       "!Ormanların korunması ve ağaçlandırma iklim değişikliğiyle nasıl ilişkilendirilir?\n"
                                       "!İklim değişikliği için sanayi alanında ne gibi değişikliklere gidebiliriz?\n"
                                       "!Yenilenebilir enerji çeşitleri nelerdir?\n")
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
        elif message.content.startswith("!İklim değişikliği için sanayi alanında ne gibi değişikliklere gidebiliriz?"):
            await message.channel.send("Sanayi sektörü, iklim değişikliği ile mücadelede daha temiz enerji kaynaklarına yönelebilir ve enerji verimliliğini artırabilir.")
        elif message.content.startswith("!Yenilenebilir enerji çeşitleri nelerdir?"):
            await message.channel.send("Yenilenebilir enerji, doğal kaynaklarla enerji üretimini sağlar ve çevresel etkileri minimaldir. Güneş, rüzgar, hidroelektrik, biyokütle, jeotermal ve gelgit enerjisi gibi kaynaklar, fosil yakıtlara göre temiz ve sürdürülebilirdir.")
        elif message.content.startswith("Selam"):
            await message.channel.send("Selam! Komutlar için !help")
        elif message.content.startswith("Merhaba"):
            await message.channel.send("Merhaba! Komutlar için !help")
        else:    
            await message.channel.send("Dediğinizi tam anlayamadım komutlar için !help")
    
    
    elif message.channel.name == 'görsel':
        if message.content.startswith('$Görsel'):
            resim_numarasi = random.randint(1, len(resimler))
            secilen_resim = resimler[resim_numarasi]
            with open(secilen_resim, "rb") as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
        elif message.content.startswith('!help'):
            await message.channel.send("30 resim içinden rastgele resim için:\n"
                                       "$Görsel")
        else:  
            await message.channel.send("Dediğinizi tam anlayamadım komutlar için !help")
    
    
    elif message.channel.name == 'youtube-video':
            if message.content.lower() == '$türkçe':
                video_numarasi = random.randint(1, len(videolar_Tr))
                video_linki = videolar_Tr[video_numarasi]
                await message.channel.send(video_linki)
            elif message.content.lower() == '$ingilizce':
                video_numarasi = random.randint(1, len(videolar_İng))
                video_linki = videolar_İng[video_numarasi]
                await message.channel.send(video_linki)
            elif message.content.startswith('!help'):
                await message.channel.send("İstediğiniz dilde rastgele video için:\n"
                                       "$türkçe veya $ingilizce")
            else:
                await message.channel.send("Lütfen $türkçe veya $ingilizce yazarak istediğiniz dilde rastgele bir video isteyin.")






client.run("TOKEN")
