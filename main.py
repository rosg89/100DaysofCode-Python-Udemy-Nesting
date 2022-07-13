#Each key can only have one value
capitals = {
  "France":"Paris",
  "Germany":"Berlin",
}

#Whe can put multiple values if we add a list
travel_log = {
  "France": ["Paris","Lille","Dijon"],
  "Germany": ["Berlin","Hamburg","Stuttgart"],
}

#We can also nest a list in a list
list = ["A","B",["C","D"]]

#Nesting dictionary in a dictionary
travel_log2 = {
  "France": {"cities_visited":["Paris","Lille","Dijon"], "total_visits":12},
  "Germany": {"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visits":5},
}

#Nesting a dictionary inside a list
travel_log_list = [
  {
    "Country":"France", 
    "cities_visited":["Paris","Lille","Dijon"], 
    "total_visits":12
  },
  {
    "Country":"Germany", 
    "cities_visited":["Berlin","Hamburg","Stuttgart"], 
    "total_visits":5
  },
]