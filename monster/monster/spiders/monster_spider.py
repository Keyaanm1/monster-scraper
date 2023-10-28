import scrapy

class MonsterSpider(scrapy.Spider):
    name = "monster-spider"
    start_urls = [
        'https://www.monster.com/jobs/q-rn-jobs?page=1&geo=43.01,-81.28'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def parse(self, response):
        # Extract job details
        job_cards = response.css('li.sc-blKGMR.etPslv')
        for job in job_cards:
            title = job.css('h3[data-testid="jobTitle"] a::text').get()
            company = job.css('span[data-testid="company"]::text').get()
            location = job.css('span[data-testid="jobDetailLocation"]::text').get()
            posted_date = job.css('span[data-testid="jobDetailDateRecency"]::text').get()
            yield {
                'title': title,
                'company': company,
                'location': location,
                'posted_date': posted_date
            }
        
        # Pagination handling
        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
        
        # Print total job postings count
        total_postings = len(job_cards)
        self.logger.info(f"Total job postings: {total_postings}")
