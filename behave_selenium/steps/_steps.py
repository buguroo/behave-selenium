import importlib

from .browser import Browser


def i_open_the_browser(context, alias):
    """
    Launch the browser using the data provided in the table.

    """
    context.table.require_column("name")
    context.table.require_column("value")

    attrs = {row["name"]: row["value"] for row in context.table}

    command_executor = attrs.pop("executor")
    desired_capabilities = attrs

    browser = Browser(command_executor, desired_capabilities)

    context.selenium_browsers[alias] = browser
    context.selenium_exitstack.enter_context(browser)



def i_load_the_url_in_the_browser(context, url, alias="default"):
    """
    """
    context.selenium_browsers[alias].get(url)


def inspecting_of_happens_that(context, stream, alias="default", timeout=None):
    """
    """
    ns = importlib.import_module(
        "behave_selenium.steps.naturalsearch.%s" % __language__)

    checks = ns.substeps.run(context.text, context)

    context.selenium_browsers[alias].check_stream(
        stream, *checks, timeout=timeout)


def the_browser_holds_that(context, alias="default"):
    assert context.selenium_browser[alias].execute_script(context.text)
