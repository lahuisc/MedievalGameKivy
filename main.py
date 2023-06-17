from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
import shelve
import math
import random
from kivy.core.audio import SoundLoader
 
# with shelve.open('Data') as data:
# # #     print(dict(data))


class ImageButton(ButtonBehavior, Image):
    pass

class ImageToggleButton(ToggleButtonBehavior, Image):
    pass

class Manager(ScreenManager):
    pass

class LoadScreen(Screen):
    def set(self):
        with shelve.open('Data') as data:
            data['loops'] = False

class HomeScreen(Screen):
    
    def playMusic(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['music'] == True:
                app.oneSong.stop()
                app.twoSong.stop()
                app.homeSong.play()
        
    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(data['coins'])
            self.ids.rubies.text = str(data['rubies'])
            self.ids.sapphires.text = str(data['sapphires'])
            self.ids.emeralds.text = str(data['emeralds'])

class StoreScreen(Screen):
    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(data['coins'])
            self.ids.rubies.text = str(data['rubies'])
            self.ids.sapphires.text = str(data['sapphires'])
            self.ids.emeralds.text = str(data['emeralds'])
    
    def basePack(self):
        with shelve.open('Data') as data:
            if data['coins'] >= 100: 
                data['pack'] = 'base'
                data['coins'] = (data['coins'] - 100)
                self.parent.current = 'basepackscrn'
                
class ArmyScreen(Screen):
    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(data['coins'])
            self.ids.rubies.text = str(data['rubies'])
            self.ids.sapphires.text = str(data['sapphires'])
            self.ids.emeralds.text = str(data['emeralds'])
    def loadCards(self):
        with shelve.open('Data') as data:
            if data['minerUnlocked'] == True:
                self.ids.miner.source = "Images/minercard.png"
            if data['swordsmanUnlocked'] == True:
                self.ids.swordsman.source = "Images/swordsmancard.png"
            if data['archerUnlocked'] == True:
                self.ids.archer.source = "Images/archercard.png"
            if data['pikemanUnlocked'] == True:
                self.ids.pikeman.source = "Images/pikemancard.png"
            if data['bardUnlocked'] == True:
                self.ids.bard.source = "Images/bardcard.png"
            if data['gnomeUnlocked'] == True:
                self.ids.gnome.source = "Images/gnomecard.png"
            if data['gnomeminerUnlocked'] == True:
                self.ids.gnomeminer.source = "Images/gnomeminercard.png"
            if data['mageUnlocked'] == True:
                self.ids.mage.source = "Images/magecard.png"
            if data['priestUnlocked'] == True:
                self.ids.priest.source = "Images/priestcard.png"
            if data['crusaderUnlocked'] == True:
                self.ids.crusader.source = "Images/crusadercard.png"
    
    def peasant(self):
        with shelve.open('Data') as data:
            data['current'] = 'peasant'
    def miner(self):
        with shelve.open('Data') as data:
            data['current'] = 'miner'
            if data['minerUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def swordsman(self):
        with shelve.open('Data') as data:
            data['current'] = 'swordsman'
            if data['swordsmanUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def archer(self):
        with shelve.open('Data') as data:
            data['current'] = 'archer'
            if data['archerUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def pikeman(self):
        with shelve.open('Data') as data:
            data['current'] = 'pikeman'
            if data['pikemanUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def bard(self):
        with shelve.open('Data') as data:
            data['current'] = 'bard'
            if data['bardUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def gnome(self):
        with shelve.open('Data') as data:
            data['current'] = 'gnome'
            if data['gnomeUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def gnomeminer(self):
        with shelve.open('Data') as data:
            data['current'] = 'gnomeminer'
            if data['gnomeminerUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def mage(self):
        with shelve.open('Data') as data:
            data['current'] = 'mage'
            if data['mageUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def priest(self):
        with shelve.open('Data') as data:
            data['current'] = 'priest'
            if data['priestUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def crusader(self):
        with shelve.open('Data') as data:
            data['current'] = 'crusader'
            if data['crusaderUnlocked'] == True:
                self.parent.current = 'upgradescrn'

class SettingsScreen(Screen):
    def musictoggle(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['music'] == True:
                data['music'] = False
                app.homeSong.stop()
            else:
                data['music'] = True
                app.homeSong.play()

class StatsScreen(Screen):
    pass

class World1Screen(Screen):
    def playMusic(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['music'] == True:
                app.homeSong.play()

    def loadLevel1(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 1:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 1

    def loadLevel2(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 2:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 2
    
    def loadLevel3(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 3:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 3

    def loadLevel4(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 4:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 4
        
    def loadLevel5(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 5:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 5
    
    def loadLevel6(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 6:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 6

    def loadLevel7(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 7:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 7

    def loadLevel8(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 8:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 8

    def loadLevel9(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 9:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 9

    def loadLevel10(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 10:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 10
    
    def loadLevel11(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 11:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 11
    
    def loadLevel12(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 12:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 12

    def loadLevel13(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 13:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 13
    
    def loadLevel14(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 14:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 14
    
    def loadLevel15(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 15:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = True
                data['endless'] = 0
                data['endmove'] = 0
                data['level'] = 15

    def endless(self):
        with shelve.open('Data') as data:   
            if data['unlockedlevel'] >= 15:
                self.parent.current = 'deckscrn'
                data['bosslevel'] = False
                data['endless'] = 1
                data['endmove'] = 0
                data['level'] = 16

class World2Screen(Screen):
    pass

class ResetSureScreen(Screen):
    def max(self):  
        with shelve.open('Data') as data:
            data['endmove'] = 0
            data['endless'] = 0
            data['bosslevel'] = False
            data['bosshealth'] = 0
            data['screen'] = 'none'
            data['gamestate'] = 'none'
            data['aimg'] = 'none'
            data['bimg'] = 'none'
            data['cimg'] = 'none'
            data['yesdraw1'] = True
            data['yesdraw2'] = True
            data['yesdraw3'] = True
            data['lane'] = 'top'
            data['iron'] = 0
            data['readydrop'] = 'none'
            data['todrop'] = 'none'
            data['selectedcards'] = 0
            data['level'] = 0
            data['unlockedlevel'] = 150
            data['coins'] = 10000
            data['rubies'] = 10
            data['emeralds'] = 10
            data['sapphires'] = 10
            data['music'] = True
            data['current'] = 'Peasant'
            data['pack'] = 'none'
            data['peasantUnlocked'] = True
            data['peasantCards'] = 0
            data['peasantHealth'] = 50
            data['peasantHealthLvl'] = 1
            data['peasantDamage'] = 10
            data['peasantDamageLvl'] = 1
            data['peasantSpeed'] = 10
            data['peasantSpeedLvl'] = 1
            data['peasantDefense'] = 20
            data['peasantDefenseLvl'] = 1
            data['peasantRange'] = 0
            data['peasantRangeLvl'] = 1
            data['peasantCost'] = 10
            data['peasantSpecial'] = 0
            data['peasantSpecialLvl'] = 1
            data['swordsmanUnlocked'] = True
            data['swordsmanCards'] = 0
            data['swordsmanHealth'] = 100
            data['swordsmanHealthLvl'] = 1
            data['swordsmanDamage'] = 15
            data['swordsmanDamageLvl'] = 1
            data['swordsmanSpeed'] = 10
            data['swordsmanSpeedLvl'] = 1
            data['swordsmanDefense'] = 25
            data['swordsmanDefenseLvl'] = 1
            data['swordsmanRange'] = 0
            data['swordsmanRangeLvl'] = 1
            data['swordsmanCost'] = 30
            data['swordsmanSpecial'] = 0
            data['swordsmanSpecialLvl'] = 1
            data['minerUnlocked'] = True
            data['minerCards'] = 0
            data['minerHealth'] = 70
            data['minerHealthLvl'] = 1
            data['minerDamage'] = 0
            data['minerDamageLvl'] = 1
            data['minerSpeed'] = 10
            data['minerSpeedLvl'] = 1
            data['minerDefense'] = 25
            data['minerDefenseLvl'] = 1
            data['minerRange'] = 0
            data['minerRangeLvl'] = 1
            data['minerCost'] = 20
            data['minerSpecial'] = 12
            data['minerSpecialLvl'] = 1
            data['archerUnlocked'] = True
            data['archerCards'] = 0
            data['archerHealth'] = 50
            data['archerHealthLvl'] = 1
            data['archerDamage'] = 6
            data['archerDamageLvl'] = 1
            data['archerSpeed'] = 10
            data['archerSpeedLvl'] = 1
            data['archerDefense'] = 10
            data['archerDefenseLvl'] = 1
            data['archerRange'] = 6
            data['archerRangeLvl'] = 1
            data['archerCost'] = 20
            data['archerSpecial'] = 0
            data['archerSpecialLvl'] = 1
            data['pikemanUnlocked'] = True
            data['pikemanCards'] = 0
            data['pikemanHealth'] = 60
            data['pikemanHealthLvl'] = 1
            data['pikemanDamage'] = 20
            data['pikemanDamageLvl'] = 1
            data['pikemanSpeed'] = 10
            data['pikemanSpeedLvl'] = 1
            data['pikemanDefense'] = 20
            data['pikemanDefenseLvl'] = 1
            data['pikemanRange'] = 0
            data['pikemanRangeLvl'] = 1
            data['pikemanCost'] = 30
            data['pikemanSpecial'] = 0
            data['pikemanSpecialLvl'] = 1
            data['bardUnlocked'] = True
            data['bardCards'] = 0
            data['bardHealth'] = 40
            data['bardHealthLvl'] = 1
            data['bardDamage'] = 0
            data['bardDamageLvl'] = 1
            data['bardSpeed'] = 10
            data['bardSpeedLvl'] = 1
            data['bardDefense'] = 10
            data['bardDefenseLvl'] = 1
            data['bardRange'] = 0
            data['bardRangeLvl'] = 1
            data['bardCost'] = 30
            data['bardSpecial'] = 5
            data['bardSpecialLvl'] = 1
            data['gnomeUnlocked'] = True
            data['gnomeCards'] = 0
            data['gnomeHealth'] = 30
            data['gnomeHealthLvl'] = 1
            data['gnomeDamage'] = 20
            data['gnomeDamageLvl'] = 1
            data['gnomeSpeed'] = 10
            data['gnomeSpeedLvl'] = 1
            data['gnomeDefense'] = 20
            data['gnomeDefenseLvl'] = 1
            data['gnomeRange'] = 0
            data['gnomeRangeLvl'] = 1
            data['gnomeCost'] = 25
            data['gnomeSpecial'] = 0
            data['gnomeSpecialLvl'] = 1
            data['gnomeminerUnlocked'] = True
            data['gnomeminerCards'] = 0
            data['gnomeminerHealth'] = 50
            data['gnomeminerHealthLvl'] = 1
            data['gnomeminerDamage'] = 0
            data['gnomeminerDamageLvl'] = 1
            data['gnomeminerSpeed'] = 10
            data['gnomeminerSpeedLvl'] = 1
            data['gnomeminerDefense'] = 50
            data['gnomeminerDefenseLvl'] = 1
            data['gnomeminerRange'] = 0
            data['gnomeminerRangeLvl'] = 1
            data['gnomeminerCost'] = 40
            data['gnomeminerSpecial'] = 24
            data['gnomeminerSpecialLvl'] = 1
            data['mageUnlocked'] = True
            data['mageCards'] = 0
            data['mageHealth'] = 70
            data['mageHealthLvl'] = 1
            data['mageDamage'] = 10
            data['mageDamageLvl'] = 1
            data['mageSpeed'] = 10
            data['mageSpeedLvl'] = 1
            data['mageDefense'] = 25
            data['mageDefenseLvl'] = 1
            data['mageRange'] = 4
            data['mageRangeLvl'] = 1
            data['mageCost'] = 45
            data['mageSpecial'] = 0
            data['mageSpecialLvl'] = 1
            data['priestUnlocked'] = True
            data['priestCards'] = 0
            data['priestHealth'] = 40
            data['priestHealthLvl'] = 1
            data['priestDamage'] = 0
            data['priestDamageLvl'] = 1
            data['priestSpeed'] = 10
            data['priestSpeedLvl'] = 1
            data['priestDefense'] = 25
            data['priestDefenseLvl'] = 1
            data['priestRange'] = 4
            data['priestRangeLvl'] = 1
            data['priestCost'] = 50
            data['priestSpecial'] = 5
            data['priestSpecialLvl'] = 1
            data['crusaderUnlocked'] = True
            data['crusaderCards'] = 0
            data['crusaderHealth'] = 200
            data['crusaderHealthLvl'] = 1
            data['crusaderDamage'] = 20
            data['crusaderDamageLvl'] = 1
            data['crusaderSpeed'] = 10
            data['crusaderSpeedLvl'] = 1
            data['crusaderDefense'] = 25
            data['crusaderDefenseLvl'] = 1
            data['crusaderRange'] = 0
            data['crusaderRangeLvl'] = 1
            data['crusaderCost'] = 70
            data['crusaderSpecial'] = 0
            data['crusaderSpecialLvl'] = 1

    def reset(self):
        with shelve.open('Data') as data:
            data['endmove'] = 0
            data['endless'] = 0
            data['bosslevel'] = False
            data['bosshealth'] = 0
            data['screen'] = 'none'
            data['gamestate'] = 'none'
            data['aimg'] = 'none'
            data['bimg'] = 'none'
            data['cimg'] = 'none'
            data['yesdraw1'] = True
            data['yesdraw2'] = True
            data['yesdraw3'] = True
            data['lane'] = 'top'
            data['iron'] = 0
            data['readydrop'] = 'none'
            data['todrop'] = 'none'
            data['selectedcards'] = 0
            data['level'] = 0
            data['unlockedlevel'] = 1
            data['coins'] = 0
            data['rubies'] = 0
            data['emeralds'] = 0
            data['sapphires'] = 0
            data['music'] = True
            data['current'] = 'Peasant'
            data['pack'] = 'none'
            data['peasantUnlocked'] = True
            data['peasantCards'] = 0
            data['peasantHealth'] = 50
            data['peasantHealthLvl'] = 1
            data['peasantDamage'] = 10
            data['peasantDamageLvl'] = 1
            data['peasantSpeed'] = 10
            data['peasantSpeedLvl'] = 1
            data['peasantDefense'] = 20
            data['peasantDefenseLvl'] = 1
            data['peasantRange'] = 0
            data['peasantRangeLvl'] = 1
            data['peasantCost'] = 10
            data['peasantSpecial'] = 0
            data['peasantSpecialLvl'] = 1
            data['swordsmanUnlocked'] = False
            data['swordsmanCards'] = 0
            data['swordsmanHealth'] = 100
            data['swordsmanHealthLvl'] = 1
            data['swordsmanDamage'] = 15
            data['swordsmanDamageLvl'] = 1
            data['swordsmanSpeed'] = 10
            data['swordsmanSpeedLvl'] = 1
            data['swordsmanDefense'] = 25
            data['swordsmanDefenseLvl'] = 1
            data['swordsmanRange'] = 0
            data['swordsmanRangeLvl'] = 1
            data['swordsmanCost'] = 30
            data['swordsmanSpecial'] = 0
            data['swordsmanSpecialLvl'] = 1
            data['minerUnlocked'] = False
            data['minerCards'] = 0
            data['minerHealth'] = 70
            data['minerHealthLvl'] = 1
            data['minerDamage'] = 0
            data['minerDamageLvl'] = 1
            data['minerSpeed'] = 10
            data['minerSpeedLvl'] = 1
            data['minerDefense'] = 25
            data['minerDefenseLvl'] = 1
            data['minerRange'] = 0
            data['minerRangeLvl'] = 1
            data['minerCost'] = 20
            data['minerSpecial'] = 12
            data['minerSpecialLvl'] = 1
            data['archerUnlocked'] = False
            data['archerCards'] = 0
            data['archerHealth'] = 50
            data['archerHealthLvl'] = 1
            data['archerDamage'] = 6
            data['archerDamageLvl'] = 1
            data['archerSpeed'] = 10
            data['archerSpeedLvl'] = 1
            data['archerDefense'] = 10
            data['archerDefenseLvl'] = 1
            data['archerRange'] = 6
            data['archerRangeLvl'] = 1
            data['archerCost'] = 20
            data['archerSpecial'] = 0
            data['archerSpecialLvl'] = 1
            data['pikemanUnlocked'] = False
            data['pikemanCards'] = 0
            data['pikemanHealth'] = 60
            data['pikemanHealthLvl'] = 1
            data['pikemanDamage'] = 20
            data['pikemanDamageLvl'] = 1
            data['pikemanSpeed'] = 10
            data['pikemanSpeedLvl'] = 1
            data['pikemanDefense'] = 20
            data['pikemanDefenseLvl'] = 1
            data['pikemanRange'] = 0
            data['pikemanRangeLvl'] = 1
            data['pikemanCost'] = 30
            data['pikemanSpecial'] = 0
            data['pikemanSpecialLvl'] = 1
            data['bardUnlocked'] = False
            data['bardCards'] = 0
            data['bardHealth'] = 40
            data['bardHealthLvl'] = 1
            data['bardDamage'] = 0
            data['bardDamageLvl'] = 1
            data['bardSpeed'] = 10
            data['bardSpeedLvl'] = 1
            data['bardDefense'] = 10
            data['bardDefenseLvl'] = 1
            data['bardRange'] = 0
            data['bardRangeLvl'] = 1
            data['bardCost'] = 30
            data['bardSpecial'] = 5
            data['bardSpecialLvl'] = 1
            data['gnomeUnlocked'] = False
            data['gnomeCards'] = 0
            data['gnomeHealth'] = 30
            data['gnomeHealthLvl'] = 1
            data['gnomeDamage'] = 20
            data['gnomeDamageLvl'] = 1
            data['gnomeSpeed'] = 10
            data['gnomeSpeedLvl'] = 1
            data['gnomeDefense'] = 20
            data['gnomeDefenseLvl'] = 1
            data['gnomeRange'] = 0
            data['gnomeRangeLvl'] = 1
            data['gnomeCost'] = 25
            data['gnomeSpecial'] = 0
            data['gnomeSpecialLvl'] = 1
            data['gnomeminerUnlocked'] = False
            data['gnomeminerCards'] = 0
            data['gnomeminerHealth'] = 50
            data['gnomeminerHealthLvl'] = 1
            data['gnomeminerDamage'] = 0
            data['gnomeminerDamageLvl'] = 1
            data['gnomeminerSpeed'] = 10
            data['gnomeminerSpeedLvl'] = 1
            data['gnomeminerDefense'] = 50
            data['gnomeminerDefenseLvl'] = 1
            data['gnomeminerRange'] = 0
            data['gnomeminerRangeLvl'] = 1
            data['gnomeminerCost'] = 40
            data['gnomeminerSpecial'] = 24
            data['gnomeminerSpecialLvl'] = 1
            data['mageUnlocked'] = False
            data['mageCards'] = 0
            data['mageHealth'] = 70
            data['mageHealthLvl'] = 1
            data['mageDamage'] = 10
            data['mageDamageLvl'] = 1
            data['mageSpeed'] = 10
            data['mageSpeedLvl'] = 1
            data['mageDefense'] = 25
            data['mageDefenseLvl'] = 1
            data['mageRange'] = 4
            data['mageRangeLvl'] = 1
            data['mageCost'] = 45
            data['mageSpecial'] = 0
            data['mageSpecialLvl'] = 1
            data['priestUnlocked'] = False
            data['priestCards'] = 0
            data['priestHealth'] = 40
            data['priestHealthLvl'] = 1
            data['priestDamage'] = 0
            data['priestDamageLvl'] = 1
            data['priestSpeed'] = 10
            data['priestSpeedLvl'] = 1
            data['priestDefense'] = 25
            data['priestDefenseLvl'] = 1
            data['priestRange'] = 4
            data['priestRangeLvl'] = 1
            data['priestCost'] = 50
            data['priestSpecial'] = 5
            data['priestSpecialLvl'] = 1
            data['crusaderUnlocked'] = False
            data['crusaderCards'] = 0
            data['crusaderHealth'] = 200
            data['crusaderHealthLvl'] = 1
            data['crusaderDamage'] = 20
            data['crusaderDamageLvl'] = 1
            data['crusaderSpeed'] = 10
            data['crusaderSpeedLvl'] = 1
            data['crusaderDefense'] = 25
            data['crusaderDefenseLvl'] = 1
            data['crusaderRange'] = 0
            data['crusaderRangeLvl'] = 1
            data['crusaderCost'] = 70
            data['crusaderSpecial'] = 0
            data['crusaderSpecialLvl'] = 1
        self.ids.sure.text = "RESET"

class TroopsScreen(Screen):
    pass

class EnemiesScreen(Screen):
    pass

class UpgradeScreen(Screen):
    def select(self):
        with shelve.open('Data') as data:
            self.ids.card.source = "Images/" + str(data['current']) + "Card.png"
            self.ids.health.text = str(data[str(data['current']) + "Health"])
            self.ids.damage.text = str(data[str(data['current']) + "Damage"])
            self.ids.defense.text = str(data[str(data['current']) + "Defense"])
            self.ids.range.text = str(data[str(data['current']) + "Range"])
            self.ids.special.text = str(data[str(data['current']) + "Special"])
            self.ids.cards.text = str(data[str(data['current']) + "Cards"])
            self.ids.healthbar.source = "Images/lvl" + str(data[str(data['current']) + "HealthLvl"]) + "health.png"
            self.ids.damagebar.source = "Images/lvl" + str(data[str(data['current']) + "DamageLvl"]) + "damage.png"
            self.ids.defensebar.source = "Images/lvl" + str(data[str(data['current']) + "DefenseLvl"]) + "defense.png"
            self.ids.rangebar.source = "Images/lvl" + str(data[str(data['current']) + "RangeLvl"]) + "range.png"
            self.ids.specialbar.source = "Images/lvl" + str(data[str(data['current']) + "SpecialLvl"]) + "special.png"

    def upgradeHealth(self):
        with shelve.open('Data') as data:
            if  (data[str(data['current']) + "Unlocked"]) == True:
                if  (data[str(data['current']) + "Cards"]) >= (data[str(data['current']) + "HealthLvl"]) + 1:
                    (data[str(data['current']) + "HealthLvl"]) = (data[str(data['current']) + "HealthLvl"]) + 1
                    (data[str(data['current']) + "Cards"]) = (data[str(data['current']) + "Cards"]) - ((data[str(data['current']) + "HealthLvl"]) )
                    (data[str(data['current']) + "Health"]) = math.ceil((data[str(data['current']) + "Health"]) * 1.15)
                    self.select()
    def upgradeDamage(self):
        with shelve.open('Data') as data:
            if  (data[str(data['current']) + "Unlocked"]) == True:
                if  (data[str(data['current']) + "Cards"]) >= (data[str(data['current']) + "DamageLvl"]) + 1:
                    (data[str(data['current']) + "DamageLvl"]) = (data[str(data['current']) + "DamageLvl"]) + 1
                    (data[str(data['current']) + "Cards"]) = (data[str(data['current']) + "Cards"]) - ((data[str(data['current']) + "DamageLvl"]))
                    (data[str(data['current']) + "Damage"]) = math.ceil((data[str(data['current']) + "Damage"]) * 1.15)
                    self.select()
    def upgradeSpeed(self):
        with shelve.open('Data') as data:
            if  (data[str(data['current']) + "Unlocked"]) == True:
                if  (data[str(data['current']) + "Cards"]) >= (data[str(data['current']) + "SpeedLvl"]) + 1:
                    (data[str(data['current']) + "SpeedLvl"]) = (data[str(data['current']) + "SpeedLvl"]) + 1
                    (data[str(data['current']) + "Cards"]) = (data[str(data['current']) + "Cards"]) - ((data[str(data['current']) + "SpeedLvl"]))
                    (data[str(data['current']) + "Speed"]) = math.ceil((data[str(data['current']) + "Speed"]) * 1.15)
                    self.select()
    def upgradeDefense(self):
        with shelve.open('Data') as data:
            if  (data[str(data['current']) + "Unlocked"]) == True:
                if  (data[str(data['current']) + "Cards"]) >= (data[str(data['current']) + "DefenseLvl"]) + 1:
                    (data[str(data['current']) + "DefenseLvl"]) = (data[str(data['current']) + "DefenseLvl"]) + 1
                    (data[str(data['current']) + "Cards"]) = (data[str(data['current']) + "Cards"]) - ((data[str(data['current']) + "DefenseLvl"]))
                    (data[str(data['current']) + "Defense"]) = math.ceil((data[str(data['current']) + "Defense"]) * 1.15)
                    self.select()
    def upgradeRange(self):
        with shelve.open('Data') as data:
            if  (data[str(data['current']) + "Unlocked"]) == True:
                if  (data[str(data['current']) + "Cards"]) >= (data[str(data['current']) + "RangeLvl"]) + 1:
                    (data[str(data['current']) + "RangeLvl"]) = (data[str(data['current']) + "RangeLvl"]) + 1
                    (data[str(data['current']) + "Cards"]) = (data[str(data['current']) + "Cards"]) - ((data[str(data['current']) + "RangeLvl"]))
                    (data[str(data['current']) + "Range"]) = math.ceil((data[str(data['current']) + "Range"]) * 1.15)
                    self.select()
    def upgradeSpecial(self):
        with shelve.open('Data') as data:
            if  (data[str(data['current']) + "Unlocked"]) == True:
                if  (data[str(data['current']) + "Cards"]) >= (data[str(data['current']) + "SpecialLvl"]) + 1:
                    (data[str(data['current']) + "SpecialLvl"]) = (data[str(data['current']) + "SpecialLvl"]) + 1
                    (data[str(data['current']) + "Cards"]) = (data[str(data['current']) + "Cards"]) - ((data[str(data['current']) + "SpecialLvl"]))
                    (data[str(data['current']) + "Special"]) = math.ceil((data[str(data['current']) + "Special"]) * 1.15)
                    self.select()

class BasePackScreen(Screen):
    rng = 0
    def flipCard(self):   
        with shelve.open('Data') as data: 
            if self.ids.card1.source == "Images/cardback.png":
                self.rng = random.randint(0,10)
                if self.rng == 0 or self.rng == 1:
                    self.ids.card1.source = "Images/peasantcard.png"
                    data['peasantCards'] = data['peasantCards'] + 1
                elif self.rng == 2 or self.rng == 3:
                    if data['minerUnlocked'] == True:
                        self.ids.card1.source = "Images/minercard.png"
                        data['minerCards'] = data['minerCards'] + 1
                    else:
                        self.flipCard()
                elif self.rng == 4 or self.rng == 5:
                    if data['swordsmanUnlocked'] == True:
                        self.ids.card1.source = "Images/swordsmancard.png"
                        data['swordsmanCards'] = data['swordsmanCards'] + 1
                    else:
                        self.flipCard()
                elif self.rng == 6 or self.rng == 7:
                    if data['archerUnlocked'] == True:
                        self.ids.card1.source = "Images/archercard.png"
                        data['archerCards'] = data['archerCards'] + 1
                    else:
                        self.flipCard()
                elif self.rng == 9:
                    if data['pikemanUnlocked'] == True:
                        self.ids.card1.source = "Images/pikemancard.png"
                        data['pikemanCards'] = data['pikemanCards'] + 1
                    else:
                        self.flipCard()
                elif self.rng == 8:
                    if data['gnomeUnlocked'] == True:
                        self.ids.card1.source = "Images/gnomecard.png"
                        data['gnomeCards'] = data['gnomeCards'] + 1
                    else:
                        self.flipCard()
                elif self.rng == 10:
                    if data['mageUnlocked'] == True:
                        self.ids.card1.source = "Images/magecard.png"
                        data['mageCards'] = data['mageCards'] + 1
                    else:
                        self.flipCard()
    def flipCard2(self):
        with shelve.open('Data') as data:   
            if self.ids.card2.source == "Images/cardback.png":
                self.rng = random.randint(0,14)
                if self.rng == 0 or self.rng == 1:
                    self.ids.card2.source = "Images/peasantcard.png"
                    data['peasantCards'] = data['peasantCards'] + 1
                elif self.rng == 2 or self.rng == 3:
                    if data['minerUnlocked'] == True:
                        self.ids.card2.source = "Images/minercard.png"
                        data['minerCards'] = data['minerCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 4 or self.rng == 5:
                    if data['swordsmanUnlocked'] == True:
                        self.ids.card2.source = "Images/swordsmancard.png"
                        data['swordsmanCards'] = data['swordsmanCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 6 or self.rng == 7:
                    if data['archerUnlocked'] == True:
                        self.ids.card2.source = "Images/archercard.png"
                        data['archerCards'] = data['archerCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 8:
                    if data['pikemanUnlocked'] == True:
                        self.ids.card2.source = "Images/pikemancard.png"
                        data['pikemanCards'] = data['pikemanCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 9:
                    if data['bardUnlocked'] == True:
                        self.ids.card2.source = "Images/bardcard.png"
                        data['bardCards'] = data['bardCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 10:
                    if data['gnomeUnlocked'] == True:
                        self.ids.card2.source = "Images/gnomecard.png"
                        data['gnomeCards'] = data['gnomeCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 11:
                    if data['gnomeminerUnlocked'] == True:
                        self.ids.card2.source = "Images/gnomeminercard.png"
                        data['gnomeminerCards'] = data['gnomeminerCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 12:
                    if data['mageUnlocked'] == True:
                        self.ids.card2.source = "Images/magecard.png"
                        data['mageCards'] = data['mageCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 13:
                    if data['priestUnlocked'] == True:
                        self.ids.card2.source = "Images/priestcard.png"
                        data['priestCards'] = data['priestCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 14:
                    if data['crusaderUnlocked'] == True:
                        self.ids.card2.source = "Images/crusadercard.png"
                        data['crusaderCards'] = data['crusaderCards'] + 1
                    else:
                        self.flipCard2()

    def reset(self):
        self.ids.card2.source = "Images/cardback.png"
        self.ids.card1.source = "Images/cardback.png"

class DeckScreen(Screen):
    def start(self):
        with shelve.open('Data') as data:
            if data['selectedcards'] == 8:
                self.ids.chosen.clear_widgets()
                self.parent.current = 'gamescrn'
                

    def loadCards(self):
        with shelve.open('Data') as data:
            if data['minerUnlocked'] == True:
                self.ids.miner.source = "Images/minercard.png"
            if data['swordsmanUnlocked'] == True:
                self.ids.swordsman.source = "Images/swordsmancard.png"
            if data['archerUnlocked'] == True:
                self.ids.archer.source = "Images/archercard.png"
            if data['pikemanUnlocked'] == True:
                self.ids.pikeman.source = "Images/pikemancard.png"
            if data['bardUnlocked'] == True:
                self.ids.bard.source = "Images/bardcard.png"
            if data['gnomeUnlocked'] == True:
                self.ids.gnome.source = "Images/gnomecard.png"
            if data['gnomeminerUnlocked'] == True:
                self.ids.gnomeminer.source = "Images/gnomeminercard.png"
            if data['mageUnlocked'] == True:
                self.ids.mage.source = "Images/magecard.png"
            if data['priestUnlocked'] == True:
                self.ids.priest.source = "Images/priestcard.png"
            if data['crusaderUnlocked'] == True:
                self.ids.crusader.source = "Images/crusadercard.png"

    def clearCards(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            self.ids.chosen.clear_widgets()
            data['selectedcards'] = 0
            app.army.clear()

    def addPeasant(self):
        self.peas = Image(source='Images/peasantcard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                self.ids.chosen.add_widget(self.peas)
                data['selectedcards'] = (data['selectedcards'] + 1)
                app.army.append('peasant')

    def addMiner(self):
        self.peas = Image(source='Images/minercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['minerUnlocked'] == True:
                    self.ids.chosen.add_widget(self.peas)
                    data['selectedcards'] = (data['selectedcards'] + 1)
                    app.army.append('miner')
    
    def addSwordsman(self):
        self.peas = Image(source='Images/swordsmancard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['swordsmanUnlocked'] == True:
                    self.ids.chosen.add_widget(self.peas)
                    data['selectedcards'] = (data['selectedcards'] + 1)
                    app.army.append('swordsman')
    
    def addArcher(self):
        self.peas = Image(source='Images/archercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['archerUnlocked'] == True:
                    self.ids.chosen.add_widget(self.peas)
                    data['selectedcards'] = (data['selectedcards'] + 1)
                    app.army.append('archer')
    
    def addPikeman(self):
        self.peas = Image(source='Images/pikemancard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['pikemanUnlocked'] == True:
                    if self.ids.pikeman.source == "Images/pikemancard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('pikeman')
                        self.ids.pikeman.source = "Images/emptycard.png"

    def addBard(self):
        self.peas = Image(source='Images/bardcard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['bardUnlocked'] == True:
                    if self.ids.bard.source == "Images/bardcard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('bard')
                        self.ids.bard.source = "Images/emptycard.png"
    
    def addGnome(self):
        self.peas = Image(source='Images/gnomecard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['gnomeUnlocked'] == True:
                    if self.ids.gnome.source == "Images/gnomecard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('gnome')
                        self.ids.gnome.source = "Images/emptycard.png"
                    
    def addGnomeminer(self):
        self.peas = Image(source='Images/gnomeminercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['gnomeminerUnlocked'] == True:
                    if self.ids.gnomeminer.source == "Images/gnomeminercard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('gnomeminer')
                        self.ids.gnomeminer.source = "Images/emptycard.png"
    
    def addMage(self):
        self.peas = Image(source='Images/magecard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['mageUnlocked'] == True:
                    if self.ids.mage.source == "Images/magecard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('mage')
                        self.ids.mage.source = "Images/emptycard.png"

    def addPriest(self):
        self.peas = Image(source='Images/priestcard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['priestUnlocked'] == True:
                    if self.ids.priest.source == "Images/priestcard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('priest')
                        self.ids.priest.source = "Images/emptycard.png"

    def addCrusader(self):
        self.peas = Image(source='Images/crusadercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['selectedcards'] <= 7:
                if data['crusaderUnlocked'] == True:
                    if self.ids.crusader.source == "Images/crusadercard.png":
                        self.ids.chosen.add_widget(self.peas)
                        data['selectedcards'] = (data['selectedcards'] + 1)
                        app.army.append('crusader')
                        self.ids.crusader.source = "Images/emptycard.png"

class GameScreen(Screen):


    top = []
    middle = []
    bottom = []

    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(data['coins'])

    class entity():
        def __init__(self, imgstr, health, damage, speed, range, defense, defensetype, special, specialtype, attacktype, alive, x, row, side, tile, sprite, animate, direction, ore):
            self.imgstr = imgstr
            self.health = health
            self.damage = damage
            self.speed = speed
            self.range = range
            self.defense = defense
            self.defensetype = defensetype
            self.special = special
            self.specialtype = specialtype
            self.attacktype = attacktype
            self.alive = alive
            self.x = x
            self.row = row
            self.side = side
            self.tile = tile
            self.sprite = sprite
            self.animate = animate
            self.direction = direction
            self.ore = ore

    def updateIron(self):
        with shelve.open('Data') as data:
            self.ids.ironcount.text = str(data['iron'])
            self.ids.coins.text = str(data['coins'])
        
    def updateIron2(self, dt):
        with shelve.open('Data') as data:
            self.ids.ironcount.text = str(data['iron'])

    def addIron(self, *args):
        with shelve.open('Data') as data:
            data['iron'] = (data['iron'] + 1)

    def black1(self):
        self.ids.a.source = 'Images/blackcard.png'

    def black2(self):
        self.ids.b.source = 'Images/blackcard.png'
    
    def black3(self):
        self.ids.c.source = 'Images/blackcard.png'

    def holeLoop(self, dt):
        for i in self.top:
                if i.side == 'hole':
                    char = Image(source = "Images/" + i.imgstr + ".png")
                    char.size_hint = 0.013, 0.43
                    xlocation = (i.tile * 0.005) 
                    char.pos_hint = {'x':xlocation, 'top':1.11}
                    char.fit_mode = "fill"
                    self.ids.troop.add_widget(char)
        for i in self.middle:
                if i.side == 'hole':
                    char = Image(source = "Images/" + i.imgstr + ".png")
                    char.size_hint = 0.013, 0.43
                    xlocation = (i.tile * 0.005) 
                    char.pos_hint = {'x':xlocation, 'top':0.805}
                    char.fit_mode = "fill"
                    self.ids.troop.add_widget(char)
        for i in self.bottom:
                if i.side == 'hole':
                    char = Image(source = "Images/" + i.imgstr + ".png")
                    char.size_hint = 0.013, 0.43
                    xlocation = (i.tile * 0.005) 
                    char.pos_hint = {'x':xlocation, 'top':0.5}
                    char.fit_mode = "fill"
                    self.ids.troop.add_widget(char)

    def loop(self, dt):
        with shelve.open('Data') as data:
            self.ids.troop.clear_widgets()
            data['gamestate'] = 'none'
            for i in self.top:
                if i.alive == False:
                    self.top.remove(i)
                if i.alive == True and i.side == 'good':
                    if i.tile == 63:
                        self.top.remove(i)
                    else:
                        if i.attacktype == "meele":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1):
                                            i.animate = 10
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                            print(str(data['bosshealth']))
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'right':
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + '1' + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                            elif any(b.side == 'hole' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for b in self.top:
                                        if b.imgstr == 'regularore':
                                            i.direction = 'left'
                                            i.ore = 'regular'
                                        if b.imgstr == 'packedore':
                                            i.direction = 'left'
                                            i.ore = 'packed'
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile >= 1:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.14}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.ore == 'regular':
                                if i.animate >= 24:
                                    i.animate = 17
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                            if i.ore == 'packed':
                                if i.animate >= 32 or i.animate <=23:
                                    i.animate = 25
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile <= 0:
                            if i.ore == 'regular':
                                i.direction = 'right'
                                data['iron'] = data['iron'] + (i.special)
                            if i.ore == 'packed':
                                i.direction = 'right'
                                data['iron'] = math.ceil(data['iron'] +((i.special) * 1.5))
                        elif i.attacktype == "spear":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1 or hit.tile == i.tile + 2):
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000072)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "range":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'range':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "bard":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                i.animate = 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                    rng = random.randint(0, data['bardSpecial'])
                                    if rng >= 3:
                                        data['iron'] = data['iron'] + 1
                                    if rng == 2:
                                        data['coins'] = data['coins'] + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "magic":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'magic':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "healer":
                            if any(b.side == 'good' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'good' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):    
                                            hit.health = hit.health + i.special
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
            for i in self.middle:
                if i.alive == False:
                    self.middle.remove(i)
                if i.alive == True and i.side == 'good':
                    if i.tile == 63:
                        self.middle.remove(i)
                    else:
                        if i.attacktype == "meele":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1):
                                            i.animate = 10
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'right':
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + '1' + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                            elif any(b.side == 'hole' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for b in self.middle:
                                        if b.imgstr == 'regularore':
                                            i.direction = 'left'
                                            i.ore = 'regular'
                                        if b.imgstr == 'packedore':
                                            i.direction = 'left'
                                            i.ore = 'packed'
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile >= 1:      
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.ore == 'regular':
                                if i.animate >= 24:
                                    i.animate = 17
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                            if i.ore == 'packed':
                                if i.animate >= 32 or i.animate <=23:
                                    i.animate = 25
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile <= 0:
                            if i.ore == 'regular':
                                i.direction = 'right'
                                data['iron'] = data['iron'] + (i.special)
                            if i.ore == 'packed':
                                i.direction = 'right'
                                data['iron'] = math.ceil(data['iron'] +((i.special) * 1.5))
                        elif i.attacktype == "spear":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1 or hit.tile == i.tile + 2):
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000072)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "range":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'range':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "bard":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                i.animate = 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                    rng = random.randint(0, data['bardSpecial'])
                                    if rng >= 3:
                                        data['iron'] = data['iron'] + 1
                                    if rng == 2:
                                        data['coins'] = data['coins'] + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "magic":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'magic':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "healer":
                            if any(b.side == 'good' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'good' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):    
                                            hit.health = hit.health + i.special
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
            for i in self.bottom:
                if i.alive == False:
                    self.bottom.remove(i)
                if i.alive == True and i.side == 'good':
                    if i.tile == 63:
                        self.bottom.remove(i)
                    else:
                        if i.attacktype == "meele":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1):
                                            i.animate = 10
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'right':
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + '1' + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                            elif any(b.side == 'hole' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for b in self.bottom:
                                        if b.imgstr == 'regularore':
                                            i.direction = 'left'
                                            i.ore = 'regular'
                                        if b.imgstr == 'packedore':
                                            i.direction = 'left'
                                            i.ore = 'packed'
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile >= 1:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.ore == 'regular':
                                if i.animate >= 24:
                                    i.animate = 17
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                            if i.ore == 'packed':
                                if i.animate >= 32 or i.animate <=23:
                                    i.animate = 25
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile <= 0:
                            if i.ore == 'regular':
                                i.direction = 'right'
                                data['iron'] = data['iron'] + (i.special)
                            if i.ore == 'packed':
                                i.direction = 'right'
                                data['iron'] = math.ceil(data['iron'] +((i.special) * 1.5))
                        elif i.attacktype == "spear":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1 or hit.tile == i.tile + 2):
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000072)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "range":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'range':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "bard":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                i.animate = 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                    rng = random.randint(0, data['bardSpecial'])
                                    if rng >= 3:
                                        data['iron'] = data['iron'] + 1
                                    if rng == 2:
                                        data['coins'] = data['coins'] + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "magic":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'magic':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                data['bosshealth'] = data['bosshealth'] - i.damage
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "healer":
                            if any(b.side == 'good' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'good' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):    
                                            hit.health = hit.health + i.special
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1

    def loopBad(self, dt):
        with shelve.open('Data') as data:
            for i in self.top:
                if i.alive == False:
                    if i.side == 'bad':
                        data['coins'] = data['coins'] + 1
                    self.top.remove(i)
                if i.alive == True and i.side == 'bad':
                    if i.attacktype == "meele":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "spear":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1 or b.tile == i.tile - 2) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1 or hit.tile == i.tile - 2):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000072)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "range":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'range':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "magic":

                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'magic':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "boss":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.top) or any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle) or any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.025, 1
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.05}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'boss':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'boss':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'boss':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.025, 1
                            xlocation = (i.tile * 0.005) - (0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.05}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile
                            else: 
                                i.animate = i.animate + 1
            for i in self.middle:
                if i.alive == False:
                    if i.side == 'bad':
                        data['coins'] = data['coins'] + 1
                    self.middle.remove(i)
                if i.alive == True and i.side == 'bad':
                    if i.attacktype == "meele":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "spear":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1 or b.tile == i.tile - 2) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1 or hit.tile == i.tile - 2):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000072)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "range":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'range':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "magic":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'magic':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "boss":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile
                            else: 
                                i.animate = i.animate + 1
            for i in self.bottom:
                if i.alive == False:
                    if i.side == 'bad':
                        data['coins'] = data['coins'] + 1
                    self.bottom.remove(i)
                if i.alive == True and i.side == 'bad':
                    if i.attacktype == "meele":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "spear":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1 or b.tile == i.tile - 2) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.48
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1 or hit.tile == i.tile - 2):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.48
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000072)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "range":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'range':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "magic":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'magic':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "boss":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile
                            else: 
                                i.animate = i.animate + 1

    def gameStateTest(self, dt):
        with shelve.open('Data') as data:
            if data['endless'] >= 1:
                if data['screen'] == 'game':
                    if any (i.side == 'bad' and i.tile <= 0 for i in self.top):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.middle):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.bottom):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.alive == True for i in self.top):
                        data['gamestate'] = 'none'
                    elif any (i.side == 'bad' and i.alive == True for i in self.middle):
                        data['gamestate'] = 'none'
                    elif any (i.side == 'bad' and i.alive == True for i in self.bottom):
                        data['gamestate'] = 'none'
                    else:
                        data['gamestate'] = 'win'
            if data['bosslevel'] == False:
                if data['screen'] == 'game':
                    if any (i.side == 'bad' and i.tile <= 0 for i in self.top):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.middle):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.bottom):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.alive == True for i in self.top):
                        data['gamestate'] = 'none'
                    elif any (i.side == 'bad' and i.alive == True for i in self.middle):
                        data['gamestate'] = 'none'
                    elif any (i.side == 'bad' and i.alive == True for i in self.bottom):
                        data['gamestate'] = 'none'
                    else:
                        data['gamestate'] = 'win'
            if data['bosslevel'] == True:
                if data['screen'] == 'game':
                    if any (i.side == 'bad' and i.tile <= 0 for i in self.top):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.middle):
                        data['gamestate'] = 'lose'
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.bottom):
                        data['gamestate'] = 'lose'
                    elif data['bosshealth'] <= 0:
                        data['gamestate'] = 'win'
            if data['screen'] != 'none':       
                if data['gamestate'] == 'win':
                    if data['endless'] >= 1:
                        self.parent.current = 'deckscrn'
                        data['endless'] = data['endless'] + 2
                        data['endmove'] = 0
                        self.clearCards
                        data['screen'] = 'none'  
                        self.ids.endless.text = str(math.ceil((data['endless']/2)))
                    else: 
                        self.clearCards
                        self.parent.current = 'winscrn'
                        data['screen'] = 'none'     
                if data['gamestate'] == 'lose':
                    self.clearCards
                    self.parent.current = 'losescrn'
                    data['screen'] = 'none'  

    def randomAdd(self, dt):
        with shelve.open('Data') as data:
            print (str(data['endmove']))
            rng = random.randint(0,7)
            if rng == 0:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('skeleton', 50 + data['endless'], 10, 10, 0, 20 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('skeleton', 50 + data['endless'], 10, 10, 0, 20 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('skeleton', 50 + data['endless'], 10, 10, 0, 20 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 1:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b5 = self.entity('spearskeleton', 50 + data['endless'], 20, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b5)
                if rnr == 1:
                    b5 = self.entity('spearskeleton', 50 + data['endless'], 20, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b5)
                if rnr == 2:
                    b5 = self.entity('spearskeleton', 50 + data['endless'], 20, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b5)
            if rng == 2:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('axeskeleton', 100 + data['endless'], 15, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('axeskeleton', 100 + data['endless'], 15, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('axeskeleton', 100 + data['endless'], 15, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 3:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b6 = self.entity('crossbowskeleton', 50 + data['endless'], 6, 10, 6, 10 + data['endless'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b6)
                if rnr == 1:
                    b6 = self.entity('crossbowskeleton', 50 + data['endless'], 6, 10, 6, 10 + data['endless'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b6)
                if rnr == 2:
                    b6 = self.entity('crossbowskeleton', 50 + data['endless'], 6, 10, 6, 10 + data['endless'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b6)
            if rng == 4:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b8 = self.entity('brokengnome', 25 + data['endless'], 30, 10, 0, 50 + data['endless'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b8)
                if rnr == 1:
                    b8 = self.entity('brokengnome', 25 + data['endless'], 30, 10, 0, 50 + data['endless'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b8)
                if rnr == 2:
                    b8 = self.entity('brokengnome', 25 + data['endless'], 30, 10, 0, 50 + data['endless'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b8)
            if rng == 5:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('darkartsgnome', 60 + data['endless'], 10, 10, 4, 25 + data['endless'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('darkartsgnome', 60 + data['endless'], 10, 10, 4, 25 + data['endless'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('darkartsgnome', 60 + data['endless'], 10, 10, 4, 25 + data['endless'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 6:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b2 = self.entity('demon', 120 + data['endless'], 8, 10, 0, 75 + data['endless'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b2)
                if rnr == 1:
                    b2 = self.entity('demon', 120 + data['endless'], 8, 10, 0, 75 + data['endless'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b2)
                if rnr == 2:
                    b2 = self.entity('demon', 120 + data['endless'], 8, 10, 0, 75 + data['endless'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b2)
            if rng == 7:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b3 = self.entity('torchskeleton', 20 + data['endless'], 50, 10, 3, 5 + data['endless'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b3)
                if rnr == 1:
                    b3 = self.entity('torchskeleton', 20 + data['endless'], 50, 10, 3, 5 + data['endless'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b3)
                if rnr == 2:
                    b3 = self.entity('torchskeleton', 20 + data['endless'], 50, 10, 3, 5 + data['endless'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b3)

    def randomAddEnd(self):
        with shelve.open('Data') as data:
            data['endmove'] = data['endmove'] + 10
            print (str(data['endmove']))
            rng = random.randint(0,7)
            if rng == 0:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('skeleton', 50 + data['endless'], 10, 10, 0, 20 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('skeleton', 50 + data['endless'], 10, 10, 0, 20 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('skeleton', 50 + data['endless'], 10, 10, 0, 20 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 1:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b5 = self.entity('spearskeleton', 50 + data['endless'], 20, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b5)
                if rnr == 1:
                    b5 = self.entity('spearskeleton', 50 + data['endless'], 20, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b5)
                if rnr == 2:
                    b5 = self.entity('spearskeleton', 50 + data['endless'], 20, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b5)
            if rng == 2:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('axeskeleton', 100 + data['endless'], 15, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('axeskeleton', 100 + data['endless'], 15, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('axeskeleton', 100 + data['endless'], 15, 10, 0, 25 + data['endless'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 3:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b6 = self.entity('crossbowskeleton', 50 + data['endless'], 6, 10, 6, 10 + data['endless'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b6)
                if rnr == 1:
                    b6 = self.entity('crossbowskeleton', 50 + data['endless'], 6, 10, 6, 10 + data['endless'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b6)
                if rnr == 2:
                    b6 = self.entity('crossbowskeleton', 50 + data['endless'], 6, 10, 6, 10 + data['endless'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b6)
            if rng == 4:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b8 = self.entity('brokengnome', 25 + data['endless'], 30, 10, 0, 50 + data['endless'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b8)
                if rnr == 1:
                    b8 = self.entity('brokengnome', 25 + data['endless'], 30, 10, 0, 50 + data['endless'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b8)
                if rnr == 2:
                    b8 = self.entity('brokengnome', 25 + data['endless'], 30, 10, 0, 50 + data['endless'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b8)
            if rng == 5:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('darkartsgnome', 60 + data['endless'], 10, 10, 4, 25 + data['endless'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('darkartsgnome', 60 + data['endless'], 10, 10, 4, 25 + data['endless'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('darkartsgnome', 60 + data['endless'], 10, 10, 4, 25 + data['endless'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 6:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b2 = self.entity('demon', 120 + data['endless'], 8, 10, 0, 75 + data['endless'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b2)
                if rnr == 1:
                    b2 = self.entity('demon', 120 + data['endless'], 8, 10, 0, 75 + data['endless'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b2)
                if rnr == 2:
                    b2 = self.entity('demon', 120 + data['endless'], 8, 10, 0, 75 + data['endless'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b2)
            if rng == 7:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b3 = self.entity('torchskeleton', 20 + data['endless'], 50, 10, 3, 5 + data['endless'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.top.append(b3)
                if rnr == 1:
                    b3 = self.entity('torchskeleton', 20 + data['endless'], 50, 10, 3, 5 + data['endless'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.middle.append(b3)
                if rnr == 2:
                    b3 = self.entity('torchskeleton', 20 + data['endless'], 50, 10, 3, 5 + data['endless'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + data['endmove'], 1, 2, 'left', 'none')
                    self.bottom.append(b3)


    irong = Clock.schedule_interval(addIron, 0.6)

    def action(self):
        self.ids.b.source = "Images/emptyCard.png"
        self.ids.c.source = "Images/emptyCard.png"
        self.ids.a.source = "Images/emptyCard.png"
        with shelve.open('Data') as data:
            data['screen'] = 'game'
            data['gamestate'] = 'none'
            data['iron'] = 0
        with shelve.open('Data') as data:
            if data['loops'] == False:
                Clock.schedule_interval(self.loop, 0.125)
                Clock.schedule_interval(self.loopBad, 0.125)
                Clock.schedule_interval(self.holeLoop, 0.125)
                Clock.schedule_interval(self.gameStateTest, 2)
                data['loops'] = True
        with shelve.open('Data') as data:
            if data['level'] == 15:
                Clock.schedule_once(self.randomAdd, 10)
                Clock.schedule_once(self.randomAdd, 20)
                Clock.schedule_once(self.randomAdd, 30)
                Clock.schedule_once(self.randomAdd, 40)
                Clock.schedule_once(self.randomAdd, 50)
                Clock.schedule_once(self.randomAdd, 60)
                Clock.schedule_once(self.randomAdd, 70)
                Clock.schedule_once(self.randomAdd, 80)
                Clock.schedule_once(self.randomAdd, 90)
                Clock.schedule_once(self.randomAdd, 100)
                Clock.schedule_once(self.randomAdd, 110)
                Clock.schedule_once(self.randomAdd, 120)
                Clock.schedule_once(self.randomAdd, 130)
                Clock.schedule_once(self.randomAdd, 140)
                Clock.schedule_once(self.randomAdd, 150)
                Clock.schedule_once(self.randomAdd, 160)
                Clock.schedule_once(self.randomAdd, 170)
                Clock.schedule_once(self.randomAdd, 180)
                Clock.schedule_once(self.randomAdd, 190)
                Clock.schedule_once(self.randomAdd, 200)
                Clock.schedule_once(self.randomAdd, 210)
                Clock.schedule_once(self.randomAdd, 220)
                Clock.schedule_once(self.randomAdd, 230)
                Clock.schedule_once(self.randomAdd, 240)
                Clock.schedule_once(self.randomAdd, 250)
            if data['endless'] >= 1:
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 9
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 9
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 9
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 10
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 8
                self.randomAddEnd()
                data['endmove'] = data['endmove'] + 7
                self.randomAddEnd()
            data['yesdraw1'] = True
            data['yesdraw2'] = True
            data['yesdraw3'] = True 
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['level'] <= 7:
                if data['music'] == True:
                    app.homeSong.stop()
                    app.twoSong.stop()
                    app.oneSong.play()
                self.ids.endless.text = ""
                self.ids.background.source = "Images/background1.png"  
                self.ids.top.source = "Images/row1.png"   
                self.ids.middle.source = "Images/row1.png"   
                self.ids.bottom.source = "Images/row1.png"   
            if data['level'] >= 8 and data['level'] <= 11:
                self.ids.background.source = "Images/background2.png" 
                self.ids.top.source = "Images/row1.png"   
                self.ids.middle.source = "Images/row1.png"   
                self.ids.bottom.source = "Images/row1.png"   
                if data['music'] == True:
                    app.homeSong.stop()
                    app.oneSong.stop()
                    app.twoSong.play()
                self.ids.endless.text = ""
            if data['level'] >= 12 and data['level'] <= 15:
                self.ids.background.source = "Images/background3.png" 
                self.ids.top.source = "Images/row2.png"   
                self.ids.middle.source = "Images/row2.png"   
                self.ids.bottom.source = "Images/row2.png" 
                self.ids.endless.text = ""  
                if data['music'] == True:
                    app.homeSong.stop()
                    app.oneSong.play()
                    app.twoSong.stop()
            if data['level'] == 16:
                self.ids.endless.text = str(math.ceil((data['endless']/2)))
                rrng = random.randint(0,2)
                if rrng == 0:
                    if data['music'] == True:
                        app.homeSong.stop()
                        app.twoSong.stop()
                        app.oneSong.play()
                    self.ids.background.source = "Images/background1.png"  
                    self.ids.top.source = "Images/row1.png"   
                    self.ids.middle.source = "Images/row1.png"   
                    self.ids.bottom.source = "Images/row1.png"   
                if rrng == 1:
                    self.ids.background.source = "Images/background2.png" 
                    self.ids.top.source = "Images/row1.png"   
                    self.ids.middle.source = "Images/row1.png"   
                    self.ids.bottom.source = "Images/row1.png"   
                    if data['music'] == True:
                        app.homeSong.stop()
                        app.oneSong.stop()
                        app.twoSong.play()
                if rrng == 2:
                    self.ids.background.source = "Images/background3.png" 
                    self.ids.top.source = "Images/row2.png"   
                    self.ids.middle.source = "Images/row2.png"   
                    self.ids.bottom.source = "Images/row2.png"   
                    if data['music'] == True:
                        app.homeSong.stop()
                        app.oneSong.play()
                        app.twoSong.stop()
                        
    def iron(self):
        self.irong()
        Clock.schedule_interval(self.updateIron2, 1)
        app = App.get_running_app()
        print (app.army)
        with shelve.open('Data') as data:
            self.ids.ironcount.text = str(data['iron'])
            self.ids.coins.text = str(data['coins'])

    def loadCards(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            aaa = app.army[0]
            self.ids.a.source = "Images/" + str(aaa) + "card.png"
            bbb = app.army[1]
            self.ids.b.source = "Images/" + str(bbb) + "card.png"
            ccc = app.army[2]
            self.ids.c.source = "Images/" + str(ccc) + "card.png"

    def drawCard1(self):
        rng = random.randint(0,7)
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['yesdraw1'] == True:
                curr = app.army[rng]
                if curr == 'peasant':
                    self.ids.a.source = "Images/PeasantCard.png"
                    data['aimg'] = "Images/PeasantCard.png"
                if curr == 'miner':
                    self.ids.a.source = "Images/MinerCard.png"
                    data['aimg'] = "Images/MinerCard.png"
                if curr == 'swordsman':
                    self.ids.a.source = "Images/SwordsmanCard.png"
                    data['aimg'] = "Images/SwordsmanCard.png"
                if curr == 'archer':
                    self.ids.a.source = "Images/ArcherCard.png"
                    data['aimg'] = "Images/ArcherCard.png"
                if curr == 'pikeman':
                    self.ids.a.source = "Images/PikemanCard.png"
                    data['aimg'] = "Images/PikemanCard.png"
                if curr == 'bard':
                    self.ids.a.source = "Images/BardCard.png"
                    data['aimg'] = "Images/BardCard.png"
                if curr == 'gnome':
                    self.ids.a.source = "Images/GnomeCard.png"
                    data['aimg'] = "Images/GnomeCard.png"
                if curr == 'gnomeminer':
                    self.ids.a.source = "Images/GnomeminerCard.png"
                    data['aimg'] = "Images/GnomeminerCard.png"
                if curr == 'mage':
                    self.ids.a.source = "Images/MageCard.png"
                    data['aimg'] = "Images/MageCard.png"
                if curr == 'priest':
                    self.ids.a.source = "Images/PriestCard.png"
                    data['aimg'] = "Images/PriestCard.png"
                if curr == 'crusader':
                    self.ids.a.source = "Images/CrusaderCard.png"
                    data['aimg'] = "Images/CrusaderCard.png"
            else:
                self.ids.a.source = str(data['aimg'])
            data['yesdraw1'] = False
    def drawCard2(self):
        rng2 = random.randint(0,7)
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['yesdraw2'] == True:
                curr = app.army[rng2]
                if curr == 'peasant':
                    self.ids.b.source = "Images/PeasantCard.png"
                    data['bimg'] = "Images/PeasantCard.png"
                if curr == 'miner':
                    self.ids.b.source = "Images/MinerCard.png"
                    data['bimg'] = "Images/MinerCard.png"
                if curr == 'swordsman':
                    self.ids.b.source = "Images/SwordsmanCard.png"
                    data['bimg'] = "Images/SwordsmanCard.png"
                if curr == 'archer':
                    self.ids.b.source = "Images/ArcherCard.png"
                    data['bimg'] = "Images/ArcherCard.png"
                if curr == 'pikeman':
                    self.ids.b.source = "Images/PikemanCard.png"
                    data['bimg'] = "Images/PikemanCard.png"
                if curr == 'bard':
                    self.ids.b.source = "Images/BardCard.png"
                    data['bimg'] = "Images/BardCard.png"
                if curr == 'gnome':
                    self.ids.b.source = "Images/GnomeCard.png"
                    data['bimg'] = "Images/GnomeCard.png"
                if curr == 'gnomeminer':
                    self.ids.b.source = "Images/GnomeminerCard.png"
                    data['bimg'] = "Images/GnomeminerCard.png"
                if curr == 'mage':
                    self.ids.b.source = "Images/MageCard.png"
                    data['bimg'] = "Images/MageCard.png"
                if curr == 'priest':
                    self.ids.b.source = "Images/PriestCard.png"
                    data['bimg'] = "Images/PriestCard.png"
                if curr == 'crusader':
                    self.ids.b.source = "Images/CrusaderCard.png"
                    data['bimg'] = "Images/CrusaderCard.png"
            else:
                self.ids.b.source = str(data['bimg'])
            data['yesdraw2'] = False
    def drawCard3(self):
        rng3 = random.randint(0,7)
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if data['yesdraw3'] == True:
                curr = app.army[rng3]
                if curr == 'peasant':
                    self.ids.c.source = "Images/PeasantCard.png"
                    data['cimg'] = "Images/PeasantCard.png"
                if curr == 'miner':
                    self.ids.c.source = "Images/MinerCard.png"
                    data['cimg'] = "Images/MinerCard.png"
                if curr == 'swordsman':
                    self.ids.c.source = "Images/SwordsmanCard.png"
                    data['cimg'] = "Images/SwordsmanCard.png"
                if curr == 'archer':
                    self.ids.c.source = "Images/ArcherCard.png"
                    data['cimg'] = "Images/ArcherCard.png"
                if curr == 'pikeman':
                    self.ids.c.source = "Images/PikemanCard.png"
                    data['cimg'] = "Images/PikemanCard.png"
                if curr == 'bard':
                    self.ids.c.source = "Images/BardCard.png"
                    data['cimg'] = "Images/BardCard.png"
                if curr == 'gnome':
                    self.ids.c.source = "Images/GnomeCard.png"
                    data['cimg'] = "Images/GnomeCard.png"
                if curr == 'gnomeminer':
                    self.ids.c.source = "Images/GnomeminerCard.png"
                    data['cimg'] = "Images/GnomeminerCard.png"
                if curr == 'mage':
                    self.ids.c.source = "Images/MageCard.png"
                    data['cimg'] = "Images/MageCard.png"
                if curr == 'priest':
                    self.ids.c.source = "Images/PriestCard.png"
                    data['cimg'] = "Images/PriestCard.png"
                if curr == 'crusader':
                    self.ids.c.source = "Images/CrusaderCard.png"
                    data['cimg'] = "Images/CrusaderCard.png"
            else:
                self.ids.c.source = str(data['cimg'])
            data['yesdraw3'] = False

    def clearCards(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            self.ids.b.source = "Images/emptyCard.png"
            self.ids.c.source = "Images/emptyCard.png"
            self.ids.a.source = "Images/emptyCard.png"
            data['selectedcards'] = 0
            app.army.clear()
            self.top.clear()
            data['gamestate'] = 'none'
            data['screen'] = 'none'
            self.middle.clear()
            self.bottom.clear()
            self.irong.cancel()
            data['iron'] = 0
            data['yesdraw1'] = True
            data['yesdraw2'] = True
            data['yesdraw3'] = True

    def select1(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if self.ids.a.source == "Images/PeasantCard.png":
                if data['iron'] >= data['peasantCost']:
                    if data['lane'] == 'top':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/PeasantCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/MinerCard.png":
                if data['iron'] >= data['minerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/MinerCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/SwordsmanCard.png":
                if data['iron'] >= data['swordsmanCost']:
                    if data['lane'] == 'top':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/swordsmanCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/ArcherCard.png":
                if data['iron'] >= data['archerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/ArcherCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/PikemanCard.png":
                if data['iron'] >= data['pikemanCost']:
                    if data['lane'] == 'top':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/PikemanCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/BardCard.png":
                if data['iron'] >= data['bardCost']:
                    if data['lane'] == 'top':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/BardCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/GnomeCard.png":
                if data['iron'] >= data['peasantCost']:
                    if data['lane'] == 'top':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/GnomeCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/GnomeminerCard.png":
                if data['iron'] >= data['gnomeminerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/GnomeminerCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/MageCard.png":
                if data['iron'] >= data['mageCost']:
                    if data['lane'] == 'top':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/MageCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/PriestCard.png":
                if data['iron'] >= data['priestCost']:
                    if data['lane'] == 'top':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/PriestCard.png"
                else:
                    data['yesdraw1'] = False
            if self.ids.a.source == "Images/CrusaderCard.png":
                if data['iron'] >= data['crusaderCost']:
                    if data['lane'] == 'top':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw1'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw1'] = True
                    data['aimg'] = "Images/crusaderCard.png"
                else:
                    data['yesdraw1'] = False
    def select2(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if self.ids.b.source == "Images/PeasantCard.png":
                if data['iron'] >= data['peasantCost']:
                    if data['lane'] == 'top':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/PeasantCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/MinerCard.png":
                if data['iron'] >= data['minerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/MinerCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/SwordsmanCard.png":
                if data['iron'] >= data['swordsmanCost']:
                    if data['lane'] == 'top':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw2'] = True
                    data['aimg'] = "Images/swordsmanCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/ArcherCard.png":
                if data['iron'] >= data['archerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/ArcherCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/PikemanCard.png":
                if data['iron'] >= data['pikemanCost']:
                    if data['lane'] == 'top':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/PikemanCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/BardCard.png":
                if data['iron'] >= data['bardCost']:
                    if data['lane'] == 'top':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/BardCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/GnomeCard.png":
                if data['iron'] >= data['peasantCost']:
                    if data['lane'] == 'top':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/GnomeCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/GnomeminerCard.png":
                if data['iron'] >= data['gnomeminerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/GnomeminerCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/MageCard.png":
                if data['iron'] >= data['mageCost']:
                    if data['lane'] == 'top':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/MageCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/PriestCard.png":
                if data['iron'] >= data['priestCost']:
                    if data['lane'] == 'top':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/PriestCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.b.source == "Images/CrusaderCard.png":
                if data['iron'] >= data['crusaderCost']:
                    if data['lane'] == 'top':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw2'] = True
                    data['bimg'] = "Images/crusaderCard.png"
                else:
                    data['yesdraw2'] = False
    def select3(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if self.ids.c.source == "Images/PeasantCard.png":
                if data['iron'] >= data['peasantCost']:
                    if data['lane'] == 'top':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['peasantCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/PeasantCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/MinerCard.png":
                if data['iron'] >= data['minerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['minerCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/MinerCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/SwordsmanCard.png":
                if data['iron'] >= data['swordsmanCost']:
                    if data['lane'] == 'top':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('swordsman', data['swordsmanHealth'], data['swordsmanDamage'], data['swordsmanSpeed'], data['swordsmanRange'], data['swordsmanDefense'], 'meele', data['swordsmanSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['swordsmanCost']
                        data['yesdraw3'] = True
                    data['aimg'] = "Images/swordsmanCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/ArcherCard.png":
                if data['iron'] >= data['archerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('archer', data['archerHealth'], data['archerDamage'], data['archerSpeed'], data['archerRange'], data['archerDefense'], 'range', data['archerSpecial'], 'none', 'range', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['archerCost']
                        data['yesdraw2'] = True
                    data['cimg'] = "Images/ArcherCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.c.source == "Images/PikemanCard.png":
                if data['iron'] >= data['pikemanCost']:
                    if data['lane'] == 'top':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('pikeman', data['pikemanHealth'], data['pikemanDamage'], data['pikemanSpeed'], data['pikemanRange'], data['pikemanDefense'], 'meele', data['pikemanSpecial'], 'none', 'spear', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['pikemanCost']
                        data['yesdraw2'] = True
                    data['cimg'] = "Images/PikemanCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.c.source == "Images/BardCard.png":
                if data['iron'] >= data['bardCost']:
                    if data['lane'] == 'top':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw2'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('bard', data['bardHealth'], data['bardDamage'], data['bardSpeed'], data['bardRange'], data['bardDefense'], 'range', data['bardSpecial'], 'bard', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['bardCost']
                        data['yesdraw2'] = True
                    data['cimg'] = "Images/BardCard.png"
                else:
                    data['yesdraw2'] = False
            if self.ids.c.source == "Images/GnomeCard.png":
                if data['iron'] >= data['peasantCost']:
                    if data['lane'] == 'top':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('gnome', data['gnomeHealth'], data['gnomeDamage'], data['gnomeSpeed'], data['gnomeRange'], data['gnomeDefense'], 'magic', data['gnomeSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['gnomeCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/GnomeCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/GnomeminerCard.png":
                if data['iron'] >= data['gnomeminerCost']:
                    if data['lane'] == 'top':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['gnomeminerCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/GnomeminerCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/MageCard.png":
                if data['iron'] >= data['mageCost']:
                    if data['lane'] == 'top':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['mageCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/MageCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/PriestCard.png":
                if data['iron'] >= data['priestCost']:
                    if data['lane'] == 'top':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['priestCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/PriestCard.png"
                else:
                    data['yesdraw3'] = False
            if self.ids.c.source == "Images/CrusaderCard.png":
                if data['iron'] >= data['crusaderCost']:
                    if data['lane'] == 'top':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'middle':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw3'] = True
                    if data['lane'] == 'bottom':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        data['iron'] = data['iron'] - data['crusaderCost']
                        data['yesdraw3'] = True
                    data['cimg'] = "Images/crusaderCard.png"
                else:
                    data['yesdraw3'] = False

    def rowTop(self):
        with shelve.open('Data') as data:
            if data['level'] <= 11:
                data['lane'] = 'top'
                self.ids.top.source = 'Images/row1selected.png'
                self.ids.middle.source = 'Images/row1.png'
                self.ids.bottom.source = 'Images/row1.png'
                print(self.top)
            if data['level'] >= 12 and data['level'] <= 15:
                data['lane'] = 'top'
                self.ids.top.source = 'Images/row2selected.png'
                self.ids.middle.source = 'Images/row2.png'
                self.ids.bottom.source = 'Images/row2.png'
                print(self.top)
            # if data['readydrop'] == 'peasant':
            #     add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 0, 'good', 1)
            #     self.top.append(add)
            # if data['readydrop'] == 'miner':
            #     add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 0, 'good', 1)
            #     self.top.append(add)
            # if data['readydrop'] != 'none':
            #     data['iron'] = data['iron'] - data[data['todrop'] + "Cost"]
            #     data['readydrop'] = 'none'           
    def rowMiddle(self):
        with shelve.open('Data') as data:
            data['lane'] = 'middle'
            if data['level'] <= 11:
                data['lane'] = 'middle'
                self.ids.middle.source = 'Images/row1selected.png'
                self.ids.bottom.source = 'Images/row1.png'
                self.ids.top.source = 'Images/row1.png'
                print(self.top)
            if data['level'] >= 12 and data['level'] <= 15:
                data['lane'] = 'middle'
                self.ids.middle.source = 'Images/row2selected.png'
                self.ids.top.source = 'Images/row2.png'
                self.ids.bottom.source = 'Images/row2.png'
                print(self.top)
        #     if data['readydrop'] == 'peasant':
        #         add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 0, 'good', 1)
        #         self.middle.append(add)
        #     if data['readydrop'] == 'miner':
        #         add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 0, 'good', 1)
        #         self.middle.append(add)
        #     if data['readydrop'] != 'none':
        #         data['iron'] = data['iron'] - data[data['todrop'] + "Cost"]
        #         data['readydrop'] = 'none'
    def rowBottom(self):
        with shelve.open('Data') as data:
            data['lane'] = 'bottom'
            if data['level'] <= 11:
                data['lane'] = 'bottom'
                self.ids.bottom.source = 'Images/row1selected.png'
                self.ids.middle.source = 'Images/row1.png'
                self.ids.top.source = 'Images/row1.png'
                print(self.top)
            if data['level'] >= 12 and data['level'] <= 15:
                data['lane'] = 'bottom'
                self.ids.bottom.source = 'Images/row2selected.png'
                self.ids.top.source = 'Images/row2.png'
                self.ids.middle.source = 'Images/row2.png'
                print(self.top)
            # if data['readydrop'] == 'peasant':
            #     add = self.entity('peasant', data['peasantHealth'], data['peasantDamage'], data['peasantSpeed'], data['peasantRange'], data['peasantDefense'], 'meele', data['peasantSpecial'], 'none', 'meele', True, 0, 0, 'good', 1)
            #     self.bottom.append(add)
            # if data['readydrop'] == 'miner':
            #     add = self.entity('miner', data['minerHealth'], data['minerDamage'], data['minerSpeed'], data['minerRange'], data['minerDefense'], 'meele', data['minerSpecial'], 'mine', 'none', True, 0, 0, 'good', 1)
            #     self.bottom.append(add)
            # if data['readydrop'] != 'none':
            #     data['iron'] = data['iron'] - data[data['todrop'] + "Cost"]
            #     data['readydrop'] = 'none'

    def summonBadGuys(self):
        with shelve.open('Data') as data:
            self.top.clear()
            self.middle.clear()
            self.bottom.clear()
            if data['level'] == 1:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 35, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 71, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 91, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 116, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 126, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 141, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 151, 1, 2, 'left', 'none')
                self.bottom.append(b9)
            elif data['level'] == 2:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 35, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 86, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 96, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 106, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 121, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 141, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 146, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 156, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 161, 1, 2, 'left', 'none')
                self.top.append(b10)
                b11 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 161, 1, 2, 'left', 'none')
                self.middle.append(b11)   
            elif data['level'] == 3:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 35, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 86, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 96, 1, 2, 'left', 'none')
                self.top.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 101, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 126, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 155, 1, 2, 'left', 'none')
                self.top.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.middle.append(b11)      
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 174, 1, 2, 'left', 'none')
                self.bottom.append(b13)
                b14 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 175, 1, 2, 'left', 'none')
                self.middle.append(b14)   
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 182, 1, 2, 'left', 'none')
                self.bottom.append(b15)         
            elif data['level'] == 4:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 91, 1, 2, 'left', 'none')
                self.top.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 98, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 112, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 123, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('spearskeleton', 60, 10, 10, 0, 10, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 143, 1, 2, 'left', 'none')
                self.middle.append(b7)
                b8 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 152, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('spearskeleton', 60, 10, 10, 0, 10, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 171, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 176, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 187, 1, 2, 'left', 'none')
                self.middle.append(b12)
                b13 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 195, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('spearskeleton', 60, 10, 10, 0, 10, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.bottom.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 206, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 212, 1, 2, 'left', 'none')
                self.top.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 224, 1, 2, 'left', 'none')
                self.bottom.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 226, 1, 2, 'left', 'none')
                self.middle.append(b18)
            elif data['level'] == 5:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.middle.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.middle.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 103, 1, 2, 'left', 'none')
                self.top.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 113, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.top.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 132, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 139, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 147, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.top.append(b10)
                b11 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 166, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 169, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 175, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 181, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 190, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 192, 1, 2, 'left', 'none')
                self.top.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 197, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 204, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 213, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 216, 1, 2, 'left', 'none')
                self.bottom.append(b20)
            elif data['level'] == 6:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 105, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 115, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 123, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 145, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 155, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.middle.append(b10)
                b11 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 163, 1, 2, 'left', 'none')
                self.bottom.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 176, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 186, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 194, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 208, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 214, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 216, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 224, 1, 2, 'left', 'none')
                self.bottom.append(b19)
            elif data['level'] == 7:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.middle.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 104, 1, 2, 'left', 'none')
                self.bottom.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 116, 1, 2, 'left', 'none')
                self.middle.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 126, 1, 2, 'left', 'none')
                self.top.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 138, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 142, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 152, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 180, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 188, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 207, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 212, 1, 2, 'left', 'none')
                self.bottom.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 218, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 222, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 231, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 233, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 243, 1, 2, 'left', 'none')
                self.bottom.append(b19)
                b20 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 249, 1, 2, 'left', 'none')
                self.middle.append(b20)
            elif data['level'] == 8:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 24, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 99, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 108, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 116, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 127, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 155, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 172, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 186, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 193, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 214, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 227, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 229, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 238, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 247, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 255, 1, 2, 'left', 'none')
                self.bottom.append(b20)
            elif data['level'] == 9:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 24, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 101, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 123, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 133, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 143, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 169, 1, 2, 'left', 'none')
                self.middle.append(b10)
                b11 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 177, 1, 2, 'left', 'none')
                self.bottom.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 186, 1, 2, 'left', 'none')
                self.middle.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 193, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 217, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 225, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 231, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 239, 1, 2, 'left', 'none')
                self.middle.append(b18)
                b19 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 246, 1, 2, 'left', 'none')
                self.top.append(b19)
                b20 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 253, 1, 2, 'left', 'none')
                self.bottom.append(b20)
                b21 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.middle.append(b21)
            elif data['level'] == 10:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.middle.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 24, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 99, 1, 2, 'left', 'none')
                self.top.append(b3)
                b4 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 110, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 118, 1, 2, 'left', 'none')
                self.top.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 127, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 175, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 183, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 190, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 198, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 214, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 227, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 229, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 238, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 250, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 255, 1, 2, 'left', 'none')
                self.bottom.append(b20)
                b21 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.top.append(b21)
                b22 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 266, 1, 2, 'left', 'none')
                self.middle.append(b22)
            elif data['level'] == 11:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 22, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 28, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 91, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 105, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 114, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 157, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 174, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 180, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 192, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 200, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 208, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 216, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 233, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 238, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 247, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 254, 1, 2, 'left', 'none')
                self.bottom.append(b20)
                b21 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.top.append(b21)
                b22 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 267, 1, 2, 'left', 'none')
                self.middle.append(b22)
            elif data['level'] == 12:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.middle.append(b1)
                b2 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 89, 1, 2, 'left', 'none')
                self.top.append(b2)
                b3 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 96, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 105, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 114, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 124, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 138, 1, 2, 'left', 'none')
                self.middle.append(b7)
                b8 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 146, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 157, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 183, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 189, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 196, 1, 2, 'left', 'none')
                self.bottom.append(b14)
                b15 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 220, 1, 2, 'left', 'none')
                self.middle.append(b16)
                b17 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 226, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 232, 1, 2, 'left', 'none')
                self.bottom.append(b18)
            elif data['level'] == 13:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 88, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 95, 1, 2, 'left', 'none')
                self.bottom.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 102, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 129, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 151, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 157, 1, 2, 'left', 'none')
                self.middle.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 164, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 182, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 192, 1, 2, 'left', 'none')
                self.bottom.append(b13)
                b14 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 201, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 209, 1, 2, 'left', 'none')
                self.top.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 220, 1, 2, 'left', 'none')
                self.middle.append(b16)
                b17 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 232, 1, 2, 'left', 'none')
                self.bottom.append(b17)
                b18 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 239, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 244, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 250, 1, 2, 'left', 'none')
                self.top.append(b20)
                b21 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.bottom.append(b21)
                b22 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 267, 1, 2, 'left', 'none')
                self.middle.append(b22)
                b23 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 273, 1, 2, 'left', 'none')
                self.top.append(b23)
            elif data['level'] == 14:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 88, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 100, 1, 2, 'left', 'none')
                self.bottom.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 102, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 129, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 132, 1, 2, 'left', 'none')
                self.middle.append(b7)
                b8 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 141, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.middle.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 183, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 189, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 200, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 210, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 215, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 223, 1, 2, 'left', 'none')
                self.bottom.append(b17)
                b18 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 231, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 244, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 250, 1, 2, 'left', 'none')
                self.top.append(b20)
                b21 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.bottom.append(b21)
                b22 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 266, 1, 2, 'left', 'none')
                self.middle.append(b22)
            elif data['level'] == 15:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('dragon', 600, 4, 10, 8, 0, 'none', 0, 'none', 'boss', True, 0, 1, 'bad', 60, 1, 2, 'left', 'none')
                data['bosshealth'] = 500
                self.top.append(b1)
                b2 = self.entity('nothing', 600, 4, 10, 8, 0, 'none', 0, 'none', 'boss', True, 0, 1, 'bad', 60, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('nothing', 600, 4, 10, 8, 0, 'none', 0, 'none', 'boss', True, 0, 1, 'bad', 60, 1, 2, 'left', 'none')
                self.bottom.append(b3)

class LoseScreen(Screen):
    pass

class WinScreen(Screen):
    def set(self):
        self.ids.card1.source = "Images/cardback.png"
    def flipCard(self):
        with shelve.open('Data') as data:   
            print(data['level'])
            print(data['unlockedlevel'])
            if data['level'] == 1 and data['unlockedlevel'] == 1:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/minercard.png"
                    data['minerCards'] = data['minerCards'] + 1
                    data['minerUnlocked'] = True
                    data['unlockedlevel'] = 2
            if data['level'] == 2 and data['unlockedlevel'] == 2:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/swordsmancard.png"
                    data['swordsmanCards'] = data['swordsmanCards'] + 1
                    data['swordsmanUnlocked'] = True
                    data['unlockedlevel'] = 3
            if data['level'] == 3 and data['unlockedlevel'] == 3:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard50.png"
                    data['coins'] = data['coins'] + 50
                    data['unlockedlevel'] = 4
            if data['level'] == 4 and data['unlockedlevel'] == 4:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/archercard.png"
                    data['archerCards'] = data['archerCards'] + 1
                    data['archerUnlocked'] = True
                    data['unlockedlevel'] = 5
            if data['level'] == 5 and data['unlockedlevel'] == 5:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard50.png"
                    data['coins'] = data['coins'] + 50
                    data['unlockedlevel'] = 6
            if data['level'] == 6 and data['unlockedlevel'] == 6:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/pikemancard.png"
                    data['pikemanCards'] = data['pikemanCards'] + 1
                    data['pikemanUnlocked'] = True
                    data['unlockedlevel'] = 7
            if data['level'] == 7 and data['unlockedlevel'] == 7:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/bardcard.png"
                    data['bardCards'] = data['bardCards'] + 1
                    data['bardUnlocked'] = True
                    data['unlockedlevel'] = 8
            if data['level'] == 8 and data['unlockedlevel'] == 8:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard50.png"
                    data['coins'] = data['coins'] + 50
                    data['unlockedlevel'] = 9
            if data['level'] == 9 and data['unlockedlevel'] == 9:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/gnomecard.png"
                    data['gnomeCards'] = data['gnomeCards'] + 1
                    data['gnomeUnlocked'] = True
                    data['unlockedlevel'] = 10
            if data['level'] == 10 and data['unlockedlevel'] == 10:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/gnomeminercard.png"
                    data['gnomeminerCards'] = data['gnomeminerCards'] + 1
                    data['gnomeminerUnlocked'] = True
                    data['unlockedlevel'] = 11
            if data['level'] == 11 and data['unlockedlevel'] == 11:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/magecard.png"
                    data['mageCards'] = data['mageCards'] + 1
                    data['mageUnlocked'] = True
                    data['unlockedlevel'] = 12
            if data['level'] == 12 and data['unlockedlevel'] == 12:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/sapphirecard.png"
                    data['sapphires'] = data['sapphires'] + 1
                    data['unlockedlevel'] = 13
            if data['level'] == 13 and data['unlockedlevel'] == 13:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/priestcard.png"
                    data['priestCards'] = data['priestCards'] + 1
                    data['priestUnlocked'] = True
                    data['unlockedlevel'] = 14
            if data['level'] == 14 and data['unlockedlevel'] == 14:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/crusadercard.png"
                    data['crusaderCards'] = data['crusaderCards'] + 1
                    data['crusaderUnlocked'] = True
                    data['unlockedlevel'] = 15
            if data['level'] == 15 and data['unlockedlevel'] == 15:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/emeraldcard.png"
                    data['emeralds'] = data['emeralds'] + 1
                    data['unlockedlevel'] = 16
            else:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard10.png"
                    data['coins'] = data['coins'] + 10


kv = Builder.load_file('medieval.kv')

class MedievalApp(App):
    homeSong = SoundLoader.load('Home_1.wav')
    oneSong = SoundLoader.load('world1.wav')
    twoSong = SoundLoader.load('world1.2.wav')
    music = True
    army=[]
    def build(self):
        return kv

MedievalApp().run()