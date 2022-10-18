
![Logo](https://i.imgur.com/4WQFtvI.png)


# Unofficial TV Genie API

A TV Genie API for accessing EPG information of various channels available on TV Genie
## API Reference

#### Get EPG Data

```http
  GET /schedule
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `channel` | `string` | **Required**. channel slug on TVGenie |

#### Example

`/schedule?channel=star-plus`

#### Try it Out

[https://tcewpt.deta.dev/schedule?channel=star-plus](https://tcewpt.deta.dev/schedule?channel=star-plus)


## Credits

- Thanks to [@adamschwartz](https://github.com/adamschwartz) for [web.scraper.workers.dev](https://github.com/adamschwartz/web.scraper.workers.dev)


## License

- Copyright © 2022 - [Licensed under the terms of the GNU General Public License Version 3 ‐ 29 June 2007](https://github.com/aditya76-git/tv-genie-api/blob/main/README.md)


## Authors

- Copyright © 2022 - [aditya76-git](https://www.github.com/aditya76-git)
