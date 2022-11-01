import os.path


import pygame
import sys
import time

import pygame.image

pygame.init()
"""Değerler"""
para=0
elmas=0
minerfiyat=50
minerfiyat1=500
minerfiyat2=3000
tıklamagücü=1

pickaxefiyat1=100
pickaxefiyat2=100
pickaxefiyat3=100
pickaxefiyat4=100
skillbookfiyat=200
skillbookfiyat1=500
skillbookfiyat2=1000
"""RGB renk Kodları"""
beyaz = (255,255,255)
siyah=(0,0,0)
sarı=(255,255,0)
mavi=(0,191,255)
yeşil=(50,205,50)
""" yazı ekleme"""
parayazısıtipi=pygame.font.SysFont("arial",30,5)
tıklamagücüyazıtipi=pygame.font.SysFont("arial",20,5)
diamondyazıtipi=pygame.font.SysFont("arial",30,5)
shopyazıtipi=pygame.font.SysFont("arial",20,5)
tradediamondyazıtipi=pygame.font.SysFont("arial",30,5)
trademoneyyazıtipi=pygame.font.SysFont("arial",30,5)
tradeceviryazıtipi=pygame.font.SysFont("arial",30,5)


"""sesler"""
doğruses=pygame.mixer.Sound(os.path.join("doğruses.mp3"))
yanlışses=pygame.mixer.Sound(os.path.join("yanlışses.mp3"))
tıklamases=pygame.mixer.Sound(os.path.join("tıklamases.mp3"))
"""ses volume"""
yanlışses.set_volume(0.03)
doğruses.set_volume(0.03)
tıklamases.set_volume(0.07)



"""Arkaplan Yükleme"""
background=pygame.image.load("background.jpg")
"""Resim Yükleme """

money=pygame.image.load("money.png")
diamond=pygame.image.load("diamond.png")
tradediamond=pygame.image.load("tradediamond.png")
trademoney=pygame.image.load("trademoney.png")

pickaxe=pygame.image.load("pickaxe.png")

pickaxemarket=pygame.image.load("pickaxemarket.png")
pickaxemarketmouse=pygame.image.load("pickaxemarketmouse.png")
pickaxemarket1=pygame.image.load("pickaxemarket1.png")
picaxemarketmouse1=pygame.image.load("pickaxemarketmouse1.png")
pickaxemarket2=pygame.image.load("pickaxemarket2.png")
pickaxemarketmouse2=pygame.image.load("pickaxemarketmouse2.png")
pickaxemarket3=pygame.image.load("pickaxemarket3.png")
pickaxemarketmouse3=pygame.image.load("pickaxemarketmouse3.png")
pickaxebackground=pygame.image.load("pickaxebackground.png")

miner = pygame.image.load("miner.png")
skillbook=pygame.image.load("skillbook.png")
skilbookbackground=pygame.image.load("skilbookbackground.jpg")
shop =pygame.image.load("shop.png")
shopbackground=pygame.image.load("menubackground.jpg")
minerbackground=pygame.image.load("minerbackground.jpg")
pickaxeshopmenu=pygame.image.load("pickaxeshopmenu.png")
pickaxeshopbackground=pygame.image.load("pickaxeshopbackground.jpg")
trade=pygame.image.load("trade.png")
tradebackground=pygame.image.load("tradebackground.jpg")
mineryardımcı=pygame.image.load("mineryardımcı.png")
mineryardımcı1=pygame.image.load("mineryardımcı1.png")
mineryardımcı2=pygame.image.load("mineryardımcı2.png")
sesaçık=pygame.image.load("sesaçık.png")
seskapalı=pygame.image.load("seskapalı.png")
tempses=pygame.image.load("sesaçık.png")
arrow=pygame.image.load("arrow.png")
dikdörtgen=pygame.image.load("dikdörtgen.png")
skillbookmarket=pygame.image.load("skilbookmarket.png")
skillbookmarket1=pygame.image.load("skillbookmarket1.png")
skillbookmarket2=pygame.image.load("skilbookmarket2.png")
skillbookmoney=pygame.image.load("skillbookmoney.png")
"""mp3"""
"""Effect"""
skillbookeffect=pygame.image.load("effect/skillbookeffect.png")
shopeffect=pygame.image.load("effect/shopeffect.png")
tradeeffect=pygame.image.load("effect/tradeeffect.png")
minereffect=pygame.image.load("effect/minereffect.png")
pickaxeshopeffect=pygame.image.load("effect/pickaxeshopeffect.png")
#minersmenu effect
mineryardımcıeffect=pygame.image.load("effect/minermenu/mineryardımcıeffect.png")
mineryardımcı1effect=pygame.image.load("effect/minermenu/mineryardımcı1effect.png")
mineryardımcı2effect=pygame.image.load("effect/minermenu/mineryardımcı2effect.png")



