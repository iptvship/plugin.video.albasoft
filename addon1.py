import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import logging
from operator import itemgetter

def show_tags():
  tag_handle = int(sys.argv[1])
  xbmcplugin.setContent(tag_handle, 'tags')

  for tag in tags:
    iconPath = os.path.join(home, 'logos', tag['icon'])
    li = xbmcgui.ListItem(tag['name'], iconImage=iconPath)
    url = sys.argv[0] + '?tag=' + str(tag['id'])
    xbmcplugin.addDirectoryItem(handle=tag_handle, url=url, listitem=li, isFolder=True)

  xbmcplugin.endOfDirectory(tag_handle)


def show_streams(tag):
  stream_handle = int(sys.argv[1])
  xbmcplugin.setContent(stream_handle, 'streams')
  logging.warning('TAG show_streams!!!! %s', tag)
  for stream in streams[str(tag)]:
    logging.debug('STREAM HERE!!! %s', stream['name'])
    iconPath = os.path.join(home, 'logos', stream['icon'])
    li = xbmcgui.ListItem(stream['name'], iconImage=iconPath)
    xbmcplugin.addDirectoryItem(handle=stream_handle, url=stream['url'], listitem=li)

  xbmcplugin.endOfDirectory(stream_handle)


def get_params():
  """
  Retrieves the current existing parameters from XBMC.
  """
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace('?', '')
    if params[len(params) - 1] == '/':
      params = params[0:len(params) - 2]
    pairsofparams = cleanedparams.split('&')
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split('=')
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
  return param


def lower_getter(field):
  def _getter(obj):
    return obj[field].lower()

  return _getter


addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))

tags = [
  {
    'name': 'Live TV',
    'id': 'LiveTV',
    'icon': 'livetv.png'
  }, {
    'name': 'Filma Shqip',
    'id': 'FilmaShqip',
    'icon': 'icon.png'
  }, {
    'name': 'Movies',
    'id': 'Movies',
    'icon': 'movies.png'
  }, {
    'name': 'Radio',
    'id': 'Radio',
    'icon': 'radio.png'
  }]


LiveTV = [{
  'name': 'RTK 1',
  'url': 'http://wowza.rtkit.com:1935/live/livestream/playlist.m3u8',
  'icon': 'rtk.png',
  'disabled': False
  }, {
  'name': 'A1 Shiptar',
  'url': 'http://217.23.12.187:8080/a1shiptarealb11/playlist.m3u8',
  'icon': 'a1.png',
  'disabled': False
  }, {
  'name': 'ALB Movei',
  'url': 'rtmp://188.138.17.8:1935/albuk/albuk+.stream',
  'icon': 'albukhd.png',
  'disabled': False
  }, {
  'name': 'ALB Musik HD',
  'url': 'rtmp://188.138.17.8:1935/albuk/albmus.stream',
  'icon': 'albukhd.png',
  'disabled': False
  }, {
  'name': '21.Tv',
  'url': 'http://live.tvmak.com/tv/tv21.m3u8',
  'icon': '21.png',
  'disabled': False
  }, {
  'name': 'Dukagjini',
  'url': 'http://84.22.48.253:89/dukagjini/mono.m3u8',
  'icon': 'Dukagjini.png',
  'disabled': False
  }, {
  'name': 'Tibuna',
  'url': 'http://84.22.48.253:8080/tribuna/test.m3u8',
  'icon': 'Tibuna.png',
  'disabled': False
  }, {
  'name': 'News24',
  'url': 'rtmp://109.236.81.91/hls/news24',
  'icon': 'News24.png',
  'disabled': False
  }, {
  'name': 'Oranews',
  'url': 'rtmp://109.236.81.91/hls/oranews',
  'icon': 'Oranews.png',
  'disabled': False
  }, {
  'name': 'A1 Internacional HD',
  'url': 'http://217.23.12.187:8080/a1internacionalHDmahiyahsat/playlist.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
 }]

FilmaShqip = [{
  'name': 'Azemi',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Azemi.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Balada_e_Kurbinit',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Balada_e_Kurbinit.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Dashuria_e_Bjeshkeve_Te_Nemuna',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Dashuria_e_Bjeshkeve_Te_Nemuna.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Epoka_Para_Gjyqit_,Drama_e_Ekrem_Kryeziut',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Epoka_Para_Gjyqit_,Drama_e_Ekrem_Kryeziut.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Gjurme_Shqiptare_ Historia_e_jashtezakonshme_e_maleve_te_kuqe',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Gjurme_Shqiptare_ Historia_e_jashtezakonshme_e_maleve_te_kuqe.mp4.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Gjurme_Shqiptare_Nje_Zhan_D_Ark_shqiptare',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Gjurme_Shqiptare_Nje_Zhan_D_Ark_shqiptare.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Gjurme_te_bardha_Filmi_i_Ekrem_Kryeziut',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Gjurme_te_bardha_Filmi_i_Ekrem_Kryeziut.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Guri_i_beses',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Guri_i_beses.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'JESUS_Hiri_i_Zotit_Jezu_Krisht',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/JESUS_Hiri_i_Zotit_Jezu_Krisht.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Nxenesit_e_klases_sime',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Nxenesit_e_klases_sime.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Rojet_e_Mjegulles',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Rojet_e_Mjegulles.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Shkelqimi_i_perkohshem',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Shkelqimi_i_perkohshem.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Shkolla_e_Maleve',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Shkolla_e_Maleve.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Shoket',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Shoket.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Shpresa',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Shpresa.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Si_gjithe_te_tjeret',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Si_gjithe_te_tjeret.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Sinjali_i_dashurise',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Sinjali_i_dashurise.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Taulanti_kerkon_nje_moter',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Taulanti_kerkon_nje_moter.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Thirrja',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Thirrja.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Toka_jone',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Toka_jone.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Tomka_dhe_shoket_e_tij',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Tomka_dhe_shoket_e_tij.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Vjeshte_e_xehte',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Vjeshte_e_xehte.mp4',
  'icon': 'icon.png',
  'disabled': False
  }, {
  'name': 'Yje_mbi_Drin',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_Shqip/Yje_mbi_Drin.mp4',
  'icon': 'icon.png',
  'disabled': False
  
}]

