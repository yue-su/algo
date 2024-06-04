
def findCompatibleRestaurants(ned, mary):
    ned_dict = {}
    mary_dict = {}
    compatible = []
    res = []

    for i in range(len(ned)):
        ned_dict[ned[i]] = i
    
    for i in range(len(mary)):
        mary_dict[mary[i]] = i

    for restaurant in mary:
        if restaurant in ned_dict:
            score = ned_dict[restaurant] + mary_dict[restaurant]
            compatible.append([restaurant,score])

    compatible.sort(key = lambda x:x[1])
    
    res.append(compatible[0])

    for result in compatible[1:]:
        if result[1] == res[0][1]:
            res.append(result)

    return [item[0] for item in res]

# we do have to get all the compatible ones
# the first compatible one must be the one with min score and we can add to the res
# if the following ones with the same score, we add them to, if not we can break the loop

# we only need to convert one array to dict, the other one we could use a for loop with index




nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findCompatibleRestaurants(nedsChoices, marysChoices)
== ["Shogun"])

nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["KFC", "Shogun", "Burger King"]
print(findCompatibleRestaurants(nedsChoices, marysChoices)
== ["Shogun"])

nedsChoices = ["Guppy House", "In-n-Out", "Dairy Queen"]
marysChoices = ["In-n-Out", "Guppy House", "Dairy Queen"]
print(findCompatibleRestaurants(nedsChoices, marysChoices).sort()
== ["Guppy House", "In-n-Out"].sort())

nedsChoices = ["Olive Garden", "Outback Steakhouse", "Red Lobster"]
marysChoices = ["Olive Garden", "Outback Steakhouse", "Red Lobster"]
print(findCompatibleRestaurants(nedsChoices, marysChoices)
== ["Olive Garden"])

nedsChoices = ["Hometown Buffet", "Olive Garden", "Red Lobster"]
marysChoices = ["Panda Express", "Denny's", "Red Lobster"]
print(findCompatibleRestaurants(nedsChoices, marysChoices)
== ["Red Lobster"])

nedsChoices = ["Costco Food Court"]
marysChoices = ["Costco Food Court"]
print(findCompatibleRestaurants(nedsChoices, marysChoices)
== ["Costco Food Court"])

nedsChoices = ["Costco Food Court", "Saigon Deli", "Med Mix"]
marysChoices = ["Med Mix", "Saigon Deli", "Costco Food Court"]
print(findCompatibleRestaurants(nedsChoices, marysChoices).sort()
== ["Saigon Deli", "Costco Food Court", "Med Mix"].sort())

nedsChoices = ["Costco Food Court"]
marysChoices = ["Med Mix", "Saigon Deli", "Costco Food Court"]
print(findCompatibleRestaurants(nedsChoices, marysChoices)
== ["Costco Food Court"])