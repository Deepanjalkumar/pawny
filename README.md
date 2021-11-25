Pawny is a data breach cli tool used to detect breaches related to email address and domain name.

![pawny_face](https://user-images.githubusercontent.com/55708909/143451718-14558807-0334-47e9-876a-363e99825967.png)

# Installation

Install pawny with git

                     git clone https://github.com/Deepanjalkumar/pawny.git
                     
                     cd pawny
                     
                     pip3 install -r requirements.txt
                     
# Usage/Examples

                     For detecting email address :
                      
                                  python3 epawny -e email_address -a api_key -o output.txt
                                  
                     For detecting domain name :

                                  python3 dpawny -e domain_name -a api_key -o output.txt
