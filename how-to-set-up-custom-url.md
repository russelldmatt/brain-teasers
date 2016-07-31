### Add CNAME file to repo ###
Very simple, just create a file "CNAME" that looks like this:
www.brainteasers.io

### Add two "A records" to godaddy ###
- Go to all domains
- Under brainteasers.io, click the settings wheel dropdown and select "Manager DNS"
- Under records, add two A records with Host = @ and "Points to" = 192.30.252.153 and 92.30.252.154.
- Delete the previous A record that already existed that pointed to 50.63.202.50?? This seemed necessary but didn't read it anywhere...

At the end of this step, this is what this command looked like:

$ dig brainteasers.io +nostats +nocomment +nocmd

; <<>> DiG 9.8.3-P1 <<>> brainteasers.io +nostats +nocomment +nocmd
;; global options: +cmd
;brainteasers.io.		IN	A
brainteasers.io.	3766	IN	A	192.30.252.153
brainteasers.io.	3766	IN	A	192.30.252.154

### Go back to github and change baseurl in _config.yml ###

Before doint this, when I went to www.brainteasers.io, I would get a bunch of missing resources.  For example:

Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/0.5_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/1_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/1.5_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/2_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/2.5_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/3_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/3.5_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/4_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/stars/4.5_stars.png
Failed to load resource: the server responded with a status of 404 (Not Found) http://www.brainteasers.io/brain-teasers/css/main.css

But when I went to
http://russelldmatt.github.io/brain-teasers/css/main.css
it would redirect me to
http://www.brainteasers.io/css/main.css

From that, I guessed I should change the baseurl in _config.yml from "/brain-teasers" to "".

Worked!

Helpful resources:
- http://andrewsturges.com/blog/jekyll/tutorial/2014/11/06/github-and-godaddy.html
- https://help.github.com/articles/setting-up-an-apex-domain/
- http://stackoverflow.com/questions/9082499/custom-domain-for-github-project-pages

