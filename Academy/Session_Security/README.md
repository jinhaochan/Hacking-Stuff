Session Security
---


## Session Hijacking

Stealing a valid Session cookie and using it to validate yourself

## Session Fixation

Creates a valid Session Identifier, and tricks the victim in binding their credentials to that Session Identifier

## XSS + CSRF

A stored or reflected XSS and result in a CSRF when an victim triggers the script

Same-Origin Policy is not sufficient to block CSRF, as SOP does not prevent sending requests. It only prevents a page from accessing results of cross-domain requests.

A CSRF can be GET based or POST based

Stored XSS can bypass CSRF tokens because it can read them easily

## Open Redirect

Open Redirect redirects the users to a website after an action is completed. By changing the redirect address, you can send the user to wherever you want
