class Grammar:
    """
    This class represents the whole grammar of toki pona.
    """

    @staticmethod
    def get_rules() -> str:
        return f"""
            text: (ADJECTIVE | UNKNOWN)+
            ADJECTIVE: "pona" | "ike"

            UNKNOWN: /[A-Za-z]+/

            %import common.WS
            %ignore WS
        """
