from playwright.sync_api import Page, expect

test_username = "Hanna"
test_surname = "Shymanovich"
test_age = "30"
test_note = "test"

def test_input_validation(page: Page):
    # Test data
    form_data = {
        "firstname": "Hanna",
        "surname": "Shymanovich",
        "age": "30",
        "notes": "test"
    }
    
    page.goto("https://testpages.eviltester.com/styled/validation/input-validation.html")

    # Fill the form 
    page.locator("input[name=firstname]").fill(form_data["firstname"])
    page.locator("input[name=surname]").fill(form_data["surname"])
    page.locator("input[name=age]").fill(form_data["age"])
    page.locator("textarea[name=notes]").fill(form_data["notes"])

    # Submit the form
    page.get_by_role("button", name="Submit").click()

    # Assertion
    expect(page.locator("#firstname-value")).to_have_text(form_data["firstname"])
    expect(page.locator("#surname-value")).to_have_text(form_data["surname"])
    expect(page.locator("#age-value")).to_have_text(form_data["age"])
    expect(page.locator("#notes-value")).to_have_text(form_data["notes"])

