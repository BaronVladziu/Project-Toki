class Grammar:
    """
    This class represents the whole grammar of toki pona.
    """

    @staticmethod
    def get_rules() -> str:
        return f"""
            text: ADJECTIVE+
            ADJECTIVE: "pona" | "ike"

            %import common.WS
            %ignore WS
        """
