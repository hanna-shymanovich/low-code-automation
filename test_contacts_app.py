from playwright.sync_api import Page, expect, Route
from http.cookies import SimpleCookie
import json

def test_api_examples(page: Page) -> None:
    created_contact = {}
    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    login_email = "random@mail.org"
    login_pwd = "1234567"
    first_name = "John"
    last_name = "Doe"
    email = "john.doe@example.com"
    phone_number = "123456789"

    def handle_contacts(route: Route):
        if route.request.method == "POST":
            # Modify request payload to include country
            payload = route.request.post_data_json  # <-- no parentheses
            payload["country"] = "USA"
            response = route.fetch(post_data=json.dumps(payload))
            nonlocal created_contact
            created_contact = response.json()
            route.fulfill(response=response)
        elif route.request.method == "GET":
            response = route.fetch()
            json_data = response.json()
            json_data.append({"_id": "001", "firstName": "Fake", "lastName": "Contact", "email": "fake@mail.com",
                            "phone": "12345", "owner": "6894ad53a0504000151c0ba5", "__v": 0})
            route.fulfill(response=response, json=json_data)
        else:
            route.continue_()

    page.route("**/contacts", handle_contacts)

    # login via API
    response = page.request.post(url=base_url + "/users/login",
                      data={"email": login_email, "password": login_pwd})
    assert response.ok, "Login response status should be OK"
    assert "set-cookie" in response.headers, "Login response should contain set-cookie header"
    # retrieve auth token from the response set-cookie header
    # Task-Part-2: Get auth token from browser context
    cookies = page.context.cookies()  # get all cookies in the current browser context
    token_cookie = next((c for c in cookies if c["name"] == "token"), None)
    assert token_cookie is not None, "Auth token cookie not found in browser context"
    token = token_cookie["value"]

    # UI test part - add new contact
    page.goto(base_url + "/contactList")
    page.get_by_role("button", name="Add a New Contact").click()
    page.locator("#firstName").fill(first_name)
    page.locator("#lastName").fill(last_name)
    page.locator("#email").fill(email)
    page.locator("#phone").fill(phone_number)
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#myTable")).to_be_visible()

    # verify created entity
    assert created_contact["firstName"] == first_name, "Created contact first name should equal to that entered"
    assert created_contact["lastName"] == last_name, "Created contact last name should equal to that entered"
    assert created_contact["email"] == email, "Created contact email should equal to that entered"
    assert created_contact["phone"] == phone_number, "Created contact phone should equal to that entered"
    # Task-Part-3.2: Add an assertion for country field
    assert created_contact["country"] == "USA", "Created contact country should equal 'USA'"


    # Task-Part-4: Update the contact's firstName using PATCH API request, assert the response status and the updated field value
    updated_first_name = "Johnny"
    patch_response = page.request.patch(
        url=f"{base_url}/contacts/{created_contact['_id']}",
        headers={"Authorization": f"Bearer {token}"},
        data={"firstName": updated_first_name}
    )
    assert patch_response.ok, "PATCH response should be OK"
    updated_contact = patch_response.json()
    assert updated_contact["firstName"] == updated_first_name, "First name should be updated"

    # clean server state
    response = page.request.delete(url=base_url + "/contacts/" + created_contact["_id"], 
                     headers={"Authorization": "Bearer " + token})
    assert response.ok, "Delete Contact response status should be OK"
