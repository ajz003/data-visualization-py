import unittest
import requests



class PythonReposTestCase(unittest.TestCase):
    """Tests for python_repos.py."""

    def test_get_status_code(self):
        # Make an API call and store the response.
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_get_30_repos(self):
        # Make an API call and store the response.
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        print("Status code:", r.status_code)

        # Store API response in a variable.
        response_dict = r.json()

        # Explore information about the repositories.
        repo_dicts = response_dict['items']

        names, plot_dicts = [], []

        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])

            # Get the project description, if one is available.
            description = repo_dict['description']
            if not description:
                description = "No description provided."
            
            plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': description,
                'xlink': repo_dict['html_url'],
            }
            plot_dicts.append(plot_dict)

        self.assertEqual(30, len(repo_dicts))

    def test_get_at_least_1_repo(self):
        # Make an API call and store the response.
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        print("Status code:", r.status_code)

        # Store API response in a variable.
        response_dict = r.json()

        # Explore information about the repositories.
        repo_dicts = response_dict['items']

        names, plot_dicts = [], []

        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])

            # Get the project description, if one is available.
            description = repo_dict['description']
            if not description:
                description = "No description provided."
            
            plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': description,
                'xlink': repo_dict['html_url'],
            }
            plot_dicts.append(plot_dict)

        self.assertGreater(len(repo_dicts), 0)
    

unittest.main()