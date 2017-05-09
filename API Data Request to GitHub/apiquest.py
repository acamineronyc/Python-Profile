# Processing an API Response
# 1.Import Request
import requests

# Make an API call and store the response.

# 2. We store the URL of the API call.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# 3. requests() make the call
# We call get() and pass the URL.
# The object is store in the variable response.

response = requests.get(url)

# 4.
# The response object has an attribute called status_code to tell is request was sucessful
# We print the value of the status_code to make sure the call went through successfully. 200

print("Status code: ", response.status_code)

# 5. Store API response in a variable.
# The API returns the information in JSON format,
# We use the json() method to convert the information to a Python dictionary
# Then WE STORE THE RESULTING DICTIONARY the variable "response_dict".

response_dict = response.json()

# Process results: Print the KEYS from response_dict.

print(response_dict.keys())

############################################################################################
# Working with the Response Dictionary or the data store there

# Print the value associated with "total_count".
# total_count represents the total number of Python repositories on GitHub.

print("Total repositories: ", response_dict['total_count'])

# Explore information about repositories
# 'items' represents a list containing a number of dictionaries with data about an individual Python repository.

# Store this list pf dictionaries in repo_dicts.

repo_dicts = response_dict['items']

# Print the length of repo_dicts to see how many repositories we have information for.
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
repo_dict = repo_dicts[0]

# 4. Print the number of keys in the dictionary to see how much information we have
print("\nkeys:", len(repo_dict))

# Print
for key in sorted(repo_dict.keys()):
    print(key)
file = 'www.hh.com', id
# GitHub’s API returns a lot of information about each repository: there are 68 keys in repo_dict

# Let’s print out the values for a number of keys from the first repository’s dictionary- repo_dict:
print("\nSelected information about first repository:")
# We print the name of the project
print('Name:', repo_dict['name'])

# OJO: An entire dictionary represents the project’s owner EX: owner = ['login', 'vinta'] etc...
# so we use the "key owner" to access the dictionary representing the owner
# and then use the "key login" to get the owner’s login name.
print('Owner:', repo_dict['owner']['login'])   # owner = ['login', 'vinta'] etc..

# Print how many stars the project has earned and the URL for the project’s GitHub repository.
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])

# Show when it was created and when it was last updated
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])

# Finally, we print the repository’s description
print('Description:', repo_dict['description'])

#####################################################################################
# Summarizing the Top Repositories
# Write a loop to print selected information about each of the repositories returned
# by the API call so we can include them all in the visualization:


print("\nSelected information about each repository:")

# Loop through all the dictionaries in repo_dicts.
# Inside the loop we print the name of each project,
# its owner, how many stars it has, its URL on GitHub, and the project’s description
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

# Monitoring API Rate Limits, Most APIs are rate-limited
# Which means there’s a limit to how many requests you can make in a certain amount of time.

# PENDING #












