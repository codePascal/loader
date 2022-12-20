import unittest

import loader.loader as loader


class TestLoader(unittest.TestCase):
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
