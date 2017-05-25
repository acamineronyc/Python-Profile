import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code: ", response.status_code)

# Store API response in a variable.
response_dict = response.json()

# Process results
print(response_dict.keys())

# Working with the Response Dictionary or the data store there
print("Total repositories: ", response_dict['total_count'])

# Explore information about repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
repo_dict = repo_dicts[0]
print("\nkeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

file = 'www.hh.com', id

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])   # owner = ['login', 'vinta'] etc..
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

#####################################################################################
# Summarizing the Top Repositories
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

# Visualizing repositories using Pygal












