"""Using generators to write more idiomatic code."""

# Scenario 1: preferring generator expressions to list expressions

# Harmful

for upper_case_name in [name.upper() for name in get_all_usernames()]:
    process_username(upper_case_name)

# Idiomatic
for upper_case_name in (name.upper() for name in get_all_usernames()):
    process_username(upper_case_name)

# Scenario 2: using a generator to lazily load infinite sequences
# Harmful
def get_twitter_stream_for_keyword(keyword):
    imaginary_twitter_api = ImaginaryTwitterAPI()

    if imaginary_twitter_api.can_get_stream_data(keyword):
        return imaginary_twitter_api.get_stream(keyword)

current_stream = get_twitter_stream_for_keyword('#jeffknup')
for tweet in current_stream:
    process_tweet(tweet)

# Idiomatic
def get_twitter_stream_for_keyword_idiomatic(keyword):
    """get_twitter_stream_for_keyword_idiomatic will be a generator."""
    imaginary_twitter_api = imaginary_twitter_api()
    while imaginary_twitter_api.can_get_stream_data(keyword):
        yield imaginary_twitter_api.get_stream(keyword)

# Since get_twitter_stream_for_keyword_idiomatic is a generator,
# we can safely loop through till we're tired
for tweet in get_twitter_stream_for_keyword_idiomatic('#jeffknupp'):
    process_tweet(tweet)
    