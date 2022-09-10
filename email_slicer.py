# 1 - Request user's email address
email = input("Hello. What is your email address? ").strip()
# The strip function at the end is important as it strips away any blank spaces the user may leave

# 2 - Slice username
user = email[:email.index("@")]
# Slices from the start until but not including the "@"

# 3 - Slice domain name
domain = email[email.index("@") + 1 :]
# Slices one element after the "@"

# 4 - Format message
output = "Your username is {} and domain name is {}".format(user, domain)

# 5 - Display output message
print(output)