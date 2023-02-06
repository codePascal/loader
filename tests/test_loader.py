import unittest

from .context import loader


class TestLoader(unittest.TestCase):

    def test_get_api_key(self):
        self.assertEqual(loader.get_api_key(), "9f1134e3-3878-4263-80db-76170259c3b0")

    def test_get_rand_user_agent(self):
        self.assertTrue(loader.get_rand_user_agent() in [
            "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        ])

    def test_request(self):
        url = 'https://motherfuckingwebsite.com/'
        req = loader.get_request(url)
        self.assertEqual(req.text[:15], '<!DOCTYPE html>')

    def test_soup(self):
        url = 'https://motherfuckingwebsite.com/'
        soup = loader.get_soup(loader.get_request(url))
        self.assertEqual(soup.find('h1').text,
                         "This is a motherfucking website.")

    def test_fetch(self):
        url = 'https://www.nfl.com/standings/league/2020/reg'
        data = loader.fetch(url, ('table', {
            'class': "d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}"}))
        self.assertEqual(data[0][0][0], 'NFL Team')
        self.assertEqual(data[0][0][1], 'W')
        self.assertEqual(data[0][0][-1], 'Last 5')
        self.assertEqual(data[0][1][1], '1')


if __name__ == "__main__":
    unittest.main()
