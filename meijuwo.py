import scrapy


class MeijuwoSpider(scrapy.Spider):
    name = 'meijuwo'
    allowed_domains = ['meijuwo.net']
    start_urls = ['https://www.meijuwo.net/type/meiju-1/']

    def parse(self, response):
        for li in response.css("ul.myui-vodlist li"):
            links = li.css('a')
            yield from response.follow_all(links, self.parse_author)

        # pagination_links = response.css('')
        # yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        starring = ''
        director = ''

        for p in response.css('div.myui-content__detail p'):
            spanText = p.css('span::text').get()
            # print(spanText)
            if spanText == "主演：":
                for a in p.css("a::text"):
                    starring = starring + "," + a.get()

            if spanText == "导演：":
                for a in p.css("a::text"):
                    director = director + "," + a.get()

        yield {
            "logo": response.css('div.myui-content__thumb a img::attr(src)').get(),
            "title": response.css('div.myui-content__detail h1::text').get(),
            "starring": starring,
            "director": director,
            "content": response.css('span.sketch::text').get()
        }
