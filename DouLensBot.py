import telebot
from decouple import config
from pathlib import Path
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = config('DouLens_Bot')
bot = telebot.TeleBot(BOT_TOKEN)

# ------------------------------------------------------------- DATA ------------------------------------------------------------- #
# Soflens Natural Colors - Data
SoflensNaturalColors = {
'SoflensNaturalColors01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Amazon.jpeg',
'SoflensNaturalColors02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Aquamarine.jpeg',
'SoflensNaturalColors03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Dark Hazel.jpeg',
'SoflensNaturalColors04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Emerald.jpeg',
'SoflensNaturalColors05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - India.jpeg',
'SoflensNaturalColors06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Indigo.jpeg',
'SoflensNaturalColors07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Jade.jpeg',
'SoflensNaturalColors08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Pacific.jpeg',
'SoflensNaturalColors09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Platinum.jpeg',
'SoflensNaturalColors10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Soflens Natural Colors\\SofLens Natural Colors - Topaz.jpeg'}

# Naturél - Data
Naturel = {
'Naturel01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Hazel.jpg',
'Naturel02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Ivory.jpg',
'Naturel03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Jade.jpg',
'Naturel04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Marron.jpg',
'Naturel05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Zircon.jpg',
'Naturel06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Blue.jpg',
'Naturel07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - Core Green.jpg',
'Naturel08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - La Green.jpg',
'Naturel09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - La Hazel.jpg',
'Naturel10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - La Lolite.jpg',
'Naturel11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - La Agate.jpg',
'Naturel12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Naturél\\Naturél - La Gray.jpg'}  

# Air Optix Colors - Data
AirOptixColors = {
'AirOptixColors01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Brilliant Blue.jpg',
'AirOptixColors02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Brown.jpg',
'AirOptixColors03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Gemstone Green.jpg',
'AirOptixColors04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Gray.jpg',
'AirOptixColors05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Green.jpg',
'AirOptixColors06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Honey.jpg',
'AirOptixColors07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Purehazel.jpg',
'AirOptixColors08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Sterling Gray.jpg',
'AirOptixColors09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - True Sapphire.jpg',
'AirOptixColors10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Turquoise.jpg',
'AirOptixColors11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Amethyst.jpg',
'AirOptixColors12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Air Optix Colors\\Air Optix Colors - Blue.jpg'}

# Luminous - Data
Luminous = {
'Luminous01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Blue.jpg',
'Luminous02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Crystal.jpg',
'Luminous03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Dazzling Green.jpg',
'Luminous04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Gray.jpg',
'Luminous05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Green.jpg',
'Luminous06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Hazel.jpg',
'Luminous07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Latin Brown.jpg',
'Luminous08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Latin Gray.jpg',
'Luminous09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Lazord.jpg',
'Luminous10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Luminous\\Luminous - Lemon.jpg'}

# MyLense - Data
MyLense = {
'MyLense01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Capri.jpg',
'MyLense02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\MyLense - Turquoise.jpg',
'MyLense03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Light Blue.jpg',
'MyLense04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Light Brown.jpg',
'MyLense05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Light Gray.jpg',
'MyLense06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Light Green.jpg',
'MyLense07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Oro Brown.jpg',
'MyLense08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Oro Gray.jpg',
'MyLense09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Oro Hazel.jpg',
'MyLense10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\MyLense\\Mylense - Oro Ice.jpg'}

# Lorans - Data
Lorans = {
'Lorans01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Latte.jpg',
'Lorans02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Navy.jpg',
'Lorans03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Pearl.jpg',
'Lorans04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Caramel.jpg',
'Lorans05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Blue.jpg',
'Lorans06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Brown.jpg',
'Lorans07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Kadet Gray.jpg',
'Lorans08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lorans\\Lorans - Pale Gray.jpg'}

