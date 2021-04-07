myDictionary={
"pramod":"Human",

"rocky":"Dog",

"marks":[12,25,36],

"anotherDictionary":{"player":"Virat", "cook":"Geetha"},

1:2
}
# Dictionary methods 
print(myDictionary.keys())

print(list(myDictionary.keys()))

print(myDictionary.values())

print(myDictionary.items())

print(myDictionary)
updateDict={
    "friend":"Pranav",
}
myDictionary.update(updateDict) #updates the updateDict into myDictionary 
print(myDictionary)

print(myDictionary.get("friend2")) #doesnt throw error gives none 
print(myDictionary["friend2"]) #throws error if the friend key is not present
