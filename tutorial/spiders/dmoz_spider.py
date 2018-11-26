import scrapy
from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	offest=0
	base_url="https://hr.tencent.com/position.php?&start="
	start_urls=[base_url+str(offest)]
	
	
	def parse(self, response):
		node_list=response.xpath("//tr[@class='odd']|//tr[@class='even']")
		for node in node_list:
			position_name=node.xpath("./td[1]/a/text()").extract()[0]
			position_link=node.xpath("./td[1]/a/@href").extract()[0]
			position_range=node.xpath("./td[2]/text()").extract()
			if len(position_range)!=0:
				position_range=node.xpath("./td[2]/text()").extract()[0]
			position_number=node.xpath("./td[3]/text()").extract()[0]
			position_location=node.xpath("./td[4]/text()").extract()[0]
			position_time=node.xpath("./td[5]/text()").extract()[0]
			item=TutorialItem()
			item['position_name']=position_name
			item['position_link']=position_link
			item['position_range']=position_range
			item['position_number']=position_number
			item['position_location']=position_location
			item['position_time']=position_time
			yield item
			
		if response.xpath("//a[@class='noactive' and @id='next']/@href").extract() != "javascript:;":
			url="https://hr.tencent.com/"+response.xpath("//a[@id='next']/@href").extract()[0]
			yield scrapy.Request(url,callback=self.parse)
			
			
			