from typing import List


def _filter_unique_emails(new_emails, visited_emails=[]):
    print(f"new_emails = {new_emails}")
    print(f"visited_emails = {visited_emails}")
    
    unique_emails = []
    for email in new_emails:
        if email not in visited_emails:
            unique_emails.append(email)
            visited_emails.append(email)

    return unique_emails


def _filter_emails_based_on_campaign_settings(emails: List[str], settings: dict, all_emails: List[str]):
    print(f"settings.get(\"do_not_contact_other_campaign_leads\") > {settings.get('do_not_contact_other_campaign_leads')}")
    
    if settings.get("do_not_contact_other_campaign_leads"):
        return _filter_unique_emails(emails, all_emails)
    return _filter_unique_emails(emails)


# is_blocked = lambda email, domain: ...
def is_blocked(email, domain):
    pass


def process_campaigns(campaigns: List[dict]):
    # TODO: implement blocked_domains
    # TODO: challenge: impelment blocked_domains with 1 line function
    unique_emails=[]
    all_emails = dict()

    for campaign in campaigns:  # TODO: dedupe before, or consider 2 visit within the same campaign
        # all_emails.update(campaign["emails"])
        for email in campaign["emails"]:
            if email in all_emails:
                all_emails[email] += 1
            else:
                all_emails[email] = 1

    print(f"all_emails > {all_emails}")

    emails_per_campaign = {}

    for campaign in campaigns:
        campaign_emails=[]  # TODO: dedupe emails
        for email in campaign["emails"]:
            if not campaign["settings"].get("do_not_contact_other_campaign_leads"):
                campaign_emails.append(email)
            elif all_emails[email] == 1:
                campaign_emails.append(email)
        emails_per_campaign[campaign["id"]] = campaign_emails
    # emails_per_campaign = {}
    # all_emails = []

    # for campaign in campaigns:
    #     campaign_emails = _filter_emails_based_on_campaign_settings(
    #         campaign["emails"], campaign["settings"], all_emails
    #     )
    #     emails_per_campaign[campaign["id"]] = campaign_emails
    #     print(f"all_emails > {all_emails}")
    #     print(f"campaign_emails > {campaign_emails}")

    #     all_emails.extend(campaign_emails)
    #     break

    print(f"emails_per_campaign > {emails_per_campaign}")
    return emails_per_campaign

"""
We expect:
{
    1: ["sarah@techcorp.com", "mike@startup.io"],
    2: ["jennifer@business.net", "robert@enterprise.co"],
    3: ["lisa@newco.com", "john@acme.com", "mark@venture.org"],
    4: ["lisa@newco.com", "john@acme.com", "mark@venture.org"],
}
"""


###### BELOW READ-ONLY

assert process_campaigns(
    [
        {
            "id": 1,
            "settings": {
                "do_not_contact_other_campaign_leads": True,
                "blocked_domains": ["techcorp.com"],  # not implemented
            },
            "emails": [
                "john@acme.com",
                "sarah@techcorp.com",
                "mike@startup.io",
            ],
        },
        {
            "id": 2,
            "settings": {
                "do_not_contact_other_campaign_leads": True,
                "blocked_domains": ["enterprise.co"],
            },
            "emails": [
                "john@acme.com",
                "jennifer@business.net",
                "robert@enterprise.co",
            ],
        },
        {
            "id": 3,
            "settings": {
                "do_not_contact_other_campaign_leads": False,
                "blocked_domains": ["techcorp.com"],
            },
            "emails": [
                "lisa@newco.com",
                "john@acme.com",
                "mark@venture.org",
            ],
        },
        {
            "id": 4,
            "settings": {
                "do_not_contact_other_campaign_leads": False,
                "blocked_domains": ["venture.com"],
            },
            "emails": [
                "lisa@newco.com",
                "lisa@newco.com",
                "john@acme.com",
                "mark@venture.org",
            ],
        },
    ]
) == {
    # without blocked_domains implemented
    1: ["sarah@techcorp.com", "mike@startup.io"],
    2: ["jennifer@business.net", "robert@enterprise.co"],
    3: ["lisa@newco.com", "john@acme.com", "mark@venture.org"],
    4: ["lisa@newco.com", "john@acme.com", "mark@venture.org"],
    # with blocked_domains implemented
    # 1: ["mike@startup.io"],
    # 2: ["jennifer@business.net"],
    # 3: ["lisa@newco.com", "john@acme.com", "mark@venture.org"],
    # 4: ["lisa@newco.com", "john@acme.com", "mark@venture.org"],

}

print('Passing!')