"""Oyun Başlığı"""
pygame.display.set_caption("Miner")

"""Pencere Boyut oluşturma"""
screen = pygame.display.set_mode((1024,606))
"""Mouse gözükmemesi"""
pygame.mouse.set_visible(False)
ses=True
open=True
shopmenu = False
shop_area = (774,0,1024,606)
skilbookmenu= False
skilbook_area=(774,0,1024,606)
minermenu=False
miner_area=(774,0,1024,606)
trademenu=False
trade_area=(774,0,1024,606)
pickaxeshop= False
pickaxeshop_area=(774,0,1024,606)
"""Pickaxe Animasyon"""
pickaxeadım=0
animasyonimg=[pygame.image.load("pickaxeanimasyon/pickaxeanimasyon.png"),
                  pygame.image.load("pickaxeanimasyon/pickaxeanimasyon1.png"),
                  pygame.image.load("pickaxeanimasyon/pickaxeanimasyon2.png"),
                  pygame.image.load("pickaxeanimasyon/pickaxeanimasyon3.png"),
                  pygame.image.load("pickaxeanimasyon/pickaxeanimasyon4.png"),
                  pygame.image.load("pickaxeanimasyon/pickaxeanimasyon5.png")
                ]
"""Fonksiyonlar"""

mouseX, mouseY = pygame.mouse.get_pos()
tıky=mouseY-30
tık=False
while open:
    screen.fill(siyah)
    screen.blit(background, (0, 0))
    mouseX, mouseY = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            open=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pos())
            """Ekrana basılınca gelen para"""

            if 0<mouseX<1024 and 0<mouseY<506 and shopmenu==False and minermenu==False and pickaxeshop==False and skilbookmenu==False and trademenu==False:
                print(pygame.mouse.get_pos())
                pygame.mixer.Sound.play(tıklamases)
                tık=True
                para=int(tıklamagücü+para)

            if 100>=mouseX>=0 and 506<=mouseY<=606:
                print(pygame.mouse.get_pos())
                shopmenu = True
                minermenu = False
                trademenu = False
                pickaxeshop = False
                skilbookmenu = False
                continue

            if 200>=mouseX>=100 and 506<=mouseY<=606:
                print(pygame.mouse.get_pos())
                minermenu=True
                shopmenu=False
                trademenu=False
                pickaxeshop=False
                skilbookmenu=False
                continue
            if 300>=mouseX>=200 and 506<=mouseY<=606:
                print(pygame.mouse.get_pos())
                pickaxeshop=True
                shopmenu = False
                trademenu = False
                minermenu = False
                skilbookmenu = False
                continue
            if 400>=mouseX>=300 and 506<=mouseY<=606:
                print(pygame.mouse.get_pos())
                skilbookmenu=True
                shopmenu = False
                trademenu = False
                pickaxeshop = False
                minermenu = False
                continue
            if 500>=mouseX>=400 and 506<=mouseY<=606:
                print(pygame.mouse.get_pos())
                trademenu=True
                shopmenu = False
                minermenu = False
                pickaxeshop = False
                skilbookmenu = False
                continue
            if 512<=mouseX<=562 and 0<=mouseY<=50:
                if ses==True and 512<=mouseX<=562 and 0<=mouseY<=50:
                    sesaçık=seskapalı
                    yanlışses.set_volume(0)
                    doğruses.set_volume(0)
                    tıklamases.set_volume(0)
                    ses=False

                    continue
                elif ses==False and 512<=mouseX<=562 and 0<=mouseY<=50:
                    sesaçık=tempses
                    yanlışses.set_volume(0.03)
                    doğruses.set_volume(0.03)
                    tıklamases.set_volume(0.07)
                    ses=True
                    continue
                continue



            """Shop ayarlamaları"""
            if skilbookmenu==True and trademenu==False and shopmenu==False and pickaxeshop==False and minermenu==False and skilbook_area[0]<=mouseX<skilbook_area[2] and skilbook_area[1]<mouseY<skilbook_area[3]:
                print("menüye tıklandı")
                if 774<mouseX<874 and 0<mouseY<100:
                    print("a")
                    if elmas>=skillbookfiyat:
                        tıklamagücü=int(tıklamagücü*1.4)
                        elmas=elmas-skillbookfiyat
                        skillbookfiyat=int(skillbookfiyat*1.8)
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                if 774 < mouseX < 874 and 100 < mouseY < 200:
                    print("a")
                    if elmas>=skillbookfiyat1:
                        tıklamagücü=int(tıklamagücü*1.4)
                        elmas=elmas-skillbookfiyat1
                        skillbookfiyat1 = int(skillbookfiyat1 * 1.8)
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                if 774 < mouseX < 874 and 200 < mouseY < 300:
                    print("a")
                    if elmas>=skillbookfiyat2:
                        tıklamagücü=int(tıklamagücü*1.4)
                        elmas=elmas-skillbookfiyat2
                        skillbookfiyat2 = int(skillbookfiyat2 * 1.8)
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)

                continue
            if shopmenu == True and trademenu==False and skilbookmenu==False and pickaxeshop==False and minermenu==False and  shop_area[0]<=mouseX<shop_area[2] and shop_area[1]<mouseY<shop_area[3]:
                print("menüye tıklandı")
                continue
            if pickaxeshop==True and trademenu==False and shopmenu==False and minermenu==False and skilbookmenu==False and  pickaxeshop_area[0]<=mouseX<pickaxeshop_area[2] and pickaxeshop_area[1]<mouseY<pickaxeshop_area[3]:
                print("Menüye Tıklandı")
                if 774<mouseX<889 and 0<mouseY<115:
                    if elmas>=pickaxefiyat1:
                        pygame.mixer.Sound.play(doğruses)
                        elmas=elmas-pickaxefiyat1
                        pickaxe=pickaxemarketmouse

                    else:
                        pygame.mixer.Sound.play(yanlışses)
                        pickaxe=pickaxe
                if 774 < mouseX < 889 and 115 < mouseY < 230:
                    if elmas>=pickaxefiyat2:
                        pygame.mixer.Sound.play(doğruses)
                        elmas=elmas-pickaxefiyat2
                        pickaxe=picaxemarketmouse1
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                        pickaxe=pickaxe
                if 774 < mouseX < 889 and 230 < mouseY < 345:
                    if elmas >= pickaxefiyat3:
                        pygame.mixer.Sound.play(doğruses)
                        elmas = elmas - pickaxefiyat3
                        pickaxe = pickaxemarketmouse2
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                        pickaxe = pickaxe
                if 774 < mouseX < 889 and 345 < mouseY < 460:
                    if elmas>=pickaxefiyat4:
                        pygame.mixer.Sound.play(doğruses)
                        elmas=elmas-pickaxefiyat4
                        pickaxe=pickaxemarketmouse3
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                        pickaxe=pickaxe


                continue
            if trademenu==True and pickaxeshop==False and shopmenu==False and skilbookmenu==False and minermenu==False and trade_area[0]<=mouseX<trade_area[2] and trade_area[1]<mouseY<trade_area[3]:
                print("Menüye Tıklandı")
                print(pygame.mouse.get_pos())
                if 853<=mouseX<=936 and 107<=mouseY<=130:
                    if para>=10000:
                        para=para-10000
                        elmas=elmas+1
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                    print("Çevirildi")

                if 853<=mouseX<=936 and 256<=mouseY<=280:
                    if elmas>=1:
                        para=para+10000
                        elmas=elmas-1
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                    print("Çevirildi")
                if 850 <= mouseX <= 942 and 395 <= mouseY <= 425:
                    if para>=500000:
                        para=para-500000
                        elmas=elmas+50
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)

                if 850 <= mouseX <= 942 and 540 <= mouseY <= 580:
                    if elmas>=50:
                        para=para+500000
                        elmas=elmas-50
                        pygame.mixer.Sound.play(doğruses)
                    else:
                        pygame.mixer.Sound.play(yanlışses)
                continue




            if minermenu==True and trademenu==False and pickaxeshop==False and shopmenu==False and skilbookmenu==False and miner_area[0]<=mouseX<miner_area[2] and miner_area[1]<mouseY<miner_area[3]:
                print("Menüye Tıklandı")
                if 774<mouseX<874 and 0<mouseY<100:
                    if para<minerfiyat:

                        pygame.mixer.Sound.play(yanlışses)

                        para=para
                    else:
                        pygame.mixer.Sound.play(doğruses)

                        para=int(para-minerfiyat)
                        tıklamagücü=int(tıklamagücü+3)
                        minerfiyat=int(minerfiyat*1.02)


                if 774<mouseX<874 and 100<mouseY<200:
                    if para<minerfiyat1:
                        pygame.mixer.Sound.play(yanlışses)
                        para=para
                    else:
                        pygame.mixer.Sound.play(doğruses)
                        para=int(para-minerfiyat1)
                        tıklamagücü=int(tıklamagücü+10)
                        minerfiyat1=int(minerfiyat1*1.02)
                if 774 < mouseX < 874 and 200 < mouseY < 300:
                    if para<minerfiyat2:
                        pygame.mixer.Sound.play(yanlışses)
                        para=para
                    else:
                        pygame.mixer.Sound.play(doğruses)
                        para=int(para-minerfiyat2)
                        tıklamagücü=int(tıklamagücü+50)
                        minerfiyat2=int(minerfiyat2*1.02)


                continue

                    #Menü butonlarını bu kısma yazmalısın

            else:
                print(shop,shop_area,mouseX,mouseY)
                shopmenu = False
                skilbookmenu=False
                pickaxeshop=False
                minermenu=False
                trademenu=False
                tık=False

                if 100 >= mouseX >= 0 and 506 <= mouseY <= 606:
                    print(pygame.mouse.get_pos())
                if 200 >= mouseX >= 100 and 506 <= mouseY <= 606:
                    print(pygame.mouse.get_pos())
                if 300 >= mouseX >= 200 and 506 <= mouseY <= 606:
                    print(pygame.mouse.get_pos())
                if 400 >= mouseX >= 300 and 506 <= mouseY <= 606:
                    print(pygame.mouse.get_pos())

    """ANA EKRAN """
    screen.blit(money,(0,10))
    screen.blit(diamond,(0,75))
    screen.blit(shop,(0,606-100))
    screen.blit(miner,(100,606-100))
    screen.blit(pickaxeshopmenu,(200,506))
    screen.blit(skillbook,(300,506))
    screen.blit(trade,(400,506))
    screen.blit(sesaçık,(512,0))

    tıklamagücü_text=tıklamagücüyazıtipi.render("Tıklama Gücü:"+str(tıklamagücü),True,sarı)
    money_text=parayazısıtipi.render(""+str(para),True,sarı)
    diamond_text=diamondyazıtipi.render(""+str(elmas),True,mavi)

    screen.blit(money_text,(70,20))
    screen.blit(diamond_text,(70,85))
    screen.blit(tıklamagücü_text,(0,480))
    """ana ekran effect"""
    if 0 <= mouseX <= 100 and 506 <= mouseY <= 606:
        screen.blit(shopeffect, (0, 506))
    if 100 <= mouseX <= 200 and 506 <= mouseY <= 606:
        screen.blit(minereffect, (100, 506))
    if 200 <= mouseX <= 300 and 506 <= mouseY <= 606:
        screen.blit(pickaxeshopeffect, (200, 506))

    if 300<=mouseX<=400 and 506<=mouseY<=606:
        screen.blit(skillbookeffect,(300,506))
    if 400 <= mouseX <= 500 and 506 <= mouseY <= 606:
        screen.blit(tradeeffect, (400, 506))






    """MENÜ İÇERİK AYARI"""
    if shopmenu:
        screen.fill((0,200,35),pygame.Rect(shop_area[0],shop_area[1],shop_area[2],shop_area[3]))
        screen.blit(shopbackground,(774,0))
    if skilbookmenu:
        skillbookfiyat_text=shopyazıtipi.render(""+str(skillbookfiyat),True,mavi)
        skillbookfiyat1_text=shopyazıtipi.render(""+str(skillbookfiyat1),True,mavi)
        skillbookfiyat2_text=shopyazıtipi.render(""+str(skillbookfiyat2),True,mavi)
        skillbookçarpan_text=tıklamagücüyazıtipi.render("Tık.G X1.4 ",True,sarı)
        skillbookçarpan1_text = tıklamagücüyazıtipi.render("Tık.G X1.4 ", True, sarı)
        skillbookçarpan2_text = tıklamagücüyazıtipi.render("Tık.G X1.4 ", True, sarı)
        screen.fill((0, 200, 35), pygame.Rect(skilbook_area[0], skilbook_area[1], skilbook_area[2], skilbook_area[3]))
        screen.blit(skilbookbackground, (774, 0))
        screen.blit(skillbookmarket,(774,0))
        screen.blit(skillbookmoney,(880,10))
        screen.blit(skillbookmoney, (880, 110))
        screen.blit(skillbookmoney, (880, 210))
        screen.blit(skillbookmarket1,(774,100))
        screen.blit(skillbookmarket2,(774,210))
        screen.blit(skillbookfiyat_text,(930,15))
        screen.blit(skillbookfiyat1_text, (930, 115))
        screen.blit(skillbookfiyat2_text, (930, 215))
        screen.blit(skillbookçarpan_text,(874,60))
        screen.blit(skillbookçarpan_text, (874, 160))
        screen.blit(skillbookçarpan_text, (874, 260))
    if minermenu:


        screen.fill((0, 200, 35), pygame.Rect(miner_area[0], miner_area[1], miner_area[2], miner_area[3]))
        screen.blit(minerbackground, (774, 0))
        minersatınaltext = shopyazıtipi.render("FİYAT: " + str(minerfiyat), True, sarı)
        minersatınaltext1 = shopyazıtipi.render("FİYAT: " + str(minerfiyat1), True, sarı)
        minersatınaltext2 = shopyazıtipi.render("FİYAT: " + str(minerfiyat2), True, sarı)
        minerçarpantext = shopyazıtipi.render("      +3 " , True, sarı)
        minerçarpantext1 = shopyazıtipi.render("      +10 "  , True, sarı)
        minerçarpantext2 = shopyazıtipi.render("      +50 " , True, sarı)
        screen.blit(mineryardımcı,(774,0))
        screen.blit(mineryardımcı1,(774,100))
        screen.blit(mineryardımcı2, (774, 200))

        screen.blit((minersatınaltext),(874,20))
        screen.blit((minerçarpantext),(874,55))
        screen.blit((minersatınaltext1), (874, 120))
        screen.blit((minerçarpantext1), (874, 155))
        screen.blit((minersatınaltext2), (874, 220))
        screen.blit((minerçarpantext2), (874, 255))
        """minermenu effect"""
        if 774<=mouseX<=874 and 0<=mouseY<=100:
            screen.blit(mineryardımcıeffect,(774,0))
        if 774 <= mouseX <= 874 and 100 <= mouseY <= 200:
            screen.blit(mineryardımcı1effect,(774,100))
        if 774 <= mouseX <= 874 and 200 <= mouseY <= 300:
            screen.blit(mineryardımcı2effect,(774,200))
    if pickaxeshop:
        screen.fill((0, 200, 35), pygame.Rect(pickaxeshop_area[0], pickaxeshop_area[1], pickaxeshop_area[2], pickaxeshop_area[3]))
        screen.blit(pickaxeshopbackground, (774, 0))
        pickaxefiyat_text=tradediamondyazıtipi.render("100",True,mavi)

        pygame.draw.rect(screen,beyaz,pygame.Rect(774,0,100,400))
        screen.blit(pickaxebackground,(774,0))
        screen.blit(pickaxebackground, (774, 115))
        screen.blit(pickaxebackground, (774, 230))
        screen.blit(pickaxebackground, (774, 345))
        screen.blit(pickaxemarket,(782,8))
        screen.blit(pickaxemarket1,(782,122))
        screen.blit(pickaxemarket2,(782,237))
        screen.blit(pickaxemarket3, (782, 353))
        screen.blit(tradediamond,(900,27))
        screen.blit(tradediamond, (900, 142))
        screen.blit(tradediamond, (900, 257))
        screen.blit(tradediamond, (900, 372))
        screen.blit(pickaxefiyat_text,(970,31))
        screen.blit(pickaxefiyat_text, (970, 145))
        screen.blit(pickaxefiyat_text, (970, 261))
        screen.blit(pickaxefiyat_text, (970, 376))
    if trademenu:
        tradediamond_text=tradediamondyazıtipi.render("1",True,mavi)
        trademoney_text=trademoneyyazıtipi.render("10000",True,sarı)
        tradediamond_text1 = tradediamondyazıtipi.render("1", True, mavi)
        trademoney_text1 = trademoneyyazıtipi.render("10000", True, sarı)
        tradediamond_text2=tradediamondyazıtipi.render("50",True,mavi)
        trademoney_text2=trademoneyyazıtipi.render("500K",True,sarı)
        tradediamond_text3=tradediamondyazıtipi.render("500K",True,sarı)
        trademoney_text3=trademoneyyazıtipi.render("50",True,sarı)
        tradecevir_text=tradeceviryazıtipi.render("CEVIR",True,(255,80,80))
        screen.fill((0, 200, 35), pygame.Rect(trade_area[0], trade_area[1], trade_area[2], trade_area[3]))
        screen.blit(tradebackground,(774,0))

        screen.blit(trademoney,(800,10))
        screen.blit(arrow,(880,15))
        screen.blit(tradediamond,(940,10))
        screen.blit((tradediamond_text),(961,70))
        screen.blit((trademoney_text),(785,70))

        screen.blit(trademoney, (940, 160))
        screen.blit(arrow,(880,165))
        screen.blit(tradediamond, (800, 160))
        screen.blit((tradediamond_text1), (820, 220))
        screen.blit((trademoney_text1), (925, 220))

        screen.blit(trademoney,(800,300))
        screen.blit(arrow,(880,315))
        screen.blit(tradediamond,(940,300))
        screen.blit(tradediamond_text2,(955,360))
        screen.blit(trademoney_text2,(800,365))

        screen.blit(trademoney, (940, 455))
        screen.blit(arrow, (880, 465))
        screen.blit(tradediamond, (800, 455))
        screen.blit(tradediamond_text2, (810, 515))
        screen.blit(trademoney_text2, (940, 515))





        screen.blit(dikdörtgen,(840,95))
        screen.blit(dikdörtgen, (840, 245))
        screen.blit(dikdörtgen, (840, 395))
        screen.blit(dikdörtgen, (840, 540))

        screen.blit(tradecevir_text,(850,100))
        screen.blit(tradecevir_text, (850, 250))
        screen.blit(tradecevir_text,(850,400))
        screen.blit(tradecevir_text,(850,545))
        """Mouse ile üstüne genildiğinde renk değişimi"""
        if 850<=mouseX<=942 and 105<=mouseY<=132:
            tradecevir_text = tradeceviryazıtipi.render("CEVIR", True, mavi)
            screen.blit(tradecevir_text, (850, 100))
        if 850<=mouseX<=942 and 253<=mouseY<=283:
            tradecevir_text1=tradeceviryazıtipi.render("CEVIR", True, mavi)
            screen.blit(tradecevir_text1,(850,250))
        if 850 <= mouseX <= 942 and 395 <= mouseY <= 425:
            tradecevir_text2 = tradeceviryazıtipi.render("CEVIR", True, mavi)
            screen.blit(tradecevir_text2,(850,400))
        if 850 <= mouseX <= 942 and 540 <= mouseY <= 580:
            tradecevir_text3 = tradeceviryazıtipi.render("CEVIR", True, mavi)
            screen.blit(tradecevir_text3, (850, 545))

    if tık==True:
        screen.blit(tıklamagücü_text, (mouseX, tıky))
        tıky -= 4



    """BAŞLANGIÇ MOUSE GÖRÜNÜM"""
    screen.blit(pickaxe, (mouseX - 30, mouseY - 30))
    #screen.blit(pickaxe,(mouseX-40,mouseY-25))





    pygame.display.update()
