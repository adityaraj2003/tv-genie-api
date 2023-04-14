

import requests
import json
from datetime import date

from utils import *

def get_epg_data(channel):
    try:
        url = f"https://web.scraper.workers.dev/?url=https%3A%2F%2Ftvgenie.in%2F{channel}-schedule&selector=tr&scrape=text&pretty=true"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        data_json = response.json()

        epg_data = []

        for item in data_json['result']['tr']:
            item = item.replace('&nbsp;', '').replace('&amp;', '')
            if "Today" in item:
                item = item.replace(", Today", "")
                item = item.split()

                start_time = f"{item[-2]} {item[-1]}"
                if int(item[-2].split(":")[0]) < 10:
                    start_time = f"0{start_time}"

                if "E" not in item[-3]:
                    episode_number = "N/A"
                    show_name = item[:-2]
                else:
                    episode_number = item[-3]
                    show_name = item[:-3]

                show = " ".join(show_name)

                epg_data.append({
                    'showName': show.rstrip(),
                    'startTime': convert_24(start_time).rstrip() + ":00",
                    'episodeNum': episode_number,
                    'date': date.today().strftime("%Y-%m-%d")
                })

        for index, item in enumerate(epg_data[:-1]):
            end_time = epg_data[index + 1]["startTime"]
            start_time_utc = get_tplay_time(item["startTime"], "05:30:00", item["date"])
            end_time_utc = get_tplay_time(epg_data[index + 1]["startTime"], "05:30:00", item["date"])
            duration = get_time_difference(item["startTime"], epg_data[index + 1]["startTime"])

            item.update({
                "endTime": end_time,
                'utcStartTimeStamp': start_time_utc,
                'utcEndTimeStamp': end_time_utc,
                'duration': duration
            })

        return {'epg': epg_data}

    except Exception as e:
        print(f"Error: {e}")
        return None
