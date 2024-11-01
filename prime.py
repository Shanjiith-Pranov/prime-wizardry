import re

n = 13

print(not re.match('^.?$|^(..+?)\1+$.', '1'*n))


# Where this is from:
## https://www.youtube.com/watch?v=5vbk0TwkokM (i love standupmaths)
## https://illya.sh/the-codeumentary-blog/regular-expression-check-if-number-is-prime/ (really interesting breakdown of why this works)