Movies = [{
  'name': 'DER_BEAR_2015',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/DER_BEAR.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'BATMANN_DIJON_2016',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/BATMANN_DIJON.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Ant_Man_2015',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Ant_Man_2015.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Breaking_Thru_2015',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Breaking_Thru_2015.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Arrowhead_2016',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Arrowhead_2016.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Avatar_Aufbruch_nach_Pandora_2009',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Avatar_Aufbruch_nach_Pandora_2009.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'BRAVEHEART',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/BRAVEHEART.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Bibi_und_Tina_2014',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Bibi_und_Tina_2014.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'DER_GAST',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/DER_GAST.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Der_Marsianer_Rettet_Mark_Watney_2015',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Der_Marsianer_Rettet_Mark_Watney_2015.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Der_Pate_1972',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Der_Pate_1972.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Die_Bestimmung_Divergent',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Die_Bestimmung_Divergent.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Die_Eisknigin_Vllig_Unverfroren',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Die_Eisknigin_Vllig_unverfroren_stream.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Die_Legende_der_Weachter_2010',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Die_Legende_der_Weachter_2010.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Die_Hebamme_II_2016',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Die_Hebamme_II_2016.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Dragonheart_3_The_Sorcerers_Curse',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Dragonheart_3_The_Sorcerers_Curse.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Dying_of_the_Light_2015',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Dying_of_the_Light_2015.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'EDGE_OF_TOMORO',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/EDGE_OF_TOMORO.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'END_GAME',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/END_GAME.mp4',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Everest_2015',
  'url': 'http://alba.sytes.net/radio/musik/moveis/files/Filma_International_de/Everest_2015.mp4',
  'icon': 'alba.png',
  'disabled': False
  
  }]


Radio = [{
  'name': 'ALBASOFT RADIO',
  'url': 'http://alba.sytes.net:8000/;stream.mp3',
  'icon': 'alba.png',
  'disabled': False
  }, {
  'name': 'Radio Xheti',
  'url': 'http://178.32.62.154:9922/;stream.mp3',
  'icon': 'radioxheti.png',
  'disabled': False
  }, {
  'name': 'Radi Dedi',
  'url': 'http://www.dedi24.com:8000/;stream.mp3',
  'icon': 'radiodedi.png',
  'disabled': False
  }, {
  'name': 'Radio Dukagjini',
  'url': 'http://s6.voscast.com:8824/;stream.mp3',
  'icon': 'Radio_Dukagjini.png',
  'disabled': False
  }, {
  'name': 'Radio Alba',
  'url': 'http://streaming.jusahost.com:9222/;stream.mp3',
  'icon': 'Radio_alba.png',
  'disabled': False
  }, {
  'name': 'Radio Ahireti',
  'url': 'http://37.59.28.208:8018',
  'icon': 'Radio_Ahireti.png',
  'disabled': False
  }, {
  'name': 'Radio Alba Klin',
  'url': 'http://87.117.228.65:15400',
  'icon': 'RadioAlbaKlin.png',
  'disabled': False
  }, {
  'name': 'Radio Gjakova',
  'url': 'http://37.26.69.30:8080',
  'icon': 'RadioGjakova.png',
  'disabled': False
  }, {
  'name': 'Radio Gurbeti',
  'url': 'http://192.184.9.79:8218;stream.mp3',
  'icon': 'RadioGurbeti.png',
  'disabled': False
  }, {
  'name': 'Radio Turbo',
  'url': 'http://pgturbo.mine.nu:5040',
  'icon': 'RadioTurbo.png',
  'disabled': False
  }, {
  'name': 'Radio Fontana',
  'url': 'http://46.4.104.253:8010/;stream.mp3',
  'icon': 'Radio_Fontana.png',
  'disabled': False
}]


streams = {
  'LiveTV': sorted((i for i in LiveTV if not i.get('disabled', False)), key=lower_getter('name')),
  'FilmaShqip': sorted((i for i in FilmaShqip if not i.get('disabled', False)), key=lower_getter('name')),
  'Movies': sorted((i for i in Movies if not i.get('disabled', False)), key=lower_getter('name')),
  'Radio': sorted((i for i in Radio if not i.get('disabled', False)), key=lower_getter('name')),
  # 'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  # 'FilmaShqip': sorted(FilmaShqip, key=lower_getter('name')),
  # 'Movies': sorted(Movies, key=lower_getter('name')),
  # 'Radio': sorted(Radio, key=lower_getter('name')),
}

PARAMS = get_params()
TAG = None
logging.warning('PARAMS!!!! %s', PARAMS)

try:
  TAG = PARAMS['tag']
except:
  pass

logging.warning('ARGS!!!! sys.argv %s', sys.argv)

if TAG == None:
  show_tags()
else:
  show_streams(TAG)