# Amara - Data
Amara = {
'Amara01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Pure Hazel.jpg',
'Amara02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Royal Blue.jpg',
'Amara03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Sky Gray.jpg',
'Amara04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Smoke Gray.jpg',
'Amara05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Spanish Late.jpg',
'Amara06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Steel Gray.jpg',
'Amara07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Warm Gray.jpg',
'Amara08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Ash Gray.jpg',
'Amara09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Brown Gold.jpg',
'Amara10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Burned Cinnamon.jpg',
'Amara11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Cappuccino.jpg',
'Amara12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Caramel Stone.jpg',
'Amara13' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Charcoal Gray.jpg',
'Amara14' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Cool Gray.jpg',
'Amara15' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Crocodile Green.jpg',
'Amara16' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Dark Sepia.jpg',
'Amara17' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Desert Rose.jpg',
'Amara18' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Gentle Gray.jpg',
'Amara19' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Golden Sand.jpg',
'Amara20' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Gravity.jpg',
'Amara21' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Hazel Wood.jpg',
'Amara22' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Horizon Gray.jpg',
'Amara23' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Macchiato.jpg',
'Amara24' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Mocca.jpg',
'Amara25' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Olive Gray.jpg',
'Amara26' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Panther Eye.jpg',
'Amara27' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Amara\\Amara - Pearl.jpg'}

# Lazord - Data
Lazord = {
'Lazord01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - White Smoke.jpg',
'Lazord02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Azure.jpg',
'Lazord03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Ice Skate.jpg',
'Lazord04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Kenzo Hazel.jpg',
'Lazord05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Lazorde.jpg',
'Lazord06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Magic Gray.jpg',
'Lazord07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Magic Hazel.jpg',
'Lazord08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Magic Ice.jpg',
'Lazord09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Magic Pearl.jpg',
'Lazord10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Pure Avela.jpg',
'Lazord11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Pure Blue.jpg',
'Lazord12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Pure Gray.jpg',
'Lazord13' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Pure Green.jpg',
'Lazord14' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Smoke Gray.jpg',
'Lazord15' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Lazord\\Lazord - Tropical Green.jpg'}

# Dahab - Data
Dahab = {
'Dahab01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Sky.jpg',
'Dahab02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Sabrin Gray Green.jpg',
'Dahab03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Sabrin Gray.jpg',
'Dahab04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Sabrin Soul.jpg',
'Dahab05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Medusa.jpg',
'Dahab06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Smokey.jpg',
'Dahab07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Solitaire.jpg',
'Dahab08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Sun Kiss.jpg',
'Dahab09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Swarovski.jpg',
'Dahab10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Tiffany Blue.jpg',
'Dahab11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Topaz.jpg',
'Dahab12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Aqua.jpg',
'Dahab13' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Caramel.jpg',
'Dahab14' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Cat Eye.jpg',
'Dahab15' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Creamy.jpg',
'Dahab16' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Diamond.jpg',
'Dahab17' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Hind.jpg',
'Dahab18' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Ice.jpg',
'Dahab19' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Kaf.jpg',
'Dahab20' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Lumiere Gray.jpg',
'Dahab21' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Lumiere Hazel.jpg',
'Dahab22' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Lumirere Blue.jpg',
'Dahab23' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Lumirere Brown.jpg',
'Dahab24' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Lumirere Green.jpg',
'Dahab25' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Marble.jpg',
'Dahab26' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Dahab\\Dahab - Marron.jpg'}

# Diva - Data
Diva = {
'Diva01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Latte.jpg',
'Diva02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Moon.jpg',
'Diva03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Navy.jpg',
'Diva04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Nut.jpg',
'Diva05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Olivian.jpg',
'Diva06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Toffee.jpg',
'Diva07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Truffle.jpg',
'Diva08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Woody.jpg',
'Diva09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Amande.jpg',
'Diva10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Clay.jpg',
'Diva11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Gris.jpg',
'Diva12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Diva\\Diva - Ivory.jpg'}

# Solótica Solflex Natural Colors - Data
SoloticaSolflexNaturalColors = {
'SoloticaSolflexNaturalColors01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Cristal.jpg',
'SoloticaSolflexNaturalColors02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Esmeralda.jpg',
'SoloticaSolflexNaturalColors03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Mel.jpg',
'SoloticaSolflexNaturalColors04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Ocre.jpg',
'SoloticaSolflexNaturalColors05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Quartzo.jpg',
'SoloticaSolflexNaturalColors06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Topazio.jpg',
'SoloticaSolflexNaturalColors07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Solflex Natural Colors\\Solótica - Solflex Natural Colors - Verde.jpg',}

# Solótica Aquarella Daily - Data
SoloticaAquarellaDaily = {
'SoloticaAquarellaDaily01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Daily\\Solótica - Aquarella Daily - Cyan Blue.jpg',
'SoloticaAquarellaDaily02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Daily\\Solótica - Aquarella Daily - Golden Ochre.jpg',
'SoloticaAquarellaDaily03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Daily\\Solótica - Aquarella Daily - Sea Green.jpg',
'SoloticaAquarellaDaily04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Daily\\Solótica - Aquarella Daily - Sepia Gray.jpg',
'SoloticaAquarellaDaily05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Daily\\Solótica - Aquarella Daily - Sienna Brown.jpg'}

# Solótica Aquarella Quarterly - Data
SoloticaAquarellaQuarterly = {
'SoloticaAquarellaQuarterly01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Quarterly\\Solótica - Aquarella Quarterly - Cambuci Green.jpg',
'SoloticaAquarellaQuarterly02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Quarterly\\Solótica - Aquarella Quarterly - Dandara Hazel.jpg',
'SoloticaAquarellaQuarterly03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Quarterly\\Solótica - Aquarella Quarterly - Amazonia Green.jpg',
'SoloticaAquarellaQuarterly04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Quarterly\\Solótica - Aquarella Quarterly - Arara Blue.jpg',
'SoloticaAquarellaQuarterly05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Quarterly\\Solótica - Aquarella Quarterly - Beleza Gray.jpg',
'SoloticaAquarellaQuarterly06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Aquarella Quarterly\\Solótica - Aquarella Quarterly - Bossa Nova Gray.jpg'}

# Solótica Hidrocor Monthly - Data
SoloticaHidrocorMonthly = {
'SoloticaHidrocorMonthly01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Monthly\\Solótica - Hidrocor Monthly - Cristal.jpg',
'SoloticaHidrocorMonthly02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Monthly\\Solótica - Hidrocor Monthly - Ocre.jpg',
'SoloticaHidrocorMonthly03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Monthly\\Solótica - Hidrocor Monthly - Quartzo.jpg',
'SoloticaHidrocorMonthly04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Monthly\\Solótica - Hidrocor Monthly - Topazio.jpg',
'SoloticaHidrocorMonthly05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Monthly\\Solótica - Hidrocor Monthly - Ambar.jpg'}

# Solótica Natural Colors - Data
SoloticaNaturalColors = {
'SoloticaNaturalColors01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Ambar.jpg',
'SoloticaNaturalColors02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Avela.jpg',
'SoloticaNaturalColors03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Cristal.jpg',
'SoloticaNaturalColors04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Grafite.jpg',
'SoloticaNaturalColors05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Ice.jpg',
'SoloticaNaturalColors06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Mel.jpg',
'SoloticaNaturalColors07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Ocre.jpg',
'SoloticaNaturalColors08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Quartzo.jpg',
'SoloticaNaturalColors09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Natural Colors\\Solótica - Natural Colors - Topazio.jpg'}

# Solótica Hidrocor Rio - Data
SoloticaHidrocorRio = {
'SoloticaHidrocorRio01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Rio\\Solótica - Hidrocor Rio - Buzios.jpg',
'SoloticaHidrocorRio02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Rio\\Solótica - Hidrocor Rio - Copacabana.jpg',
'SoloticaHidrocorRio03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Rio\\Solótica - Hidrocor Rio - Ipanema.jpg',
'SoloticaHidrocorRio04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor Rio\\Solótica - Hidrocor Rio - Parati.jpg'}

# Solótica Hidrocor - Data
SoloticaHidrocor = {
'SoloticaHidrocor01' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Grafite.jpg',
'SoloticaHidrocor02' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Ice.jpg',
'SoloticaHidrocor03' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Mel.jpg',
'SoloticaHidrocor04' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Ocre.jpg',
'SoloticaHidrocor05' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Quartzo.jpg',
'SoloticaHidrocor06' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Topazio.jpg',
'SoloticaHidrocor07' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Ambar.jpg',
'SoloticaHidrocor08' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Avela.jpg',
'SoloticaHidrocor09' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Cristal.jpg',
'SoloticaHidrocor10' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Gem Aquamarine.jpg',
'SoloticaHidrocor11' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Gem Jade.jpg',
'SoloticaHidrocor12' : 'C:\\Users\\Omarm\\Desktop\\Programming\\DouLensBot\\lenses\\Solótica\\Solótica - Hidrocor\\Solótica - Hidrocor - Gem Safira.jpg'}

# ---------------------------------------------------------- Keyboards ----------------------------------------------------------- #
# Main Keyboard
MAIN_KEYBOARD = InlineKeyboardMarkup()
MAIN_KEYBOARD.row_width = 2
MAIN_KEYBOARD.add(
InlineKeyboardButton('Soflens Natural Colors', callback_data='Soflens Natural Colors - KB'),
InlineKeyboardButton('Air Optix Colors', callback_data='Air Optix Colors - KB'),
InlineKeyboardButton('Solótica', callback_data='Solotica - KB'),
InlineKeyboardButton('Luminous', callback_data='Luminous - KB'),
InlineKeyboardButton('Naturél', callback_data='Naturel - KB'),
InlineKeyboardButton('MyLense', callback_data='MyLense - KB'),
InlineKeyboardButton('Lorans', callback_data='Lorans - KB'),
InlineKeyboardButton('Lazord', callback_data='Lazord - KB'),
InlineKeyboardButton('Amara', callback_data='Amara - KB'),
InlineKeyboardButton('Dahab', callback_data='Dahab - KB'),
InlineKeyboardButton('Diva', callback_data='Diva - KB'))

# After Sending a Photo Keyboard
WANT_ANOTHER_ONE_KB = InlineKeyboardMarkup()
WANT_ANOTHER_ONE_KB.row_width = 1
WANT_ANOTHER_ONE_KB.add(
InlineKeyboardButton('YES', callback_data='WantAnotherOne'))

# Soflens Natural Colors - Keyboard
SOFLENS_NATURAL_COLORS_KB = InlineKeyboardMarkup()
SOFLENS_NATURAL_COLORS_KB.row_width = 2
SOFLENS_NATURAL_COLORS_KB.add(
InlineKeyboardButton('Amazon', callback_data='Soflens Natural Colors - Amazon'),
InlineKeyboardButton('Aquamarine', callback_data='Soflens Natural Colors - Aquamarine'),
InlineKeyboardButton('Dark Hazel', callback_data='Soflens Natural Colors - Dark Hazel'),
InlineKeyboardButton('Emerald', callback_data='Soflens Natural Colors - Emerald'),
InlineKeyboardButton('India', callback_data='Soflens Natural Colors - India'),
InlineKeyboardButton('Indigo', callback_data='Soflens Natural Colors - Indigo'),
InlineKeyboardButton('Jade', callback_data='Soflens Natural Colors - Jade'),
InlineKeyboardButton('Pacific', callback_data='Soflens Natural Colors - Pacific'),
InlineKeyboardButton('Platinum', callback_data='Soflens Natural Colors - Platinum'),
InlineKeyboardButton('Topaz', callback_data='Soflens Natural Colors - Topaz'),
InlineKeyboardButton('All', callback_data='Soflens Natural Colors - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Air Optix Colors - Keyboard
AIR_OPTIX_COLORS_KB = InlineKeyboardMarkup()
AIR_OPTIX_COLORS_KB.row_width = 2
AIR_OPTIX_COLORS_KB.add(
InlineKeyboardButton('Brilliant Blue', callback_data='Air Optix Colors - Brilliant Blue'),
InlineKeyboardButton('Brown', callback_data='Air Optix Colors - Brown'),
InlineKeyboardButton('Gemstone Green', callback_data='Air Optix Colors - Gemstone Green'),
InlineKeyboardButton('Gray', callback_data='Air Optix Colors - Gray'),
InlineKeyboardButton('Green', callback_data='Air Optix Colors - Green'),
InlineKeyboardButton('Honey', callback_data='Air Optix Colors - Honey'),
InlineKeyboardButton('Purehazel', callback_data='Air Optix Colors - Purehazel'),
InlineKeyboardButton('Sterling Gray', callback_data='Air Optix Colors - Sterling Gray'),
InlineKeyboardButton('True Sapphire', callback_data='Air Optix Colors - True Sapphire'),
InlineKeyboardButton('Turquoise', callback_data='Air Optix Colors - Turquoise'),
InlineKeyboardButton('Amethyst', callback_data='Air Optix Colors - Amethyst'),
InlineKeyboardButton('Blue', callback_data='Air Optix Colors - Blue'),
InlineKeyboardButton('All', callback_data='Air Optix Colors - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Naturél - Keyboard
NATUREL_KB = InlineKeyboardMarkup()
NATUREL_KB.row_width = 2
NATUREL_KB.add(
InlineKeyboardButton('Core Hazel', callback_data='Naturel - Core Hazel'),
InlineKeyboardButton('Core Ivory', callback_data='Naturel - Core Ivory'),
InlineKeyboardButton('Core Jade', callback_data='Naturel - Core Jade'),
InlineKeyboardButton('Core Marron', callback_data='Naturel - Core Marron'),
InlineKeyboardButton('Core Zircon', callback_data='Naturel - Core Zircon'),
InlineKeyboardButton('Core Blue', callback_data='Naturel - Core Blue'),
InlineKeyboardButton('Core Green', callback_data='Naturel - Core Green'),
InlineKeyboardButton('La Green', callback_data='Naturel - La Green'),
InlineKeyboardButton('La Hazel', callback_data='Naturel - La Hazel'),
InlineKeyboardButton('La Lolite', callback_data='Naturel - La Lolite'),
InlineKeyboardButton('La Agate', callback_data='Naturel - La Agate'),
InlineKeyboardButton('La Gray', callback_data='Naturel - La Gray'),
InlineKeyboardButton('All', callback_data='Naturel - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Luminous - Keyboard
LUMINOUS_KB = InlineKeyboardMarkup()
LUMINOUS_KB.row_width = 2
LUMINOUS_KB.add(
InlineKeyboardButton('Blue', callback_data='Luminous - Blue'),
InlineKeyboardButton('Crystal', callback_data='Luminous - Crystal'),
InlineKeyboardButton('Dazzling Green', callback_data='Luminous - Dazzling Green'),
InlineKeyboardButton('Gray', callback_data='Luminous - Gray'),
InlineKeyboardButton('Green', callback_data='Luminous - Green'),
InlineKeyboardButton('Hazel', callback_data='Luminous - Hazel'),
InlineKeyboardButton('Latin Brown', callback_data='Luminous - Latin Brown'),
InlineKeyboardButton('Latin Gray', callback_data='Luminous - Latin Gray'),
InlineKeyboardButton('Lazord', callback_data='Luminous - Lazord'),
InlineKeyboardButton('Lemon', callback_data='Luminous - Lemon'),
InlineKeyboardButton('All', callback_data='Luminous - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# MyLense - Keyboard
MY_LENSE_KB = InlineKeyboardMarkup()
MY_LENSE_KB.row_width = 2
MY_LENSE_KB.add(
InlineKeyboardButton('Capri', callback_data='MyLense - Capri'),
InlineKeyboardButton('Turquoise', callback_data='MyLense - Turquoise'),
InlineKeyboardButton('Light Blue', callback_data='MyLense - Light Blue'),
InlineKeyboardButton('Light Brown', callback_data='MyLense - Light Brown'),
InlineKeyboardButton('Light Gray', callback_data='MyLense - Light Gray'),
InlineKeyboardButton('Light Green', callback_data='MyLense - Light Green'),
InlineKeyboardButton('Oro Brown', callback_data='MyLense - Oro Brown'),
InlineKeyboardButton('Oro Gray', callback_data='MyLense - Oro Gray'),
InlineKeyboardButton('Oro Hazel', callback_data='MyLense - Oro Hazel'),
InlineKeyboardButton('Oro Ice', callback_data='MyLense - Oro Ice'),
InlineKeyboardButton('All', callback_data='MyLense - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Lorans - Keyboard
LORANS_KB = InlineKeyboardMarkup()
LORANS_KB.row_width = 2
LORANS_KB.add(
InlineKeyboardButton('Kadet Blue', callback_data='Lorans - Kadet Blue'),
InlineKeyboardButton('Kadet Brown', callback_data='Lorans - Kadet Brown'),
InlineKeyboardButton('Kadet Caramel', callback_data='Lorans - Kadet Caramel'),
InlineKeyboardButton('Kadet Gray', callback_data='Lorans - Kadet Gray'),
InlineKeyboardButton('Kadet Latte', callback_data='Lorans - Kadet Latte'),
InlineKeyboardButton('Kadet Navy', callback_data='Lorans - Kadet Navy'),
InlineKeyboardButton('Kadet Pearl', callback_data='Lorans - Kadet Pearl'),
InlineKeyboardButton('Pale Gray', callback_data='Lorans - Pale Gray'),
InlineKeyboardButton('All', callback_data='Lorans - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Amara - Keyboard
AMARA_KB = InlineKeyboardMarkup()
AMARA_KB.row_width = 2
AMARA_KB.add(
InlineKeyboardButton('Pure Hazel', callback_data='Amara - Pure Hazel'),
InlineKeyboardButton('Royal Blue', callback_data='Amara - Royal Blue'),
InlineKeyboardButton('Sky Gray', callback_data='Amara - Sky Gray'),
InlineKeyboardButton('Smoke Gray', callback_data='Amara - Smoke Gray'),
InlineKeyboardButton('Spanish Late', callback_data='Amara - Spanish Late'),
InlineKeyboardButton('Steel Gray', callback_data='Amara - Steel Gray'),
InlineKeyboardButton('Warm Gray', callback_data='Amara - Warm Gray'),
InlineKeyboardButton('Ash Gray', callback_data='Amara - Ash Gray'),
InlineKeyboardButton('Brown Gold', callback_data='Amara - Brown Gold'),
InlineKeyboardButton('Burned Cinnamon', callback_data='Amara - Burned Cinnamon'),
InlineKeyboardButton('Cappuccino', callback_data='Amara - Cappuccino'),
InlineKeyboardButton('Caramel Stone', callback_data='Amara - Caramel Stone'),
InlineKeyboardButton('Charcoal Gray', callback_data='Amara - Charcoal Gray'),
InlineKeyboardButton('Cool Gray', callback_data='Amara - Cool Gray'),
InlineKeyboardButton('Crocodile Green', callback_data='Amara - Crocodile Green'),
InlineKeyboardButton('Dark Sepia', callback_data='Amara - Dark Sepia'),
InlineKeyboardButton('Desert Rose', callback_data='Amara - Desert Rose'),
InlineKeyboardButton('Gentle Gray', callback_data='Amara - Gentle Gray'),
InlineKeyboardButton('Golden Sand', callback_data='Amara - Golden Sand'),
InlineKeyboardButton('Gravity', callback_data='Amara - Gravity'),
InlineKeyboardButton('Hazel Wood', callback_data='Amara - Hazel Wood'),
InlineKeyboardButton('Horizon Gray', callback_data='Amara - Horizon Gray'),
InlineKeyboardButton('Macchiato', callback_data='Amara - Macchiato'),
InlineKeyboardButton('Mocca', callback_data='Amara - Mocca'),
InlineKeyboardButton('Olive Gray', callback_data='Amara - Olive Gray'),
InlineKeyboardButton('Panther Eye', callback_data='Amara - Panther Eye'),
InlineKeyboardButton('Pearl', callback_data='Amara - Pearl'),
InlineKeyboardButton('All', callback_data='Amara - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Lazord - Keyboard
LAZORD_KB = InlineKeyboardMarkup()
LAZORD_KB.row_width = 2
LAZORD_KB.add(
InlineKeyboardButton('White Smoke', callback_data='Lazord - White Smoke'),
InlineKeyboardButton('Azure', callback_data='Lazord - Azure'),
InlineKeyboardButton('Ice Skate', callback_data='Lazord - Ice Skate'),
InlineKeyboardButton('Kenzo Hazel', callback_data='Lazord - Kenzo Hazel'),
InlineKeyboardButton('Lazorde', callback_data='Lazord - Lazorde'),
InlineKeyboardButton('Magic Gray', callback_data='Lazord - Magic Gray'),
InlineKeyboardButton('Magic Hazel', callback_data='Lazord - Magic Hazel'),
InlineKeyboardButton('Magic Ice', callback_data='Lazord - Magic Ice'),
InlineKeyboardButton('Magic Pearl', callback_data='Lazord - Magic Pearl'),
InlineKeyboardButton('Pure Avela', callback_data='Lazord - Pure Avela'),
InlineKeyboardButton('Pure Blue', callback_data='Lazord - Pure Blue'),
InlineKeyboardButton('Pure Gray', callback_data='Lazord - Pure Gray'),
InlineKeyboardButton('Pure Green', callback_data='Lazord - Pure Green'),
InlineKeyboardButton('Smoke Gray', callback_data='Lazord - Smoke Gray'),
InlineKeyboardButton('Tropical Green', callback_data='Lazord - Tropical Green'),
InlineKeyboardButton('All', callback_data='Lazord - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Dahab - Keyboard
DAHAB_KB = InlineKeyboardMarkup()
DAHAB_KB.row_width = 2
DAHAB_KB.add(
InlineKeyboardButton('Sky', callback_data='Dahab - Sky'),
InlineKeyboardButton('Sabrin Gray Green', callback_data='Dahab - Sabrin Gray Green'),
InlineKeyboardButton('Sabrin Gray', callback_data='Dahab - Sabrin Gray'),
InlineKeyboardButton('Sabrin Soul', callback_data='Dahab - Sabrin Soul'),
InlineKeyboardButton('Medusa', callback_data='Dahab - Medusa'),
InlineKeyboardButton('Smokey', callback_data='Dahab - Smokey'),
InlineKeyboardButton('Solitaire', callback_data='Dahab - Solitaire'),
InlineKeyboardButton('Sun Kiss', callback_data='Dahab - Sun Kiss'),
InlineKeyboardButton('Swarovski', callback_data='Dahab - Swarovski'),
InlineKeyboardButton('Tiffany Blue', callback_data='Dahab - Tiffany Blue'),
InlineKeyboardButton('Topaz', callback_data='Dahab - Topaz'),
InlineKeyboardButton('Aqua', callback_data='Dahab - Aqua'),
InlineKeyboardButton('Caramel', callback_data='Dahab - Caramel'),
InlineKeyboardButton('Cat Eye', callback_data='Dahab - Cat Eye'),
InlineKeyboardButton('Creamy', callback_data='Dahab - Creamy'),
InlineKeyboardButton('Diamond', callback_data='Dahab - Diamond'),
InlineKeyboardButton('Hind', callback_data='Dahab - Hind'),
InlineKeyboardButton('Ice', callback_data='Dahab - Ice'),
InlineKeyboardButton('Kaf', callback_data='Dahab - Kaf'),
InlineKeyboardButton('Lumiere Gray', callback_data='Dahab - Lumiere Gray'),
InlineKeyboardButton('Lumiere Hazel', callback_data='Dahab - Lumiere Hazel'),
InlineKeyboardButton('Lumirere Blue', callback_data='Dahab - Lumirere Blue'),
InlineKeyboardButton('Lumirere Brown', callback_data='Dahab - Lumirere Brown'),
InlineKeyboardButton('Lumirere Green', callback_data='Dahab - Lumirere Green'),
InlineKeyboardButton('Marble', callback_data='Dahab - Marble'),
InlineKeyboardButton('Marron', callback_data='Dahab - Marron'),
InlineKeyboardButton('All', callback_data='Dahab - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Diva - Keyboard
DIVA_KB = InlineKeyboardMarkup()
DIVA_KB.row_width = 2
DIVA_KB.add(
InlineKeyboardButton('Latte', callback_data='Diva - Latte'),
InlineKeyboardButton('Moon', callback_data='Diva - Moon'),
InlineKeyboardButton('Navy', callback_data='Diva - Navy'),
InlineKeyboardButton('Nut', callback_data='Diva - Nut'),
InlineKeyboardButton('Olivian', callback_data='Diva - Olivian'),
InlineKeyboardButton('Toffee', callback_data='Diva - Toffee'),
InlineKeyboardButton('Truffle', callback_data='Diva - Truffle'),
InlineKeyboardButton('Woody', callback_data='Diva - Woody'),
InlineKeyboardButton('Amande', callback_data='Diva - Amande'),
InlineKeyboardButton('Clay', callback_data='Diva - Clay'),
InlineKeyboardButton('Gris', callback_data='Diva - Gris'),
InlineKeyboardButton('Ivory', callback_data='Diva - Ivory'),
InlineKeyboardButton('All', callback_data='Diva - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica - Keyboard
SOLOTICA_KB = InlineKeyboardMarkup()
SOLOTICA_KB.row_width = 2
SOLOTICA_KB.add(
InlineKeyboardButton('Solflex Natural Colors', callback_data='Solotica - Solflex Natural Colors - KB'),
InlineKeyboardButton('Aquarella Quarterly', callback_data='Solotica - Aquarella Quarterly - KB'),
InlineKeyboardButton('Hidrocor Monthly', callback_data='Solotica - Hidrocor Monthly - KB'),
InlineKeyboardButton('Aquarella Daily', callback_data='Solotica - Aquarella Daily - KB'),
InlineKeyboardButton('Natural Colors', callback_data='Solotica - Natural Colors - KB'),
InlineKeyboardButton('Hidrocor Rio', callback_data='Solotica - Hidrocor Rio - KB'),
InlineKeyboardButton('Hidrocor', callback_data='Solotica - Hidrocor - KB'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Solflex Natural Colors - Keyboard
SOLOTICA_SOLFLEX_NATURAL_COLORS_KB = InlineKeyboardMarkup()
SOLOTICA_SOLFLEX_NATURAL_COLORS_KB.row_width = 2
SOLOTICA_SOLFLEX_NATURAL_COLORS_KB.add(
InlineKeyboardButton('Cristal', callback_data='Solotica - Solflex Natural Colors - Cristal'),
InlineKeyboardButton('Esmeralda', callback_data='Solotica - Solflex Natural Colors - Esmeralda'),
InlineKeyboardButton('Mel', callback_data='Solotica - Solflex Natural Colors - Mel'),
InlineKeyboardButton('Ocre', callback_data='Solotica - Solflex Natural Colors - Ocre'),
InlineKeyboardButton('Quartzo', callback_data='Solotica - Solflex Natural Colors - Quartzo'),
InlineKeyboardButton('Topazio', callback_data='Solotica - Solflex Natural Colors - Topazio'),
InlineKeyboardButton('Verde', callback_data='Solotica - Solflex Natural Colors - Verde'),
InlineKeyboardButton('All', callback_data='Solotica - Solflex Natural Colors - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Aquarella Daily - Keyboard
SOLOTICA_AQUARELLA_DAILY_KB = InlineKeyboardMarkup()
SOLOTICA_AQUARELLA_DAILY_KB.row_width = 2
SOLOTICA_AQUARELLA_DAILY_KB.add(
InlineKeyboardButton('Cyan Blue', callback_data='Solotica - Aquarella Daily - Cyan Blue'),
InlineKeyboardButton('Golden Ochre', callback_data='Solotica - Aquarella Daily - Golden Ochre'),
InlineKeyboardButton('Sea Green', callback_data='Solotica - Aquarella Daily - Sea Green'),
InlineKeyboardButton('Sepia Gray', callback_data='Solotica - Aquarella Daily - Sepia Gray'),
InlineKeyboardButton('Sienna Brown', callback_data='Solotica - Aquarella Daily - Sienna Brown'),
InlineKeyboardButton('All', callback_data='Solotica - Aquarella Daily - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Aquarella Quarterly - Keyboard
SOLOTICA_AQUARELLA_QUARTERLY_KB = InlineKeyboardMarkup()
SOLOTICA_AQUARELLA_QUARTERLY_KB.row_width = 2
SOLOTICA_AQUARELLA_QUARTERLY_KB.add(
InlineKeyboardButton('Cambuci Green', callback_data='Solotica - Aquarella Quarterly - Cambuci Green'),
InlineKeyboardButton('Dandara Hazel', callback_data='Solotica - Aquarella Quarterly - Dandara Hazel'),
InlineKeyboardButton('Amazonia Green', callback_data='Solotica - Aquarella Quarterly - Amazonia Green'),
InlineKeyboardButton('Arara Blue', callback_data='Solotica - Aquarella Quarterly - Arara Blue'),
InlineKeyboardButton('Beleza Gray', callback_data='Solotica - Aquarella Quarterly - Beleza Gray'),
InlineKeyboardButton('Bossa Nova Gray', callback_data='Solotica - Aquarella Quarterly - Bossa Nova Gray'),
InlineKeyboardButton('All', callback_data='Solotica - Aquarella Quarterly - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Hidrocor Monthly - Keyboard
SOLOTICA_HIDROCOR_MONTHLY_KB = InlineKeyboardMarkup()
SOLOTICA_HIDROCOR_MONTHLY_KB.row_width = 2
SOLOTICA_HIDROCOR_MONTHLY_KB.add(
InlineKeyboardButton('Cristal', callback_data='Solotica - Hidrocor Monthly - Cristal'),
InlineKeyboardButton('Ocre', callback_data='Solotica - Hidrocor Monthly - Ocre'),
InlineKeyboardButton('Quartzo', callback_data='Solotica - Hidrocor Monthly - Quartzo'),
InlineKeyboardButton('Topazio', callback_data='Solotica - Hidrocor Monthly - Topazio'),
InlineKeyboardButton('Ambar', callback_data='Solotica - Hidrocor Monthly - Ambar'),
InlineKeyboardButton('All', callback_data='Solotica - Hidrocor Monthly - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Natural Colors - Keyboard
SOLOTICA_NATURAL_COLORS_KB = InlineKeyboardMarkup()
SOLOTICA_NATURAL_COLORS_KB.row_width = 2
SOLOTICA_NATURAL_COLORS_KB.add(
InlineKeyboardButton('Ambar', callback_data='Solotica - Natural Colors - Ambar'),
InlineKeyboardButton('Avela', callback_data='Solotica - Natural Colors - Avela'),
InlineKeyboardButton('Cristal', callback_data='Solotica - Natural Colors - Cristal'),
InlineKeyboardButton('Grafite', callback_data='Solotica - Natural Colors - Grafite'),
InlineKeyboardButton('Ice', callback_data='Solotica - Natural Colors - Ice'),
InlineKeyboardButton('Mel', callback_data='Solotica - Natural Colors - Mel'),
InlineKeyboardButton('Ocre', callback_data='Solotica - Natural Colors - Ocre'),
InlineKeyboardButton('Quartzo', callback_data='Solotica - Natural Colors - Quartzo'),
InlineKeyboardButton('Topazio', callback_data='Solotica - Natural Colors - Topazio'),
InlineKeyboardButton('All', callback_data='Solotica - Natural Colors - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Hidrocor Rio - Keyboard
SOLOTICA_HIDROCOR_RIO_KB = InlineKeyboardMarkup()
SOLOTICA_HIDROCOR_RIO_KB.row_width = 2
SOLOTICA_HIDROCOR_RIO_KB.add(
InlineKeyboardButton('Buzios', callback_data='Solotica - Hidrocor Rio - Buzios'),
InlineKeyboardButton('Copacabana', callback_data='Solotica - Hidrocor Rio - Copacabana'),
InlineKeyboardButton('Ipanema', callback_data='Solotica - Hidrocor Rio - Ipanema'),
InlineKeyboardButton('Parati', callback_data='Solotica - Hidrocor Rio - Parati'),
InlineKeyboardButton('All', callback_data='Solotica - Hidrocor Rio - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# Solótica Hidrocor - Keyboard
SOLOTICA_HIDROCOR_KB = InlineKeyboardMarkup()
SOLOTICA_HIDROCOR_KB.row_width = 2
SOLOTICA_HIDROCOR_KB.add(
InlineKeyboardButton('Grafite', callback_data= 'Solotica - Hidrocor - Grafite'),
InlineKeyboardButton('Ice', callback_data= 'Solotica - Hidrocor - Ice'),
InlineKeyboardButton('Mel', callback_data= 'Solotica - Hidrocor - Mel'),
InlineKeyboardButton('Ocre', callback_data= 'Solotica - Hidrocor - Ocre'),
InlineKeyboardButton('Quartzo', callback_data= 'Solotica - Hidrocor - Quartzo'),
InlineKeyboardButton('Topazio', callback_data= 'Solotica - Hidrocor - Topazio'),
InlineKeyboardButton('Ambar', callback_data= 'Solotica - Hidrocor - Ambar'),
InlineKeyboardButton('Avela', callback_data= 'Solotica - Hidrocor - Avela'),
InlineKeyboardButton('Cristal', callback_data= 'Solotica - Hidrocor - Cristal'),
InlineKeyboardButton('Gem Aquamarine', callback_data= 'Solotica - Hidrocor - Gem Aquamarine'),
InlineKeyboardButton('Gem Jade', callback_data= 'Solotica - Hidrocor - Gem Jade'),
InlineKeyboardButton('Gem Safira', callback_data= 'Solotica - Hidrocor - Gem Safira'),
InlineKeyboardButton('All', callback_data='Solotica - Hidrocor - All'),
InlineKeyboardButton('Back to Main Menu', callback_data='MainMenu'))

# ---------------------------------------------------------- START BOT ----------------------------------------------------------- #
@bot.message_handler(commands=['start'])
def start(message):
    ACCOUNT_NAME = message.from_user.full_name
    USERNAME = message.from_user.username
    USER_ID = message.from_user.id
    BOT_USERNAME = bot.get_me().username
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id, timeout=1)
    bot.send_message(chat_id=message.chat.id, text=f'Hello {ACCOUNT_NAME}\nWelcome to DouLens Bot')
    bot.send_message(chat_id=message.chat.id, text='Let Me Help You Choose The Best Contact Lenses', reply_markup=MAIN_KEYBOARD)
    bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nHas Srarted Using @{BOT_USERNAME}')
    
@bot.callback_query_handler(func=lambda call: call.data)
def handle_button_press(call):
    ACCOUNT_NAME = call.from_user.full_name
    USERNAME = call.from_user.username
    USER_ID = call.from_user.id
    BOT_USERNAME = bot.get_me().username
    
# ====== Sending Keyboards ====== #
    if call.data == 'MainMenu':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=MAIN_KEYBOARD)
    if call.data == 'WantAnotherOne':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=MAIN_KEYBOARD)
    if call.data == 'Soflens Natural Colors - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOFLENS_NATURAL_COLORS_KB)
    if call.data == 'Naturel - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=NATUREL_KB)
    if call.data == 'Air Optix Colors - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=AIR_OPTIX_COLORS_KB)
    if call.data == 'Luminous - KB': 
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=LUMINOUS_KB)
    if call.data == 'MyLense - KB': 
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=MY_LENSE_KB)
    if call.data == 'Lorans - KB': 
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=LORANS_KB)
    if call.data == 'Amara - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=AMARA_KB)
    if call.data == 'Lazord - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=LAZORD_KB)
    if call.data == 'Dahab - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=DAHAB_KB)
    if call.data == 'Diva - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=DIVA_KB)
    if call.data == 'Solotica - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_KB)
    if call.data == 'Solotica - Solflex Natural Colors - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_SOLFLEX_NATURAL_COLORS_KB)
    if call.data == 'Solotica - Aquarella Daily - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_AQUARELLA_DAILY_KB)
    if call.data == 'Solotica - Aquarella Quarterly - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_AQUARELLA_QUARTERLY_KB)
    if call.data == 'Solotica - Hidrocor Monthly - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_HIDROCOR_MONTHLY_KB)
    if call.data == 'Solotica - Natural Colors - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_NATURAL_COLORS_KB)
    if call.data == 'Solotica - Hidrocor - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_HIDROCOR_KB)
    if call.data == 'Solotica - Hidrocor Rio - KB':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=SOLOTICA_HIDROCOR_RIO_KB)

# ======== Sending Photos ======= #

# Soflens Natural Colors - Sending Photos
    if call.data == 'Soflens Natural Colors - Amazon': 
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors01'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Aquamarine':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors02'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Dark Hazel':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors03'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Emerald':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors04'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - India':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors05'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Indigo':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors06'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Jade':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors07'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Pacific':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors08'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Platinum':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors09'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - Topaz':
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors10'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Soflens Natural Colors - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors01'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors02'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors03'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors04'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors05'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors05']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors06'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors06']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors07'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors07']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors08'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors08']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors09'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors09']).stem}")
        bot.send_photo(call.message.chat.id, open(SoflensNaturalColors['SoflensNaturalColors10'], 'rb'), f"{Path(SoflensNaturalColors['SoflensNaturalColors10']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Naturél - Sending Photos
    if call.data == 'Naturel - Core Hazel':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel01'], 'rb'), f"{Path(Naturel['Naturel01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - Core Ivory':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel02'], 'rb'), f"{Path(Naturel['Naturel02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - Core Jade':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel03'], 'rb'), f"{Path(Naturel['Naturel03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - Core Marron':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel04'], 'rb'), f"{Path(Naturel['Naturel04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - Core Zircon':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel05'], 'rb'), f"{Path(Naturel['Naturel05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - Core Blue':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel06'], 'rb'), f"{Path(Naturel['Naturel06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - Core Green':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel07'], 'rb'), f"{Path(Naturel['Naturel07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - La Green':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel08'], 'rb'), f"{Path(Naturel['Naturel08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - La Hazel':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel09'], 'rb'), f"{Path(Naturel['Naturel09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - La Lolite':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel10'], 'rb'), f"{Path(Naturel['Naturel10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - La Agate':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel11'], 'rb'), f"{Path(Naturel['Naturel11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - La Gray':
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel12'], 'rb'), f"{Path(Naturel['Naturel12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Naturel - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel01'], 'rb'), f"{Path(Naturel['Naturel01']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel02'], 'rb'), f"{Path(Naturel['Naturel02']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel03'], 'rb'), f"{Path(Naturel['Naturel03']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel04'], 'rb'), f"{Path(Naturel['Naturel04']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel05'], 'rb'), f"{Path(Naturel['Naturel05']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel06'], 'rb'), f"{Path(Naturel['Naturel06']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel07'], 'rb'), f"{Path(Naturel['Naturel07']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel08'], 'rb'), f"{Path(Naturel['Naturel08']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel09'], 'rb'), f"{Path(Naturel['Naturel09']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel10'], 'rb'), f"{Path(Naturel['Naturel10']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel11'], 'rb'), f"{Path(Naturel['Naturel11']).stem}")
        bot.send_photo(call.message.chat.id, open(Naturel['Naturel12'], 'rb'), f"{Path(Naturel['Naturel12']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Air Optix Colors - Sending Photos
    if call.data == 'Air Optix Colors - Brilliant Blue':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors01'], 'rb'), f"{Path(AirOptixColors['AirOptixColors01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Brown':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors02'], 'rb'), f"{Path(AirOptixColors['AirOptixColors02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Gemstone Green':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors03'], 'rb'), f"{Path(AirOptixColors['AirOptixColors03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Gray':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors04'], 'rb'), f"{Path(AirOptixColors['AirOptixColors04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Green':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors05'], 'rb'), f"{Path(AirOptixColors['AirOptixColors05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Honey':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors06'], 'rb'), f"{Path(AirOptixColors['AirOptixColors06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Purehazel':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors07'], 'rb'), f"{Path(AirOptixColors['AirOptixColors07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Sterling Gray':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors08'], 'rb'), f"{Path(AirOptixColors['AirOptixColors08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - True Sapphire':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors09'], 'rb'), f"{Path(AirOptixColors['AirOptixColors09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Turquoise':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors10'], 'rb'), f"{Path(AirOptixColors['AirOptixColors10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Amethyst':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors11'], 'rb'), f"{Path(AirOptixColors['AirOptixColors11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - Blue':
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors12'], 'rb'), f"{Path(AirOptixColors['AirOptixColors12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Air Optix Colors - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors01'], 'rb'), f"{Path(AirOptixColors['AirOptixColors01']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors02'], 'rb'), f"{Path(AirOptixColors['AirOptixColors02']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors03'], 'rb'), f"{Path(AirOptixColors['AirOptixColors03']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors04'], 'rb'), f"{Path(AirOptixColors['AirOptixColors04']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors05'], 'rb'), f"{Path(AirOptixColors['AirOptixColors05']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors06'], 'rb'), f"{Path(AirOptixColors['AirOptixColors06']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors07'], 'rb'), f"{Path(AirOptixColors['AirOptixColors07']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors08'], 'rb'), f"{Path(AirOptixColors['AirOptixColors08']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors09'], 'rb'), f"{Path(AirOptixColors['AirOptixColors09']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors10'], 'rb'), f"{Path(AirOptixColors['AirOptixColors10']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors11'], 'rb'), f"{Path(AirOptixColors['AirOptixColors11']).stem}")
        bot.send_photo(call.message.chat.id, open(AirOptixColors['AirOptixColors12'], 'rb'), f"{Path(AirOptixColors['AirOptixColors12']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Luminous - Sending Photos
    if call.data == 'Luminous - Blue':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous01'], 'rb'), f"{Path(Luminous['Luminous01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Crystal':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous02'], 'rb'), f"{Path(Luminous['Luminous02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Dazzling Green':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous03'], 'rb'), f"{Path(Luminous['Luminous03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Gray':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous04'], 'rb'), f"{Path(Luminous['Luminous04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Green':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous05'], 'rb'), f"{Path(Luminous['Luminous05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Hazel':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous06'], 'rb'), f"{Path(Luminous['Luminous06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Latin Brown':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous07'], 'rb'), f"{Path(Luminous['Luminous07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Latin Gray':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous08'], 'rb'), f"{Path(Luminous['Luminous08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Lazord':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous09'], 'rb'), f"{Path(Luminous['Luminous09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - Lemon':
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous10'], 'rb'), f"{Path(Luminous['Luminous10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Luminous - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous01'], 'rb'), f"{Path(Luminous['Luminous01']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous02'], 'rb'), f"{Path(Luminous['Luminous02']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous03'], 'rb'), f"{Path(Luminous['Luminous03']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous04'], 'rb'), f"{Path(Luminous['Luminous04']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous05'], 'rb'), f"{Path(Luminous['Luminous05']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous06'], 'rb'), f"{Path(Luminous['Luminous06']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous07'], 'rb'), f"{Path(Luminous['Luminous07']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous08'], 'rb'), f"{Path(Luminous['Luminous08']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous09'], 'rb'), f"{Path(Luminous['Luminous09']).stem}")
        bot.send_photo(call.message.chat.id, open(Luminous['Luminous10'], 'rb'), f"{Path(Luminous['Luminous10']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# MyLense - Sending Photos
    if call.data == 'MyLense - Capri':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense01'], 'rb'), f"{Path(MyLense['MyLense01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Turquoise':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense02'], 'rb'), f"{Path(MyLense['MyLense02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Light Blue':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense03'], 'rb'), f"{Path(MyLense['MyLense03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Light Brown':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense04'], 'rb'), f"{Path(MyLense['MyLense04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Light Gray':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense05'], 'rb'), f"{Path(MyLense['MyLense05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Light Green':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense06'], 'rb'), f"{Path(MyLense['MyLense06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Oro Brown':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense07'], 'rb'), f"{Path(MyLense['MyLense07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Oro Gray':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense08'], 'rb'), f"{Path(MyLense['MyLense08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Oro Hazel':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense09'], 'rb'), f"{Path(MyLense['MyLense09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - Oro Ice':
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense10'], 'rb'), f"{Path(MyLense['MyLense10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'MyLense - All': 
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense01'], 'rb'), f"{Path(MyLense['MyLense01']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense02'], 'rb'), f"{Path(MyLense['MyLense02']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense03'], 'rb'), f"{Path(MyLense['MyLense03']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense04'], 'rb'), f"{Path(MyLense['MyLense04']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense05'], 'rb'), f"{Path(MyLense['MyLense05']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense06'], 'rb'), f"{Path(MyLense['MyLense06']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense07'], 'rb'), f"{Path(MyLense['MyLense07']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense08'], 'rb'), f"{Path(MyLense['MyLense08']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense09'], 'rb'), f"{Path(MyLense['MyLense09']).stem}")
        bot.send_photo(call.message.chat.id, open(MyLense['MyLense10'], 'rb'), f"{Path(MyLense['MyLense10']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Lorans - Sending Photos
    if call.data == 'Lorans - Kadet Latte':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans01'], 'rb'), f"{Path(Lorans['Lorans01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Kadet Navy':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans02'], 'rb'), f"{Path(Lorans['Lorans02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Kadet Pearl':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans03'], 'rb'), f"{Path(Lorans['Lorans03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Kadet Caramel':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans04'], 'rb'), f"{Path(Lorans['Lorans04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Kadet Blue':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans05'], 'rb'), f"{Path(Lorans['Lorans05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Kadet Brown':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans06'], 'rb'), f"{Path(Lorans['Lorans06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Kadet Gray':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans07'], 'rb'), f"{Path(Lorans['Lorans07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - Pale Gray':
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans08'], 'rb'), f"{Path(Lorans['Lorans08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lorans - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans01'], 'rb'), f"{Path(Lorans['Lorans01']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans02'], 'rb'), f"{Path(Lorans['Lorans02']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans03'], 'rb'), f"{Path(Lorans['Lorans03']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans04'], 'rb'), f"{Path(Lorans['Lorans04']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans05'], 'rb'), f"{Path(Lorans['Lorans05']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans06'], 'rb'), f"{Path(Lorans['Lorans06']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans07'], 'rb'), f"{Path(Lorans['Lorans07']).stem}")
        bot.send_photo(call.message.chat.id, open(Lorans['Lorans08'], 'rb'), f"{Path(Lorans['Lorans08']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Amara - Sending Photos 
    if call.data == 'Amara - Pure Hazel':
        bot.send_photo(call.message.chat.id, open(Amara['Amara01'], 'rb'), f"{Path(Amara['Amara01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Royal Blue':
        bot.send_photo(call.message.chat.id, open(Amara['Amara02'], 'rb'), f"{Path(Amara['Amara02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Sky Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara03'], 'rb'), f"{Path(Amara['Amara03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Smoke Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara04'], 'rb'), f"{Path(Amara['Amara04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Spanish Late':
        bot.send_photo(call.message.chat.id, open(Amara['Amara05'], 'rb'), f"{Path(Amara['Amara05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Steel Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara06'], 'rb'), f"{Path(Amara['Amara06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Warm Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara07'], 'rb'), f"{Path(Amara['Amara07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Ash Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara08'], 'rb'), f"{Path(Amara['Amara08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Brown Gold':
        bot.send_photo(call.message.chat.id, open(Amara['Amara09'], 'rb'), f"{Path(Amara['Amara09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Burned Cinnamon':
        bot.send_photo(call.message.chat.id, open(Amara['Amara10'], 'rb'), f"{Path(Amara['Amara10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Cappuccino':
        bot.send_photo(call.message.chat.id, open(Amara['Amara11'], 'rb'), f"{Path(Amara['Amara11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Caramel Stone':
        bot.send_photo(call.message.chat.id, open(Amara['Amara12'], 'rb'), f"{Path(Amara['Amara12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Charcoal Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara13'], 'rb'), f"{Path(Amara['Amara13']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Cool Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara14'], 'rb'), f"{Path(Amara['Amara14']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Crocodile Green':
        bot.send_photo(call.message.chat.id, open(Amara['Amara15'], 'rb'), f"{Path(Amara['Amara15']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Dark Sepia':
        bot.send_photo(call.message.chat.id, open(Amara['Amara16'], 'rb'), f"{Path(Amara['Amara16']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Desert Rose':
        bot.send_photo(call.message.chat.id, open(Amara['Amara17'], 'rb'), f"{Path(Amara['Amara17']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Gentle Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara18'], 'rb'), f"{Path(Amara['Amara18']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Golden Sand':
        bot.send_photo(call.message.chat.id, open(Amara['Amara19'], 'rb'), f"{Path(Amara['Amara19']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Gravity':
        bot.send_photo(call.message.chat.id, open(Amara['Amara20'], 'rb'), f"{Path(Amara['Amara20']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Hazel Wood':
        bot.send_photo(call.message.chat.id, open(Amara['Amara21'], 'rb'), f"{Path(Amara['Amara21']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Horizon Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara22'], 'rb'), f"{Path(Amara['Amara22']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Macchiato':
        bot.send_photo(call.message.chat.id, open(Amara['Amara23'], 'rb'), f"{Path(Amara['Amara23']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Mocca':
        bot.send_photo(call.message.chat.id, open(Amara['Amara24'], 'rb'), f"{Path(Amara['Amara24']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Olive Gray':
        bot.send_photo(call.message.chat.id, open(Amara['Amara25'], 'rb'), f"{Path(Amara['Amara25']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Panther Eye':
        bot.send_photo(call.message.chat.id, open(Amara['Amara26'], 'rb'), f"{Path(Amara['Amara26']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - Pearl':
        bot.send_photo(call.message.chat.id, open(Amara['Amara27'], 'rb'), f"{Path(Amara['Amara27']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Amara - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Amara['Amara01'], 'rb'), f"{Path(Amara['Amara01']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara02'], 'rb'), f"{Path(Amara['Amara02']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara03'], 'rb'), f"{Path(Amara['Amara03']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara04'], 'rb'), f"{Path(Amara['Amara04']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara05'], 'rb'), f"{Path(Amara['Amara05']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara06'], 'rb'), f"{Path(Amara['Amara06']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara07'], 'rb'), f"{Path(Amara['Amara07']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara08'], 'rb'), f"{Path(Amara['Amara08']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara09'], 'rb'), f"{Path(Amara['Amara09']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara10'], 'rb'), f"{Path(Amara['Amara10']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara11'], 'rb'), f"{Path(Amara['Amara11']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara12'], 'rb'), f"{Path(Amara['Amara12']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara13'], 'rb'), f"{Path(Amara['Amara13']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara14'], 'rb'), f"{Path(Amara['Amara14']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara15'], 'rb'), f"{Path(Amara['Amara15']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara16'], 'rb'), f"{Path(Amara['Amara16']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara17'], 'rb'), f"{Path(Amara['Amara17']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara18'], 'rb'), f"{Path(Amara['Amara18']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara19'], 'rb'), f"{Path(Amara['Amara19']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara20'], 'rb'), f"{Path(Amara['Amara20']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara21'], 'rb'), f"{Path(Amara['Amara21']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara22'], 'rb'), f"{Path(Amara['Amara22']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara23'], 'rb'), f"{Path(Amara['Amara23']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara24'], 'rb'), f"{Path(Amara['Amara24']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara25'], 'rb'), f"{Path(Amara['Amara25']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara26'], 'rb'), f"{Path(Amara['Amara26']).stem}")
        bot.send_photo(call.message.chat.id, open(Amara['Amara27'], 'rb'), f"{Path(Amara['Amara27']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Lazord - Sending Photos
    if call.data == 'Lazord - White Smoke':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord01'], 'rb'), f"{Path(Lazord['Lazord01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Azure':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord02'], 'rb'), f"{Path(Lazord['Lazord02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Ice Skate':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord03'], 'rb'), f"{Path(Lazord['Lazord03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Kenzo Hazel':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord04'], 'rb'), f"{Path(Lazord['Lazord04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Lazorde':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord05'], 'rb'), f"{Path(Lazord['Lazord05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Magic Gray':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord06'], 'rb'), f"{Path(Lazord['Lazord06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Magic Hazel':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord07'], 'rb'), f"{Path(Lazord['Lazord07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Magic Ice':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord08'], 'rb'), f"{Path(Lazord['Lazord08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Magic Pearl':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord09'], 'rb'), f"{Path(Lazord['Lazord09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Pure Avela':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord10'], 'rb'), f"{Path(Lazord['Lazord10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Pure Blue':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord11'], 'rb'), f"{Path(Lazord['Lazord11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Pure Gray':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord12'], 'rb'), f"{Path(Lazord['Lazord12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Pure Green':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord13'], 'rb'), f"{Path(Lazord['Lazord13']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Smoke Gray':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord14'], 'rb'), f"{Path(Lazord['Lazord14']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - Tropical Green':
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord15'], 'rb'), f"{Path(Lazord['Lazord15']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Lazord - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord01'], 'rb'), f"{Path(Lazord['Lazord01']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord02'], 'rb'), f"{Path(Lazord['Lazord02']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord03'], 'rb'), f"{Path(Lazord['Lazord03']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord04'], 'rb'), f"{Path(Lazord['Lazord04']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord05'], 'rb'), f"{Path(Lazord['Lazord05']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord06'], 'rb'), f"{Path(Lazord['Lazord06']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord07'], 'rb'), f"{Path(Lazord['Lazord07']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord08'], 'rb'), f"{Path(Lazord['Lazord08']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord09'], 'rb'), f"{Path(Lazord['Lazord09']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord10'], 'rb'), f"{Path(Lazord['Lazord10']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord11'], 'rb'), f"{Path(Lazord['Lazord11']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord12'], 'rb'), f"{Path(Lazord['Lazord12']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord13'], 'rb'), f"{Path(Lazord['Lazord13']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord14'], 'rb'), f"{Path(Lazord['Lazord14']).stem}")
        bot.send_photo(call.message.chat.id, open(Lazord['Lazord15'], 'rb'), f"{Path(Lazord['Lazord15']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Dahab - Sending Photos
    if call.data == 'Dahab - Sky':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab01'], 'rb'), f"{Path(Dahab['Dahab01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Sabrin Gray Green':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab02'], 'rb'), f"{Path(Dahab['Dahab02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Sabrin Gray':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab03'], 'rb'), f"{Path(Dahab['Dahab03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Sabrin Soul':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab04'], 'rb'), f"{Path(Dahab['Dahab04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Medusa':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab05'], 'rb'), f"{Path(Dahab['Dahab05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Smokey':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab06'], 'rb'), f"{Path(Dahab['Dahab06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Solitaire':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab07'], 'rb'), f"{Path(Dahab['Dahab07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Sun Kiss':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab08'], 'rb'), f"{Path(Dahab['Dahab08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Swarovski':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab09'], 'rb'), f"{Path(Dahab['Dahab09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Tiffany Blue':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab10'], 'rb'), f"{Path(Dahab['Dahab10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Topaz':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab11'], 'rb'), f"{Path(Dahab['Dahab11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Aqua':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab12'], 'rb'), f"{Path(Dahab['Dahab12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Caramel':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab13'], 'rb'), f"{Path(Dahab['Dahab13']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Cat Eye':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab14'], 'rb'), f"{Path(Dahab['Dahab14']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Creamy':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab15'], 'rb'), f"{Path(Dahab['Dahab15']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Diamond':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab16'], 'rb'), f"{Path(Dahab['Dahab16']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Hind':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab17'], 'rb'), f"{Path(Dahab['Dahab17']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Ice':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab18'], 'rb'), f"{Path(Dahab['Dahab18']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Kaf':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab19'], 'rb'), f"{Path(Dahab['Dahab19']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Lumiere Gray':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab20'], 'rb'), f"{Path(Dahab['Dahab20']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Lumiere Hazel':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab21'], 'rb'), f"{Path(Dahab['Dahab21']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Lumirere Blue':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab22'], 'rb'), f"{Path(Dahab['Dahab22']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Lumirere Brown':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab23'], 'rb'), f"{Path(Dahab['Dahab23']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Lumirere Green':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab24'], 'rb'), f"{Path(Dahab['Dahab24']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Marble':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab25'], 'rb'), f"{Path(Dahab['Dahab25']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - Marron':
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab26'], 'rb'), f"{Path(Dahab['Dahab26']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Dahab - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab01'], 'rb'), f"{Path(Dahab['Dahab01']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab02'], 'rb'), f"{Path(Dahab['Dahab02']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab03'], 'rb'), f"{Path(Dahab['Dahab03']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab04'], 'rb'), f"{Path(Dahab['Dahab04']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab05'], 'rb'), f"{Path(Dahab['Dahab05']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab06'], 'rb'), f"{Path(Dahab['Dahab06']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab07'], 'rb'), f"{Path(Dahab['Dahab07']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab08'], 'rb'), f"{Path(Dahab['Dahab08']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab09'], 'rb'), f"{Path(Dahab['Dahab09']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab10'], 'rb'), f"{Path(Dahab['Dahab10']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab11'], 'rb'), f"{Path(Dahab['Dahab11']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab12'], 'rb'), f"{Path(Dahab['Dahab12']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab13'], 'rb'), f"{Path(Dahab['Dahab13']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab14'], 'rb'), f"{Path(Dahab['Dahab14']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab15'], 'rb'), f"{Path(Dahab['Dahab15']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab16'], 'rb'), f"{Path(Dahab['Dahab16']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab17'], 'rb'), f"{Path(Dahab['Dahab17']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab18'], 'rb'), f"{Path(Dahab['Dahab18']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab19'], 'rb'), f"{Path(Dahab['Dahab19']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab20'], 'rb'), f"{Path(Dahab['Dahab20']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab21'], 'rb'), f"{Path(Dahab['Dahab21']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab22'], 'rb'), f"{Path(Dahab['Dahab22']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab23'], 'rb'), f"{Path(Dahab['Dahab23']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab24'], 'rb'), f"{Path(Dahab['Dahab24']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab25'], 'rb'), f"{Path(Dahab['Dahab25']).stem}")
        bot.send_photo(call.message.chat.id, open(Dahab['Dahab26'], 'rb'), f"{Path(Dahab['Dahab26']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Diva - Sending Photos
    if call.data == 'Diva - Latte':
        bot.send_photo(call.message.chat.id, open(Diva['Diva01'], 'rb'), f"{Path(Diva['Diva01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Moon':
        bot.send_photo(call.message.chat.id, open(Diva['Diva02'], 'rb'), f"{Path(Diva['Diva02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Navy':
        bot.send_photo(call.message.chat.id, open(Diva['Diva03'], 'rb'), f"{Path(Diva['Diva03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Nut':
        bot.send_photo(call.message.chat.id, open(Diva['Diva04'], 'rb'), f"{Path(Diva['Diva04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Olivian':
        bot.send_photo(call.message.chat.id, open(Diva['Diva05'], 'rb'), f"{Path(Diva['Diva05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Toffee':
        bot.send_photo(call.message.chat.id, open(Diva['Diva06'], 'rb'), f"{Path(Diva['Diva06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Truffle':
        bot.send_photo(call.message.chat.id, open(Diva['Diva07'], 'rb'), f"{Path(Diva['Diva07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Woody':
        bot.send_photo(call.message.chat.id, open(Diva['Diva08'], 'rb'), f"{Path(Diva['Diva08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Amande':
        bot.send_photo(call.message.chat.id, open(Diva['Diva09'], 'rb'), f"{Path(Diva['Diva09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Clay':
        bot.send_photo(call.message.chat.id, open(Diva['Diva10'], 'rb'), f"{Path(Diva['Diva10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Gris':
        bot.send_photo(call.message.chat.id, open(Diva['Diva11'], 'rb'), f"{Path(Diva['Diva11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - Ivory':
        bot.send_photo(call.message.chat.id, open(Diva['Diva12'], 'rb'), f"{Path(Diva['Diva12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Diva - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(Diva['Diva01'], 'rb'), f"{Path(Diva['Diva01']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva02'], 'rb'), f"{Path(Diva['Diva02']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva03'], 'rb'), f"{Path(Diva['Diva03']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva04'], 'rb'), f"{Path(Diva['Diva04']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva05'], 'rb'), f"{Path(Diva['Diva05']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva06'], 'rb'), f"{Path(Diva['Diva06']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva07'], 'rb'), f"{Path(Diva['Diva07']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva08'], 'rb'), f"{Path(Diva['Diva08']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva09'], 'rb'), f"{Path(Diva['Diva09']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva10'], 'rb'), f"{Path(Diva['Diva10']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva11'], 'rb'), f"{Path(Diva['Diva11']).stem}")
        bot.send_photo(call.message.chat.id, open(Diva['Diva12'], 'rb'), f"{Path(Diva['Diva12']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Solflex Natural Colors - Sending Photos
    if call.data == 'Solotica - Solflex Natural Colors - Cristal':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors01'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - Esmeralda':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors02'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - Mel':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors03'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - Ocre':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors04'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - Quartzo':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors05'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - Topazio':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors06'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - Verde':
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors07'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Solflex Natural Colors - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors01'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors02'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors03'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors04'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors05'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors05']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors06'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors06']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors07'], 'rb'), f"{Path(SoloticaSolflexNaturalColors['SoloticaSolflexNaturalColors07']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Aquarella Daily - Sending Photos
    if call.data == 'Solotica - Aquarella Daily - Cyan Blue':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily01'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Daily - Golden Ochre':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily02'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Daily - Sea Green':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily03'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Daily - Sepia Gray':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily04'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Daily - Sienna Brown':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily05'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Daily - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily01'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily02'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily03'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily04'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaDaily['SoloticaAquarellaDaily05'], 'rb'), f"{Path(SoloticaAquarellaDaily['SoloticaAquarellaDaily05']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Aquarella Quarterly - Sending Photos
    if call.data == 'Solotica - Aquarella Quarterly - Cambuci Green':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly01'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Quarterly - Dandara Hazel':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly02'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Quarterly - Amazonia Green':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly03'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Quarterly - Arara Blue':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly04'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Quarterly - Beleza Gray':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly05'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Quarterly - Bossa Nova Gray':
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly06'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Aquarella Quarterly - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly01'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly02'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly03'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly04'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly05'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly05']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly06'], 'rb'), f"{Path(SoloticaAquarellaQuarterly['SoloticaAquarellaQuarterly06']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Hidrocor Monthly - Sending Photos
    if call.data == 'Solotica - Hidrocor Monthly - Cristal':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly01'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Monthly - Ocre':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly02'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Monthly - Quartzo':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly03'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Monthly - Topazio':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly04'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Monthly - Ambar':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly05'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Monthly - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly01'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly02'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly03'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly04'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly05'], 'rb'), f"{Path(SoloticaHidrocorMonthly['SoloticaHidrocorMonthly05']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Natural Colors - Sending Photos
    if call.data == 'Solotica - Natural Colors - Ambar':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors01'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Avela':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors02'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Cristal':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors03'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Grafite':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors04'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Ice':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors05'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Mel':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors06'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Ocre':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors07'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Quartzo':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors08'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - Topazio':
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors09'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Natural Colors - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors01'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors02'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors03'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors04'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors05'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors05']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors06'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors06']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors07'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors07']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors08'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors08']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaNaturalColors['SoloticaNaturalColors09'], 'rb'), f"{Path(SoloticaNaturalColors['SoloticaNaturalColors09']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Hidrocor - Sending Photos
    if call.data == 'Solotica - Hidrocor - Grafite':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor01'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Ice':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor02'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Mel':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor03'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Ocre':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor04'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Quartzo':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor05'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor05']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Topazio':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor06'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor06']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Ambar':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor07'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor07']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Avela':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor08'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor08']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Cristal':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor09'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor09']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Gem Aquamarine':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor10'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor10']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Gem Jade':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor11'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor11']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - Gem Safira':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor12'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor12']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor01'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor02'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor03'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor04'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor04']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor05'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor05']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor06'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor06']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor07'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor07']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor08'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor08']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor09'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor09']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor10'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor10']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor11'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor11']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocor['SoloticaHidrocor12'], 'rb'), f"{Path(SoloticaHidrocor['SoloticaHidrocor12']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
# Solótica Hidrocor Rio - Sending Photos
    if call.data == 'Solotica - Hidrocor Rio - Buzios':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio01'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio01']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Rio - Copacabana':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio02'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio02']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Rio - Ipanema':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio03'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio03']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Rio - Parati':
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio04'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio04']).stem}")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here is Your Lens ❤️')
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')
    if call.data == 'Solotica - Hidrocor Rio - All':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'Here are Your Lenses ❤️')
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio01'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio01']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio02'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio02']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio03'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio03']).stem}")
        bot.send_photo(call.message.chat.id, open(SoloticaHidrocorRio['SoloticaHidrocorRio04'], 'rb'), f"{Path(SoloticaHidrocorRio['SoloticaHidrocorRio04']).stem}")
        bot.send_message(chat_id=call.message.chat.id, text='Want Another One?', reply_markup=WANT_ANOTHER_ONE_KB)
        bot.send_message(chat_id="-1001835134039", text=f'The User: {ACCOUNT_NAME}\nUsername: @{USERNAME}\nUser id: "{USER_ID}"\nRequested From @{BOT_USERNAME}\n{call.data}')

bot.infinity_polling()