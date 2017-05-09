# The program issue am API call and process the results by indetifying the most starred Python projects on Github
import requests
# Make an API call and store the response.
# we store the URL of the API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# We use request make the call. We call get() and pass it the URL and store the “response object” in variable “r”
r = requests.get(url)

# response object has an attribute called ‘status_code’ that tells is request was successful #200 print("Status code:", r.status_code)

# Store API response in a variable.
# The API return information in JSON format.
# Use json() method to convert the information to a PYTHON DICTIONARY
# Store resulting dictionary in “reponse_dict
response_dict = r.json()

# Process results.
print(response_dict.keys())
# Status code: 200
# dict_keys(['items', 'total_count', 'incomplete_results'])
########################################################################################################
# PART 2: Working with the Response Dictionary
# Now information from the API call is stored as a dictionary, we can work with the data stored there.
# print total_count is a key return value = total number Python repositories on Github

print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
# we store this list of dictionaries in repo_dicts.
# OJO: The value associated with ITEM is a LIST containing a number of DICTIONARIES, each have data individual repository
repo_dicts = response_dict['items']

#print the length of repo_dicts to see how many repositories we have information for
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
#To take a closer look at the information returned about each reposi- tory, we pull out the first item from #repo_dicts and store it in repo_dict

repo_dict = repo_dicts[0]

# We then print the number of keys in the dictionary to see how much informa- tion we have
print("\nKeys:", len(repo_dict))

# print all of the dictionary’s keys to see what kind of information is included.
for key in sorted(repo_dict.keys()):
    print(key)

#######################################################################################################
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


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
       print('\nName:', repo_dict['name'])
       print('Owner:', repo_dict['owner']['login'])
       print('Stars:', repo_dict['stargazers_count'])
       print('Repository:', repo_dict['html_url'])
       print('Description:', repo_dict['description'])

