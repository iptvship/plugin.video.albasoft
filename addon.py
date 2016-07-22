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

tags = [{
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
    'name': 'German Tv',
    'id': 'GermanTv',
    'icon': 'Germantv.png'
    }, {
    'name': 'Radio',
    'id': 'Radio',
    'icon': 'radio.png'
    }, {
    'name': 'Musik',
    'id': 'Musik',
    'icon': 'mp3.png'
  }]


LiveTV = [{
  'name': 'Fontana TV',
  'url': 'http://alba.sytes.net/fontana.m3u',
  'icon': 'a1espaniol.png',
  'disabled': True
  }, {
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
  'name': 'Test',
  'url': 'http://217.23.12.187:8080/a1balkantvmahirtvyahsat/playlist.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'http://217.23.12.187:8080/a1shiptarealb11/playlist.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'http://217.23.12.187:8080/a1internacionalHDmahiyahsat/playlist.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://albukhd.dyndns.tv:1935/albuk/albmus.stream',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://188.138.17.8/albuk//albuk+.stream',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://188.138.17.8:1935/albuk/albuk.stream',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://ip.opoja.tv/live/tvopoja',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://80.91.115.211/live/livestream',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'http://84.22.48.253:8080/kutia/test.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://wowza.rtkit.com/live//livestream',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'http://live.tvmak.com/tv/tv21.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'http://live.tvmak.com/tv/dasmatv.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://84.20.77.50/live/livestream1',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'rtmp://wowza.rtkit.com/live//kopliku',
  'icon': 'a1espaniol.png',
  'disabled': False
  }, {
  'name': 'Test',
  'url': 'http://84.22.48.253:8080/dukagjini/test.m3u8',
  'icon': 'a1espaniol.png',
  'disabled': False
  }]


FilmaShqip = [{
  'name': 'Shiko Shqip Filma',
  'url': 'http://alba.sytes.net/filmsh.m3u',
  'icon': 'icon.png',
  'disabled': False
  }]


Movies = [{
  'name': 'Deutsch Movei',
  'url': 'http://alba.sytes.net/radio/moveis/movei.m3u',
  'icon': 'alba.png',
  'disabled': False
  }]


GermanTv = [{
  'name': 'Per momentin nuk ka kanala jom tuj ponu',
  'url': 'http://185.39.194.95:8888/udp/224.176.0.123:10005',
  'icon': 'Germantv.png',
  'disabled': True
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


Musik = [{
  'name': 'Shqip Musik',
  'url': 'http://alba.sytes.net/radio/musik/musik.m3u',
  'icon': 'mp3.png',
  'disabled': False
  }]


streams = {
  'LiveTV': sorted((i for i in LiveTV if not i.get('disabled', False)), key=lower_getter('name')),
  'FilmaShqip': sorted((i for i in FilmaShqip if not i.get('disabled', False)), key=lower_getter('name')),
  'Movies': sorted((i for i in Movies if not i.get('disabled', False)), key=lower_getter('name')),
  'GermanTv': sorted((i for i in GermanTv if not i.get('disabled', False)), key=lower_getter('name')),
  'Radio': sorted((i for i in Radio if not i.get('disabled', False)), key=lower_getter('name')),
  'Musik': sorted((i for i in Musik if not i.get('disabled', False)), key=lower_getter('name')),
  # 'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  # 'FilmaShqip': sorted(FilmaShqip, key=lower_getter('name')),
  # 'Movies': sorted(Movies, key=lower_getter('name')),
  # 'GermanTv': sorted(GermanTv, key=lower_getter('name')),
  # 'Radio': sorted(Radio, key=lower_getter('name')),
  # 'Musik': sorted(Musik, key=lower_getter('name')),
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
