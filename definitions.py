# definitions

# search query to find pictures. No AND operator or similar needed.
search_query = [
"cute",
"feline"
]

# twitter user id
my_user_id = 1071445632789962754

# follow people tweeting with this hashtag
follow_hashtag = "#cats"

# hashtags to be added in each tweet
message_hashtags = " #ilovecats #cutecats #cats #kittens #cutekittens #catsoftwitter"

# define the message
messages = [
"I'm too sexy fur your dog.",
"OMG I'm so cute.",
"I can't believe some people prefer dogs.",
"Purr purr.",
"Cuddle cuddle, purr purr.",
"Who cares I'm not a kitten?",
"I hunt at night. Don't blame me for sleeping all day.",
"Feed me and MAYBE I'll be nice to you.",
"Look what the cat dragged in.",
"Wow. Meow.",
"I am not your servant. Ask your dog.",
"No kids please, I'm not a dog.",
"Servitude is fur dogs.",
"Meow, meow. Food, now.",
"I beg your pawdon?",
"Whatever the question is, the answer is NO.",
"Only dogs will respond to your silly calls.",
"Do not mess with my paws.",
"Only my attitude surpasses my cuteness.",
"Yes, I know I'm a furry feline.",
"I have so much personality."
]

 

# DO NOT EDIT THIS SECTION

#join the query words, separated by %20
base_url = "https://pixabay.com/en/photos/{}/?image_type=photo&pagi=".format("%20".join(search_query))  