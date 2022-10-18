import json
from urllib.request import urlopen , Request
from datetime import date

from utils import *


def getEPGData(channel):
    url = f"https://web.scraper.workers.dev/?url=https%3A%2F%2Ftvgenie.in%2F{channel}-schedule&selector=tr&scrape=text&pretty=true"
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    data_json = json.loads(response.read())





    data = {
        'epg' : [
        ]
    }

    for i in data_json['result']['tr']:
      i = i.replace('&nbsp;' , '')
      i = i.replace('&amp; ' , '')
      if "Today" in i:
        i = i.replace(", Today" , "")
        i = i.split()

        if int(i[-2].split(":")[0]) < 10:
          startTime = "0" + str(i[-2]) + " " + i[-1]

        else:
          startTime = str(i[-2]) + " " + i[-1]

        if not "E" in i[-3]:
          episodeNumber = "N/A"
          showName = i[:-2]

          show = ""
          for j in showName:
            show += j + " "
        else:
          episodeNumber = i[-3]
          showName = i[:-3]

          show = ""
          for j in showName:
            show += j + " "


    

        data['epg'].append({
          'showName' : show.rstrip(),
          'startTime' : convert24(startTime).rstrip() + ":00",
          'episodeNum' : episodeNumber,
          'date' : date.today().strftime("%Y-%m-%d")
    })


    for k in range(0 , len(data['epg']) - 1):
      data['epg'][k].update({
      "endTime" : data['epg'][k + 1]["startTime"],
      'utcStartTimeStamp' : getTplayTime(data['epg'][k]["startTime"] , "05:30:00" , data['epg'][k]["date"]),
      'utcEndTimeStamp' : getTplayTime(data['epg'][k + 1]["startTime"] , "05:30:00" , data['epg'][k]["date"]),
      'duration' : getTimeDifference(data['epg'][k]["startTime"] , data['epg'][k + 1]["startTime"])
      })


    # complete_data = json.dumps(data , indent =2 )
    return data
