from scrapy.spiders  import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com"]
     
     
    rules = (
        Rule(LinkExtractor(allow=("catalogue/category"))),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )

    def parse_item(self, response):
        rating_class = response.css("p.star-rating::attr(class)").get()
        if "One" in rating_class:
            rating = "1 Estrela"
        elif "Two" in rating_class:
            rating = "2 Estrelas"
        elif "Three" in rating_class:
            rating = "3 Estrelas"
        elif "Four" in rating_class:
            rating = "4 Estrelas"
        elif "Five" in rating_class:
            rating = "5 Estrelas"
        else:
            rating = "Sem Avaliação"
        
        price_adjust = response.css(".price_color::text").get()
        price = float(price_adjust[1:]) # Retira o £ e retorna como float
        
        availability_adjust = response.css(".availability::text")[1].get().strip()
        availability = int(re.search(r"(\d+)", availability_adjust).group(1)) # Extrai do "In Stock 99 Available" o valor numérico como Integer
        yield {
            "title": response.css(".product_main h1::text").get(default="Título Não Disponível"),
            "price": price,
            "availability": availability,
            "rating": rating,
            "genre":  response.css('a[href^="../category/books/"]::text').get()
        }
