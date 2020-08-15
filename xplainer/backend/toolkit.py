import xplainer.backend.tools as tools
from xplainer.backend.tools.abstract_tool import AbstractTool


class ToolKit:
    """
    Manages all available tools in the app.
    """

    def __init__(self):
        self.tools = [tool() for tool in tools.__all__]
        self.tools.sort(key=lambda tool: tool.name())
        self.categories = list({tool.category() for tool in self.tools})
        self.categories.sort()

    def get_categories(self) -> list:
        """
        :return: list of category names
        """
        return self.categories

    def get_tools(self, by_category: bool = False):
        """
        Get all tools either as
        - a list containing dicts {tool id: tool JSON}
        - dictionary where keys are category names and values lists of tool JSONs

        :param by_category: True if the result should be grouped by a category name; false otherwise.
        :return: all available tools
        """
        if not by_category:
            return [{tool: tool.to_json()} for tool in self.tools]

        result = {category: [] for category in self.get_categories()}
        for tool in self.tools:
            result[tool.category()].append(tool.to_json())

        return result

    def get_tool(self, tool_id: str) -> AbstractTool:
        return next(filter(lambda tool: tool.id() == tool_id, self.tools), None)
